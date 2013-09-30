tabla = {}
//////////////////Modelos////////////////////
tabla.Marcacion = Backbone.RelationalModel.extend({
        urlRoot: 'http://localhost:8000/api/marcacion/',
        base_url: function() {//este codigo es para que le agregue un slash al final
              var temp_url = Backbone.Model.prototype.url.call(this);
              return (temp_url.charAt(temp_url.length - 1) == '/' ? temp_url : temp_url+'/');
            },
        url: function() {//este codigo es para que le agregue un slash al final
          return this.base_url();
        },

        idAttribute: 'id',
    });
tabla.Proposito = Backbone.RelationalModel.extend({


        urlRoot: 'http://localhost:8000/api/proposito/',

    base_url: function() {
      var temp_url = Backbone.Model.prototype.url.call(this);
      return (temp_url.charAt(temp_url.length - 1) == '/' ? temp_url : temp_url+'/');
    },

    url: function() {
      return this.base_url();
    },



        idAttribute: 'id',
        relations: [{
            type: Backbone.HasMany,
            key: 'marcaciones',
            relatedModel: 'tabla.Marcacion',
            collectionType: 'tabla.MarcacionCollection', 
            reverseRelation: {
                key: 'proposito',
               includeInJSON: 'resource_uri',
            },
        }]
    });
tabla.Vinculacion = Backbone.RelationalModel.extend({
        urlRoot: 'http://localhost:8000/api/vinculacion/',
        idAttribute: 'id',
        defaults: {
                    vinculacion: ""       
                },
        relations: [{
            type: Backbone.HasMany,
            key: 'propositos',
            relatedModel: 'tabla.Proposito',
            collectionType: 'tabla.PropositoCollection',
            reverseRelation: {
                key: 'vinculacion',
                includeInJSON: 'resource_uri',
            },
        }],
        initialize:function() {
                this.on("change:vinculacion", function(model){
                vinculacion_nueva = model.get("vinculacion")
                //alert("El nombre de la vinculacion es " + vinculacion_nueva );
            });

       }

});
//////////////COLLECTIONS/////////////////////////////////
tabla.MarcacionCollection = Backbone.Collection.extend({
        url: 'http://localhost:8000/api/marcacion/',
        model: tabla.Marcacion,
        meta: {},
        parse: function(response) {
            this.meta = response.meta;
            return response.objects;
        }   
}); 
 


tabla.PropositoCollection = Backbone.Collection.extend({
        url: 'http://localhost:8000/api/proposito/',
        model: tabla.Proposito,
        meta: {},
        parse: function(response) {
            this.meta = response.meta;
            return response.objects;
        }   
}); 
 
tabla.VinculacionCollection = Backbone.Collection.extend({
        model: tabla.Vinculacion,        
        // A catcher for the meta object TastyPie will return.
        meta: {},
        // Set the (relative) url to the API for the item resource.
        url: "http://localhost:8000/api/vinculacion/",
        // Our API will return an object with meta, then objects list.
        parse: function(response) {
            this.meta = response.meta;
            return response.objects;
        }   
    });

