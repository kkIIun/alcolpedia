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
