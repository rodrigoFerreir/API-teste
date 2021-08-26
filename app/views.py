from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from app.models import Aluno
from app.serializer import AlunoSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

#Controller