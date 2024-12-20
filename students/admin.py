from django.contrib import admin
from .models import Student, Parent

class StudentAdmin(admin.ModelAdmin):
    list_display=['id', 'first_name', 'last_name', 'parentDisplay']
    empty_value_display = "__empty__"
    list_filter= ['last_name', 'parent']
    
    fieldsets= [
        [
            'basic_info',
            {
                "fields": ['first_name', 'last_name']
            }
        ],
        [
            'parent info',
            {
                "fields": ['parent'],
                "classes": ["collapse"],
            }
        ]
    ]
    
    @admin.display(empty_value= '__empty__')
    def parentDisplay(self, obj):
        return obj.parent.name

admin.site.register(Student, StudentAdmin)
admin.site.register(Parent)