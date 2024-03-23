from django.db import models


class FeishuUser(models.Model):
    user_uuid = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    user_name_eng = models.CharField(max_length=20)

    feishu_user_id = models.CharField(max_length=20)

    def __str__(self):
        return self.user_name_eng


class FeishuGroupBot(models.Model):
    group_name = models.CharField(max_length=20)
    bot_id = models.CharField(max_length=20)
    bot_secret = models.CharField(max_length=20)

    def __str__(self):
        return self.group_name
