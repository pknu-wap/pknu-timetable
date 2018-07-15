from rest_framework import serializers


class SearchSerializer(serializers.Serializer):
    grade = serializers.MultipleChoiceField(choices=[0, 1, 2, 3, 4, 5])
    point = serializers.MultipleChoiceField(choices=[1, 2, 3])
