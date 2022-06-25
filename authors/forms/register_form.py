from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from utils.django_forms import add_placeholder, strong_password


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Seu usuário')
        add_placeholder(self.fields['email'], 'Seu e-mail')
        add_placeholder(self.fields['first_name'], 'Ex.: John')
        add_placeholder(self.fields['last_name'], 'Ex.: Doe')
        add_placeholder(self.fields['password'], 'Sua senha')
        add_placeholder(self.fields['password2'], 'Repita sua senha')

    username = forms.CharField(
        label='Username',
        help_text=(
            # 'Username must have letters, numbers or one of those @.+-_. '
            # 'The length should be between 4 and 150 characters.'
            'Username precisa conter letras, números e um caractere especial'
            'Deve conter entre 4 e 150 caracteres'
        ),
        error_messages={
            'required': 'Este campo não pode ser vazio',
            'min_length': 'Username deve ter pelo menos 4 caracteres',
            'max_length': 'Username deve ser menor que 150 caracteres',
        },
        min_length=4, max_length=150,
    )
    first_name = forms.CharField(
        error_messages={'required': 'Escreva seu nome'},
        label='Nome'
    )
    last_name = forms.CharField(
        error_messages={'required': 'Escreva seu sobre nome'},
        label='Sobrenome'
    )
    email = forms.EmailField(
        error_messages={'required': 'E-mail é obrigatório'},
        label='E-mail',
        help_text='O email deve ser válido.',
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'Senha não pode ser vazio'
        },
        help_text=(
            'Senha precisa ter pelo menos uma letra maiúscula, '
            'uma letra minúscula e um número. O tamanho deve ser '
            'até 8 caracteres.'
        ),
        validators=[strong_password],
        label='Senha'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        label='Senha2',
        error_messages={
            'required': 'Por favor, repita sua senha'
        },
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError(
                'Email do usuário já esta em uso', code='invalid',
            )

        return email

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            password_confirmation_error = ValidationError(
                'Senha e senha2 precisam ser iguais',
                code='invalid'
            )
            raise ValidationError({
                'password': password_confirmation_error,
                'password2': [
                    password_confirmation_error,
                ],
            })
