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
        self.fields['project_created'].required = False
        self.fields["project_client"].choices = [("", "Выберите клиента*"),] + list(self.fields["project_client"].choices)[1:]
        # self.fields["project_status"].choices = [("", "Статус проекта"),] + list(self.fields["project_status"].choices)[1:]
        # self.fields['project_finished'].required = False
    class Meta:
        model = Project
        fields = ['project_name', 'project_status', 'project_client', 'project_product', 'project_sum', 'project_created',]
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'input mb-5 is-bordered', 'placeholder': 'Название проекта*'}),
            'project_status': forms.Select(attrs={'class': 'mb-5'}),
            'project_client': forms.Select(attrs={'class': 'mb-5', 'placeholder': 'Клиент'}),
            'project_product': forms.TextInput(attrs={'class': 'input  mb-5 is-bordered', 'placeholder': 'Продукт'}),
            'project_sum': forms.NumberInput(attrs={'class': 'input  mb-5 is-bordered', 'placeholder': 'Стоимость'}),
            'project_created': forms.DateTimeInput(attrs={'class': 'input mb-5 is-bordered', 'placeholder': 'Created', 'input-type': 'date'}),
            # 'project_finished': forms.DateTimeInput(attrs={'class': 'form-control container-fluid', 'placeholder': 'Finished', 'input-type': 'date'}),
            # 'slug': forms.TextInput(attrs={'class': 'form-control container-fluid', 'placeholder': 'Slug'}),
        }
    