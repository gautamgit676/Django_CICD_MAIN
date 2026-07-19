from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect
from app.models import * 
# Create your views here.

import traceback

def Home(request):
    if request.method == "POST":
        try:
            Student.objects.create(
                name=request.POST.get("name"),
                place=request.POST.get("place"),
                image=request.FILES.get("image"),
            )
            return redirect("home")

        except Exception:
            traceback.print_exc()
            raise

    students = Student.objects.all()
    return render(request, "home.html", {"students": students})

# Create your views here.

class MyView(APIView):
    def get(self, request):
        return Response({"message": "Hello, Docker!"})


