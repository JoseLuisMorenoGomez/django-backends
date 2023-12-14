from django.db import models

from django.contrib.auth.models import User
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import hooks
from wagtail.core.models import UserPagePermissionsProxy

class ChartBlock(blocks.StructBlock):
    chart_type = blocks.ChoiceBlock(
        choices=[
            ('Barplot', 'Gráfico de barras'),
            ('Treemap', 'Diagrama de árbol'),
            ('Doughnut','Doughnut'),
            ('Pie chart', 'Diagrama de tarta'),
            ('Line Plot', 'Diagrama de línea'),
        ],
        default='line_chart',
        help_text='Tipo de gráfico'
    )
    data_source = blocks.ChoiceBlock(
        choices=[
            ('json', 'JSON'),
            ('csv', 'CSV'),
            ('graphql', 'GraphQL'),
        ],
        default='json',
        help_text='Fuente de datos'
    )
    data_json = blocks.TextBlock(required=False, help_text='Datos en formato JSON')
    data_csv = blocks.FileBlock(required=False, help_text='Archivo CSV')
    data_graphql_query = blocks.TextBlock(required=False, help_text='Consulta GraphQL')
    data_source_url = blocks.URLBlock(required=False, help_text='URL del archivo de datos')

class ChartPage(Page):
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('chart', ChartBlock()),
    ])

    explanation = models.TextField(blank=True)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.SET_NULL)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
        FieldPanel('explanation'),
    ]

    def save(self, *args, **kwargs):
        # Asignar el usuario que está guardando la página
        user = UserPagePermissionsProxy.get_for_user(self.owner).user
        self.created_by = user

        super().save(*args, **kwargs)

# Registro del modelo en el admin
class ChartPageAdmin(ModelAdmin):
    model = ChartPage
    menu_label = 'Páginas de Gráficos'
    menu_icon = 'chart-line'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('title', 'url_path', 'explanation', 'creation_datetime', 'created_by')

modeladmin_register(ChartPageAdmin)

