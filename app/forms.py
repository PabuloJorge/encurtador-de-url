from django.forms import ModelForm
from app.models import sites

# Create the form class.
class SitesForm(ModelForm):
    class Meta:
        model = sites
        fields = ['codigo', 'url']