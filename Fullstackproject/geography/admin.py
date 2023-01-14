from django.contrib import admin

# Register your models here.
from geography.models import SalaryInCity, SalaryVacancies, Image

admin.site.register(SalaryInCity)
admin.site.register(SalaryVacancies)
admin.site.register(Image)