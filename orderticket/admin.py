from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(Customer)
# admin.site.register(order)
from django.contrib import admin
from orderticket.models import HistoryOIChange,HistoryOITotal,LiveOIChange,LiveOITotal,LiveOITotalAllSymbol,LiveEquityResult,LiveOIPercentChange,HistoryOIPercentChange, LiveSegment

# Register your models here.
admin.site.register(LiveOIChange)
admin.site.register(LiveOITotal)
admin.site.register(LiveOIPercentChange)
admin.site.register(LiveSegment)
admin.site.register(LiveOITotalAllSymbol)