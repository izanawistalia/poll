from django.forms import ModelForm

from .models import candidates

class candidateForm(ModelForm):
    class Meta:
        model = candidates
        fields = '__all__'
        exclude = ['expert']