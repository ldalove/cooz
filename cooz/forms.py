from django import forms

class SearchForm(forms.Form):
	location = forms.CharField(laben="", max_length="100")
