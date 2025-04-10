from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(default="cake")
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
        


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    ingredient = models.ManyToManyField(Ingredient)
    instruction = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    preparation_time = models.IntegerField()
    cooking_time = models.IntegerField()
    serving = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    tools = models.TextField()
    photo_url = models.CharField(max_length=255)

    def __str__(self):
        return self.title





   

