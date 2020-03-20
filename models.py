# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=45, blank=True, null=True)
    category_desc = models.CharField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_visible = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'categories'


class ClubEvents(models.Model):
    club_event_id = models.AutoField(primary_key=True)
    club_event_name = models.CharField(max_length=100, blank=True, null=True)
    club_event_dt = models.DateTimeField(blank=True, null=True)
    club = models.ForeignKey('Clubs', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'club_events'


class ClubTypes(models.Model):
    club_type_id = models.AutoField(primary_key=True)
    club_type_name = models.CharField(max_length=45, blank=True, null=True)
    club_type_desc = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'club_types'


class Clubs(models.Model):
    club_id = models.AutoField(primary_key=True)
    club_name = models.CharField(max_length=200)
    club_introduce = models.CharField(max_length=200)
    club_desc = models.CharField(max_length=3000)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    club_img_url = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_central = models.IntegerField()
    is_united = models.IntegerField()
    club_type = models.ForeignKey(ClubTypes, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'clubs'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Notifications(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    notification_content = models.CharField(max_length=1000)
    notification_type_id = models.IntegerField()
    read_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'notifications'


class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=150)
    post_content = models.CharField(max_length=3000)
    post_title_img_url = models.CharField(max_length=1000, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    is_deleted = models.TextField()  # This field type is a guess.
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_notice = models.IntegerField()
    club = models.ForeignKey(Clubs, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posts'


class RelInterestClubs(models.Model):
    intrest_club_id = models.AutoField(primary_key=True)
    club = models.ForeignKey(Clubs, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rel_interest_clubs'


class Replies(models.Model):
    reply_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    parent_reply = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    post = models.ForeignKey(Posts, models.DO_NOTHING)
    reply_content = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'replies'


class UsersAdditionalInfo(models.Model):
    user_info = models.OneToOneField(AuthUser, models.DO_NOTHING, primary_key=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    token_kakao = models.CharField(max_length=100, blank=True, null=True)
    token_google = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_verfied = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'users_additional_info'
