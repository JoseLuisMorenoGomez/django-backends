# admin.py

from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail.snippets.models import register_snippet
from .models import Chart, ChartPage

# Registro del modelo Chart en el admin
class ChartAdmin(ModelAdmin):
    model = Chart
    menu_label = 'Gráficos'
    menu_icon = 'chart-line'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('chart_type', 'data_source', 'data_source_url')

modeladmin_register(ChartAdmin)

# Registro del modelo ChartPage en el admin
class ChartPageAdmin(ModelAdmin):
    model = ChartPage
    menu_label = 'Páginas de Gráficos'
    menu_icon = 'chart-line'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('title', 'url_path', 'explanation', 'creation_datetime', 'created_by')

modeladmin_register(ChartPageAdmin)

