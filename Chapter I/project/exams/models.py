from django.db import models


class Exam(models.Model):
    exam_name = models.CharField(max_length=50, default=None)
    max_points = models.IntegerField(default=None)

    def __str__(self):
        return self.exam_name


class User(models.Model):
    user_name = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.user_name


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, default=None)
    score = models.IntegerField(default=None, unique=True)
