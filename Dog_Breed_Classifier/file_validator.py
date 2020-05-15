import imghdr

from django.forms import ValidationError


def validate_file_extension(value):
    try:
        value_type = imghdr.what(value.file)
    except FileNotFoundError:
        value_type = None
    if (value_type is None):
        raise ValidationError(u'File Type not supported!')