//////////////////////////////////VISTAS////////////////////////
////////////////////VINCULACIONES/////////
// Vista para todas las vinculaciones
tabla.ListaVinculacionView = Backbone.View.extend({
    tagName: 'table',
    initialize: function(){
        this.collection.on('change', this.render, this);
         this.collection.on('add', this.render, this); 
},

    render: function() {
        this.$el.empty();//esto es para que no se duplique la lista, vacio el dom
        this.collection.each(
            function(vinculacion) {

                var vinculacionView = new tabla.VinculacionView({ model: vinculacion });
                this.$el.append(vinculacionView.render().el);
                var propositos = vinculacion.get( 'propositos' );
   //             console.log(propositos.toJSON());
                listaPropositoView = new tabla.ListaPropositoView({ collection: propositos});
                this.$el.append(listaPropositoView.render().el);
            }, this);
        return this;
    }
});
// vista para cada vinculacion en particular
tabla.VinculacionView = Backbone.View.extend({
    tagName: 'tbody',
    template: _.template($('#vinculacionTemplate').html() ), 
   
    initialize: function(){
      //  this.model.on('change', this.render, this);
},
       events: {
     'dblclick' : 'showAlert',
     'click .edit': 'editarVinculacion',
     'click .create': 'crearProposito',
     
    },

     crearProposito: function(){
    var nombre = prompt("Please enter the new name");
    if (!nombre)return;
    console.log(this.model.get('resource_uri'));
    console.log(this.model.get('resource_uri'));
    console.log('holaa');
    var nuevoProposito = new tabla.Proposito( {  proposito: nombre 
                                                //, vinculacion: this.model.get('resource_uri')
                                                ,mes_ano:'2013-09-01' } );//
    propositos = this.model.get('propositos');
    propositos.add(nuevoProposito);
    nuevoProposito.save();
   // console.log(this.model.get('meta'));
    propositos = this.model.get('propositos');
    console.log(propositos.toJSON());
    propositos.add(nuevoProposito);
    propositos2 = this.model.get('propositos');
    console.log(propositos2.toJSON());
    console.log(nuevoProposito.toJSON());

    //this.model.set('vinculacion', nombre); 

    },

     editarVinculacion: function(){
    var nombre = prompt("Please enter the new name");
     if (!nombre)return;

    this.model.set('vinculacion', nombre);
    console.log(this.model.toJSON());
    this.model.save();

    },
      

    showAlert: function(){
        alert("Click en vinculacion");
    }, 
    render: function() {

        this.$el.html(this.template(this.model.toJSON()) ); 
        this.$el.addClass("loqui");
        return this;
    }
});
///////////////PROPOSITOS//////////////
// Vista para todas los propositos
tabla.ListaPropositoView = Backbone.View.extend({
    tagName: 'tbody',

    initialize: function(){
        this.collection.on('change', this.render, this);
        this.collection.on('add', this.render, this); 
},

      events: {
     //'click th' : 'showAlert',  
    // 'doubleclick .edit': 'editarVinculacion', 

    },

    showAlert: function(){
        alert("Click en proposito");
    },   

    render: function() {
          this.$el.empty();//esto es para que no se duplique la lista, vacio el dom
        this.collection.each(
            function(proposito) {
                var propositoView = new tabla.PropositoView({ model: proposito });
               // console.log(propositoView.render().el);

                this.$el.append(propositoView.render().el);
           }, this);
        return this;
    }
});
///////////////// vista para CADA PROPOSITO PARTICULAR///////////////////////
tabla.PropositoView = Backbone.View.extend({
    tagName: 'tr',

    template: _.template($('#propositoTemplate').html() ),    

      initialize: function(){
        this.model.on('change', this.render, this);
        this.model.on('destroy', this.remove, this); // 3. Adding a destroy announcer..
        //this.model.on('add:marcaciones',this.actualizar,this);
            
},
      events: {
        'dblclick th' : 'editProp',
        'click td' : 'showAlert',
        'click .delete' : 'DestroyProposito' 
    },


    editProp: function(){
    var nombre = prompt("Please enter the new name");
    if (!nombre)return;
    
    this.model.save({proposito: nombre},{patch: true});
    


    },

    DestroyProposito: function(){
        this.model.destroy();  
    },

    showAlert: function(event){
        //alert("Click en marcacion");
        //alert(event.target.id);
        //alert(this.model.get('resource_uri'));
        var mes_ano = this.model.get('mes_ano');
        var  solomesano = mes_ano.substring(0,7);//quito el dia de la fecha
       // console.log(solomesano+'-'+event.target.id);
        var cumplimiento;
        //alert('esta check? '+$('#'+event.target.id,this.$el).is(':checked'));
        //console.log(this.model.toJSON());

        if($('#'+event.target.id,this.$el).is(':checked'))//si no esta marcado hacer
        {
            console.log('NO esta marcado, Marcar');
            cumplimiento=1;
            //console.log(cumplimiento);
            //console.log(this.model.get('resource_uri'));
            var nuevaMarcacion = new tabla.Marcacion();
            marcaciones= this.model.get('marcaciones');
              nuevaMarcacion.save({ proposito: this.model ,
                                                    dia: solomesano+'-'+event.target.id,
                                                    cumplimiento: cumplimiento 
                                                },{success :function(){//lequito la hora!!
                                                   var diahora= nuevaMarcacion.get('dia');
                                                   var dia = diahora.substring(0,10);
                                                    nuevaMarcacion.set('dia',dia) ;
                                                   // console.log(nuevaMarcacion.toJSON());        
                                                                     }  
                                                });


                marcaciones=this.model.get('marcaciones');
                marcaciones.add(nuevaMarcacion);
                this.model.set('marcaciones', marcaciones);
            
            $('#'+event.target.id,this.$el).attr("checked","true");
           
            $('#'+event.target.id,this.$el).addClass("marcado");

            
        }
        else//si esta marcado entonces desmarcar
        {
             console.log('SIIII esta marcado, DesMarcar');
            cumplimiento=0;
          //  console.log(cumplimiento);
            var marcaciones =this.model.get('marcaciones');
            dia = solomesano + '-'+event.target.id;
           // console.log(marcaciones.toJSON());
            var marcacion =  marcaciones.findWhere({dia: solomesano + '-'+event.target.id  });
           // console.log(marcacion.toJSON());
            marcacion.set({cumplimiento:cumplimiento})
           // console.log(marcacion.toJSON());

           //$('#'+event.target.id,this.$el).attr("checked","false");

            marcacion.save();       

        }
        
          

    }, 

    render: function() {

        this.$el.html( this.template(this.model.toJSON()) );
        marcaciones_collection = this.model.get('marcaciones');     

        marcaciones_collection.each(
            function(marcacion) {

                if(marcacion.get('cumplimiento')!= 0 ) 
                {var dia = marcacion.get('dia');
                                var  solodia = dia.substring(8);//quito el dia de la fecha
                                id = "#" + solodia;
                               // console.log(id);
                                //$("#01",this.$el).addClass("checked");
                                //$("#01",this.$el).addattr("checked");
                               $(id,this.$el).attr("checked","true");
                
                               // console.log(solodia);
                              //  var marcacionView = new tabla.MarcacionView({ model: marcacion });
                                //console.log(marcacionView.render().el);
                              //  this.$el.append(marcacionView.render().el);
                }
                
            }, this);

        return this;
    },
    remove: function(){
        this.$el.remove();  // 4. Calling Jquery remove function to remove that HTML li tag element..
    }
});

//////////MARCACIONES///////////////////////

/*
tabla.MarcacionView = Backbone.View.extend({
    tagName: 'td',
    template: _.template($('#marcacionTemplate').html() ),  
    render: function() {

        this.$el.html(this.template(this.model.toJSON()) ); 
        return this;
    }
});*/

// Router
var AppRouter = Backbone.Router.extend({

    routes:{
        "":"list"        
    },

    list:function () {
        vinculacion_collection = new tabla.VinculacionCollection();
        listaVinculacionView = new tabla.ListaVinculacionView({ collection: vinculacion_collection});
        vinculacion_collection.fetch({  //data:{"year":"2014","month":"12"},

            success:function(){
                $('#vinculaciones').html(listaVinculacionView.render().el);                 

            } 
        });

       /* proposito_collection = new tabla.PropositoCollection();
        listaPropositoView = new tabla.ListaPropositoView({ collection: proposito_collection});
        proposito_collection.fetch({
            success:function(){
                console.log(listaPropositoView.render().el);
                $('#vinculaciones2').html(listaPropositoView.render().el);
                                // $('#vinculaciones2').html("asfd");

            } 
        });*/

    }   
});

var app = new AppRouter();
Backbone.history.start();
  
