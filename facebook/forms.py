from django.forms import ModelForm, fields
from .models import Facebook


class FacebookForm(ModelForm):
  class Meta:
    model = Facebook
    fields = ['email', 'password']