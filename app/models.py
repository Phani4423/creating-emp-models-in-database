from django.db import models

# Create your models here.

class Dept(models.Model):
    deptno = models.IntegerField(primary_key=True)
    deptname = models.CharField(max_length=100)
    loc = models.CharField(max_length=100)
    def __str__(self):
        return self.deptname
class Emp(models.Model):
    empno = models.IntegerField(primary_key=True)
    empname = models.CharField(max_length=100)
    sal = models.DecimalField(max_digits=10,decimal_places=2)
    hiredate = models.DateField(auto_now_add=True)
    deptno = models.ForeignKey(Dept,on_delete=models.CASCADE)
    comm = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    def __str__(self):
        return self.empname
    
