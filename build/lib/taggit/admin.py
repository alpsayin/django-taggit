from django.contrib import admin

from taggit.models import Tag, TaggedItem


class TaggedItemInline(admin.StackedInline):
    model = TaggedItem

class TagAdmin(admin.ModelAdmin):

    list_display = ["name","slug"]
    search_fields = ('name','slug')
    inlines = [
        TaggedItemInline
    ]

    def has_add_permission(self, request):
        return request.user.groups.filter(name='Editors').exists()

    def has_change_permission(self, request, obj=None):
        return request.user.groups.filter(name='Editors').exists()

    def has_delete_permission(self, request, obj=None):
        return request.user.groups.filter(name='Editors').exists()


admin.site.register(Tag, TagAdmin)
admin.site.register(TaggedItem)
