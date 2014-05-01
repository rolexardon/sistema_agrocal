# -*- coding: utf-8 -*-
# -*- coding: utf8 -*-
from django import forms
from django.forms import ModelForm
from django.forms.widgets import Select, TextInput, EmailInput, DateInput, Textarea, SelectMultiple

from empleados.models import Empleado

class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        widgets = {
            'identidad':   TextInput(attrs={'class':'form-control','size_tag':'col-lg-8','required':'required'}),
            'p_nombre':     TextInput(attrs={'class':'form-control','size_tag':'col-lg-8','required':'required'}),
            's_nombre':     TextInput(attrs={'class':'form-control','size_tag':'col-lg-8'}),
            'p_apellido':   TextInput(attrs={'class':'form-control','size_tag':'col-lg-8','required':'required'}),
            's_apellido':   TextInput(attrs={'class':'form-control','size_tag':'col-lg-8'}),
            'direccion':   TextInput(attrs={'class':'form-control','size_tag':'col-lg-8'}),
            'genero':       Select(attrs={'class':'form-control','size_tag':'col-lg-5','required':'required'}),
            't_fijo':   TextInput(attrs={'class':'form-control','size_tag':'col-lg-8','required':'required'}),
            't_movil':   TextInput(attrs={'class':'form-control','size_tag':'col-lg-8','required':'required'}),
            'tipo':       Select(attrs={'class':'form-control','size_tag':'col-lg-5','required':'required'}),
            'e_civil':       Select(attrs={'class':'form-control','size_tag':'col-lg-5','required':'required'}),
            'f_nacimiento': DateInput(attrs={'class':'form-control','size_tag':'col-lg-5','required':'required'}),
        }