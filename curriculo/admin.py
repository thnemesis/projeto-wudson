from django.contrib import admin
from curriculo.models  import Curriculo,Address,ProfessionalExperience,Phone,AcademicEducation

# Register your models here.
@admin.register(Curriculo)
class CurriculoAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email','phone_number')


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id','dd','number')

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id','uf','city')


@admin.register(ProfessionalExperience)
class ProfessionalExperienceAdmin(admin.ModelAdmin):
    list_display = ('id','curriculo','company_name','role')

@admin.register(AcademicEducation)
class AcademicEducationAdmin(admin.ModelAdmin):
    list_display = ('id','curriculo','course','institution')