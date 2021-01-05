from django import forms

class CategoryForm(forms.Form):
    name = forms.CharField(max_length=50)
    icon = forms.CharField(max_length=200)
    status = forms.CharField(max_length=10)

class BrandForm(forms.Form):
    name = forms.CharField(max_length=50)
    logo = forms.ImageField(upload_to="brands")
    status = forms.CharField(max_length=10)
