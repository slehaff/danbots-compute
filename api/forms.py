from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class Form3dScan(forms.Form):
    deviceid = forms.CharField(required=True, max_length=32, strip=True)
    color_picture = forms.ImageField(label="Color Picture", required=True)
    blackWhite_picture = forms.ImageField(label="Black/White Picture", required=True)
    noLight_picture = forms.ImageField(label="NoLight Picture", required=True)

    def __init__(self, *args, **kwargs):
        super(Form3dScan, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.add_input(Submit('submit', 'Send'))
        self.helper.add_input(Submit('cancel', 'Fortryd', css_class='btn-secondary', formnovalidate='formnovalidate', formaction='/'))

class SaveFileForm(forms.Form):
    file = forms.FileField()
    def __init__(self, *args, **kwargs):
        super(SaveFileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.add_input(Submit('submit', 'Send'))
        self.helper.add_input(Submit('cancel', 'Fortryd', css_class='btn-secondary', formnovalidate='formnovalidate', formaction='/'))
