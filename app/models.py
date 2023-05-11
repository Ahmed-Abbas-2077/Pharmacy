from django.db import models

class Customer(models.Model):
    Code = models.AutoField(primary_key=True)
    First_Name = models.CharField(max_length=10)
    Second_Name = models.CharField(max_length=10,null=True)

    def __str__(self) -> str:
        return f"{self.First_Name} {self.Second_Name}"
    
class Customer_Condition(models.Model):
    Customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    Condition = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.Customer.Code}"
    
class Dispense(models.Model):
    code = models.CharField(max_length=4)
    Dispense_date = models.DateField()
    Pharmacist_ID = models.IntegerField()
    Prescription_ID = models.IntegerField()

    def __str__(self) -> str:
        return self.code
    
class Medication(models.Model):
    code = models.ForeignKey(Dispense,on_delete=models.CASCADE)
    Med_Name = models.CharField(max_length=20)
    Manufacturer = models.CharField( max_length=20)
    Supplier = models.IntegerField()
    Strength = models.IntegerField()
    Price = models.IntegerField()
    Dosage_form = models.CharField(max_length=50)
    Expiration_date = models.DateField()
    Amount = models.IntegerField()

    def __str__(self) -> str:
        return self.code
    