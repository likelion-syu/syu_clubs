from django.db import models
from common.models import Clubs
from django.contrib.auth.models import User

class ClubReplies(models.Model):
    reply_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    parent_reply = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    club = models.ForeignKey(Clubs, models.DO_NOTHING)
    reply_content = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()