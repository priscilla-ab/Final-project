from django.contrib import admin
from .models import Recipe ,Category ,Ingredient

class RecipeAdmin(admin.ModelAdmin):
    list_display = ("id","title","created_date")
    search_fields =["id","title"]

# Register your models here.
admin.site.register(Recipe,RecipeAdmin) 
admin.site.register(Category)
admin.site.register(Ingredient)
