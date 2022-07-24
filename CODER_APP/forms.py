from django import forms


class EquiposForm(forms.Form):
    name=forms.CharField
    base=forms.CharField
    chief=forms.CharField
    chassis=forms.CharField
    powerunit=forms.CharField

