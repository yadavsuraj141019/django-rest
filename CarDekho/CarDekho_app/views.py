from django.shortcuts import render
from .models import Carlist,Showroomlist
from django.http import JsonResponse
from .api_file.serializers import CarSerializer,ShowroomSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser


# neeche vala code bhi sahi hai aur sahi se work karta hai par is code mai humko json mai convert karne ke liye
# sabse pehle python dictionary mai convert karna padta hai 

# def car_list_view(request):

#     car = Carlist.objects.all()                                               
    
#     data = {
#         'car': list(car.values()),
#     }
#     return JsonResponse(data)     


# neeche vala code se bhi hum data fetch kar sakte hai serializer ke madad se yaha pe humko python dictionary nahi 
# karna padega.....

@api_view(['GET','POST'])
def car_list_view(request):
    if request.method == 'GET':
        car = Carlist.objects.all()
        serializer = CarSerializer(car, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET','PUT','DELETE'])   # PUT is used for update the data
def car_detail_view(request,id):
    if request.method == 'GET':
        car = Carlist.objects.get(id=id)
        serializer = CarSerializer(car)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        car =  Carlist.objects.get(id=id)
        serializer = CarSerializer(car, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    if request.method == 'DELETE':
         car =  Carlist.objects.get(id=id)
         car.delete()
         return Response({"message": "Car deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    



# abhi tak aapne upar jo dekha views vo function based view tha aur neeche vala class based view hai....

 
class Showroom_View(APIView):

    # BasicAuthentication Code Are Below:

    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAdminUser]
    #permission_classes = [AllowAny]
    #permission_classes = [IsAuthenticated]

    # SessionAuthentication Code Are Below

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request):
        showroom = Showroomlist.objects.all()
        serializer = ShowroomSerializer(showroom, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ShowroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        


class Showroom_Details(APIView):

    def get(self, request, id):
        try:
            showroom = Showroomlist.objects.get(id=id)
        except Showroomlist.DoesNotExists:
            return Response({'Error':'Showroom Not Found'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = ShowroomSerializer(showroom)
        return Response(serializer.data)

    def put(self, request, id):
        showroom = Showroomlist.objects.get(id=id)
        serializer = ShowroomSerializer(showroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        showroom = Showroomlist.objects.get(id=id)
        showroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

