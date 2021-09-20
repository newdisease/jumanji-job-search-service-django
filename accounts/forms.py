from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField


class SignupForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name')
        field_classes = {'username': UsernameField}
        help_texts = {
            'username': None,
        }
