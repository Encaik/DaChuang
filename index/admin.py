from django.contrib import admin
from index.models import user, report, company


admin.site.site_header = '上市公司年报信息搜索平台后台管理'
admin.site.site_title = '大创'


class UserAdmin(admin.ModelAdmin):
    list_display = ("uid", "uname", "email", "telephone", "unit", "job", "creatdate")


class ReportAdmin(admin.ModelAdmin):
    list_display = ("rid", "year", "rcp_id")


class ComponyAdmin(admin.ModelAdmin):
    list_display = ("cid", "cnum", "cfname", "website")

admin.site.register(user, UserAdmin)
admin.site.register(report, ReportAdmin)
admin.site.register(company, ComponyAdmin)
