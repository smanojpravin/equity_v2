from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# class Customer(models.Model):
#     ACTIVE_CHOICES = (
#     ("Active", "Active"),
#     ("Inactive", "InActive"),

#     )
    
#     name = models.CharField(max_length=200)
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
#     joineddate  = models.DateField(auto_now_add=True)
#     status = models.CharField(max_length=20,choices = ACTIVE_CHOICES,default = 'Active')
#     loginkey = models.CharField(null=True,blank=True,max_length=20)
#     def __str__(self):
#         return f"{self.name }"

# class order(models.Model):
    
#     customer = models.ForeignKey('Customer',on_delete=models.CASCADE)
#     ordertag = models.IntegerField()
#     race = models.CharField(max_length=500)
#     orderdetail = models.CharField(max_length=2000)
#     total = models.CharField(max_length=100)
#     orderdate = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return f"{self.customer.name }"


class EquityThree(models.Model):
    symbol = models.CharField(max_length=20)
    time = models.TimeField(auto_now_add=False)
    date = models.DateField(auto_now_add=False)
    change_perc = models.FloatField(default=0)

    def __str__(self):
        return self.symbol
    class Meta:

        app_label = 'orderticket'

class HistoryOIChange(models.Model):
    time = models.DateTimeField(auto_now_add=False)
    call1 = models.CharField(max_length=20,default="")
    call2 = models.CharField(max_length=20,default="")
    put1 = models.CharField(max_length=20,default="")
    put2 = models.CharField(max_length=20,default="")
    callstrike = models.CharField(max_length=20)
    putstrike = models.CharField(max_length=20)
    symbol = models.CharField(max_length=20)
    expiry = models.DateField(auto_now_add=False)
    max_ceoi_strike = models.IntegerField(default=0)
    put_max_ceoi_strike = models.IntegerField(default=0)
    call_percentage = models.IntegerField(default=0)
    put_percentage = models.IntegerField(default=0)
    call_ceoi_total =  models.IntegerField(default=0)
    put_ceoi_total =  models.IntegerField(default=0)
    put_final = models.IntegerField(default=0)
    call_final = models.IntegerField(default=0)

    def __str__(self):
        return self.call1+" "+self.callstrike+" "+self.symbol
    class Meta:

        app_label = 'orderticket'
class HistoryOIPercentChange(models.Model):
    time = models.DateTimeField(auto_now_add=False)
    call1 = models.CharField(max_length=20,default="")
    call2 = models.CharField(max_length=20,default="")
    put1 = models.CharField(max_length=20,default="")
    put2 = models.CharField(max_length=20,default="")
    callstrike = models.CharField(max_length=20)
    putstrike = models.CharField(max_length=20)
    symbol = models.CharField(max_length=20)
    expiry = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.call1+" "+self.callstrike+" "+self.symbol
    class Meta:

        app_label = 'orderticket'
class LiveOIChange(models.Model):
    time = models.DateTimeField(auto_now_add=False)
    call1 = models.CharField(max_length=20,default="")
    call2 = models.CharField(max_length=20,default="")
    put1 = models.CharField(max_length=20,default="")
    put2 = models.CharField(max_length=20,default="")
    callstrike = models.CharField(max_length=20)
    putstrike = models.CharField(max_length=20)
    symbol = models.CharField(max_length=20)
    expiry = models.DateField(auto_now_add=False)
    max_ceoi_strike = models.IntegerField(default=0)
    put_max_ceoi_strike = models.IntegerField(default=0)
    call_percentage = models.IntegerField(default=0)
    put_percentage = models.IntegerField(default=0)
    call_ceoi_total =  models.IntegerField(default=0)
    put_ceoi_total =  models.IntegerField(default=0)
    put_final = models.IntegerField(default=0)
    call_final = models.IntegerField(default=0)

    def __str__(self):
        return self.call1+" "+self.callstrike+" "+self.symbol
    class Meta:

        app_label = 'orderticket'
class HistoryOITotal(models.Model):
    time = models.DateTimeField(auto_now_add=False)
    call1 = models.CharField(max_length=20,default="")
    call2 = models.CharField(max_length=20,default="")
    put1 = models.CharField(max_length=20,default="")
    put2 = models.CharField(max_length=20,default="")
    callstrike = models.CharField(max_length=20)
    putstrike = models.CharField(max_length=20)
    symbol = models.CharField(max_length=20)
    expiry = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.call1+" "+self.callstrike+" "+self.symbol
    class Meta:

        app_label = 'orderticket'
