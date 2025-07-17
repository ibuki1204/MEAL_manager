from django import forms
from .models import Meal, WeightRecord

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['name', 'description', 'image', 'calories', 'protein', 'fat', 'carbs', 'date', 'time']

class WeightForm(forms.ModelForm):
    class Meta:
        model = WeightRecord
        fields = ['weight', 'date']
