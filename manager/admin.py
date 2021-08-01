# Django Admin in-built functionality to import and export
# data files

from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from manager.models import Inventory, Member


class InventoryResource(resources.ModelResource):

    class Meta:
        model = Inventory
        widgets = {
            'expiration_date': {'format': '%d/%m/%y'},
        }


class MemberResource(resources.ModelResource):

    class Meta:
        model = Member
        widgets = {
            'date_joined': {'format': '%d/%m/%y %H:%M'},
        }


class InventoryAdmin(ImportExportModelAdmin):
    resource_class = InventoryResource


class MemberAdmin(ImportExportModelAdmin):
    resource_class = MemberResource


admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Member, MemberAdmin)
