from django import forms
from .models import Res, Res_1


class ReservationsForm(forms.ModelForm):
    user_name = forms.CharField(max_length=40,
                                widget=forms.TextInput(attrs={'type': 'text', 'name': 'name', 'id': 'name', 'class': 'form-control',
                                                              'placeholder': 'Имя', 'required': 'required',
                                                              'data-rule': 'minlen:4', 'data-msg': 'Please enter at least 4 chars'}))
    user_email = forms.EmailField(
        widget=forms.TextInput(attrs={'type': 'email', 'id': 'email', 'name': 'email', 'class': 'form-control',
                                                              'placeholder': 'Email', 'required': 'required', 'data-rule': 'email', 'data-msg': 'Please enter a valid email'}))

    user_phone = forms.CharField(max_length=15,
                                widget=forms.TextInput(attrs={'type': 'text', 'name': 'phone', 'id': 'phone', 'class': 'form-control',
                                           'placeholder': 'Телефон', 'required': 'required',
                                           'data-rule': 'minlen:4', 'data-msg': 'Please enter at least 4 chars'}))

    user_message = forms.CharField(max_length=400,
                                widget=forms.Textarea(attrs={'type': 'message', 'name': 'message', 'class': 'form-control',
                                                              'rows': '5', 'placeholder': 'Сообщение', 'required': 'required'}))


    class Meta:
        model = Res

        fields = ('your_name', 'your_email',  'date_reg', 'date_time', 'number_tel',  'of_people', 'message')

class MessageForm(forms.ModelForm):
    your_name = forms.CharField(max_length=40,
                                widget=forms.TextInput(attrs={'type': 'text', 'name': 'name', 'class': 'form-control',
                                                              'id': 'name', 'placeholder': 'Имя',
                                                              'required': 'required'}))
    your_email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'email', 'class': 'form-control',
                                                                'name': 'email', 'id': 'email', 'placeholder': 'Email:',
                                                                'required': 'required'}))
    subject = forms.CharField(max_length=40,
                              widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'name': 'subject',
                                                            'id': 'subject', 'placeholder': 'Тема',
                                                            'required': 'required'}))
    message = forms.CharField(max_length=400,
                              widget=forms.Textarea(attrs={'class': 'form-control', 'name': 'message', 'placeholder': 'Сообщение',
                                                           'required': 'required'}))

    class Meta:
        model = Res_1
        fields = ('your_name', 'your_email', 'subject', 'message')