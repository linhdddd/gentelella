from django.contrib import admin #1
from django.db.models import Q #2
from django.utils.translation import ugettext_lazy as _
from .models import Categories, News #3

# Register your models here.
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category', 'status', 'sort_order')
    search_fields = ['name', ]
    none_type = type(None)

    def get_form(self, request, obj=None, **kwargs):
        request.obj = obj

        if isinstance(obj, self.none_type) is True:
            self.exclude = ("sort_order", )
        else:
            self.exclude = None

        return super(CategoriesAdmin, self).get_form(request, obj, **kwargs)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
        list_display = ('title', 'get_category', 'status')
        date_hierarchy = 'created_at'  # 1
        search_fields = ['title', 'categories__name']

        def get_category(self, obj):  # 2
            return obj.categories.name

        get_category.short_description = _('Categories')  # 3
        get_category.admin_order_field = 'category__name'  # 4

        list_filter = (
            ('categories', admin.RelatedFieldListFilter),  # 5
        )