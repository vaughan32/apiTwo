from rest_framework import serializers
from RestApi.models import Worker

class WorkerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'