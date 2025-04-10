import django_filters
from .models import Recipe

class Recipefilters(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name="category__slug",lookup_expr="iexact")
    class Meta:
        model = Recipe
        fields = {
            "title":["iexact","icontains"],
            # "category__slug":["exact"],
            "ingredient":["iexact","icontains"],
            "preparation_time":["iexact","icontains"],
            "cooking_time":["iexact","icontains"],
            "serving":["exact"]}
        





