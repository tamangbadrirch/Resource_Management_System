from django.shortcuts import redirect, render
from CRUD import auth_required
#from django.contrib.auth.models import User, auth
from CRUDApp.models import Employees

def INDEX(request):
    emp = Employees.objects.all() #getting data of tables
    empCount = emp.count()
    context={       #dictionary banayeko
        'emp': emp,
        'empCount': emp.count(),
    }
    return render(request,'index.html',context) #passing the disctionary to template

#landingpage
def LANDING(request):
     return render(request,'landing.html')
# class UserSearchView(View):
#     #@auth_required
#     def post(self, request, *args, **kwargs):
#         category=request.POST.get("category",None)
#         result=CRUDApp_Employees.objects.filter(category__icontains=category)
#         return redirect("/login")

@auth_required
def INDEX(request,*args,**kwargs):
    user_session=request.session.get("current_user",None)
    emp = Employees.objects.filter(username=user_session['user_name']).all() #getting data of tables
    empCount = emp.count()
    context={       #dictionary banayeko
        'emp': emp,
        'empCount': emp.count(),
        'result':None
    }
    print(context,user_session)
    return render(request,'index.html',context)


#landingpage
def SEARCH(request):
    user_session=request.session.get("current_user",None)
    category = request.POST.get("category", None)
    result=Employees.objects.filter(category__icontains=category,username=user_session['user_name'])
    # emp = Employees.objects.all()  # getting data of tables
    context = {  # dictionary banayeko
        'emp': result,
        # 'empCount': emp.count(),
        # 'result':result,
    }
    print(context)
    return render(request, 'index.html', context)

    # return render(request,'search.html')

def LOGOUT(request):
    request.session["current_user"] = None
    return redirect('landing')

#for adding records
def ADD(request):
    if request.method == "POST":
        user_session = request.session.get("current_user", None)
        name = request.POST.get('name')
        category = request.POST.get('category')
        url = request.POST.get('url')
        description = request.POST.get('description')
        # print(name,category,url,description) #for testing
        #creating variables & saving data
        emp = Employees(
            username = user_session['user_name'],
            name = name,
            category = category,
            url = url,
            description = description
        )
        emp.save()
        return redirect('home')

    return render(request,'index.html')

#for edit
def EDIT(request):
    emp = Employees.objects.all()
    context={
        'emp': emp,
    }
    return redirect(request,'index.html',context)

#for update query
def UPDATE(request,id):
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        url = request.POST.get('url')
        description = request.POST.get('description')

        data = {
            'id': id,
            'name': name,
            'category': category,
            'url' : url,
            'description':  description,
        }
        Employees.objects.filter(id=id).update(**data)

        # data.save()
        return redirect('home')
    #
    # return redirect(request,'index.html')

#for delete query
def DELETE(request,id):
    emp = Employees.objects.filter(id = id)
    emp.delete()

    context = {
        'emp':emp,
    }
    return redirect('home')