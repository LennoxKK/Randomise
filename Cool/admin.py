from django.contrib import admin

# Register your models here.
from .models import Article, BStudyMember,  Groups_BackUp, Reporter, The_member

admin.site.register(Article)
admin.site.register(Reporter)
admin.site.register(The_member)
admin.site.register(BStudyMember)
admin.site.register(Groups_BackUp)