from django import forms

class WebsiteForm(forms.Form):
    website_url = forms.CharField(label='Website URL', max_length=200)