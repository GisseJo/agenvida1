$( document ).ready(function() {    
var search_view = new SearchView({ el: $("#search_container") });
///////////////Traigo todas las Vinculaciones/////////////////////////////    
vinculacion_collection = new tabla.VinculacionCollection();
vinculacion_collection.fetch( {success:function(){
       //alert('Traigo todas las vinculaciones Cant: '+ vinculacion_collection.length);
      //alert('su meta es '+ JSON.stringify(vinculacion_collection.meta) )
      //alert('sus modelos son es '+ JSON.stringify(vinculacion_collection.models) )
    listaVinculacionView = new tabla.ListaVinculacionView({ collection: vinculacion_collection});        
    $(document.body).append(listaVinculacionView.render().el);
    vinculacion_collection.each(
            function(vinculacion) {
                //  console.log(vinculacion.get("vinculacion"));
                //console.log(vinculacion.toJSON())
                //VinculacionView = new tabla.VinculacionView({ model: vinculacion, el: $("#sidebar-nuevo")});
        });
    } 
});


/*
    vinculacion1 = new tabla.Vinculacion({ vinculacion: "Nueva Vinculacion"});
    vinculacion1.set({prioridad:"alta"});
    var nombre_vinculacion = vinculacion1.get("vinculacion");
     vinculacion1.set({vinculacion:"Nueva Vinculacion2"});
    alert(nombre_vinculacion);

///////////////TRaigo la MArcacion de id :2////////////////////////////
    var marcacion_nueva1 = new tabla.Marcacion({id:2});  
    marcacion_nueva1.fetch({                     
    success:function(){
            alert('Traigo UNA marcacion '+ JSON.stringify(marcacion_nueva1.attributes)); //imprime los atributos
 			
        }
    });
///////Creacion de una vinculacion////////////////////////////////////////
    var vinculacion_nueva = new tabla.Vinculacion({vinculacion:"jajajaja"});
    vinculacion_nueva.save({                     // se genera GET /usuarios/1
    success:function(){
    	
        //alert("Creacion de una nueva vinculacion" + JSON.stringfy(vinculacion_nueva.attributes)); // imprime {"id":1, "nombre": "Alfonso", "apellidos": "Marin Marin"}
    }
});
    ///////////////TRaigo la vinculacion de id :1////////////////////////////
    var vinculacion_nueva1 = new tabla.Vinculacion({id:1});  
    vinculacion_nueva1.fetch({                     
    success:function(){
    	vinculacion_nueva1.set({vinulacion:"cambie el nombre"});
    	vinculacion_nueva1.save();
          //  alert('Traigo UNA vinculacion '+ JSON.stringify(vinculacion_nueva1.attributes)); //imprime los atributos
        }
    });
*/
///////////Destroy funciona de lujo
//var vinculacion_nueva3 = new tabla.Vinculacion({id:3});
//vinculacion_nueva3.destroy();
console.log( "ready!" );



});
