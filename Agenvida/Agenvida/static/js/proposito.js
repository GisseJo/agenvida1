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

    render: function() {
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
    render: function() {
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
  
