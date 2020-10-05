from django.contrib import admin
from .models import Content

class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'sort', 'like_count', 'status']
    actions = ['make_published', 'make_draft', 'make_withdrawn']

    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p') #queryset.update
        self.message_user(request, '{}개의 컨텐츠를 배포 상태로 변경'.format(updated_count))
    make_published.short_description = '지정 컨텐츠를 배포 상태로 변경'

    def make_draft(self, request, queryset):
        updated_count = queryset.update(status='d') #queryset.update
        self.message_user(request, '{}개의 컨텐츠를 중 상태 로 변경'.format(updated_count))
    make_draft.short_description = '지정 컨텐츠를 준비 중 상태로 변경'

    def make_withdrawn(self, request, queryset):
        updated_count = queryset.update(status='w') #queryset.update
        self.message_user(request, '{}개의 컨텐츠를 철수 상태 로 변경'.format(updated_count))
    make_withdrawn.short_description = '지정 컨텐츠를 철수 상태로 변경'

admin.site.unregister(Content)
admin.site.register(Content, ContentAdmin)