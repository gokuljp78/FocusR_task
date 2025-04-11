from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import user,bank_detials
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from types import SimpleNamespace

# Create your views here.
@api_view(['GET','POST'])
def ret(reqest):
    
    # user_obj = SimpleNamespace(name="test", ac_number=123, mobile=9876543210)
    

    # bal=user.objects.all()
    # # json1={
    # #     'data':list(bal.values())
    # # }
    # # print(bal.values())
        # serializer=UserSerializer(instance=user_obj)
        # print("workinh")
        # return Response(serializer.data)
        # return render(reqest,'firstpage.html')
    if reqest.method == 'GET':
        data = {
        "name": "gokul",
        "ac_number": 1234,
        "mobile": 1234567890
}   

        serializer = UserSerializer(data=data)  
        if serializer.is_valid():
            print(serializer.validated_data)
            return Response(serializer.data) 
    if reqest.method =='POST':
        serializer=UserSerializer(data=reqest.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 

def ret2(reqest,pk):

    return HttpResponse(f"pass key working;;;{pk}") 
