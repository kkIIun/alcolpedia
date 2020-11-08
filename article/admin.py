from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import *


User = get_user_model()


# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


class TagInline(admin.TabularInline):
    extra = 0
    model = Content.tag.through
    verbose_name = "태그 선택"
    verbose_name_plural = "태그 선택"


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "publisher", "sort",
                    "difficulty", 'bookmark_count', )
    list_filter = ('sort', 'status',)
    actions = ['make_published', 'make_draft', 'make_withdrawn']
    fieldsets = (
        ("컨텐츠 정보", {
            "fields": (
                "title", "sort", "status", "difficulty",
            ),
        }),
        ("컨텐츠 파일", {
            "fields": (
                "image", "audio", "tag",
            ),
        }),
        ("컨텐츠 설명", {
            "fields": (
                "summary", "body",
            ),
        }),
    )

    # publisher는 자동으로 save_model이 호출될 때 입력
    exclude = ('publisher', ' bookmark', )

    inlines = [
        TagInline,
    ]

    def save_model(self, request, obj, form, change):
        obj.publisher = request.user
        super().save_model(request, obj, form, change)

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

