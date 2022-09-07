from rest_framework import serializers
from .models import ForTest

class EmployeeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ForTest
        fields = ['id', 'name', 'surname', 'patronymic', 'position', 'date_of_receipt', 'salary', 'head']


