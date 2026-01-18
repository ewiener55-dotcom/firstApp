from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class RateActivity(models.Model):
    Title = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='images/')
    Rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title

