from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(AllJobsStats)
admin.site.register(FullStackStats)
admin.site.register(StatsImages)