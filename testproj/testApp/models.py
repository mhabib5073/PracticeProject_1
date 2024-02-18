from django.db import models

class Employee(models.Model):
    eid = models.AutoField(primary_key=True)
    ename = models.CharField(max_length=100, blank=True, null=True)
    esal = models.CharField(max_length=100, blank=True, null=True)
    eaddress = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.ename
    
    class Meta:
        managed = False
        db_table = 'employee'



    
