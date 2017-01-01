# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-01 07:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def forwards(app, schema_editor):
    with schema_editor.connection.cursor() as db:
        db.execute("""
        CREATE TABLE "dip_platform_game" ("id" serial NOT NULL PRIMARY KEY);

        CREATE TABLE "dip_platform_user" (
            "id" serial NOT NULL PRIMARY KEY,
            "username" varchar(32) NOT NULL,
            "email" varchar(32) NOT NULL
        );

        CREATE TABLE "dip_platform_player" (
            "id" serial NOT NULL PRIMARY KEY,
            "name" varchar(32) NOT NULL,
            "game_id" integer NOT NULL,
            "user_id" integer NOT NULL
        );

        CREATE TABLE "dip_platform_territoryownership" (
            "id" serial NOT NULL PRIMARY KEY,
            "territory_name" varchar(32) NOT NULL,
            "owner_id" integer NOT NULL
        );

        CREATE TABLE "dip_platform_unit" (
            "id" serial NOT NULL PRIMARY KEY,
            "type" varchar(1) NOT NULL CHECK (type IN ('T', 'F')),
            "territory_name" varchar(32) NOT NULL,
            "owner_id" integer NOT NULL
        );

        ALTER TABLE "dip_platform_player"
        ADD CONSTRAINT "dip_platform_player_game_id_6ed70aed_fk_dip_platform_game_id"
        FOREIGN KEY ("game_id") REFERENCES "dip_platform_game" ("id")
        DEFERRABLE INITIALLY DEFERRED;
        CREATE INDEX "dip_platform_player_6072f8b3" ON "dip_platform_player" ("game_id");

        ALTER TABLE "dip_platform_territoryownership"
        ADD CONSTRAINT "dip_platform_territ_owner_id_4df09a97_fk_dip_platform_player_id"
        FOREIGN KEY ("owner_id") REFERENCES "dip_platform_player" ("id")
        DEFERRABLE INITIALLY DEFERRED;
        CREATE INDEX "dip_platform_territoryownership_5e7b1936" ON "dip_platform_territoryownership" ("owner_id");

        ALTER TABLE "dip_platform_unit"
        ADD CONSTRAINT "dip_platform_unit_owner_id_5a9b4727_fk_dip_platform_player_id"
        FOREIGN KEY ("owner_id") REFERENCES "dip_platform_player" ("id")
        DEFERRABLE INITIALLY DEFERRED;
        CREATE INDEX "dip_platform_unit_5e7b1936" ON "dip_platform_unit" ("owner_id");

        ALTER TABLE "dip_platform_player"
        ADD CONSTRAINT "dip_platform_player_user_id_b00c9ab7_fk_dip_platform_user_id"
        FOREIGN KEY ("user_id") REFERENCES "dip_platform_user" ("id")
        DEFERRABLE INITIALLY DEFERRED;
        CREATE INDEX "dip_platform_player_e8701ad4" ON "dip_platform_player" ("user_id");
        """)

def backwards(app, schema_editor):
    with schema_editor.connection.cursor() as db:
        db.execute("""
        DROP TABLE dip_platform_game;
        DROP TABLE dip_platform_user;
        DROP TABLE dip_platform_player;
        DROP TABLE dip_platform_territoryownership;
        DROP TABLE dip_platform_unit;
        """)

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    state_operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dip_platform.Game')),
            ],
        ),
        migrations.CreateModel(
            name='TerritoryOwnership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('territory_name', models.CharField(max_length=32)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dip_platform.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('T', 'TROOP'), ('F', 'FLEET')], max_length=1)),
                ('territory_name', models.CharField(max_length=32)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dip_platform.Player')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dip_platform.User'),
        ),
    ]

    database_operations = [migrations.RunPython(forwards, reverse_code=backwards, atomic=False)]
    operations = [migrations.SeparateDatabaseAndState(database_operations=database_operations, state_operations=state_operations)]
