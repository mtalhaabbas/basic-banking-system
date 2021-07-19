from django.db import models
from django.db.models.deletion import CASCADE

account_type = (
    ('Business', 'Business'),
    ('Current', 'Current'),
    ('Saving', 'Saving'),
    
)

class customer(models.Model):
    account_type = models.CharField(max_length=40,blank=False,null=False, choices=account_type,help_text='Account Type')
    account_number = models.CharField(max_length=30,null=False,blank=False,help_text='Customer Account number',unique=True)
    full_name =  models.CharField(max_length=50,null=False,blank=False,help_text='Full Name')
    email = models.EmailField(blank=False,null=False,help_text='Customer Email')
    address = models.CharField(max_length=180, blank=True,null=True,help_text='Postal Address')
    current_balance = models.FloatField(blank=False,null=False,help_text='Current Balance')
    created_at = models.DateTimeField(auto_now_add=True)
    delete = models.BooleanField(default=False)


    def __str__(self):
        return str(self.full_name)

    class Meta:
        verbose_name_plural = 'Customer Details'



class transcation(models.Model):
    user = models.ForeignKey(customer,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    description =  models.CharField(max_length=200,null=False,blank=False,help_text='description')
    cr = models.FloatField(blank=True,null=True)
    dr = models.FloatField(blank=True,null=True)
    balance = models.FloatField(blank=False,null=False,help_text='Balance')
    delete = models.BooleanField(default=False)


    def __str__(self):
        return str(self.description)

    class Meta:
        verbose_name_plural = 'Transcation Details'