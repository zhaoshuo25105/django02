from django.contrib import admin
from .models import *
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name','age','email']
    list_display_links = ('name','email')
    list_editable = ['age']
    search_fields = ('name',)
    list_filter = ('name',)
    fieldsets = (
        (
            '基本选项',{
                'fields':('name','age')
            }
        ),
        (
            '高级选项',{
                'fields':('email','picture'),
                'classes':('collapse',)
            }
        )
    )



class BookAdmin(admin.ModelAdmin):
    list_display = ['title','publicate']
    date_hierarchy = "publicate"

admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Publisher)
admin.site.register(Wife)




