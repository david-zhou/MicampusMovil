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

@register.filter
def get_gamatricula_at(list, index):
    return list[index].Matricula_id

@register.filter
def get_mat_at(list, index):
    return list[index].Matricula

@register.filter
def get_cg_at(list, index):
    return list[index].Clave_Grupo

