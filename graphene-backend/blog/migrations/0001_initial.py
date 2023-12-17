# Generated by Django 4.2.6 on 2023-12-17 22:15

import blog.abstract
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True, verbose_name='Category Name')),
                ('slug', models.SlugField(max_length=80, unique=True)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('parent', models.ForeignKey(blank=True, help_text='Categories, unlike tags, can have a hierarchy. You might have a Jazz category, and under that have children categories for Bebop and Big Band. Totally optional.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='blog.blogcategory')),
            ],
            options={
                'verbose_name': 'Blog Category',
                'verbose_name_plural': 'Blog Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='BlogCategoryBlogPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='blog.blogcategory', verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='BlogIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'verbose_name': 'Blog index',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.fields.RichTextField(blank=True, verbose_name='body')),
                ('date', models.DateField(default=datetime.datetime.today, help_text='This date may be displayed on the blog post. It is not used to schedule posts to go live at a later date.', verbose_name='Post date')),
                ('author', models.ForeignKey(blank=True, limit_choices_to=blog.abstract.limit_author_choices, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author_pages', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('blog_categories', modelcluster.fields.ParentalManyToManyField(blank=True, through='blog.BlogCategoryBlogPage', to='blog.blogcategory')),
                ('header_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Header image')),
            ],
            options={
                'verbose_name': 'Blog page',
                'verbose_name_plural': 'Blog pages',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogTag',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('taggit.tag',),
        ),
        migrations.CreateModel(
            name='BlogPageTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='blog.blogpage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_items', to='taggit.tag')),
            ],
        ),
        migrations.AddField(
            model_name='blogpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='blog.BlogPageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='blogcategoryblogpage',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='blog.blogpage'),
        ),
    ]
