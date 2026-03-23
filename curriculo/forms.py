from django import forms
from .models import Curriculo, Address, Phone, AcademicEducation, ProfessionalExperience


class CurriculoForm(forms.ModelForm):
    class Meta:
        model = Curriculo
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu nome'
            }),

            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu Telefone'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu email'
            }),

            'linkedin': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://linkedin.com/in/seu-perfil'
            }),

            'github': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://github.com/seu-usuario'
            }),

            'objective': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descreva seu objetivo profissional'
            }),

            'resume_professional': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Resumo profissional'
            }),

            'ability': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Ex: Python, Django, JavaScript'
            }),

            'curse_certifications': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Cursos e certificações'
            }),

            'Languages': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Português, Inglês'
            }),
        }
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'Email',
            'linkedin': 'LinkedIn',
            'github': 'GitHub',
            'objective': 'Objetivo Profissional',
            'resume_professional': 'Resumo Profissional',
            'ability': 'Habilidades',
            'curse_certifications': 'Cursos e Certificações',
            'Languages': 'Idiomas'
        }




class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = '__all__'


class AcademicEducationForm(forms.ModelForm):
    class Meta:
        model = AcademicEducation
        fields = '__all__'


class ProfessionalExperienceForm(forms.ModelForm):
    class Meta:
        model = ProfessionalExperience
        fields = '__all__'