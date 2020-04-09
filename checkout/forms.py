from django import forms
from .models import UserOrder


class PaymentForm(forms.Form):
    """
    Payment section in the checkout for users
    """
    MONTH_CHOICES = [(month, month) for month in range(1, 12)]
    YEAR_CHOICES = [(year, year) for year in range(2020, 2036)]

    credit_card_number = forms.CharField(
        label="Credit/Debit Card Number:",
        required=False
    )
    cvv = forms.CharField(label="CVV:", required=False)
    expiry_month = forms.ChoiceField(label="Month:", choices=MONTH_CHOICES,
                                     required=False)
    expiry_year = forms.ChoiceField(label="Year:", choices=YEAR_CHOICES,
                                    required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    class Meta:
        model = UserOrder
        fields = (
            "first_name",
            "last_name",
            "phone_number",
            "country",
            "town_or_city",
            "street_address1",
            "street_address2",
            "county",
            "postcode"
        )
