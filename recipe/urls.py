from django.urls import path
from . import views


urlpatterns = [
    path('recipes/',views.ListRecipe.as_view(),name='recipe'),
    path('recipes/<int:pk>/',views.DetailRecipe.as_view(),name='DetailRecipe'),
    path('recipes/category/<slug:category_slug>/',views.GetByCategories.as_view(),name="get_by_category"),
    path('recipes/ingredient/<slug:ingredient_name>/',views.GetByIngredients.as_view(),name="get_by_ingredients"),
    path('categories/',views.ListCategories.as_view(),name="list_categories"),
    path('categories/<int:pk>/',views.Updatedeletecategory.as_view(),name="updatedelete_category"),
    path('ingredients/',views.ListIngredients.as_view(),name="list_ingredients"),
    path('ingredients/<int:pk>/',views.UpdatedeleteIngredient.as_view(),name="updatedelte_ingredient"),

    
        
        
       




 

 

 


]   
