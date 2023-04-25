from django.db import models

MAX_FIELD_LEN = 80


class Employee(models.Model):
    first_name = models.CharField(max_length=MAX_FIELD_LEN)
    last_name = models.CharField(max_length=MAX_FIELD_LEN)
    role = models.CharField(max_length=MAX_FIELD_LEN)
    img_address = models.CharField(max_length=MAX_FIELD_LEN)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Email(models.Model):
    sender_name = models.CharField(max_length=MAX_FIELD_LEN)
    sender_email = models.EmailField()
    date_sent = models.DateTimeField()
    message = models.TextField()

    def __str__(self):
        return f"From {self.sender_name} ({self.sender_email}) on {self.date_sent}: {self.message}"
