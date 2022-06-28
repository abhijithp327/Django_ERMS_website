from django.contrib import admin
from empolyee.models import EmpolyeeDetail, EmpolyeeEducation, EmpolyeeExperience


# Register your models here.
admin.site.register(EmpolyeeDetail)
admin.site.register(EmpolyeeEducation)
admin.site.register(EmpolyeeExperience)
