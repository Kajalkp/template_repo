from django.shortcuts import render

# Create your views here.
def employeeView(request):
    Ename=input("enter the name ")
    Edesignation=input("enter the designation ")
    Esalary=int(input("enter the salary "))
    Eexp=int(input("enter the expenditure "))
    d={'name':Ename,'desig':Edesignation,'sal':Esalary,'exp':Eexp}
    return render(request,'templateApp2/1.html',d)