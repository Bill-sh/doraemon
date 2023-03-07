from rest_framework import serializers

from lolin.models import Students, ClassName


class ClassNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassName
        fields = '__all__'


class StudentsSerializer(serializers.ModelSerializer):
    className = ClassNameSerializer(many=False, read_only=True)
    className_id = serializers.IntegerField()

    class Meta:
        model = Students
        fields = '__all__'
