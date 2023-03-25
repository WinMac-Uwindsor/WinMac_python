from rest_framework import serializers

class FieldSerializer(serializers.Serializer):
    # id = serializers.IntegerField(label = "Enter ID")
    Name = serializers.CharField(label = "Enter Student Name")
    Company = serializers.CharField(label = "Enter Company")
    Role = serializers.CharField(label = "Enter Role")
    Date = serializers.CharField(label = "Enter Date")
    InternshipDuration = serializers.IntegerField(label = "Enter InternshipDuration")
    Intake = serializers.CharField(label = "Enter Intake")