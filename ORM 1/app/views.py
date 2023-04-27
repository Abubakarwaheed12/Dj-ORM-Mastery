from django.shortcuts import render
from app.models import Students , Teacher 
from django.db.models import Q

# for used raw sql to insert data 

from django.db import connection
# Create your views here.



def home(request):
    students=Students.objects.all().order_by('age')
    
    
    if request.method=='GET':
        min=(request.GET.get('min'))
        max=request.GET.get('max')
        
        
        if min:
            students=Students.objects.filter( Q(age__gte=int(min))).order_by('age')
        
        if max:
            students=Students.objects.filter(Q(age__lte=int(max))).order_by('age')
          
        if min and max:
            students=Students.objects.filter(Q(age__lte=int(max)) & Q(age__gte=int(min))).order_by('age')
            print(students)
            
          
            
        if min==None and max==None:
            min=''
            max=''
            
    context={
        'students':students,
    }
    reh = Students.objects.get(name='rehman')
    print(reh.teacher.all())
    return render(request, 'home/index.html' , context=context)
