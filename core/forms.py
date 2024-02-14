from django.forms import ModelForm
from .models import Diurese

class DiureseForm(ModelForm):
    class Meta:
        model= Diurese
        fields = '__all__'
