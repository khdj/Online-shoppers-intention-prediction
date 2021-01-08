from django.db import models
from .field_choices import *


class OnlineShopper(models.Model):
    Administrative = models.IntegerField()  # administrative pages visited
    AdministrativeDuration = models.FloatField()
    Informational = models.IntegerField()
    InformationalDuration = models.FloatField()
    ProductRelated = models.IntegerField()
    ProductRelatedDuration = models.FloatField()
    SpecialDay = models.FloatField()
    Month = models.CharField(
        max_length=4,
        choices=MONTH_CHOICES
    )
    OperatingSystems = models.IntegerField(choices=OS_CHOICES)
    Browser = models.IntegerField(choices=BROWSER_CHOICES)
    Region = models.IntegerField(choices=REGION_CHOICES)
    VisitorType = models.CharField(
        max_length=17,
        choices=VISITOR_TYPE_CHOICES
    )
    Weekend = models.BooleanField()
    Revenue = models.BooleanField(null=True)  # target field
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Administrative : {self.Administrative},\n" \
               f"AdministrativeDuration : {self.AdministrativeDuration},\n" \
               f"Info : {self.InformationalDuration},\n" \
               f"InfoDuration : {self.InformationalDuration},\n" \
               f"Prod : {self.ProductRelated},\n" \
               f"ProdDuration : {self.ProductRelatedDuration},\n" \
               f"SpecialDay : {self.SpecialDay},\n" \
               f"Month : {self.Month},\n" \
               f"OS : {self.OperatingSystems},\n" \
               f"Browser : {self.Browser},\n" \
               f"Region : {self.Region},\n" \
               f"VisitorType : {self.VisitorType},\n" \
               f"Weekend : {self.Weekend},\n" \
               f"Revenue : {self.Revenue},\n" \
               f"dateCreation : {self.created}\n"

    class Meta:
        ordering = ['created']
