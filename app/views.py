from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request, "home.html")        
# Create your views here.

class MyView(APIView):
    def get(self, request):
        return Response({"message": "Hello, Docker!"})


