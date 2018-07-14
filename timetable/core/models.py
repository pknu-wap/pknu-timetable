from django.db import models


class Subject(models.Model):
    target_college = models.CharField(max_length=30, blank=True)
    target_department = models.CharField(max_length=30)
    no = models.CharField(max_length=10)
    division = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    eng_name = models.CharField(max_length=50)
    point = models.IntegerField()
    point_system = models.CharField(max_length=5)
    type = models.CharField(max_length=10)
    quota = models.IntegerField()
    is_FL = models.BooleanField()
    professor = models.CharField(max_length=30, blank=True)
    day_night = models.CharField(max_length=10)
    grade = models.IntegerField()
    time_and_location = models.CharField(max_length=50)
    department = models.CharField(max_length=30)

    def __str__(self):
        return '%s (%s-%s)' % (self.name, self.no, self.division)
