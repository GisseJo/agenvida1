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
/////////////PRUEBAS/////////////////////////////////////////////////////
///////////////Traigo todas las Vinculaciones/////////////////////////////    
/*    vinculacion_collection = new tabla.VinculacionCollection();
    vinculacion_collection.fetch( {success:function(){
       // alert('Traigo todas las vinculaciones Cant: '+ vinculacion_collection.length);
      //  alert('su meta es '+ JSON.stringify(vinculacion_collection.meta) )
        //alert('sus modelos son es '+ JSON.stringify(vinculacion_collection.models) )
        
        vinculacion_collection.each(function(vinculacion) {
          console.log(vinculacion.get("vinculacion"));
        });

        console.log('aca otra cosa');
            // Select donuts with names longer than 2
        vinculacion_collection.select(function(vinculacion) {
          return vinculacion.get("vinculacion").length > 10;
        });
        // Map...
        console.log('map')
        vinculacion_collection.map(function(vinculacion) {
          return vinculacion.get("vinculacion");
        });
        } 
    });
*/
///////////////TRaigo la Marcacion de id :1////////////////////////////
/*var marcacion_nueva1 = new tabla.Marcacion({id:2});  
    marcacion_nueva1.fetch({                     
    success:function(){
            //alert('Traigo UNA marcacion '+ JSON.stringify(marcacion_nueva1.attributes)); //imprime los atributos
        }
    });
///////////////TRaigo la Proposito de id :1////////////////////////////
var proposito_nueva1 = new tabla.Proposito({id:2});  
    proposito_nueva1.fetch({                     
    success:function(){
            //alert('Traigo UN proposito'+ JSON.stringify(proposito_nueva1.attributes)); //imprime los atributos
        }
    });
///////////////TRaigo la vinculacion de id :1////////////////////////////
    var vinculacion_nueva1 = new tabla.Vinculacion({id:1});  
    vinculacion_nueva1.fetch({                     
    success:function(){
          //  alert('Traigo UNA vinculacion '+ JSON.stringify(vinculacion_nueva1.attributes)); //imprime los atributos
        }
    });
*/
/*
///////Creacion de una vinculacion////////////////////////////////////////
    var vinculacion_nueva = new tabla.Vinculacion({vinculacion:"algo"});
    vinculacion_nueva.save({                     // se genera GET /usuarios/1
    success:function(){
        //alert("Creacion de una nueva vinculacion" + JSON.stringfy(vinculacion_nueva.attributes)); // imprime {"id":1, "nombre": "Alfonso", "apellidos": "Marin Marin"}
    }
});*/
//////////////////////////////////VISTAS////////////////////////


 SearchView = Backbone.View.extend({
    initialize: function(){
        this.render();
    },
    render: function(){
        // Compile the template using underscore
        var template = _.template( $("#search_template").html(), {} );
        // Load the compiled HTML into the Backbone "el"
        this.$el.html( template );
    },
    events: {
        "click input[type=button]": "doSearch"  
    },
    doSearch: function( event ){
        // Button clicked, you can access the element that was clicked with event.currentTarget
        alert( "Search for " + $("#search_input").val() );
    }
});