from rest_framework import serializers
from .models import Plate
import re


class PlateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        required=True
    )

    class Meta:
        model = Plate
        fields = '__all__'
        # fields = ('title', '_id')

    def validate_title(self, value):
        # print(f"Значение '{value}'")
        # compiling the pattern for alphanumeric string
        pattern = re.compile(r"^[АВЕКМНОРСТУХABEKMHOPCTYX]\d{3}[АВЕКМНОРСТУХABEKMHOPCTYX]{2}\d{2,3}$", re.I)
        print(re.fullmatch(pattern, str(value)))
        if not (re.fullmatch(pattern, str(value))):
            raise serializers.ValidationError(
                detail=' The plate is not in standard ',
                code='500')
        return value