class LiveOITotal(models.Model):
    time = models.DateTimeField(auto_now_add=False)
    call1 = models.CharField(max_length=20,default="")
    call2 = models.CharField(max_length=20,default="")
    put1 = models.CharField(max_length=20,default="")
    put2 = models.CharField(max_length=20,default="")
    callstrike = models.CharField(max_length=20)
    putstrike = models.CharField(max_length=20)
    symbol = models.CharField(max_length=20)
    expiry = models.DateField(auto_now_add=False)
    strikegap = models.CharField(max_length=20,default="")

    def __str__(self):
        return self.call1+" "+self.callstrike+" "+self.symbol
    class Meta:

        app_label = 'orderticket'
class LiveOIPercentChange(models.Model):
    time = models.DateTimeField(auto_now_add=False)
    call1 = models.CharField(max_length=20,default="")
    call2 = models.CharField(max_length=20,default="")
    put1 = models.CharField(max_length=20,default="")
    put2 = models.CharField(max_length=20,default="")
    callstrike = models.CharField(max_length=20)
    putstrike = models.CharField(max_length=20)
    symbol = models.CharField(max_length=20)
    expiry = models.DateField(auto_now_add=False)
    strikegap = models.CharField(max_length=20,default="")

    def __str__(self):
        return self.call1+" "+self.callstrike+" "+self.symbol
    class Meta:

        app_label = 'orderticket'

class LiveOITotalAllSymbol(models.Model):
    time = models.DateTimeField(auto_now_add=False)
    call1 = models.CharField(max_length=20,default="")
    call2 = models.CharField(max_length=20,default="")
    put1 = models.CharField(max_length=20,default="")
    put2 = models.CharField(max_length=20,default="")
    callstrike = models.CharField(max_length=20)
    putstrike = models.CharField(max_length=20)
    symbol = models.CharField(max_length=20)
    expiry = models.DateField(auto_now_add=False)
    callone = models.CharField(max_length=20,default="") 
    putone = models.CharField(max_length=20,default="")
    callhalf = models.CharField(max_length=20,default="")
    puthalf = models.CharField(max_length=20,default="")

    def __str__(self):
        return self.call1+" "+self.callstrike+" "+self.symbol
    class Meta:

        app_label = 'orderticket'

class LiveEquityResult(models.Model):
    time = models.TimeField(auto_now_add=False)
    date = models.DateTimeField(auto_now_add=False)
    symbol = models.CharField(max_length=20,default="")
    open = models.CharField(max_length=20,default="")
    high = models.CharField(max_length=20,default="")
    low = models.CharField(max_length=20,default="")
    prev_day_close = models.CharField(max_length=20,default="")
    ltp = models.CharField(max_length=20)
    strike = models.CharField(max_length=20)
    opencrossed = models.CharField(max_length=20,default="")
    section = models.IntegerField(default=0)
    difference = models.CharField(max_length=10,default="")
    change_perc = models.FloatField(default=0)
    below_three = models.CharField(max_length=20,default=False)

    def __str__(self):
        return self.symbol+" "+self.ltp+" "+self.strike
    class Meta:

        app_label = 'orderticket'

class TestEquityResult(models.Model):
    time = models.TimeField(auto_now_add=False)
    date = models.DateTimeField(auto_now_add=False)
    symbol = models.CharField(max_length=20,default="")
    open = models.CharField(max_length=20,default="")
    high = models.CharField(max_length=20,default="")
    low = models.CharField(max_length=20,default="")
    prev_day_close = models.CharField(max_length=20,default="")
    ltp = models.CharField(max_length=20)
    strike = models.CharField(max_length=20)
    opencrossed = models.CharField(max_length=20,default="")

    def __str__(self):
        return self.symbol+" "+self.ltp+" "+self.strike
    class Meta:

        app_label = 'orderticket'

class LiveSegment(models.Model):
    symbol = models.CharField(max_length=20)
    segment = models.CharField(max_length=20)
    time = models.TimeField(auto_now_add=False)
    date = models.DateField(auto_now_add=False)
    change_perc = models.FloatField(default=0)
    doneToday = models.CharField(max_length=10,default="")

    # def __str__(self):
    #     return self.symbol+" "+self.segment+" "+self.date

    class Meta:

        app_label = 'orderticket'

class SuperLiveSegment(models.Model):
    symbol = models.CharField(max_length=20)
    segment = models.CharField(max_length=20)
    time = models.TimeField(auto_now_add=False)
    date = models.DateField(auto_now_add=False)
    change_perc = models.FloatField(default=0)

    def __str__(self):
        return self.symbol+" "+self.segment

    class Meta:

        app_label = 'orderticket'
