from graphene_django.types import DjangoObjectType
from graphene import ObjectType
import graphene
from .models import Autor

class AutorType(DjangoObjectType):
    class Meta:
        model = Autor

class Query(ObjectType):
    autores = graphene.List(AutorType)
    
    def resolve_autores(self, info, **kwargs):
        return Autor.objects.all()

class Mutation(graphene.ObjectType):
    pass