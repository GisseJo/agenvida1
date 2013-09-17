from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.constants import ALL
from tastypie import fields
from tastypie.bundle import Bundle
from tastypie.exceptions import NotFound
from principal.models import Vinculacion,Proposito, Marcacion
from django.contrib.auth.models import User


class UsuarioResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'usuario'
        fields = ['username', 'first_name']
        allowed_methods = ['get']
        authentication = BasicAuthentication()
        include_resource_uri = False
class VinculacionResource(ModelResource):
   # propositos = fields.ToManyField('principal.resource.PropositoResource', 'propositos', full=True)
    
    class Meta:
        # Datos del Modelo:vinculacion
        queryset = Vinculacion.objects.all()
        resource_name = 'vinculacion'
        #authentication = BasicAuthentication()
        authorization = DjangoAuthorization()
        allowed_methods = ['get', 'post', 'delete', 'put']
        always_return_data = True
        filtering = { "vinculacion" : ALL } #para hacer el filtro
                                            #http://localhost:8000/api/whatever/?format=xml&title__contains=what
        #fields = ['vinculacion'] #campos a mostrar
        #include_resource_uri = False # si muestro o no la url del recurso
        #excludes = ['id']
        include_resource_uri = False
   
        
class PropositoResource(ModelResource):
    # Datos del Modelo:usuario,vinculacion, mes_ano, proposito
      #  vinculacion = fields.ForeignKey('principal.resource.VinculacionResource',
       #                              'vinculacion', full=True) # se pone a true para que me muestre la informacion
                       
                                                                #y no solo el link donde se encuentra la informacion
        marcaciones = fields.ToManyField('principal.resource.MarcacionResource', 'marcaciones', full=True)
        usuario = fields.ForeignKey('principal.resource.UsuarioResource',
                                     'usuario', full=True)
        class Meta:
            queryset = Proposito.objects.all()
            resource_name = 'proposito'
            authorization = Authorization()
            allowed_methods = ['get', 'post', 'delete', 'put']
            always_return_data = True
            excludes = ['id']
            include_resource_uri = False
        
   #     def apply_authorization_limits(self, request, object_list):
    #        return object_list.filter(usuario=request.user)
     #   def obj_create(self, bundle, **kwargs):
      #      return super(PropositoResource, self).obj_create(bundle, usuario=bundle.request.user)




class MarcacionResource(ModelResource):
    # Datos del Modelo:proposito , dia , cumplimiento
    #proposito = fields.ForeignKey('principal.resource.PropositoResource',
     #                                'proposito', full=True)
    usuario = fields.ForeignKey('principal.resource.UsuarioResource',
                                     'usuario', full=True)
    class Meta:
        queryset = Marcacion.objects.all()
        resource_name = 'marcacion'
        authorization = Authorization()        
        allowed_methods = ['get', 'post', 'delete', 'put']
        always_return_data = True
        excludes = ['id','usuario']
        include_resource_uri = False
        
#    def apply_authorization_limits(self, request, object_list):
 #           return object_list.filter(usuario=request.user)
  #  def obj_create(self, bundle, **kwargs):
   #         return super(PropositoResource, self).obj_create(bundle, usuario=bundle.request.user)

        
