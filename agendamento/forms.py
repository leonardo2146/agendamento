from django import forms
from .models import Agendamento
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['data', 'espaco', 'descricao']
        widgets = {
            'data' : forms.DateInput(attrs={'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
        super(AgendamentoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Agendar'))