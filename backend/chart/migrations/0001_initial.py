# Generated by Django 4.2.6 on 2023-12-14 12:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chart_type', models.CharField(choices=[('line_chart', 'Gráfico de Líneas'), ('bar_chart', 'Gráfico de Barras'), ('evolution_chart', 'Gráfico de Evolución')], default='line_chart', help_text='Tipo de gráfico', max_length=20)),
                ('data_source', models.CharField(choices=[('json', 'JSON'), ('csv', 'CSV'), ('graphql', 'GraphQL')], default='json', help_text='Fuente de datos', max_length=20)),
                ('data_json', models.TextField(blank=True, help_text='Datos en formato JSON')),
                ('data_csv', models.FileField(blank=True, help_text='Archivo CSV', null=True, upload_to='chart_data/')),
                ('data_graphql_query', models.TextField(blank=True, help_text='Consulta GraphQL')),
                ('data_source_url', models.URLField(blank=True, help_text='URL del archivo de datos')),
            ],
        ),
        migrations.CreateModel(
            name='ChartPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.fields.StreamField([('paragraph', wagtail.blocks.RichTextBlock()), ('chart', wagtail.blocks.PageChooserBlock(page_type=['chart.Chart']))], use_json_field=True)),
                ('explanation', models.TextField(blank=True)),
                ('creation_datetime', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]