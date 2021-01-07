from rest_framework import serializers

from .models import OnlineShoppersIntentions
from .field_choices import *


class OnlineShoppersIntentionsSerializer(serializers.Serializer):

    Administrative = serializers.IntegerField()  # administrative pages visited
    AdministrativeDuration = serializers.FloatField()   #time spent on administrative pages
    Informational = serializers.IntegerField()  # ajouter les commentaires explicatifs
    InformationalDuration = serializers.FloatField()
    ProductRelated = serializers.IntegerField()
    ProductRelatedDuration = serializers.FloatField()
    SpecialDay = serializers.FloatField()
    Month = serializers.ChoiceField(choices=MONTH_CHOICES)
    OperatingSystems = serializers.IntegerField()
    Browser = serializers.IntegerField()
    Region = serializers.IntegerField()
    VisitorType = serializers.ChoiceField(VISITOR_TYPE_CHOICES)
    Weekend = serializers.BooleanField()
    Revenue = serializers.BooleanField(allow_null=True)  # target field

    def create(self, validated_data):
        """Create and return a new `OnlineShoppersIntentions` instance, given the validated data."""
        return OnlineShoppersIntentions.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass
        #ici j'ai mis en commentaire, j'avais oublié que j'avais pas changé (c'était pas le plus important)

        """
        #Update and return an existing `House` instance, given the validated data.
        instance.CRIM = validated_data.get('CRIM', instance.CRIM)
        instance.ZN = validated_data.get('ZN', instance.ZN)
        instance.INDUS = validated_data.get('INDUS', instance.INDUS)
        instance.CHAS = validated_data.get('CHAS', instance.CHAS)
        instance.NOX = validated_data.get('NOX', instance.NOX)
        instance.RM = validated_data.get('RM', instance.RM)
        instance.AGE = validated_data.get('AGE', instance.AGE)
        instance.DIS = validated_data.get('DIS', instance.DIS)
        instance.RAD = validated_data.get('RAD', instance.RAD)
        instance.TAX = validated_data.get('TAX', instance.TAX)
        instance.PTRATIO = validated_data.get('PTRATIO', instance.PTRATIO)
        instance.B = validated_data.get('B', instance.B)
        instance.LSTAT = validated_data.get('LSTAT', instance.LSTAT)
        # instance.MEDV = validated_data.get('MEDV' , instance.MEDV )
        instance.save()
        return instance
        """
