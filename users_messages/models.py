from django.db import models


class Message(models.Model):
    owner = models.ForeignKey(
        "auth.User", related_name="owner", on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        "auth.User", related_name="receiver", on_delete=models.CASCADE
    )

    subject = models.CharField(max_length=100, blank=True, default="")
    body = models.TextField(blank=True, default="")

    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.owner} message for {self.receiver} ({self.id})"
