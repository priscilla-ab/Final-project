from rest_framework.generics import ListAPIView ,RetrieveAPIView ,RetrieveUpdateDestroyAPIView,ListCreateAPIView 
from .models import Recipe,Category,Ingredient
from .serializer import Recipeserializer ,Categoryserializer ,Ingredientserializer
from django.contrib.auth.decorators import login_required 
from django.contrib.admin.views.decorators import staff_member_required
from .filters import Recipefilters
from django.utils.decorators import method_decorator

@method_decorator(login_required,name='dispatch')
class ListRecipe(ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = Recipeserializer
    filterset_class = Recipefilters
    

 

@method_decorator(login_required,name='dispatch') 
class DetailRecipe(RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = Recipeserializer

class GetByCategories(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = Recipeserializer
    def get_queryset(self):
        id_object = Category.objects.get(slug = self.kwargs["category_slug"])
        id = id_object.pk
        return super().get_queryset().filter(category_id = id)


class GetByIngredients(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = Recipeserializer
    def get_queryset(self):
        id_object = Ingredient.objects.get(name = self.kwargs["ingredient_name"])
        id = id_object.pk
        return super().get_queryset().filter(ingredient = id)
    
class ListCategories(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = Categoryserializer
    lookup_field = 'name'

@method_decorator(staff_member_required,name='dispatch') 
class Updatedeletecategory(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = Categoryserializer


class ListIngredients(ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class =Ingredientserializer
  
@method_decorator(staff_member_required,name='dispatch')    
class UpdatedeleteIngredient(RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class =Ingredientserializer



    
