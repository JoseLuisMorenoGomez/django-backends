# models.py

from django.db import models
from wagtail.blocks import blocks as wagtail_blocks
from wagtail.admin.panels import  FieldPanel, PageChooserPanel, MultiFieldPanel 
from wagtail.snippets.models import register_snippet
from wagtail.documents.blocks  import DocumentChooserBlock
from wagtail import StreamField 


class CustomPageChooserBlock(wagtail_blocks.PageChooserBlock):
    class Meta:
        template = 'blocks/custom_page_chooser_block.html'

    def get_api_fields(self):
        return [
            wagtail_blocks.FieldPanel('data_graphql_query'),
        ]

    def get_csv_fields(self):
        return [
            DocumentChooserBlock('data_csv'),
        ]

class Chart(models.Model):
    chart_type = models.CharField(
        max_length=20,
        choices=[
            ('line_chart', 'Gráfico de Líneas'),
            ('bar_chart', 'Gráfico de Barras'),
            ('evolution_chart', 'Gráfico de Evolución'),
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
    data_csv = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Archivo CSV'
    )
    data_graphql_query = models.TextField(blank=True, help_text='Consulta GraphQL')
    data_source_url = models.URLField(blank=True, help_text='URL del archivo de datos')

    panels = [
        FieldPanel('chart_type'),
        FieldPanel('data_source'),
        CustomPageChooserBlock(target_model=Chart),
        FieldPanel('data_json'),
        DocumentChooserBlock('data_csv'),
        FieldPanel('data_graphql_query'),
        FieldPanel('data_source_url'),
    ]

    def str(self):
        return self.chart_type

# ...

class ChartPage(Page):
    body = StreamField([
        ('paragraph', wagtail_blocks.RichTextBlock()),
        ('chart', CustomPageChooserBlock(target_model=Chart)),
    ])

    explanation = models.TextField(blank=True)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.SET_NULL)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
        FieldPanel('explanation'),
    ]

    def save(self, *args, **kwargs):
        user = UserPagePermissionsProxy.get_for_user(self.owner).user
        self.created_by = user
        super().save(*args, **kwargs)

# ...