from django.db import models

class Contact(models.Model):
    full_name = models.CharField("ФИО", max_length=100)
    phone = models.CharField("телефон", max_length=20)
    organisation = models.CharField("Организация", max_length=100, blank=True)
    note = models.TextField("заметки", blank=True)

    def __str__(self):
        return self.full_name

class Event(models.Model):
    title = models.CharField("название", max_length=100)
    datetime = models.DateTimeField("Дата и время")
    description = models.TextField("описание", blank=True)

    def __str__(self):
        return f"{self.title} ({self.datetime.strftime('%d.%m.%Y %H:%M')})"