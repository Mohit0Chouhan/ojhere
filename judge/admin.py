from django.contrib import admin

from .models import Problem , Solution, Test

admin.site.register(Problem)
admin.site.register(Solution)
admin.site.register(Test)