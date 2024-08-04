from django.contrib import admin
from .models import Todo,Category ,Tag
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):#function
    list_display=[
        'pk',
        'title',
        'is_active',#This is shown on the admin page.
                 ]
    list_display_links=[#It allows you to click on all of them, like a blue view or a link.
        'pk',
        'title',
    ]
   


class TodoAdmin(admin.ModelAdmin):#function
    list_display=[
        'pk',
        'category',
        'title',
        'is_active',#This is shown on the admin page.
        #'created_at',
        #'updated_at'
                 ]
    list_display_links=[#It allows you to click on all of them, like a blue view or a link.
        'pk',
        'category',
        'title',
    ]
    

admin.site.register(Todo,TodoAdmin)#save admin
admin.site.register(Category,CategoryAdmin)#save admin
admin.site.register(Tag)#save admin