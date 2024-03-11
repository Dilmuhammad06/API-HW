from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User
from .utils import valider

class SignUp(serializers.ModelSerializer):
    auth_status = serializers.CharField(required=False,read_only=True)
    county_code = serializers.CharField(required=False,read_only=True)


    def __init__(self,*args,**kwargs):
        super(SignUp,self).__init__(*args,**kwargs)
        self.fields['phone']=serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ('auth_status','county_code','phone_number')

    def validate(self,data):
        user_inp = data.get('phone')

        emf = valider(user_inp)

        if emf == 'uzbekistan':
            data = {
                'phone_number': user_inp,
                'country_code':emf
            }
        elif emf == 'kazakhstan':
            data = {
                'phone_number': user_inp,
                'country_code':emf
            }
        elif emf == 'russia':
            data = {
                'phone_number': user_inp,
                'country_code':emf
            }
        elif emf == 'america':
            data = {
                'phone_number': user_inp,
                'country_code':emf
            }
        elif emf == 'korea':
            data = {
                'phone_number': user_inp,
                'country_code':emf
            }
        else:
            data = {
                'status':False,
                'message':'Validation Error'
            }
            raise ValidationError(data)
        return data