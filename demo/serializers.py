from rest_framework import serializers
from .models import User, Activity_Period


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity_Period
        fields = ['start_time', 'end_time']

class UserSerializer(serializers.ModelSerializer):
    activity_period = ActivitySerializer(many=True)

    class Meta:
        model = User
        fields = ['user_id', 'real_name', 'tz', 'activity_period']
