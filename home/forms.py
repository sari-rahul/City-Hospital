from django import forms
from .models import Bookings


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = '__all__'
        widgets = {
            'booking_date': DateInput()
        }