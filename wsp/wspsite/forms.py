from django import forms
from .models import OrderData
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field
from django.core.validators import RegexValidator

class OrderDataForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('thankyou')
        self.helper.form_method = 'get'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-6'
        self.helper.layout = Layout(
            'responsibleParty',
            'email',
            'phone',
            'cases',
            'address1',
            'address2',
            'city',
            'state',
            'comments'
        )
        self.helper.add_input(Submit('submit', 'Submit Order'))
        self.helper.attrs['autocomplete'] = 'off'
  
        for field in self.fields.values():
            field.widget.attrs['title'] = ''

    STATES = [
        ('', 'Choose...'),
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    ]

    responsibleParty = forms.CharField(
        label = "Responsibility Party Name",
        max_length = 200,
        required = False,
    )

    email = forms.EmailField(
        label = "Email Address",
        max_length = 200,
        required = False,
    )

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )

    phone = forms.IntegerField(
        validators=[phone_regex],
        label = "Phone",
        required = False,
        widget=forms.TextInput(attrs={'placeholder': '+(515) 555-1212'}),
    )

    cases = forms.IntegerField(
        label = "Number of Cases",
        min_value = 25,
        required = False,
    )

    address1 = forms.CharField(
        label = "Address 1",
        max_length = 200,
        required = False,
    )

    address2 = forms.CharField(
        label = "Address 2",
        max_length = 200,
        required = False,
    )

    city= forms.CharField(
        label = "City",
        max_length = 200,
        required = False,
    )

    state = forms.TypedChoiceField(
        label = "States",
        choices = STATES,
        required = False,
    )

    comments = forms.CharField(
        label = "Comments",
        max_length=200,
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 50})
    )