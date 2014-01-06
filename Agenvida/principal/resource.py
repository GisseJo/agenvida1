from tastypie.resources import ModelResource
from tastypie.authorization import Authorization,DjangoAuthorization
from tastypie.authentication import BasicAuthentication,Authentication,SessionAuthentication,ApiKeyAuthentication
 
from tastypie.constants import ALL , ALL_WITH_RELATIONS
from tastypie import fields
from tastypie.bundle import Bundle
from tastypie.exceptions import NotFound
from principal.models import Vinculacion,Proposito, Marcacion, PropositoParticular
from django.contrib.auth.models import User
from datetime import date

from tastypie.exceptions import Unauthorized

class UserObjectsOnlyAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        # This assumes a ``QuerySet`` from ``ModelResource``.
        return object_list.filter(usuario=bundle.request.user)

    def read_detail(self, object_list, bundle):
        # Is the requested object owned by the user?
        return bundle.obj.usuario == bundle.request.user

    def create_list(self, object_list, bundle):
        # Assuming their auto-assigned to ``user``.
        return object_list
    
   

    def update_list(self, object_list, bundle):
        allowed = []

        # Since they may not all be saved, iterate over them.
        for obj in object_list:
            if obj.usuario == bundle.request.user:
                allowed.append(obj)

        return allowed

    def update_detail(self, object_list, bundle):
        return bundle.obj.usuario == bundle.request.user

    def delete_list(self, object_list, bundle):
        # Sorry user, no deletes for you!
        raise Unauthorized("Sorry, no deletes.")

    def delete_detail(self, object_list, bundle):
        return True


class UsuarioResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'usuario'
        fields = ['username', 'first_name']
        allowed_methods = ['get']
        authentication = BasicAuthentication()
        include_resource_uri = False
    #def dehydrate(self, bundle): #para enviar solo el id y nada mas
    #    return bundle.data['name']


class VinculacionResource(ModelResource):
    propositos = fields.ToManyField('principal.resource.PropositoResource',# 'propositos',
    attribute=lambda bundle: Proposito.objects.filter(vinculacion=bundle.obj, usuario=bundle.request.user , mes_ano__year=bundle.request.GET.get('year') if bundle.request.GET.get('year') else date.today().year , mes_ano__month=bundle.request.GET.get('month') if bundle.request.GET.get('month') else date.today().month),# con esto filtro y hago que solo se 
                                                                                                    #devuelta los prop de este usuario
         full=True, null=True, blank=True) # en caso de que no halla un proposito para una vinculacion , full = true para enviar todos los datos
    #lambda bundle: Proposito.objects.filter(vinculacion=bundle.obj, usuario=bundle.request.user)
    class Meta:
        # Datos del Modelo:vinculacion
        queryset = Vinculacion.objects.all()
        resource_name = 'vinculacion'
        authentication = Authentication()
        #authorization = Authorization()
        authorization = Authorization()
        allowed_methods = ['get']
        always_return_data = True
        filtering = { "vinculacion" : ALL, 
                        "propositos" : ALL_WITH_RELATIONS
        } #para hacer el filtro
                                            #http://localhost:8000/api/whatever/?format=xml&title__contains=what
        #fields = ['vinculacion'] #campos a mostrar
        #include_resource_uri = False # si muestro o no la url del recurso
        #excludes = ['id']
        # include_resource_uri = False

      


    #def dehydrate(self, bundle): #para enviar solo el id y nada mas
    #    return bundle.data['id']
   
        
class PropositoResource(ModelResource):
    # Datos del Modelo:usuario,vinculacion, mes_ano, proposito
        vinculacion = fields.ForeignKey('principal.resource.VinculacionResource',
                                     'vinculacion') # se pone a true para que me muestre la informacion
                       
                                                                #y no solo el link donde se encuentra la informacion
        marcaciones = fields.ToManyField('principal.resource.MarcacionResource', 'marcaciones', full=True,readonly=True)
        #usuario = fields.ForeignKey('principal.resource.UsuarioResource',
        #                             'usuario', full=True)
        class Meta:
            queryset = Proposito.objects.all()
            resource_name = 'proposito'
            #authentication = BasicAuthentication()
            #authorization = DjangoAuthorization()
            authorization = UserObjectsOnlyAuthorization()
            list_allowed_methods = ['get', 'post','patch']
            authentication = SessionAuthentication()
            always_return_data = True
            #excludes = ['id']
            #include_resource_uri = False
            filtering = { "proposito" : ALL,
                            "mes_ano":ALL                            
            }
        def obj_create(self, bundle, **kwargs):
            return super(PropositoResource, self).obj_create(bundle, usuario=bundle.request.user)
        
        



class MarcacionResource(ModelResource):
    # Datos del Modelo:proposito , dia , cumplimiento
    proposito = fields.ForeignKey('principal.resource.PropositoResource',
                                     'proposito')
    #usuario = fields.ForeignKey('principal.resource.UsuarioResource',
    #                                 'usuario')
    class Meta:
        queryset = Marcacion.objects.all()
        resource_name = 'marcacion'
        #authentication = BasicAuthentication()
        authentication = SessionAuthentication()
        authorization = UserObjectsOnlyAuthorization()
       # authorization = Authorization()        
        allowed_methods = ['get', 'post', 'delete', 'put']
        always_return_data = True
       # excludes = ['proposito']
        include_resource_uri = False
        
    #def apply_authorization_limits(self, request, object_list):NO FUNCA EN EL NUEVO TASTYPIE 0.10.0
     #       return object_list.filter(usuario=request.user)
    def obj_create(self, bundle, **kwargs):
            return super(MarcacionResource, self).obj_create(bundle, usuario=bundle.request.user)


class PParticularResource(ModelResource):

        class Meta:
            queryset = PropositoParticular.objects.all()
            resource_name = 'pparticular'
            authentication = SessionAuthentication()
            authorization = UserObjectsOnlyAuthorization()
            #authorization = Authorization()
            allowed_methods = ['get', 'post', 'delete', 'put','patch']
            always_return_data = True
            #excludes = ['id']
            #include_resource_uri = False
            filtering = { "nombre" : ALL,
                            "mes_ano":ALL                            
            }
        
        def obj_create(self, bundle, **kwargs):
            return super(PParticularResource, self).obj_create(bundle, usuario=bundle.request.user)
    



