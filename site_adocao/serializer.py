from rest_framework import serializers
from site_adocao.models import Apoio, Cachorro, Gato, Outro

class ApoioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apoio
        fields = '__all__'

class CachorroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cachorro
        fields = '__all__'

class GatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gato
        fields = '__all__'

class OutroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outro
        fields = '__all__'