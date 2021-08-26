from django.db import models
from rest_framework import serializers
from rest_framework.fields import Field

from app.models import Aluno


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg',]