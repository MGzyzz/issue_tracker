from django.forms import ValidationError
import re

def at_lest(string):
    pattern = r'[№%#$%^&*]'

    if re.search(pattern, string):
        raise ValidationError(
            'Your summary contains illegal characters',
            code='Illegal characters',
        )
    elif len(string) > 30:
        raise ValidationError(
            'This value is too long',
            code='too_long',
            params={'length': 5})


def limit_words_description(string):
    if len(string) > 100:
        raise ValidationError(
            'This text contains more than 100 characters',
            code='long description'
        )