# Generated by Django 2.2.16 on 2020-10-03 16:17

from django.db import migrations, models
import django.db.models.deletion
import django_lifecycle.mixins
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0048_fips_checksums'),
        ('ansible', '0024_remove_collectionversion_certification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='deprecated',
        ),
        migrations.CreateModel(
            name='AnsibleCollectionDeprecated',
            fields=[
                ('pulp_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('pulp_created', models.DateTimeField(auto_now_add=True)),
                ('pulp_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ansible.Collection')),
                ('repository_version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection_memberships', to='core.RepositoryVersion')),
            ],
            options={
                'unique_together': {('collection', 'repository_version')},
            },
            bases=(django_lifecycle.mixins.LifecycleModelMixin, models.Model),
        ),
    ]