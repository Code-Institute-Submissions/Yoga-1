from django.contrib import admin
from .models import Course


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'coursedate',
        'price',
        'rating',
    )

    ordering = ('sku',)


admin.site.register(Course, CourseAdmin)

