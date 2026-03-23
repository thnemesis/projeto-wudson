
from django.shortcuts import render,redirect
from .models import Curriculo
from .forms import CurriculoForm

# Create your views here.
def index(request):
    return render(request,'index.html',)


def create(request):
    if request.method == 'POST':
        form = CurriculoForm(request.POST)
        print('//////////////////////////////////////////////////////////////')
        print(form.is_valid())
        if form.is_valid():
            print('//////////////////////////////////////////////////////////////')

            form.save()
            return redirect('index')
        else:
            if form.errors:
                print(form.errors)
    else:
        form = CurriculoForm()

    return render(request,'cadrastro.html',{'form':form})
    

def get_list(request):
    resumes = Curriculo.objects.all()
    return render(request, 'index.html', {'c': resumes})


def get(request,pk):
    resumes = Curriculo.objects.filter(id=pk)
    print(resumes)
    return render(request, 'curriculum.html', {'c': resumes[0]})


def search(request):
    query = request.GET.get('q','')
    print(query)
    result = []
    if query:
        result = Curriculo.objects.filter(name__icontains=query)
    if result:
        c = result.first()
    else:
        c = None
    return render(request, 'conclusao.html', {'c': c})




"""
print('--------------------------------curriculum-------------------------------')
        print(c.first_name)
                {{c.first_name}}
                
        print(c.last_name)
                {{curriculum.last_namecurriculum.last_name}}
                
        print(c.email)
                {{c.email}}
                
        print(c.github)
            {{c.github}}
            
        print(c.address)
            {{c.address}}
            
        print(c.resume_professional)
            {{c.resume_professional}}
            
        print(c.curse_certifications)
            {{c.curse_certifications}}0,,,,,,,,,,
01            
        print(c.linkedin)
            {{c.linkedincurriculum.linkedin}}
            
        print(c.objective)
            {{c.objective}}
            
        print(c.phone_number) 
            {{c.phone_number}}
            
        print(c.ability)
            {{c.ability}}
            
        print(c.Languages)
            {{c.Languages}}
print('--------------------------------curriculum-------------------------------')
"""