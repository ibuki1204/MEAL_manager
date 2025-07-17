from django.db import models
from django.contrib.auth.models import User

class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # 朝食/昼食/夕食など
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='meal_photos/', null=True, blank=True)
    calories = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbs = models.FloatField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.name} on {self.date}"

class WeightRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.weight} kg on {self.date}"

class Goal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    target_weight = models.FloatField()

    def __str__(self):
        return f"Target: {self.target_weight} kg"

