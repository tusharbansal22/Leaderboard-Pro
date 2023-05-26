from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields
import leaderboard.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, default='', primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('username', models.CharField(max_length=64, unique=True)),
                ('first_name', models.CharField(blank=True, default='', max_length=64)),
                ('last_name', models.CharField(blank=True, default='', max_length=64)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='codechefUser',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, default='', primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=64, unique=True)),
                ('max_rating', models.PositiveIntegerField(default=0)),
                ('Global_rank', models.CharField(default='NA', max_length=10)),
                ('Country_rank', models.CharField(default='NA', max_length=10)),
                ('rating', models.PositiveIntegerField(default=0)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('avatar', models.CharField(default='', max_length=256)),
            ],
            options={
                'ordering': ['-rating'],
            },
        ),
        migrations.CreateModel(
            name='codeforcesUser',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, default='', primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=64, unique=True)),
                ('max_rating', models.PositiveIntegerField(default=0)),
                ('rating', models.PositiveIntegerField(default=0)),
                ('last_activity', models.PositiveIntegerField(default=253402300800.0)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('avatar', models.CharField(default='', max_length=256)),
            ],
            options={
                'ordering': ['-rating'],
            },
        ),
        migrations.CreateModel(
            name='githubUser',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, default='', primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=64, unique=True)),
                ('contributions', models.PositiveIntegerField(default=0)),
                ('repositories', models.PositiveIntegerField(default=0)),
                ('stars', models.PositiveIntegerField(default=0)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('avatar', models.CharField(default='', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='LeetcodeUser',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, default='', primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=64, unique=True)),
                ('ranking', models.PositiveIntegerField(default=0)),
                ('easy_solved', models.PositiveIntegerField(default=0)),
                ('medium_solved', models.PositiveIntegerField(default=0)),
                ('hard_solved', models.PositiveIntegerField(default=0)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('avatar', models.CharField(default='', max_length=256)),
            ],
            options={
                'ordering': ['ranking'],
            },
        ),
        migrations.CreateModel(
            name='openlakeContributor',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, default='', primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=64, unique=True)),
                ('contributions', models.PositiveIntegerField(default=0)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-contributions'],
            },
        ),
        migrations.CreateModel(
            name='UserNames',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, default='', primary_key=True, serialize=False)),
                ('cc_uname', models.CharField(max_length=64)),
                ('cf_uname', models.CharField(max_length=64)),
                ('gh_uname', models.CharField(max_length=64)),
                ('lt_uname', models.CharField(default='', max_length=64)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OpenlakeFriends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('olFriend_uname', models.CharField(max_length=64)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LeetcodeFriends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ltFriend_uname', models.CharField(max_length=64)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GithubFriends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ghFriend_uname', models.CharField(max_length=64)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='codeforcesUserRatingUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.PositiveIntegerField(default=0)),
                ('prev_index', models.PositiveIntegerField(default=0)),
                ('rating', models.PositiveIntegerField(default=0)),
                ('timestamp', models.PositiveIntegerField(default=0)),
                ('cf_user', models.ForeignKey(default=leaderboard.models.get_default_cf_user, on_delete=django.db.models.deletion.CASCADE, related_name='rating_updates', to='leaderboard.codeforcesuser')),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='CodeforcesFriends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cfFriend_uname', models.CharField(max_length=64)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CodechefFriends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ccFriend_uname', models.CharField(max_length=64)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
