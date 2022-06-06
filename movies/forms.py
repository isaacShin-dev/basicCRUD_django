from .models import Movie
from django import forms

class MovieForm(forms.ModelForm):
    
    title = forms.CharField(max_length=150)
    description = forms.Textarea()
    score = forms.IntegerField(min_value = 0 , max_value = 5,
                               widget = forms.NumberInput(
                                   attrs={
                                       'step':1.0,
                                   }
                               ))
    # created_at = forms.DateField(
    #                             widget = forms.DateInput(
    #                                 attrs = {
    #                                     'type':'date'
    #                                     }
    #                                 )
    #                             )
    
    class Meta:
        model = Movie
        fields = ('title', 'description', 'score')
