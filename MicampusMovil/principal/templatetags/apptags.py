from django import template

register = template.Library()

@register.filter
def get_at_index(list, index):
    return list[index].Clave_Materia


@register.filter
def get_nombre_at(list, index):
    return list[index].Nombre


@register.filter
def get_calificacion_at(list, index):
    return list[index].Calificacion_Final