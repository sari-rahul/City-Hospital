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
        labels = {
            'p_name': "Patient's Name",
            'p_email': "Patient's Email",
            'p_phone': "Patient's Phone number",
            'doc_name': "Doctor's Name",
            'booking_date': "Booking Date",
        }


       
