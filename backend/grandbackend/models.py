from django.db import models

# Create your models here.
class AppUser(models.Model):
    name = models.CharField(max_length = 128)
    username = models.CharField(max_length = 128)
    password = models.CharField(max_length = 128)

class AppUserProfile(models.Model):
    app_user = models.OneToOneField(AppUser, on_delete = models.CASCADE)
    dob = models.DateField()
    gender = models.IntegerField() # Male = 0, Female = 1, Other = 2
    weight = models.DecimalField(max_digits=4, decimal_places=1) #Assume max 3 digit weight in kg and 1 decimal place
    height = models.DecimalField(max_digits=4, decimal_places=1)
    activityLevel = models.IntegerField() # Sedantry = 0, Lightly Active = 1, Moderately Active = 2, Very Active = 3
    usersGoal = models.IntegerField() # Increase Weight = 0, 1 = Maintain Weight, 2 = Lose Weight

class FoodItem(models.Model):
    name = models.CharField(max_length = 256)
    energy_100g = models.DecimalField(max_digits = 24, decimal_places = 6)
    cholesterol_100g = models.DecimalField(max_digits = 24, decimal_places = 6)
    carbohydrates_100g = models.DecimalField(max_digits = 24, decimal_places = 6)
    sugars_100g = models.DecimalField(max_digits = 24, decimal_places = 6)
    proteins_100g = models.DecimalField(max_digits = 24, decimal_places = 6)
    mean_pro_car = models.DecimalField(max_digits = 24, decimal_places = 6)
    user_goal_map = models.CharField(max_length = 128)
    activity_map = models.CharField(max_length = 128)

class UserFoodHistory(models.Model):
    user = models.ForeignKey('AppUser', on_delete = models.CASCADE)
    food = models.ForeignKey('FoodItem', on_delete = models.CASCADE) 
    food_time = models.CharField(max_length = 128)
    rating = models.IntegerField()
