# Generated by Django 4.0.5 on 2022-06-12 13:20

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_homepage_options_homepage_banner_cta_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='content',
            field=wagtail.fields.StreamField([('cta', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=60, required=True)), ('text', wagtail.blocks.RichTextBlock(features=['bold', 'italic'], required=True)), ('button_page', wagtail.blocks.PageChooserBlock(require=False)), ('button_url', wagtail.blocks.URLBlock(required=False)), ('button_text', wagtail.blocks.CharBlock(default='Read More', max_length=40, required=True))]))], blank=True, null=True, use_json_field=None),
        ),
    ]
