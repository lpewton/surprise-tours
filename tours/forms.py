from django import forms

from .models import Tour


class TourForm(forms.ModelForm):

    class Meta:
        model = Tour
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['continent'].label_from_instance = lambda obj: obj.friendly_name
