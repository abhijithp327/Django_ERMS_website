from django.shortcuts import redirect, render
from.models import *
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def Index(request):
    return render(request, 'index.html')


def Signup(request):
    error = ""
    if request.method =="POST":
        fn = request.POST['firstname']
        ln =request.POST['lastname']
        ec =request.POST['empcode']
        em =request.POST['email']
        pw =request.POST['pwd']
        
        try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username=em, password=pw)
            EmpolyeeDetail.objects.create(user = user, empcode = ec)
            EmpolyeeEducation.objects.create(user = user)
            EmpolyeeExperience.objects.create(user = user)
            error = "no"
            
        except:
            error = "yes"
            
            
        
            
    return render(request, 'signup.html',locals())


def Emp_Login(request):
    error =""
    if request.method == 'POST':
        u = request.POST['emailid']
        p = request.POST['password']
        User = authenticate(username = u, password = p)
        
        if User:
            login(request,User)
            error = "no"
            
        else:
            error = "yes"
            
            
            
    return render(request, 'emp_login.html', locals())



def Emp_Home(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    return render(request, 'emp_home.html')




def Profile(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    User = request.user
    employee = EmpolyeeDetail.objects.get(user=User)
    if request.method =="POST":
        fn = request.POST['firstname']
        ln =request.POST['lastname']
        ec =request.POST['empcode']
        dp =request.POST['department']
        de =request.POST['designation']
        co =request.POST['contact']
        jd =request.POST['jdate']
        gen =request.POST['gender']
        
        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.empcode = ec
        employee.empdept = dp
        employee.designation = de
        employee.contact = co
        employee.gender = gen
        
        if jd:
            employee.joiningdate = jd
           
        

        try:
            employee.save()
            employee.user.save()
            error = "no"
            
        except:
            error = "yes"
            
            
        
            
    return render(request, 'profile.html', locals())




def Logout(request):
    logout(request)
    return redirect('index')



def Admin_Login(request):
    return render(request, 'admin_login.html')




def My_Experience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    
    User = request.user
    experience = EmpolyeeExperience.objects.get(user=User)
    
    return render(request, 'myexperience.html',locals())




def Edit_Experience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    User = request.user
    experience = EmpolyeeExperience.objects.get(user=User)
    
    if request.method == "POST":
        company1name = request.POST['company1name']
        company1desig = request.POST['company1desig']
        company1salary = request.POST['company1salary']
        company1duration = request.POST['company1duration']
        
        
        company2name = request.POST['company2name']
        company2desig = request.POST['company2desig']
        company2salary = request.POST['company2salary']
        company2duration =request.POST['company2duration']
        
        
        
        company3name = request.POST['company3name']
        company3desig = request.POST['company3desig']
        company3salary = request.POST['company3salary']
        company3duration =request.POST['company3duration']
        
        experience.company1name = company1name
        experience.company1desig = company1desig
        experience.company1salary = company1salary
        experience.company1duration = company1duration
        
        experience.company2name = company2name
        experience.company2desig = company2desig
        experience.company2salary = company2salary
        experience.company2duration = company2duration
        
        experience.company3name = company3name
        experience.company3desig = company3desig
        experience.company3salary = company3salary
        experience.company3duration = company3duration
        
        

        try:
            experience.save()
            error = "no"
        except:
            error = "yes"
            
            
    return render(request, 'edit_experience.html',locals())






def My_Education(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    
    User = request.user
    education = EmpolyeeEducation.objects.get(user=User)
    
    return render(request, 'my_education.html',locals())




def Edit_Education(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    User = request.user
    education = EmpolyeeEducation.objects.get(user=User)
    
    if request.method == "POST":
        coursepg = request.POST['coursepg']
        schoolclgpg = request.POST['schoolclgpg']
        yearofpassingpg = request.POST['yearofpassingpg']
        percentagepg = request.POST['percentagepg']
        
        
        coursegra = request.POST['coursegra']
        schoolclggra = request.POST['schoolclggra']
        yearofpassingra = request.POST['yearofpassingra']
        percentagegra =request.POST['percentagegra']
        
        
        
        coursessc= request.POST['coursessc']
        schoolclgssc= request.POST['schoolclgssc']
        yearofpassingssc= request.POST['yearofpassingssc']
        percentagessc=request.POST['percentagessc']
        
        
        coursehsc=request.POST['coursehsc']
        schoolclghsc= request.POST['schoolclghsc']
        yearofpassinghsc= request.POST['yearofpassinghsc']
        percentagehsc=request.POST['percentagehsc']
        
        
        
        
        education.coursepg = coursepg
        education.schoolclgpg = schoolclgpg
        education.yearofpassingpg = yearofpassingpg
        education.percentagepg =   percentagepg
        
        
        
        education.coursegra = coursegra
        education.schoolclggra = schoolclggra
        education.yearofpassingra = yearofpassingra
        education.percentagegra =   percentagegra
        
        
        education.coursessc = coursessc
        education.schoolclgssc = schoolclgssc
        education.yearofpassingssc = yearofpassingssc
        education.percentagessc =   percentagessc
        
        
        
        education.coursehsc = coursehsc
        education.schoolclghsc = schoolclghsc
        education.yearofpassinghsc = yearofpassinghsc
        education.percentagehsc =   percentagehsc
        
        
        try:
            education.save()
            error = "no"
        except:
            error = "yes"
            
            
    return render(request, 'edit_education.html',locals())




def Change_Password(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
   
   
    User = request.user
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        
        
        
        
        try:
            if User.check_password(c):
                User.set_password(n)
                User.save()
                error = "no"
            else:
                error = "not"
                
        except:
            error = "yes"
            
            
    return render(request, 'change_password.html',locals())




def Admin_Login(request):
    error =""
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['pwd']
        User = authenticate(username = u, password = p)
        try:
            if User.is_staff:
                login(request,User)
                error = "no"
            
            else:
                error = "yes"
            
        except:
            error = "yes"
            
    return render(request, 'admin_login.html', locals())




def Admin_Home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin_home.html')



def Change_Passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
   
   
    User = request.user
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        
        
        
        
        try:
            if User.check_password(c):
                User.set_password(n)
                User.save()
                error = "no"
            else:
                error = "not"
                
        except:
            error = "yes"
            
            
    return render(request, 'change_passwordadmin.html',locals())





def All_Employee(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    employee = EmpolyeeDetail.objects.all()
    return render(request, 'all_employee.html',locals())














