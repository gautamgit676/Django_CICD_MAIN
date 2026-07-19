from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from app.models import * 
# Create your views here.

def Home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        place = request.POST.get("place")
        image = request.FILES.get("image")

        Student.objects.create(name=name,place=place,image=image,)
        return redirect("home")  # or redirect("/") if that's your URL

    students = Student.objects.all()
    return render(request,"home.html",{"students": students,},)  


# Create your views here.

class MyView(APIView):
    def get(self, request):
        return Response({"message": "Hello, Docker!"})


