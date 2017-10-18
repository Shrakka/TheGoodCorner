from django import forms

class AnnounceForm(forms.Form):
    
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'create-title'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class' : 'text-area'}), max_length=2000)
    surname = forms.CharField(max_length=50)
    email = forms.EmailField()


class ContactForm(forms.Form):
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs={'class' : 'text-area'}), max_length=2000)
    
class EditForm(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'create-title'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class' : 'text-area'}), max_length=2000)