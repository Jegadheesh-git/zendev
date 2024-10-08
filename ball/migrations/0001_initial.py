# Generated by Django 5.1 on 2024-08-13 13:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('match', '0001_initial'),
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BatsmanActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BatSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BowlingSide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CreaseMovement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DeliverySide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DismissalType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ExtraType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FieldingActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='KeeperActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Length',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ShotConnection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ShotZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Stroke',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UmpireActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WagonWheel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ball',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ballNumber', models.IntegerField()),
                ('over', models.IntegerField()),
                ('innings', models.IntegerField()),
                ('runs', models.IntegerField()),
                ('extra1', models.IntegerField()),
                ('extra2', models.IntegerField()),
                ('isDead', models.BooleanField()),
                ('penalty', models.IntegerField()),
                ('wide', models.IntegerField()),
                ('noBall', models.IntegerField()),
                ('isFreeHit', models.BooleanField()),
                ('boundaryRuns', models.IntegerField()),
                ('overThrow', models.IntegerField()),
                ('ballSpeed', models.FloatField()),
                ('ballSpeedMetric', models.CharField(choices=[('kph', 'kph'), ('mph', 'mph')], max_length=50)),
                ('swing', models.IntegerField()),
                ('batSpeed', models.FloatField()),
                ('isWicket', models.BooleanField()),
                ('shortRuns', models.IntegerField()),
                ('bowler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='balls_bowler', to='player.player')),
                ('fielder1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='balls_fielder1', to='player.player')),
                ('fielder2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='balls_fielder2', to='player.player')),
                ('matchId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='match.match')),
                ('nonStriker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='balls_non_striker', to='player.player')),
                ('striker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='balls_striker', to='player.player')),
                ('batsmanActivity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ball.batsmanactivity')),
                ('batSubject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ball.batsubject')),
                ('bowlingSide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ball.bowlingside')),
                ('creaseMovement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ball.creasemovement')),
                ('deliverySide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ball.deliveryside')),
                ('dismissalType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ball.dismissaltype')),
                ('extraType1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='balls_extra_type1', to='ball.extratype')),
                ('extraType2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='balls_extra_type2', to='ball.extratype')),
                ('fieldingActivity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ball.fieldingactivity')),
                ('keeperActivity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ball.keeperactivity')),
                ('length', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ball.length')),
                ('shotConnection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ball.shotconnection')),
                ('shotZone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ball.shotzone')),
                ('stroke', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ball.stroke')),
                ('umpireActivity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ball.umpireactivity')),
                ('wagonWheel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ball.wagonwheel')),
            ],
        ),
    ]
