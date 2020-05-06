from .models import feedback
from django.forms import ModelForm,Textarea
from django.utils.translation import gettext_lazy as _
class FeedBackForm(ModelForm):
    class Meta:
        model = feedback
        fields = ['msg']
        widgets = {
            'msg': Textarea(attrs={'cols': 80, 'rows': 10}),
        }
        labels = {
            'msg': _('Feedback'),
        }