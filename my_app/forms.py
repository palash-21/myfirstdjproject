from django import forms


class CreateToDoList(forms.Form):
    name = forms.CharField(label="Name", max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
