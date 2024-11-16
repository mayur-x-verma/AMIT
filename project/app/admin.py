# admin.py
# from .admin_site import MyAdminSite
from django.contrib import admin
from django.apps import apps
from .models import JobApplication, Feedback, Subscriber, JobVacancy
from django.utils.html import format_html



# admin_site = MyAdminSite(name='myadmin')
# @admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subscribed_at')
    search_fields = ('full_name', 'email')
# Customize the admin interface for the JobApplication model
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'college_name', 'marks')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('college_name',)

    def view_resume(self, obj):
        if obj.resume:
            return format_html('<a href="{}">View Resume</a>', obj.resume.url)
        return "No resume uploaded"

    view_resume.short_description = 'Resume'



# Customize the admin interface for the Feedback model
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('email', 'message', 'created_at')
    search_fields = ('email', 'message')
    list_filter = ('created_at',)


# Get all models in the current application
models = apps.get_models()

admin.site.register(JobApplication, JobApplicationAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(JobVacancy)



# Register each model
# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass


