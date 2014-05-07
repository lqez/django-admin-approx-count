from django.contrib.admin import ModelAdmin
from approx_count.mixin import MaxIdAdminMixin, TableStatusAdminMixin

__all__ = ['MaxIdModelAdmin', 'TableStatusModelAdmin']


class MaxIdModelAdmin(MaxIdAdminMixin, ModelAdmin):
    pass


class TableStatusModelAdmin(TableStatusAdminMixin, ModelAdmin):
    pass
