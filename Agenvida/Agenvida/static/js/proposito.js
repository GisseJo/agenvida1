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
            reverseRelation: {
                key: 'proposito',
                includeInJSON: 'id',
            },
        }]
    });
tabla.Vinculacion = Backbone.Model.extend({
        urlRoot: 'http://localhost:8000/api/vinculacion/',
        idAttribute: 'id',
        defaults: {
                    vinculacion: ""       
                },
       initialize:function() {
                 this.on("change:vinculacion", function(model){
                vinculacion_nueva = model.get("vinculacion")
                alert("El nombre de la vinculacion es " + vinculacion_nueva );
            });

       }

        });
    //////////////collections/////////////////////////////////
tabla.PropositoCollection = Backbone.Collection.extend({
        url: 'http://localhost:8000/api/proposito/',
        model: tabla.Marcacion,
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


 SearchView = Backbone.View.extend({
    initialize: function(){
        this.render();
    },
    render: function(){
        var variables = { search_label: "Mi busqueda"}
        // Compile the template using underscore
        //var template = _.template( $("#search_template").html(), {} );
        var template = _.template( $("#search_template").html(), variables );
        // Load the compiled HTML into the Backbone "el"
        this.$el.html( template );
    },
    events: {
        "click input[type=button]": "doSearch"  
    },
    doSearch: function( event ){
        // Button clicked, you can access the element that was clicked with event.currentTarget
        alert( "Search for " + $("#search_input").val() );
        vinculacion = new tabla.Vinculacion({nombre:123});
        alert(vinculacion.nombre)
    }
});


// View for all people
tabla.ListaVinculacionView = Backbone.View.extend({
    tagName: 'ul',

    render: function() {
        this.collection.each(function(vinculacion) {
            var vinculacionView = new tabla.VinculacionView({ model: vinculacion });
            this.$el.append(vinculacionView.render().el);
        }, this);

        return this;
    }
});

// The View for a Person
tabla.VinculacionView = Backbone.View.extend({
    tagName: 'li',


    template: _.template($('#vinculacionTemplate').html() ),
    
    render: function() {
        this.$el.html( this.template(this.model.toJSON()) );
        return this;
    }
});



  
