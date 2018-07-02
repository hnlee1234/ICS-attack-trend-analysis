from django import forms
from .models import Vulner
from mptt.forms import TreeNodeChoiceField

class VulnerModelForm(forms.ModelForm):
    vulner = TreeNodeChoiceField(queryset=Vulner.objects.all(),
                                   level_indicator=u'+--')

    class Meta:
    	model = Vulner
    	fields = '__all__'