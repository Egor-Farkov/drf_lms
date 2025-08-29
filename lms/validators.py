from rest_framework.exceptions import ValidationError

valid_word = "youtube.com"


def validate_forbidden_word(value):
    if valid_word not in value.lower():
        raise ValidationError("не содержит youtube.com")
