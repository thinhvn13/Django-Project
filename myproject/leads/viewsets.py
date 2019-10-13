from rest_framework import viewsets, permissions
from .models import Lead
from .serializers import LeadSerializer

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permissions_class=[
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer