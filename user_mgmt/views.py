import hashlib
from django.shortcuts import redirect, render
from django.views.generic import View
from django.http import HttpResponse
from . models import User


# Create your views here.
class UserLoginView(View):
    def get(self, request):
        return render(request, "login1.html")

    def post(self, request):
        user_name = request.POST.get("user_name")
        password_hash = hashlib.sha256(request.POST.get("password").encode('utf-8')).hexdigest()
        password = request.POST.get("password")
        user = User.objects.filter(user_name=user_name, password=password_hash).first()

        if user:
            request.session["current_user"]={
                "user_name": user.user_name,
                "role": user.role,
            }
            return redirect('home')
        return HttpResponse("<h1>Invalid User Name Password</h1>")


class UserLoginOutView(View):
    def get(self, request):
        request.session["current_user"] = None
        return redirect("/login")



class UserAddView(View):
  #  @auth_required
    def get(self, request, *args, **kwargs):
        return render(request, "useradd.html")

    def post(self, request, *args, **kwargs):
        data = {
            "user_name": request.POST.get("user_name"),
            "password": hashlib.sha256(request.POST.get("password").encode('utf-8')).hexdigest(),
            "role": "admin",
        }
        user = User.objects.create(**data)
        user.save()
        print("Sign Up Successfull")
        return redirect('/login')


