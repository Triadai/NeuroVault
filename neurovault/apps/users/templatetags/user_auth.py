from django import template
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from ..forms import UserCreateForm

register = template.Library()


@register.inclusion_tag('registration/_login.html')
def login_form():
    return {'form': AuthenticationForm()}


@register.inclusion_tag('registration/_signup.html')
def signup_form():
    return {'form': UserCreateForm(instance=User())}
