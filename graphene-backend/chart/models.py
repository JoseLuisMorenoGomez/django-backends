# models.py

from django.db import models
from wagtail.snippets.models import register_snippet
from django.contrib.auth.models import User
from wagtail  import blocks as wagtail_blocks
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel,  PageChooserPanel
from wagtail import hooks
from wagtail.models import UserPagePermissionsProxy, Page

@register_snippet
class Chart(models.Model):
    chart_type = models.CharField(
        max_length=20,
        choices=[
            ('line_chart', 'Gráfico de Líneas'),
            ('bar_chart', 'Gráfico de Barras'),
            ('evolution_chart', 'Gráfico de Evolución'),
            # Agrega más opciones según sea necesario
        ],
        default='line_chart',
        help_text='Tipo de gráfico'
    )
    data_source = models.CharField(
        max_length=20,
        choices=[
            ('json', 'JSON'),
            ('csv', 'CSV'),
            ('graphql', 'GraphQL'),
        ],
        default='json',
        help_text='Fuente de datos'
    )
    data_json = models.TextField(blank=True, help_text='Datos en formato JSON')
    data_csv = models.FileField(upload_to='chart_data/', null=True, blank=True, help_text='Archivo CSV')
    data_graphql_query = models.TextField(blank=True, help_text='Consulta GraphQL')
    data_source_url = models.URLField(blank=True, help_text='URL del archivo de datos')

    panels = [
        FieldPanel('chart_type'),
        FieldPanel('data_source'),
        FieldPanel('data_json'),
        FieldPanel('data_csv'),
        FieldPanel('data_graphql_query'),
        FieldPanel('data_source_url'),
    ]

    def __str__(self):
        return self.chart_type


class ChartPage(Page):
    body = StreamField([
        ('paragraph', wagtail_blocks.RichTextBlock()),
        ('chart', wagtail_blocks.PageChooserBlock(target_model=Chart)),
    ] , use_json_field=True)

    explanation = models.TextField(blank=True)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.SET_NULL)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('explanation'),
    ]

    def save(self, *args, **kwargs):
        # Asignar el usuario que está guardando la página
        user = UserPagePermissionsProxy.get_for_user(self.owner).user
        self.created_by = user

        super().save(*args, **kwargs)






