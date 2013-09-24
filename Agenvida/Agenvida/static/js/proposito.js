tabla = {}
//////////////////Modelos////////////////////
tabla.Marcacion = Backbone.RelationalModel.extend({
        urlRoot: 'http://localhost:8000/api/marcacion/',
        idAttribute: 'id',
    });
tabla.Proposito = Backbone.RelationalModel.extend({
        urlRoot: 'http://localhost:8000/api/proposito/',
        idAttribute: 'id',
        relations: [{
            type: Backbone.HasMany,
            key: 'marcaciones',
            relatedModel: 'tabla.Marcacion',
            collectionType: 'tabla.MarcacionCollection', 
            reverseRelation: {
                key: 'proposito',
                includeInJSON: 'id',
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
                includeInJSON: 'id',
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
                console.log(propositos.toJSON());
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
    var nuevoProposito = new tabla.Proposito( {proposito: nombre} );
    propositos = this.model.get('propositos');
    console.log(propositos.toJSON());
    propositos.add(nuevoProposito);los
    propositos2 = this.model.get('propositos');
    console.log(propositos2.toJSON());
    console.log(nuevoProposito.toJSON());

    //this.model.set('vinculacion', nombre); 

    },

     editarVinculacion: function(){
    var nombre = prompt("Please enter the new name");
     if (!nombre)return;

    this.model.set('vinculacion', nombre);

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
                this.$el.append(propositoView.render().el);
           }, this);
        return this;
    }
});
// vista para cada proposito en particular
tabla.PropositoView = Backbone.View.extend({
    tagName: 'tr',

    template: _.template($('#propositoTemplate').html() ),    

      initialize: function(){
        this.model.on('change', this.render, this);
          this.model.on('destroy', this.remove, this); // 3. Adding a destroy announcer..
          
},
      events: {
        'dblclick th' : 'editProp',
        'click td' : 'showAlert',
        'click .delete' : 'DestroyProposito' 
    },


    editProp: function(){
    var nombre = prompt("Please enter the new name");
    if (!nombre)return;
    this.model.set('proposito', nombre);

    },

    DestroyProposito: function(){
        this.model.destroy();  
    },

    showAlert: function(){
        alert("Click en marcacion");
    }, 

    render: function() {

        this.$el.html( this.template(this.model.toJSON()) );
        marcaciones_collection = this.model.get('marcaciones');     

        marcaciones_collection.each(
            function(marcacion) {
                var dia = marcacion.get('dia');
                var  solodia = dia.substring(8);
                id = "#" + solodia;
                console.log(id);
                //$("#01",this.$el).addClass("checked");
                //$("#01",this.$el).addattr("checked");
               $(id,this.$el).attr("checked","checked");

                console.log(solodia);
                var marcacionView = new tabla.MarcacionView({ model: marcacion });
                this.$el.append(marcacionView.render().el);

                
            }, this);

        return this;
    },
    remove: function(){
        this.$el.remove();  // 4. Calling Jquery remove function to remove that HTML li tag element..
    }
});

//////////MARCACIONES///////////////////////
tabla.MarcacionView = Backbone.View.extend({
    tagName: 'td',
    template: _.template($('#marcacionTemplate').html() ),  
    render: function() {

        this.$el.html(this.template(this.model.toJSON()) ); 
        return this;
    }
});

// Router
var AppRouter = Backbone.Router.extend({

    routes:{
        "":"list"        
    },

    list:function () {
        vinculacion_collection = new tabla.VinculacionCollection();
        listaVinculacionView = new tabla.ListaVinculacionView({ collection: vinculacion_collection});
        vinculacion_collection.fetch({
            success:function(){
                $('#vinculaciones').html(listaVinculacionView.render().el);                 

            } 
        });
    }   
});

var app = new AppRouter();
Backbone.history.start();
  
