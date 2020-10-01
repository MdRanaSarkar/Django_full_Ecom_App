from django import forms

class SearchForm(forms.Form):
	query = forms.CharField(max_length=200)
	cat_id=forms.IntegerField()