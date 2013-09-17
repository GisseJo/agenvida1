$( document ).ready(function() {


    
var search_view = new SearchView({ el: $("#search_container") });




 vinculacion_collection = new tabla.VinculacionCollection();
    vinculacion_collection.fetch( {success:function(){
       //alert('Traigo todas las vinculaciones Cant: '+ vinculacion_collection.length);
      //alert('su meta es '+ JSON.stringify(vinculacion_collection.meta) )
      //alert('sus modelos son es '+ JSON.stringify(vinculacion_collection.models) )
        vinculacion_collection.each(function(vinculacion) {
          console.log(vinculacion.get("vinculacion"));
        });
    } 
});
console.log( "ready!" );
});
