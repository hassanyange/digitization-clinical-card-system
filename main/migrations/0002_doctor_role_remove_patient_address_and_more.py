# Generated by Django 5.0.1 on 2024-04-11 09:52

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('about', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='patient',
            name='address',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='age',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='patient',
            name='anuani',
            field=models.CharField(default='here', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='elimu',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='jina_kamili',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='jina_la_mume',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='jina_la_mwenyekiti',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='kata_wilaya',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='kazi',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='kijiji_au_mtaa',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='kimo',
            field=models.CharField(choices=[('JUU YA 150', 'JUU YA 150'), ('CHINI YA 150', 'CHINI YA 150')], max_length=110, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='number_ya_simu',
            field=models.CharField(default=django.utils.timezone.now, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='number_ya_uandikishaji',
            field=models.CharField(default="30", max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='umri',
            field=models.IntegerField(default=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Pregnance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mimba_ya_ngapi', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.patient')),
            ],
        ),
        migrations.CreateModel(
            name='LabaratoryMaasurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('damu_group', models.CharField(blank=True, max_length=200, null=True)),
                ('vipimo_vingine', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pregnance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.pregnance')),
            ],
        ),
        migrations.CreateModel(
            name='FirstTimePatientInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chini_ya_miaka_20', models.BooleanField()),
                ('miaka_10_au_zaid_tokea_mimba_ya_mwisho', models.BooleanField()),
                ('kajifungua_kwa_kupasuliwa', models.BooleanField()),
                ('kuharibika_kwa_mimba_2_au_zaidi', models.BooleanField()),
                ('ugonjwa_wa_moyo', models.BooleanField()),
                ('kifua_kikuu', models.BooleanField()),
                ('kisukari', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pregnance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.pregnance')),
            ],
        ),
        migrations.CreateModel(
            name='AttendenceReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarehe_ya_mahudhurio', models.DateField()),
                ('uzito', models.CharField(blank=True, max_length=200, null=True)),
                ('blood_pressure', models.CharField(blank=True, max_length=200, null=True)),
                ('albimu_kwenye_mkojo', models.CharField(blank=True, max_length=200, null=True)),
                ('damu', models.CharField(blank=True, max_length=200, null=True)),
                ('sukari_kweny_mkojo', models.CharField(blank=True, max_length=200, null=True)),
                ('umri_wa_mimba_wa_wiki', models.CharField(blank=True, max_length=200, null=True)),
                ('kimo_cha_mimba_kwa_wiki', models.CharField(blank=True, max_length=200, null=True)),
                ('mlalo_wa_mtoto', models.CharField(blank=True, max_length=200, null=True)),
                ('kitangulizi_kuanzia_wiki_ya_36', models.CharField(blank=True, max_length=200, null=True)),
                ('mapigo_ya_moyo_ya_mtoto', models.CharField(blank=True, max_length=200, null=True)),
                ('mtoto_anacheza_baada_ya_wiki_20', models.CharField(blank=True, choices=[('NDIO', 'NDIO'), ('HAPANA', 'HAPANA')], max_length=200, null=True)),
                ('kivimba_miguu_odema', models.CharField(blank=True, max_length=200, null=True)),
                ('ferrous_sulpate', models.CharField(blank=True, max_length=200, null=True)),
                ('folic_acid', models.CharField(blank=True, max_length=200, null=True)),
                ('mebendazole', models.CharField(blank=True, max_length=200, null=True)),
                ('sahihi_ya_mhudumu', models.CharField(blank=True, max_length=200, null=True)),
                ('bp_40_90_au_zaidi', models.BooleanField(null=True)),
                ('hb_chini_ya_60_per', models.BooleanField(null=True)),
                ('albumin_kwenye_mkojo', models.BooleanField(null=True)),
                ('sukari_kwenye_mkojo', models.BooleanField(null=True)),
                ('mama_anazo_dalili_za_hatari', models.BooleanField(null=True)),
                ('umri_wa_mimba_zaidi_ya_wiki_40', models.BooleanField(null=True)),
                ('mtoto_kufia_tumboni', models.BooleanField(null=True)),
                ('kuvimba_miguu_au_mikono', models.BooleanField(null=True)),
                ('mama_ana_mapacha', models.BooleanField(null=True)),
                ('kipimo_cha_mimba_kikubwa_au_kidogo_kuliko_umri_wake', models.BooleanField(null=True)),
                ('mama_ameshauriwa_azalie_wapi', models.BooleanField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('malaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.patient')),
                ('jina_la_mhudumu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.doctor')),
                ('pregnance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.pregnance')),
            ],
        ),
        migrations.CreateModel(
            name='PreviousPregnanciesInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mimba_ya_ngapi', models.IntegerField(default=1)),
                ('amezaa_mara_ngapi', models.IntegerField(default=1)),
                ('watoto_walio_hai', models.IntegerField(default=1)),
                ('mimba_zilizo_haribika', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pregnance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.pregnance')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='cheo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.role'),
        ),
    ]
