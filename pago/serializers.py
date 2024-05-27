from rest_framework import serializers
from .models import DatosPago, Boleta

class DatosPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosPago
        fields = '__all__'

class BoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boleta
        fields = '__all__'

    def create(self, validated_data):
        return Boleta.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.fecha_emision = validated_data.get('fecha_emision', instance.fecha_emision)
        instance.cliente = validated_data.get('cliente', instance.cliente)
        instance.total_original = validated_data.get('total_original', instance.total_original)
        instance.moneda_original = validated_data.get('moneda_original', instance.moneda_original)
        instance.total_final = validated_data.get('total_final', instance.total_final)
        instance.moneda_final = validated_data.get('moneda_final', instance.moneda_final)
        instance.estado = validated_data.get('estado', instance.estado)
        instance.save()
        return instance