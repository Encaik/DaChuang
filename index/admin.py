from django.contrib import admin
from index.models import Users, Reports


admin.site.site_header = '上市公司年报搜索平台后台管理'
admin.site.site_title = '大创'


class UsersAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class ReportsAdmin(admin.ModelAdmin):
    list_display = ("num", "year")

admin.site.register(Users, UsersAdmin)
admin.site.register(Reports, ReportsAdmin)
