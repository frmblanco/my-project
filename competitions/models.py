from django.db import models

from django.utils import timezone
from custom_user.models import CustomUser


class Competitions(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField(blank=True, null=True)
    attending_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class CompetitionFile(models.Model):
    attending_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True)
    competition_id = models.ForeignKey(Competitions, on_delete=models.CASCADE, blank=True)
    user_file = models.FileField(blank=True)

    def create_row(self, attending_user, competition_id, user_file):
        self.attending_user = attending_user
        self.competition_id = competition_id
        self.user_file = user_file

    def __str__(self):
        return "%s %s" % (self.attending_user, self.competition_id)