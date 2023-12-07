from django import forms
from django.forms.widgets import NumberInput
import datetime


class common_form(forms.Form):
    name=forms.CharField(max_length=100, label="Enter your name :",initial="Your name :")
    comment = forms.CharField(widget=forms.Textarea, max_length=100,label="Enter your valuable comment below :")
    messages = forms.CharField(widget=forms.Textarea(attrs={'rows':3}),initial="Your messages :")
    email = forms.EmailField(
        required=False,
        label="Email address",
        
    )
    remember_me = forms.BooleanField()
    agree = forms.BooleanField(initial=True, required=False)
    date = forms.DateField(initial=datetime.date.today())
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect,choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES)