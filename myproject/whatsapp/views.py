from rest_framework import viewsets, permissions
from .serializer import  *
from rest_framework import viewsets
from .filters import TaskFilter
from django_filters.rest_framework import  DjangoFilterBackend
from rest_framework.filters import SearchFilter

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = Serializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_class = TaskFilter
    search_fields = ['task_name']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]