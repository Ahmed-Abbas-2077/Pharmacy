from django import forms 

class CreateCustomer(forms.Form):
    First_Name = forms.CharField(label='First_Name' , max_length=10)
    Second_Name = forms.CharField(label='Second_Name' , max_length=10)
    
