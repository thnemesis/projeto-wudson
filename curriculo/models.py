from django.db import models

# Create your models here.
class Phone(models.Model):
    dd = models.CharField(max_length=2,null=False,blank=False)
    number = models.CharField(max_length=9,null=False,blank=False)

    def __str__(self):
        return f'{self.dd} {self.number}'


class Address(models.Model):
    uf = models.CharField(max_length=2,null=False,blank=False)
    city = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return f'{self.city} - {self.uf}'

class Curriculo(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    phone_number = models.CharField(max_length=100,null=False,blank=False)
    email = models.EmailField(max_length=100,null=False,blank=False)
    address = models.CharField(max_length=100,null=False,blank=False)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    objective = models.TextField(max_length=255,blank=False, null=False)
    resume_professional = models.TextField(max_length=500,blank=True, null=True)
    ability = models.TextField(max_length=255,blank=True, null=True)
    curse_certifications = models.TextField(max_length=455,blank=True, null=True)
    Languages = models.CharField(max_length=100,blank=True, null=True)




    def __str__(self):
        return f'{self.name}'

class AcademicEducation(models.Model):
    curriculo = models.ForeignKey(
        Curriculo,
        on_delete=models.CASCADE,
        related_name='educations'
    )

    course = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        return f'{self.course} {self.institution} {self.start_year} {self.end_year}'


class ProfessionalExperience(models.Model):
    curriculo = models.ForeignKey(
        Curriculo,
        on_delete=models.CASCADE,
        related_name='experiences'
    )
    company_name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    stat_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True)
    activities = models.TextField()

    def __str__(self):
        return f'{self.role} - {self.company_name}'



