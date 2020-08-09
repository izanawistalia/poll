from django.db import models

# Create your models here.
class expertise(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class candidates(models.Model):
    name = models.CharField(max_length=50, null=True)
    challenges_solved = models.IntegerField(null=True)
    votes = models.IntegerField(default=0, null=True)
    expert = models.ManyToManyField(expertise, through='specialty')

    def __str__(self):
        return self.name

class specialty(models.Model):
    RATINGS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    name = models.ForeignKey(candidates, on_delete = models.CASCADE)
    subject = models.ForeignKey(expertise, on_delete = models.CASCADE)
    rating = models.CharField(max_length=5, choices=RATINGS, null=True)

    class Meta:
        unique_together = [['name', 'subject']]
