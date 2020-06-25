from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=10, null=True)
    real_name = models.CharField(max_length=20, null=True)
    tz = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.user_id


class Activity_Period(models.Model):
    start_time = models.DateTimeField(auto_now=False, null=True)
    end_time = models.DateTimeField(auto_now=False, null=True)
    time = models.ManyToManyField(User, related_name='activity_period')
