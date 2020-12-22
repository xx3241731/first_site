from django.contrib import admin
from mysite.models import Post
from mysite.models import AccessInfo, StoreIncome, Branch

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')

admin.site.register(Post, PostAdmin)

admin.site.register(AccessInfo)

class BranchAdmin(admin.ModelAdmin):
    list_display = ('title','name')
admin.site.register(Branch,BranchAdmin)

class StoreIncomeAdmin(admin.ModelAdmin):
    list_display = ('branch', 'income_year', 'income_month','income')

admin.site.register(StoreIncome,StoreIncomeAdmin)


