from django import forms

from orders.models import Order


class CartAddProductForm(forms.Form):
    duration = forms.TypedChoiceField(
        choices=[(i, str(i)) for i in range(1, 13)],
        coerce=int, widget=forms.Select(attrs={'class': 'form-select mb-2'}),
    )

    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'first_name',
            'last_name',
            'email',
            'address',
            'postal_code',
            'city',
            'state',
        )

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
        }
