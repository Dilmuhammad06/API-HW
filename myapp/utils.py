import re
from rest_framework.validators import ValidationError

uzbekistan_pattern = r'^\+998\d{9}$'
kazakhstan_pattern = r'^\+7\d{10}$'
russia_pattern = r'^\+7\d{10}$'
america_pattern = r'^\+1\d{10}$'
korea_pattern = r'^\+82\d{9,10}$'


def valider(value):

    if re.match(uzbekistan_pattern, value) is not None:
        return 'uzbekistan'
    elif re.match(kazakhstan_pattern, value) is not None:
        return 'kazakhstan'
    elif re.match(russia_pattern, value) is not None:
        return 'russia'
    elif re.match(america_pattern, value) is not None:
        return 'america'
    elif re.match(korea_pattern, value) is not None:
        return 'korea'
    else:
        data = {
            'status':False,
            'message':'Validation Error'
        }
        raise ValidationError(data)
