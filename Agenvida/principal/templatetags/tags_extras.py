from django import template
from django.core.exceptions import ObjectDoesNotExist
import calendar

register = template.Library()
   
    
@register.filter(name='dia_marcado')    	
def dia_marcado(proposito, dia):
	try:
		marcacion  = proposito.marcaciones.get(dia__day=dia , cumplimiento=1 )
		return '1'
	except:		
		return '0'
        
        
@register.filter(name='dias_mes')        
def dias_mes(proposito):
    """ Devuelve la cantidad de dias que tiene el mes del proposito"""
    print 'Este es el mes'
    return calendar.monthrange(proposito.mes_ano.year,proposito.mes_ano.month)[1]



@register.filter(name='dias_mes_string')        
def dias_mes_string(proposito):
    """ Devuelve la cantidad de dias  que tiene el mes del proposito(cant de x)"""
    print 'Este es el mes'
    print proposito.mes_ano.month
    print 'x'*calendar.monthrange(proposito.mes_ano.year,proposito.mes_ano.month)[1]
    return 'x'*calendar.monthrange(proposito.mes_ano.year,proposito.mes_ano.month)[1]
   