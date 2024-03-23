from django.db import models


class Gpu(models.Model):
    uuid = models.CharField(max_length=100)
    gpu_index = models.IntegerField(primary_key=True)
    gpu_name = models.CharField(max_length=100)

    def __str__(self):
        return self.gpu_name


class Machine(models.Model):
    uuid = models.CharField(max_length=100)
    machine_name = models.CharField(max_length=100)

    def __str__(self):
        return self.machine_name


class User(models.Model):
    uuid = models.CharField(max_length=100)
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_name_eng = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100)
    total_time = models.IntegerField()

    def __str__(self):
        return self.user_name_eng


class UsageRecord(models.Model):
    user_id = models.IntegerField()
    gpu_id = models.IntegerField()
    machine_id = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    usage_time = models.IntegerField()

