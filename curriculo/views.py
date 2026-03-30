
from django.shortcuts import render,redirect,get_object_or_404
from .models import Curriculo
from .forms import CurriculoForm
from django.http import HttpResponse
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer


# Create your views here.
def index(request):
    return render(request,'index.html',)


def create(request):
    if request.method == 'POST':
        form = CurriculoForm(request.POST)
        if form.is_valid():
            request.session['curriculo'] = form.cleaned_data
            return redirect('confirmar')
        else:
            if form.errors:
                print(form.errors)
    else:
        form = CurriculoForm()

    return render(request,'cadrastro.html',{'form':form})
    

def get_list(request):
    resumes = Curriculo.objects.all()
    return render(request, 'index.html', {'c': resumes})


def get(request, pk):
    curriculo = Curriculo.objects.get(id=pk)

    experiencia_lista = curriculo.resume_professional.split('\n') if curriculo.resume_professional else []
    educacao_lista = curriculo.curse_certifications.split('\n') if curriculo.curse_certifications else []
    habilidades_lista = curriculo.ability.split('\n') if curriculo.ability else []

    return render(request, 'curriculo.html', {
        'c': curriculo,
        'experiencia_lista': experiencia_lista,
        'educacao_lista': educacao_lista,
        'habilidades_lista': habilidades_lista
    })

def search(request):
    query = request.GET.get('q','')
    result = []

    if query:
        result = Curriculo.objects.filter(name__icontains=query)

    if result:
        c = result.first()

        experiencia_lista = c.resume_professional.split('\n') if c.resume_professional else []
        educacao_lista = c.curse_certifications.split('\n') if c.curse_certifications else []
        habilidades_lista = c.ability.split('\n') if c.ability else []

    else:
        c = None
        experiencia_lista = []
        educacao_lista = []
        habilidades_lista = []

    return render(request, 'curriculo.html', {
        'c': c,
        'experiencia_lista': experiencia_lista,
        'educacao_lista': educacao_lista,
        'habilidades_lista': habilidades_lista
    })

def resume(request):
    return render(request, 'curriculo.html')


def confirmar(request):
    dados = request.session.get('curriculo')

    if not dados:
        return redirect('create')

    experiencia_lista = dados.get('resume_professional', '').split('\n')
    educacao_lista = dados.get('curse_certifications', '').split('\n')
    habilidades_lista = dados.get('ability', '').split('\n')

    return render(request, 'curriculo.html', {
        'c': dados,
        'experiencia_lista': experiencia_lista,
        'educacao_lista': educacao_lista,
        'habilidades_lista': habilidades_lista
    })

def salvar(request):
    dados = request.session.get('curriculo')

    if dados:
        Curriculo.objects.create(**dados)

        # limpa a sessão
        del request.session['curriculo']

        return redirect('index')

    return redirect('create')

def gerar_pdf(request, id):
    curriculo = get_object_or_404(Curriculo, id=id)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="curriculo_{curriculo.name}.pdf"'

    doc = SimpleDocTemplate(response)
    styles = getSampleStyleSheet()

    elementos = []

    elementos.append(Paragraph(f"<b>{curriculo.name}</b>", styles['Title']))
    elementos.append(Spacer(1, 12))

    
    elementos.append(Paragraph(f"Telefone: {curriculo.phone_number}", styles['Normal']))
    elementos.append(Paragraph(f"Email: {curriculo.email}", styles['Normal']))
    elementos.append(Paragraph(f"Endereço: {curriculo.address}", styles['Normal']))
    elementos.append(Spacer(1, 12))

    if curriculo.linkedin:
        elementos.append(Paragraph(f"LinkedIn: {curriculo.linkedin}", styles['Normal']))
    if curriculo.github:
        elementos.append(Paragraph(f"GitHub: {curriculo.github}", styles['Normal']))
    elementos.append(Spacer(1, 12))

   
    elementos.append(Paragraph("<b>Objetivo</b>", styles['Heading2']))
    elementos.append(Paragraph(curriculo.objective, styles['Normal']))
    elementos.append(Spacer(1, 12))

   
    if curriculo.resume_professional:
        elementos.append(Paragraph("<b>Resumo Profissional</b>", styles['Heading2']))
        elementos.append(Paragraph(curriculo.resume_professional, styles['Normal']))
        elementos.append(Spacer(1, 12))

   
    if curriculo.ability:
        elementos.append(Paragraph("<b>Habilidades</b>", styles['Heading2']))
        elementos.append(Paragraph(curriculo.ability, styles['Normal']))
        elementos.append(Spacer(1, 12))

    
    if curriculo.curse_certifications:
        elementos.append(Paragraph("<b>Cursos e Certificações</b>", styles['Heading2']))
        elementos.append(Paragraph(curriculo.curse_certifications, styles['Normal']))
        elementos.append(Spacer(1, 12))

   
    if curriculo.Languages:
        elementos.append(Paragraph("<b>Idiomas</b>", styles['Heading2']))
        elementos.append(Paragraph(curriculo.Languages, styles['Normal']))

    doc.build(elementos)

    return response