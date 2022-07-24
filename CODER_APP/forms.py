from django import forms


class EquiposForm(forms.Form):
    name=forms.CharField()
    base=forms.CharField()
    chief=forms.CharField()
    chassis=forms.CharField()
    powerunit=forms.CharField()

class PilotosForm(forms.Form):
    name=forms.CharField()
    team=forms.CharField()
    country=forms.CharField()
    podiums= forms.CharField()
    points= forms.CharField()
    Date=forms.DateField()

class PistasForm(forms.Form):
    name=forms.CharField()
    country=forms.CharField()
    laps=forms.CharField()
    length=forms.CharField()
    record=forms.CharField()

