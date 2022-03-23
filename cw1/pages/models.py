from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=30, unique=True)
    pwd = models.CharField(max_length=90)
    def __str__(self):
        return self.username

class Professor(models.Model):
    p_code = models.CharField(max_length=10, unique=True)
    p_Name = models.CharField(max_length=20)
    def __str__(self):
        return self.p_code

class Module(models.Model):
    m_code = models.CharField(max_length=10)
    m_name = models.CharField(max_length=60)
    m_year = models.IntegerField()
    m_semester = models.IntegerField()
    prof_module = models.ManyToManyField('Professor')
    def __str__(self):
        return "%s, %d, %d" % (self.m_code, self.m_year, self.m_semester)

    class Meta:
        unique_together = ['m_code', 'm_name', 'm_year','m_semester']

class Rating(models.Model):
    rating = models.FloatField()
    module = models.ForeignKey('Module', related_name="m_rate", on_delete=models.CASCADE)
    professor = models.ForeignKey('Professor', related_name='p_rate', on_delete=models.CASCADE)
    def __str__(self):
        return "%s, %s %f" % (self.module.m_name, self.professor.p_Name, self.rating)
