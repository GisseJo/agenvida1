(function() {
// Views
tabla.vinculacionListView = Backbone.View.extend({
 
    tagName:'ul',
 
    initialize:function () {
        this.model.bind("reset", this.render, this);
    },
 
    render:function (eventName) {
        _.each(this.model.models, function (wine) {
            $(this.el).append(new VinculacionListItemView({model:wine}).render().el);
        }, this);
        return this;
    }
 
});
 
tabla.VinculacionListItemView = Backbone.View.extend({
 
    tagName:"li",
 
    template:_.template($('#tpl-wine-list-item').html()),
 
    render:function (eventName) {
        $(this.el).html(this.template(this.model.toJSON()));
        return this;
    }
 
});
 

 
// Router
var AppRouter = Backbone.Router.extend({
 
    routes:{
        "":"list",
        
    },
 
    list:function () {
        this.viculacionList = new tabla.VinculacionCollection();
        this.vinculacionListView = new VinculacionListView({model:this.wineList});
        this.vinculacionList.fetch();
        $('#vinculaciones').html(this.wineListView.render().el);
    }
 
    
});
 

});

$(document).ready(function(){
 vinculacion =  new tabla.Vinculacion() ;
console.log('hola');    
 });    


