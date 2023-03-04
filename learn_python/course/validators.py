from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy


def validate_more_zero(value):
    if value <= 0:
        raise ValidationError(
            gettext_lazy('%(value)s должно быть больше нуля!'),
            params={'value': value},
        )
