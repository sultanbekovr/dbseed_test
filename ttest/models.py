from django.db import models

class ForTest(models.Model):
    POSITIONS = (
        ('1', 'Junior Developer'),
        ('2', 'Middle Developer'),
        ('3', 'Senior Developer'),
        ('4', 'Team Lead'),
        ('5', 'Director')
    )

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    position = models.CharField(max_length=25, choices=POSITIONS)
    date_of_receipt = models.DateField()
    salary = models.IntegerField()
    head = models.ForeignKey('ForTest', on_delete=models.SET_NULL, null=True)
