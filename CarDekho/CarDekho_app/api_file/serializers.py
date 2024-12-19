from rest_framework import serializers
from ..models import Carlist,Showroomlist,Review

def alphanumeric(value):
    if not str(value).isalnum:
        raise serializers.ValidationError("Only Alphanumeric Characters Are Allowed")

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class CarSerializer(serializers.ModelSerializer):

    # neeche vala code models serializer ka hai isse aapko models ke fields ko one by one likhna nahi padta isliye model serializer ka use karte hai neeche vala code likhna nahi padta model serializer ke madad
    # se models mai jitna field hota hai automatic serializer mai create hota hai aur 
    # create or update bhi automatic hota hai model serializer ke madad se....

    Reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Carlist
        fields = "__all__"    # __all__ isse automatic sare fields le lega models ka







    # neeche vala code serializer ka hai jaisa model mai field banate hai vaise hi same field serializer mai banana padta hai... 


    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField()
    # description = serializers.CharField()
    # active = serializers.BooleanField(read_only=True)
    # chassisnumber = serializers.CharField(validators = [alphanumeric])
    # price = serializers.DecimalField(max_digits=9, decimal_places=2)

    # def create(self, validated_data):
    #     return Carlist.objects.create(**validated_data)
    

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description',instance.description)
    #     instance.active = validated_data.get('active',instance.active)
    #     instance.chassisnumber = validated_data.get('chassisnumber',instance.chassisnumber)
    #     instance.price = validated_data.get('price',instance.price)
    #     instance.save()
    #     return instance
    
    def validate_price(self, value):
        if value <= 20000.00:
            raise serializers.ValidationError("Price must be greater than 20000.00")
        return value
    
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name And Description Must Be Different")
        
        return data


class ShowroomSerializer(serializers.ModelSerializer):
    Showrooms = serializers.StringRelatedField(many=True)
    class Meta:
        model = Showroomlist
        fields = "__all__"



