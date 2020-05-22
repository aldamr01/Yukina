# Django
from django import forms 

# Application
from app.dashboard.app_models.dashboard import SensorConfig

class SensorConfigUpdateForm(forms.ModelForm):
    min_tds = forms.FloatField(
        min_value= 1,
        max_value= 2000,        
        widget= forms.NumberInput(
            attrs= {
                'class': 'form-control',
                'type': 'number'
            }
        ),
        required= True,
    )
    max_tds = forms.FloatField(
        min_value= 1,
        max_value= 2000,
        widget= forms.NumberInput(
            attrs= {
                'class': 'form-control',
                'type': 'number'
            }
        ),
        required= True,
    )
    min_ph = forms.FloatField(
        min_value= 1,
        max_value= 12,
        widget= forms.NumberInput(
            attrs= {
                'class': 'form-control',
                'type': 'number'
            }
        ),
        required= True,
    )
    max_ph = forms.FloatField(
        min_value= 1,
        max_value= 12,
        widget= forms.NumberInput(
            attrs= {
                'class': 'form-control',
                'type': 'number'
            }
        ),
        required= True,
    )
    min_humidity = forms.FloatField(
        min_value= 1,
        max_value= 100,
        widget= forms.NumberInput(
            attrs= {
                'class': 'form-control',
                'type': 'number'
            }
        ),
        required= True,
    )
    max_humidity = forms.FloatField(
        min_value= 1,
        max_value= 100,
        widget= forms.NumberInput(
            attrs= {
                'class': 'form-control',
                'type': 'number'
            }
        ),
        required= True,
    )
    min_water_temperature = forms.FloatField(
        min_value= 1,
        max_value= 50,
        widget= forms.NumberInput(
            attrs= {
                'class': 'form-control',
                'type': 'number'
            }
        ),
        required= True,
    )
    max_water_temperature = forms.FloatField(
        min_value= 1,
        max_value= 50,
        widget= forms.NumberInput(
            attrs= {
                'class': 'form-control',
                'type': 'number'
            }
        ),
        required= True,
    )
    min_air_temperature = forms.FloatField(
        min_value= 1,
        max_value= 50,
        widget= forms.NumberInput(
            attrs= {
                'class': 'form-control',
                'type': 'number'
            }
        ),
        required= True,
    )
    max_air_temperature = forms.FloatField(
        min_value= 1,
        max_value= 50,
        widget= forms.NumberInput(
            attrs= {
                'class': 'form-control',
                'type': 'number'
            }
        ),
        required= True,
    )
    
    class Meta:
        model = SensorConfig
        fields = ('max_air_temperature', 'min_air_temperature',
                  'min_water_temperature', 'max_water_temperature',
                  'min_humidity', 'max_humidity',
                  'min_tds', 'max_tds',
                  'min_ph', 'max_ph',)
        