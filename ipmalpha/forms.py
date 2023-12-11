from django import forms
from ipmclients.models import *
from ipmalpha.models import *


class AddProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super(AddProjectForm, self).__init__(*args, **kwargs)   
        self.fields['project_sum'].required = False
        self.fields['project_status'].required = False
        self.fields['project_product'].required = False
        # self.fields['project_finished'].required = False
    class Meta:
        model = Project
        fields = ['project_name', 'project_status', 'project_client', 'project_product', 'project_sum', 'project_created',]
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control container-fluid', 'placeholder': 'Название проекта*'}),
            'project_status': forms.Select(attrs={'class': 'form-control container-fluid', 'placeholder': 'Статус'}),
            'project_client': forms.Select(attrs={'class': 'form-control container-fluid', 'placeholder': 'Клиент'}),
            'project_product': forms.TextInput(attrs={'class': 'form-control container-fluid', 'placeholder': 'Продукт'}),
            'project_sum': forms.NumberInput(attrs={'class': 'form-control container-fluid', 'placeholder': 'Стоимость'}),
            'project_created': forms.DateTimeInput(attrs={'class': 'form-control container-fluid', 'placeholder': 'Created', 'input-type': 'date'}),
            # 'project_finished': forms.DateTimeInput(attrs={'class': 'form-control container-fluid', 'placeholder': 'Finished', 'input-type': 'date'}),
            # 'slug': forms.TextInput(attrs={'class': 'form-control container-fluid', 'placeholder': 'Slug'}),
        }