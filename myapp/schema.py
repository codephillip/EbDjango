from graphene import ObjectType, Node, Schema
from graphene_django.fields import DjangoConnectionField
from graphene_django.types import DjangoObjectType
from myapp.models import *


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        interfaces = (Node, )


class IngredientNode(DjangoObjectType):
    class Meta:
        model = Ingredient
        interfaces = (Node, )


class Query(ObjectType):
    category = Node.Field(CategoryNode)
    all_categories = DjangoConnectionField(CategoryNode)

    ingredient = Node.Field(IngredientNode)
    all_ingredients = DjangoConnectionField(IngredientNode)


schema = Schema(query=Query)