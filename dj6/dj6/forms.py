from secrets import choice
from django import forms

from my_app.models import Email, Phone

categories = [
        ('query', 'Query'),
        ('complant', 'Complant'),
        ('other', 'Other'),
        ]

colors = [('red','Red'), ('blue','Blue'), ('yellow','Yellow'), ('violet','Violet') ]
gender = [('male', 'Male'), ('female', 'Female'), ('other', 'Other')]
class ContactForm(forms.form):
    name = forms.CharField(max_length=20)
    password = forms.CharField(max_length=15, widget= forms.PasswordInput)
    email = forms.EmailField(required=False)
    category = forms.ChoiceField(choices= categories, required=False)
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea, required=False)
    fav_color = forms.MultipleChoiceField(choices=colors, widget= forms.CheckboxSelectMultiple, required=False)
    gender = forms.MultipleChoiceField(choices=gender, widget=forms.RadioSelect, required=False)


class EmailForm(forms.ModelForm):
        class Meta:
                Model = Email
                Feilds = ('sender_mail', 'subject', 'body') 


class PhoneForm(forms.ModelForm):
        class Meta:
                Model = Phone
                feilds = ('name', 'address', 'phone')

