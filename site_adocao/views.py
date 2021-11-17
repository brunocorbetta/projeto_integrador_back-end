from rest_framework import viewsets, generics
from site_adocao.models import Apoio, Cachorro, Gato, Outro
from site_adocao.serializer import ApoioSerializer, CachorroSerializer, GatoSerializer, OutroSerializer

class ApoioViewSet(viewsets.ModelViewSet):
    """Exibindo todos os apoios"""
    queryset = Apoio.objects.all()
    serializer_class = ApoioSerializer

class CachorroViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cachorros"""
    queryset = Cachorro.objects.all()
    serializer_class = CachorroSerializer

class GatoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os gatos"""
    queryset = Gato.objects.all()
    serializer_class = GatoSerializer

class OutroViewSet(viewsets.ModelViewSet):
    """Exibindo todos os outros"""
    queryset = Outro.objects.all()
    serializer_class = OutroSerializer
