from django.contrib import admin

from .models import Tag,Image,Project,Category,Comment,Donation,Rate,Report


# Register your models here.

class comment_admin(admin.ModelAdmin):
    list_display = ('user','project','comment_message','is_available')
    list_filter = ('project',"user")
    search_fields = ['user__username','user__first_name','project__title']

class project_admin(admin.ModelAdmin):
    list_display = ('title','user','category','average_rating','is_available','is_featured')
    list_filter = ('category','tags',"user")
    search_fields = ['user__username','user__first_name','title']
    
class report_admin(admin.ModelAdmin):
    list_display = ('report_message','user','is_accepted')
    list_filter = ('project__tags',"is_accepted")
    search_fields = ['project__title']

class image_admin(admin.ModelAdmin):
    list_display = ('project',)
    list_filter = ('project__title','project__tags')
    
class donation_admin(admin.ModelAdmin):
    list_display = ('amount','project',"user")
    list_filter = ('project__title','project__tags')

class rate_admin(admin.ModelAdmin):
    list_display = ('project','rate',"user")
    list_filter = ('project__title','project__tags')
    
admin.site.register(Project,project_admin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Image,image_admin)
admin.site.register(Comment,comment_admin)
admin.site.register(Donation,donation_admin)
admin.site.register(Rate,rate_admin)
admin.site.register(Report,report_admin)
