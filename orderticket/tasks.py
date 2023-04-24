from operator import le
from time import sleep
from xml.etree.ElementPath import find
from celery import shared_task
from .models import *
from nsetools import *
from datetime import datetime as dt
from truedata_ws.websocket.TD import TD
import websocket

from celery.schedules import crontab
from celery import Celery
from celery.schedules import crontab
import time
from nsetools import Nse
from ordermanagement.celery import app
from django_celery_beat.models import PeriodicTask, PeriodicTasks
from datetime import datetime, time,timedelta
from celery.exceptions import SoftTimeLimitExceeded
from pytz import timezone
import pendulum
import calendar
from datetime import date
import time as te
from orderticket.views import hello_equity

#hello_equity(repeat=2,repeat_until=None)

def equity(connection_check):

    startTime = datetime.combine(datetime.now(timezone('Asia/Kolkata')), time(8,59)).time()
    market_stop_time = datetime.combine(datetime.now(timezone('Asia/Kolkata')), time(18,1)).time()
    nowTime = datetime.now(timezone('Asia/Kolkata')).time()

    if nowTime < startTime:
        print("Market not started- deleting old data")
        LiveEquityResult.objects.all().delete()


    if nowTime > startTime and nowTime < market_stop_time:

        try:
            equity_username = 'tdwsp135'
            equity_password = 'saaral@135'
            realtime_port = 8082
                    
#             fnolist = ['AARTIIND','ABB','ACC','ABFRL','ADANIENT','ADANIPORTS','AMBUJACEM','APOLLOHOSP','ASIANPAINT','ATUL','AUBANK','AUROPHARMA','AXISBANK',
#                        'BAJAJFINSV','BAJFINANCE','BALKRISIND','BALRAMCHIN','BANDHANBNK','BATAINDIA','BERGEPAINT','BHARATFORG','BHARTIARTL','BPCL','BRITANNIA',
#                        'BSOFT','CANFINHOME','CHAMBLFERT','CHOLAFIN','CIPLA','COFORGE','COLPAL','CONCOR','COROMANDEL','CROMPTON','CUMMINSIND','DABUR','DALBHARAT',
#                        'DELTACORP','DIVISLAB','DIXON','DLF','DRREDDY','EICHERMOT','ESCORTS','GLENMARK','GNFC','GODREJCP','GODREJPROP','GRANULES','GRASIM',
#                        'GUJGASLTD','HAVELLS','HCLTECH','HDFC','HDFCBANK','HDFCLIFE','HEROMOTOCO','HINDALCO','HINDUNILVR','ICICIBANK','ICICIGI','ICICIPRULI',
#                        'IGL','INDHOTEL','INDIAMART','INDIGO','INDUSINDBK','INFY','INTELLECT','IPCALAB','IRCTC','JINDALSTEL','JKCEMENT','JSWSTEEL','JUBLFOOD',
#                        'KOTAKBANK','LALPATHLAB','LAURUSLABS','LICHSGFIN','LT','LTIM','LTTS','LUPIN','M&M','MARICO','MARUTI','MCDOWELL-N','MCX','METROPOLIS',
#                        'MFSL','MGL','MUTHOOTFIN','NAUKRI','NAVINFLUOR','NESTLEIND','OBEROIRLTY','PEL','PERSISTENT','PIIND','POLYCAB','PVR','RAMCOCEM','SBICARD',
#                        'SBILIFE','SBIN','SHREECEM','SHRIRAMFIN','SUNPHARMA','SUNTV','SYNGENE','TATACHEM','TATACOMM','TATACONSUM','TATAMOTORS','TCS','TECHM',
#                        'TITAN','TORNTPHARM','TORNTPOWER','TRENT','TVSMOTOR','UBL','ULTRACEMCO','UPL','VOLTAS','WHIRLPOOL','WIPRO']
            
            fnolist = ["AARTIIND",
"ABB",
"ABBOTINDIA",
"ACC",
"ADANIPORTS",
"ALKEM",
"AMBUJACEM",
"APOLLOHOSP",
"ASIANPAINT",
"ATUL",
"AUBANK",
"AUROPHARMA",
"AXISBANK",
"BAJAJ-AUTO",
"BAJAJFINSV",
"BAJFINANCE",
"BALKRISIND",
"BALRAMCHIN",
"BANDHANBNK",
"BATAINDIA",
"BERGEPAINT",
"BHARATFORG",
"BHARTIARTL",
"BOSCHLTD",
"BPCL",
"BRITANNIA",
"BSOFT",
"CANFINHOME",
"CHAMBLFERT",
"CHOLAFIN",
"CIPLA",
"COFORGE",
"COLPAL",
"CONCOR",
"COROMANDEL",
"CROMPTON",
"CUMMINSIND",
"DABUR",
"DALBHARAT",
"DEEPAKNTR",
"DIVISLAB",
"DIXON",
"DLF",
"DRREDDY",
"EICHERMOT",
"ESCORTS",
"GLENMARK",
"GNFC",
"GODREJCP",
"GODREJPROP",
"GRANULES",
"GRASIM",
"GUJGASLTD",
"HAVELLS",
"HCLTECH",
"HDFC",
"HDFCAMC",
"HDFCBANK",
"HDFCLIFE",
"HINDALCO",
"HINDUNILVR",
"ICICIBANK",
"ICICIGI",
"ICICIPRULI",
"IGL",
"INDHOTEL",
"INDIAMART",
"INDIGO",
"INDUSINDBK",
"INFY",
"INTELLECT",
"IPCALAB",
"IRCTC",
"ITC",
"JINDALSTEL",
"JSWSTEEL",
"JUBLFOOD",
"KOTAKBANK",
"LAURUSLABS",
"LICHSGFIN",
"LT",
"LTIM",
"LTTS",
"LUPIN",
"M&M",
"MARICO",
"MARUTI",
"MCDOWELL-N",
"MCX",
"METROPOLIS",
"MFSL",
"MGL",
"MPHASIS",
"MRF",
"MUTHOOTFIN",
"NAUKRI",
"NAVINFLUOR",
"OBEROIRLTY",
"OFSS",
"PEL",
"PERSISTENT",
"PIDILITIND",
"PIIND",
"POLYCAB",
"PVR",
"RAMCOCEM",
"SBICARD",
"SBILIFE",
"SBIN",
"SHREECEM",
"SHRIRAMFIN",
"SRF",
"SUNPHARMA",
"SUNTV",
"SYNGENE",
"TATACHEM",
"TATACOMM",
"TATACONSUM",
"TATAMOTORS",
"TCS",
"TECHM",
"TITAN",
"TORNTPHARM",
"TRENT",
"TVSMOTOR",
"UBL",
"ULTRACEMCO",
"UPL",
"VEDL",
"VOLTAS",
"WIPRO",
"ZYDUSLIFE"]

            
            # fnolist = ['PEL']
            print('Starting Real Time Feed.... ')
            print(f'Port > {realtime_port}')

            if connection_check == 'start':
                # Graceful exit
                td_app.stop_live_data(fnolist)
                td_app.disconnect()
                td_app.disconnect()
            else:
                print("Proper graceful exit")

            td_app = TD(equity_username, equity_password, live_port=realtime_port, historical_api=False)
            req_ids = td_app.start_live_data(fnolist)
            live_data_objs = {}
            connection_check = 'start'

            te.sleep(2)

            liveData = {}
            for req_id in req_ids:
                if (td_app.live_data[req_id].ltp) == None:
                    continue
                else:
                    liveData[td_app.live_data[req_id].symbol] = [td_app.live_data[req_id].ltp,td_app.live_data[req_id].day_open,td_app.live_data[req_id].day_high,td_app.live_data[req_id].day_low,td_app.live_data[req_id].prev_day_close,dt.now(timezone("Asia/Kolkata")).strftime('%H:%M:%S'),td_app.live_data[req_id].change_perc]


            callcrossedset = LiveEquityResult.objects.filter(strike__contains="Call Crossed")
            callonepercentset = LiveEquityResult.objects.filter(strike="Call 1 percent")
            putcrossedset = LiveEquityResult.objects.filter(strike="Put Crossed")
            putonepercentset = LiveEquityResult.objects.filter(strike="Put 1 percent")
            opencallcross = LiveEquityResult.objects.filter(opencrossed="call")
            openputcross = LiveEquityResult.objects.filter(opencrossed="put")

            callcrossedsetDict = {}
            callonepercentsetDict = {}
            putcrossedsetDict = {}
            putonepercentsetDict = {}
            opencallcrossDict = {}
            openputcrossDict = {}

            for i in callcrossedset:
                callcrossedsetDict[i.symbol] = [i.time,i.below_three]
            for i in callonepercentset:
                callonepercentsetDict[i.symbol] = [i.time,i.below_three]
            for i in putcrossedset:
                putcrossedsetDict[i.symbol] = [i.time,i.below_three]
            for i in putonepercentset:
                putonepercentsetDict[i.symbol] = [i.time,i.below_three]
            for i in opencallcross:
                opencallcrossDict[i.symbol] = [i.time,i.below_three]
            for i in openputcross:
                openputcrossDict[i.symbol] = [i.time,i.below_three]

            # Graceful exit
            td_app.stop_live_data(fnolist)
            td_app.disconnect()
            td_app.disconnect()

            three_list = list(EquityThree.objects.all().values_list('symbol', flat=True)) 
            super_three_list = list(SuperLiveSegment.objects.all().values_list('symbol', flat=True)) 
            
            for key,value in liveData.items():
                print(f"Key: {key} \nValue:{value}")

                LiveSegment.objects.filter(symbol=key).all().delete()

                # Script comes inside +3 or -3
                if value[6] >= 3 and key not in three_list:
                    three = EquityThree(symbol=key,change_perc=value[6],date=dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d'),time=dt.now(timezone("Asia/Kolkata")).strftime('%H:%M:%S'))
                    three.save()
                elif value[6] <= -3 and key not in three_list:
                    three = EquityThree(symbol=key,change_perc=value[6],date=dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d'),time=dt.now(timezone("Asia/Kolkata")).strftime('%H:%M:%S'))
                    three.save()

                if float(value[6]) >= 1.5 and key not in super_three_list:
                    gain = SuperLiveSegment(symbol=key,segment="gain",change_perc=value[6],date=dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d'),time=dt.now(timezone("Asia/Kolkata")).strftime('%H:%M:%S'))
                    gain.save()

                elif float(value[6]) <= -1.5 and key not in super_three_list:
                    loss = SuperLiveSegment(symbol=key,segment="loss",change_perc=value[6],date=dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d'),time=dt.now(timezone("Asia/Kolkata")).strftime('%H:%M:%S'))
                    loss.save()

                if float(value[6]) <= 0:
                    below = LiveSegment(symbol=key,segment="below",change_perc=value[6],date=dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d'),time=dt.now(timezone("Asia/Kolkata")).strftime('%H:%M:%S'))
                    below.save()

                elif float(value[6]) >= 0:
                    above = LiveSegment(symbol=key,segment="above",change_perc=value[6],date=dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d'),time=dt.now(timezone("Asia/Kolkata")).strftime('%H:%M:%S'))
                    above.save()

            above = list(LiveSegment.objects.filter(segment="above").values_list('symbol', flat=True))
            below = list(LiveSegment.objects.filter(segment="below").values_list('symbol', flat=True))

            print(f"Total symbols found in option symbol: {len(LiveOITotalAllSymbol.objects.all())}")
            print(callcrossedset)
            print(f"open crossed {callcrossedsetDict}")

            # excluding section symbols
            section_check_time = datetime.combine(datetime.now(timezone('Asia/Kolkata')), time(10,15))
            #LiveHighLow.objects.filter(date__lte=section_check_time.date()).delete()
            if nowTime > section_check_time.time():
                # LiveHighLow.objects.all().delete()
                
                if LiveHighLow.objects.all().count() == 0:
                    for key, value in liveData.items():
                        # print(f"{key} + {value}")
                        high_value = value[2]
                        low_value = value[3]
                        high_low_diff = float(high_value)-float(low_value)
                        callcross = LiveHighLow(symbol=key,high=value[2],low=value[3],ltp=value[0],time=value[5],high_low_diff=high_low_diff)
                        callcross.save()


                for live in LiveHighLow.objects.all():
                    cross_check = LiveHighLow.objects.filter(symbol=live.symbol)
                    if "None" in cross_check[0].cross:
                        if float(liveData[live.symbol][0]) > float(live.high):
                            print(f"$$$$$$$$$$$$$$$$$$$$$$$$$$$ {live.symbol} $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                            LiveHighLow.objects.filter(symbol=live.symbol).update(cross="call", time=liveData[live.symbol][5])
                        elif float(liveData[live.symbol][0]) < float(live.low):
                            print(f"$$$$$$$$$$$$$$$$$$$$$$$$$$$ {live.symbol} $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                            LiveHighLow.objects.filter(symbol=live.symbol).update(cross="put", time=liveData[live.symbol][5])

            for e in LiveOITotalAllSymbol.objects.all():
                

                try:
                    # History Check
                    historyLen = HistoryOITotal.objects.filter(symbol=e.symbol)
                    
                    # total oi earliest
                    if len(historyLen) > 0:
                        historyStrike = HistoryOITotal.objects.filter(symbol=e.symbol).earliest('time')
                        strikegp = LiveOITotal.objects.filter(symbol=e.symbol)
                        
                        # Call strike 
                        callstrike = historyStrike.callstrike
                        # Put strike 
                        putstrike = historyStrike.putstrike
                        # Strike
                        strike_gap = (float(strikegp[0].strikegap)) * 2
                        # Call 1 percent 
                        callone = float(callstrike) - strike_gap
                        # Put 1 percent
                        putone = float(putstrike) + strike_gap

                    # total oi live
                    else:
                        callstrike = e.callstrike
                        putstrike = e.putstrike
                        callone = e.callone
                        putone = e.putone
                    
                    strikegp = LiveOITotal.objects.filter(symbol=e.symbol)
                    # call
                    if e.symbol in liveData and e.symbol in above:
                        try:
                            print(e.symbol)
                            # Difference Calculation
                            historyput = HistoryOIChange.objects.filter(symbol=e.symbol)
                            historycall = HistoryOITotal.objects.filter(symbol=e.symbol)
                            strikegp = LiveOITotal.objects.filter(symbol=e.symbol)

                            if len(historyput) > 0:
                                diffputstrike = HistoryOIChange.objects.filter(symbol=e.symbol).earliest('time')
                                diffputstrike = diffputstrike.putstrike
                                print("######### CALL #############")
                                print(f"diff put history {diffputstrike}")
                                history_len = 0
                                if diffputstrike == 0 or diffputstrike == '0':
                                    diffputstrike_db = HistoryOIChange.objects.filter(symbol=e.symbol).order_by('time')
                                    count = 1
                                    while diffputstrike == 0 or diffputstrike == '0':
                                        if count < len(diffputstrike_db):
                                            diffputstrike = diffputstrike_db[count].putstrike
                                            count +=1
                                        else:
                                            diffputstrike = LiveOIChange.objects.filter(symbol=e.symbol).earliest('time')
                                            diffputstrike = diffputstrike.putstrike
                                            break
                                    print(f"diff put history {diffputstrike}")
                            else:
                                is_available = LiveOIChange.objects.filter(symbol=e.symbol)
                                if len(is_available) > 0:
                                    diffputstrike = LiveOIChange.objects.filter(symbol=e.symbol).earliest('time')
                                    diffputstrike = diffputstrike.putstrike
                                    if diffputstrike == 0 or diffputstrike == '0':
                                        diffputstrike = LiveOIChange.objects.filter(symbol=e.symbol).order_by('time')
                                        diffputstrike = diffputstrike[1].putstrike
                                else:
                                    diffputstrike = 0

                            if len(historycall) > 0:
                                diffcallstrike = HistoryOITotal.objects.filter(symbol=e.symbol).earliest('time')
                                diffcallstrike = diffcallstrike.callstrike
                            else:
                                diffcallstrike = LiveOITotal.objects.filter(symbol=e.symbol).earliest('time')
                                diffcallstrike = diffcallstrike.callstrike
                                # diffcallstrike = e.callstrike
                            
                            difference = float(diffputstrike) - float(diffcallstrike)
                            section = int(abs((float(diffputstrike) - float(diffcallstrike))/float(strikegp[0].strikegap)))
                            print(f"call Strike: {callstrike}")
                            print(f"ltp check: {liveData[e.symbol][0]}")
                            print(f"call one {callone}")
                            
                            if e.symbol in putcrossedsetDict or e.symbol in putonepercentsetDict:
                                LiveEquityResult.objects.filter(symbol=e.symbol).update(ltp=liveData[e.symbol][0],high=liveData[e.symbol][2],low=liveData[e.symbol][3])
                                print("already crossed")
                                continue
                                
                            if float(liveData[e.symbol][1]) > float(callstrike):
                            # open Check
                                print("open checked")
                                if e.symbol in opencallcrossDict:
                                    print("Symbol crossed in open")
                                    LiveEquityResult.objects.filter(symbol=e.symbol).update(ltp=liveData[e.symbol][0],high=liveData[e.symbol][2],low=liveData[e.symbol][3])
                                    # LiveEquityResult.objects.filter(symbol = e.symbol).delete()
                                    # callcross = LiveEquityResult(symbol=e.symbol,
                                    #                             open=liveData[e.symbol][1],
                                    #                             high=liveData[e.symbol][2],
                                    #                             low=liveData[e.symbol][3],
                                    #                             prev_day_close=liveData[e.symbol][4],
                                    #                             ltp=liveData[e.symbol][0],
                                    #                             strike="Call Crossed",
                                    #                             opencrossed="call",
                                    #                             time=opencallcrossDict[e.symbol][0],
                                    #                             date=dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S'),
                                    #                             section=section,
                                    #                             difference=difference,
                                    #                             change_perc=liveData[e.symbol][6],
                                    #                             below_three=opencallcrossDict[e.symbol][1])
                                    # callcross.save()
                                    continue
                                else:
                                    if liveData[e.symbol][6] < 3 and liveData[e.symbol][6] > 0:
                                        callcross = LiveEquityResult(symbol=e.symbol,open=liveData[e.symbol][1],high=liveData[e.symbol][2],low=liveData[e.symbol][3],prev_day_close=liveData[e.symbol][4],ltp=liveData[e.symbol][0],strike="Call Crossed",opencrossed="call",time=liveData[e.symbol][5],date=dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S'),section=section,difference=difference,change_perc=liveData[e.symbol][6],below_three=True)
                                        callcross.save()
                                    else:
                                        callcross = LiveEquityResult(symbol=e.symbol,
                                                                    open=liveData[e.symbol][1],
                                                                    high=liveData[e.symbol][2],
                                                                    low=liveData[e.symbol][3],
                                                                    prev_day_close=liveData[e.symbol][4],
                                                                    ltp=liveData[e.symbol][0],
                                                                    strike="Call Crossed",
                                                                    opencrossed="call",
                                                                    time=liveData[e.symbol][5],
                                                                    date=dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S'),
                                                                    section=section,
                                                                    difference=difference,
                                                                    change_perc=liveData[e.symbol][6],
                                                                    below_three=False)
                                        callcross.save()
                                    continue

                            # High Check
                            elif float(liveData[e.symbol][2]) > float(callstrike):
                                print("high checked")
                                print(f"change percentage {liveData[e.symbol][6]}")
                                print(f"change percentage type {type(liveData[e.symbol][6])}")
                                if e.symbol in callcrossedsetDict:
                                    LiveEquityResult.objects.filter(symbol=e.symbol).update(ltp=liveData[e.symbol][0],high=liveData[e.symbol][2],low=liveData[e.symbol][3])
                                    # LiveEquityResult.objects.filter(symbol = e.symbol).delete()
                                    # callcross = LiveEquityResult(symbol=e.symbol,
                                    #                             open=liveData[e.symbol][1],
                                    #                             high=liveData[e.symbol][2],
                                    #                             low=liveData[e.symbol][3],
                                    #                             prev_day_close=liveData[e.symbol][4],
                                    #                             ltp=liveData[e.symbol][0],
                                    #                             strike="Call Crossed",
                                    #                             opencrossed="Nil",
                                    #                             time=callcrossedsetDict[e.symbol][0],
                                    #                             date=dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S'),
                                    #                             section=section,
                                    #                             difference=difference,
                                    #                             change_perc=liveData[e.symbol][6],
                                    #                             below_three=callcrossedsetDict[e.symbol][1])
                                    # callcross.save()
                                    continue
                                else:
                                    if int(liveData[e.symbol][6]) >= 3:
                                        print("insife if")
                                        callcross = LiveEquityResult(symbol=e.symbol,open=liveData[e.symbol][1],high=liveData[e.symbol][2],low=liveData[e.symbol][3],prev_day_close=liveData[e.symbol][4],ltp=liveData[e.symbol][0],strike="Call Crossed",opencrossed="Nil",time=liveData[e.symbol][5],date=dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S'),section=section,difference=difference,change_perc=liveData[e.symbol][6], below_three=False)
                                        callcross.save()
                                    else:
                                        print("insife else")
                                        callcross = LiveEquityResult(symbol=e.symbol,open=liveData[e.symbol][1],high=liveData[e.symbol][2],low=liveData[e.symbol][3],prev_day_close=liveData[e.symbol][4],ltp=liveData[e.symbol][0],strike="Call Crossed",opencrossed="Nil",time=liveData[e.symbol][5],date=dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S'),section=section,difference=difference,change_perc=liveData[e.symbol][6], below_three=True)
                                        callcross.save()
                                    continue

                            # ltp checked       
                            elif float(liveData[e.symbol][0]) > float(callstrike):
                                print("ltp checked")
                                if e.symbol in callcrossedsetDict:
                                    LiveEquityResult.objects.filter(symbol=e.symbol).update(ltp=liveData[e.symbol][0],high=liveData[e.symbol][2],low=liveData[e.symbol][3])
                                    # LiveEquityResult.objects.filter(symbol = e.symbol).delete()
                                    # callcross = LiveEquityResult(symbol=e.symbol,open=liveData[e.symbol][1],high=liveData[e.symbol][2],low=liveData[e.symbol][3],prev_day_close=liveData[e.symbol][4],ltp=liveData[e.symbol][0],strike="Call Crossed",opencrossed="Nil",time=callcrossedsetDict[e.symbol][0],date=dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S'),section=section,difference=difference,change_perc=liveData[e.symbol][6],below_three=callcrossedsetDict[e.symbol][1])
                                    # callcross.save()
                                    continue
                                else:
                                    if liveData[e.symbol][6] < 3 and liveData[e.symbol][6] > 0:
                                        callcross = LiveEquityResult(symbol=e.symbol,open=liveData[e.symbol][1],high=liveData[e.symbol][2],low=liveData[e.symbol][3],prev_day_close=liveData[e.symbol][4],ltp=liveData[e.symbol][0],strike="Call Crossed",opencrossed="Nil",time=liveData[e.symbol][5],date=dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S'),section=section,difference=difference,change_perc=liveData[e.symbol][6], below_three=True)
                                        callcross.save()
                                    else:
                                        callcross = LiveEquityResult(symbol=e.symbol,open=liveData[e.symbol][1],high=liveData[e.symbol][2],low=liveData[e.symbol][3],prev_day_close=liveData[e.symbol][4],ltp=liveData[e.symbol][0],strike="Call Crossed",opencrossed="Nil",time=liveData[e.symbol][5],date=dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S'),section=section,difference=difference,change_perc=liveData[e.symbol][6], below_three=False)
                                        callcross.save()
                            
                            elif float(liveData[e.symbol][0]) >= float(callone) and float(liveData[e.symbol][0]) < float(callstrike):
                                print("100% percent check")
                                # liveData[e.symbol][0]
                                if e.symbol in callcrossedsetDict:
                                    continue
                                else:
                                    if e.symbol in callonepercentsetDict:
                                        LiveEquityResult.objects.filter(symbol=e.symbol).update(ltp=liveData[e.symbol][0],high=liveData[e.symbol][2],low=liveData[e.symbol][3])
                                        # print("already in one percent")
                                        # LiveEquityResult.objects.filter(symbol = e.symbol).delete()
                                        # callcross = LiveEquityResult(symbol=e.symbol,open=liveData[e.symbol][1],high=liveData[e.symbol][2],low=liveData[e.symbol][3],prev_day_close=liveData[e.symbol][4],ltp=liveData[e.symbol][0],strike="Call 1 percent",opencrossed="Nil",time=callonepercentsetDict[e.symbol][0],date=dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S'),section=section,difference=difference,change_perc=liveData[e.symbol][6],below_three=callonepercentsetDict[e.symbol][1])
                                        # callcross.save()
                                        continue
                                    else:
                                        print('new one percent')
                                        LiveEquityResult.objects.filter(symbol=e.symbol).delete()
                                        if liveData[e.symbol][6] < 3 and liveData[e.symbol][6] > 0:
                                            # print("Call 1 percent")
                                            callone = LiveEquityResult(symbol=e.symbol,open=liveData[e.symbol][1],high=liveData[e.symbol][2],low=liveData[e.symbol][3],prev_day_close=liveData[e.symbol][4],ltp=liveData[e.symbol][0],strike="Call 1 percent",opencrossed="Nil",time=liveData[e.symbol][5],date=dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S'),section=section,difference=difference,change_perc=liveData[e.symbol][6],below_three=True)
                                            callone.save()
                                        else:
                                            callone = LiveEquityResult(symbol=e.symbol,open=liveData[e.symbol][1],high=liveData[e.symbol][2],low=liveData[e.symbol][3],prev_day_close=liveData[e.symbol][4],ltp=liveData[e.symbol][0],strike="Call 1 percent",opencrossed="Nil",time=liveData[e.symbol][5],date=dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S'),section=section,difference=difference,change_perc=liveData[e.symbol][6], below_three=False)
                                            callone.save()

                            else:
                                LiveEquityResult.objects.filter(symbol=e.symbol).delete()
                                callone = LiveEquityResult(symbol=e.symbol,open=liveData[e.symbol][1],high=liveData[e.symbol][2],low=liveData[e.symbol][3],prev_day_close=liveData[e.symbol][4],ltp=liveData[e.symbol][0],strike="Call",opencrossed="Nil",time=liveData[e.symbol][5],date=dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S'),section=section,difference=difference,change_perc=liveData[e.symbol][6])
                                callone.save()
                        except Exception as ex:
                            print(ex)

                    # Put
                    if e.symbol in liveData and e.symbol in below:
                        try:
                            print("the symbol is in above")
                            # Difference Calculation
                            historycall = HistoryOIChange.objects.filter(symbol=e.symbol)
                            historyput = HistoryOITotal.objects.filter(symbol=e.symbol)
                            strikegp = LiveOITotal.objects.filter(symbol=e.symbol)

                            if len(historycall) > 0:
                                diffcallstrike = HistoryOIChange.objects.filter(symbol=e.symbol).earliest('time')
                                diffcallstrike = diffcallstrike.callstrike
                                print("######### PUT #############")
                                print(f"diff call history {diffcallstrike}")
                                history_len = 0
                                if diffcallstrike == 0 or diffcallstrike == '0':
                                    diffcallstrike_db = HistoryOIChange.objects.filter(symbol=e.symbol).order_by('time')
                                    count = 1
                                    while diffcallstrike == 0 or diffcallstrike == '0':
                                        if count < len(diffcallstrike_db):
                                            diffcallstrike = diffcallstrike_db[count].putstrike
                                            count +=1
                                        else:
                                            diffcallstrike = LiveOIChange.objects.filter(symbol=e.symbol).earliest('time')
                                            diffcallstrike = diffcallstrike.callstrike
                                            break
                            else:
                                is_available = LiveOIChange.objects.filter(symbol=e.symbol)
                                if len(is_available) > 0:
                                    diffcallstrike = LiveOIChange.objects.filter(symbol=e.symbol).earliest('time')
                                    diffcallstrike = diffcallstrike.callstrike
                                    if diffcallstrike == 0 or diffcallstrike == '0':
                                        diffcallstrike = LiveOIChange.objects.filter(symbol=e.symbol).order_by('time')
                                        diffcallstrike = diffcallstrike[1].callstrike
                                else:
                                    diffcallstrike = 0
                                # diffcallstrike = e.callstrike

                            if len(historyput) > 0:
                                diffputstrike = HistoryOITotal.objects.filter(symbol=e.symbol).earliest('time')
                                diffputstrike = diffputstrike.putstrike
                            else:
                                diffputstrike = LiveOITotal.objects.filter(symbol=e.symbol).earliest('time')
                                diffputstrike = diffputstrike.putstrike
                            
                            difference = float(diffcallstrike) - float(diffputstrike)
                            section = int(abs((float(diffcallstrike) - float(diffputstrike))/float(strikegp[0].strikegap)))
                            
                            if e.symbol in callcrossedsetDict or e.symbol in callonepercentsetDict:
                                LiveEquityResult.objects.filter(symbol=e.symbol).update(ltp=liveData[e.symbol][0],high=liveData[e.symbol][2],low=liveData[e.symbol][3])
                                print("already crossed")
                                continue
                                
                            # open check
                            if float(liveData[e.symbol][1]) < float(putstrike):
                                print("open check")
                                if e.symbol in openputcrossDict:
                                    LiveEquityResult.objects.filter(symbol=e.symbol).update(ltp=liveData[e.symbol][0],high=liveData[e.symbol][2],low=liveData[e.symbol][3])
                                    # LiveEquityResult.objects.filter(symbol = e.symbol).delete()
                                    # putcross = LiveEquityResult(symbol=e.symbol,open=liveData[e.symbol][1],high=liveData[e.symbol][2],low=liveData[e.symbol][3],prev_day_close=liveData[e.symbol][4],ltp=liveData[e.symbol][0],strike="Put Crossed",opencrossed="put",time=openputcrossDict[e.symbol][0],date=dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S'),section=section,difference=difference,change_perc=liveData[e.symbol][6],below_three=openputcrossDict[e.symbol][1])
                                    # putcross.save()
                                    continue
                                else:
                                    if liveData[e.symbol][6] > -3 and liveData[e.symbol][6] < 0:
                                        putcross = LiveEquityResult(symbol=e.symbol,open=liveData[e.symbol][1],high=liveData[e.symbol][2],low=liveData[e.symbol][3],prev_day_close=liveData[e.symbol][4],ltp=liveData[e.symbol][0],strike="Put Crossed",opencrossed="put",time=liveData[e.symbol][5],date=dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S'),section=section,difference=difference,change_perc=liveData[e.symbol][6],below_three=True)
                                        putcross.save()
                                    else:
                                        putcross = LiveEquityResult(symbol=e.symbol,open=liveData[e.symbol][1],high=liveData[e.symbol][2],low=liveData[e.symbol][3],prev_day_close=liveData[e.symbol][4],ltp=liveData[e.symbol][0],strike="Put Crossed",opencrossed="put",time=liveData[e.symbol][5],date=dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S'),section=section,difference=difference,change_perc=liveData[e.symbol][6],below_three=False)
                                        putcross.save()
                                    continue

                            #low Check   
                            elif float(liveData[e.symbol][3]) < float(putstrike):
                                print("low check")
                                if e.symbol in putcrossedsetDict:
                                    LiveEquityResult.objects.filter(symbol=e.symbol).update(ltp=liveData[e.symbol][0],high=liveData[e.symbol][2],low=liveData[e.symbol][3])
                                    print("already crossed")
                                    # LiveEquityResult.objects.filter(symbol = e.symbol).delete()
                                    # putcross = LiveEquityResult(symbol=e.symbol,open=liveData[e.symbol][1],high=liveData[e.symbol][2],low=liveData[e.symbol][3],prev_day_close=liveData[e.symbol][4],ltp=liveData[e.symbol][0],strike="Put Crossed",opencrossed="Nil",time=putcrossedsetDict[e.symbol][0],date=dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S'),section=section,difference=difference,change_perc=liveData[e.symbol][6],below_three=putcrossedsetDict[e.symbol][1])
                                    # putcross.save()
                                    continue
                                else:
                                    print("just crossed")
                                    if liveData[e.symbol][6] > -3 and liveData[e.symbol][6] < 0:
                                        putcross = LiveEquityResult(symbol=e.symbol,open=liveData[e.symbol][1],high=liveData[e.symbol][2],low=liveData[e.symbol][3],prev_day_close=liveData[e.symbol][4],ltp=liveData[e.symbol][0],strike="Put Crossed",opencrossed="Nil",time=liveData[e.symbol][5],date=dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S'),section=section,difference=difference,change_perc=liveData[e.symbol][6],below_three=True)
                                        putcross.save()
                                    else:
                                        putcross = LiveEquityResult(symbol=e.symbol,open=liveData[e.symbol][1],high=liveData[e.symbol][2],low=liveData[e.symbol][3],prev_day_close=liveData[e.symbol][4],ltp=liveData[e.symbol][0],strike="Put Crossed",opencrossed="Nil",time=liveData[e.symbol][5],date=dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S'),section=section,difference=difference,change_perc=liveData[e.symbol][6],below_three=False)
                                        putcross.save()
                                    continue

                            #ltp check 
                            elif float(liveData[e.symbol][0]) < float(putstrike):
                                # liveData[e.symbol][0]
                                print("ltp check")
                                print("already crossed")
                                if e.symbol in putcrossedsetDict:
                                    LiveEquityResult.objects.filter(symbol=e.symbol).update(ltp=liveData[e.symbol][0],high=liveData[e.symbol][2],low=liveData[e.symbol][3])
                                    # # Deleting the older
                                    # LiveEquityResult.objects.filter(symbol =e.symbol).delete()
                                    # # updating latest data
                                    # putcross = LiveEquityResult(symbol=e.symbol,open=liveData[e.symbol][1],high=liveData[e.symbol][2],low=liveData[e.symbol][3],prev_day_close=liveData[e.symbol][4],ltp=liveData[e.symbol][0],strike="Put Crossed",opencrossed="Nil",time=putcrossedsetDict[e.symbol][0],date=dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S'),section=section,difference=difference,change_perc=liveData[e.symbol][6],below_three=putcrossedsetDict[e.symbol][1])
                                    # putcross.save()
                                    # print("put crossed updating only the data")
                                    continue
                                else:
                                    print("just crossed")
                                    if liveData[e.symbol][6] > -3 and liveData[e.symbol][6] < 0:
                                        # print("Put crossed")
                                        putcross = LiveEquityResult(symbol=e.symbol,open=liveData[e.symbol][1],high=liveData[e.symbol][2],low=liveData[e.symbol][3],prev_day_close=liveData[e.symbol][4],ltp=liveData[e.symbol][0],strike="Put Crossed",opencrossed="Nil",time=liveData[e.symbol][5],date=dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S'),section=section,difference=difference,change_perc=liveData[e.symbol][6],below_three=True)
                                        putcross.save()
                                    else:
                                        putcross = LiveEquityResult(symbol=e.symbol,open=liveData[e.symbol][1],high=liveData[e.symbol][2],low=liveData[e.symbol][3],prev_day_close=liveData[e.symbol][4],ltp=liveData[e.symbol][0],strike="Put Crossed",opencrossed="Nil",time=liveData[e.symbol][5],date=dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S'),section=section,difference=difference,change_perc=liveData[e.symbol][6],below_three=False)
                                        putcross.save()

                            elif float(liveData[e.symbol][0]) <= float(putone) and float(liveData[e.symbol][0]) > float(putstrike):
                                print("one percent check")
                                # liveData[e.symbol][0]
                                if e.symbol in putcrossedsetDict:
                                    # print("Already crossed put")
                                    continue
                                else:
                                    if e.symbol in putonepercentsetDict:
                                        LiveEquityResult.objects.filter(symbol=e.symbol).update(ltp=liveData[e.symbol][0],high=liveData[e.symbol][2],low=liveData[e.symbol][3])
                                        # # print("Already crossed 1 percent")
                                        # LiveEquityResult.objects.filter(symbol =e.symbol).delete()
                                        # # updating latest data
                                        # putcross = LiveEquityResult(symbol=e.symbol,open=liveData[e.symbol][1],high=liveData[e.symbol][2],low=liveData[e.symbol][3],prev_day_close=liveData[e.symbol][4],ltp=liveData[e.symbol][0],strike="Put 1 percent",opencrossed="Nil",time=putonepercentsetDict[e.symbol][0],date=dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S'),section=section,difference=difference,change_perc=liveData[e.symbol][6],below_three=putonepercentsetDict[e.symbol][1])
                                        # putcross.save()
                                        continue
                                    else:
                                        LiveEquityResult.objects.filter(symbol=e.symbol).delete()
                                        if liveData[e.symbol][6] > -3 and liveData[e.symbol][6] < 0:
                                            # print("Put 1 percent")
                                            putone = LiveEquityResult(symbol=e.symbol,open=liveData[e.symbol][1],high=liveData[e.symbol][2],low=liveData[e.symbol][3],prev_day_close=liveData[e.symbol][4],ltp=liveData[e.symbol][0],strike="Put 1 percent",opencrossed="Nil",time=liveData[e.symbol][5],date=dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S'),section=section,difference=difference,change_perc=liveData[e.symbol][6],below_three=True)
                                            putone.save()
                                        else:
                                            putone = LiveEquityResult(symbol=e.symbol,open=liveData[e.symbol][1],high=liveData[e.symbol][2],low=liveData[e.symbol][3],prev_day_close=liveData[e.symbol][4],ltp=liveData[e.symbol][0],strike="Put 1 percent",opencrossed="Nil",time=liveData[e.symbol][5],date=dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S'),section=section,difference=difference,change_perc=liveData[e.symbol][6],below_three=False)
                                            putone.save()
                            else:
                                print("default update")
                                LiveEquityResult.objects.filter(symbol=e.symbol).delete()
                                putone = LiveEquityResult(symbol=e.symbol,open=liveData[e.symbol][1],high=liveData[e.symbol][2],low=liveData[e.symbol][3],prev_day_close=liveData[e.symbol][4],ltp=liveData[e.symbol][0],strike="Put",opencrossed="Nil",time=liveData[e.symbol][5],date=dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S'),section=section,difference=difference,change_perc=liveData[e.symbol][6])
                                putone.save()
                        except Exception as ex:
                            print(ex)

                except Exception as equityException:
                    print(f"Exception for {e.symbol} with {equityException}")
                    continue

            connection_check = 'end'

        except websocket.WebSocketConnectionClosedException as e:
            print('This caught the websocket exception in equity realtime')
            td_app.disconnect()
            td_app.disconnect()
            # return render(request,"testhtml.html",{'symbol':item,'counter':1}) 
        except IndexError as e:
            print('This caught the exception in equity realtime')
            print(e)
            td_app.disconnect()
            td_app.disconnect()
        except Exception as e:
            print(e)
            td_app.disconnect()
            td_app.disconnect()

while True:

    if "connection_check" in locals():
        pass
    else:
        print('not in locals')
        connection_check = ''
    connection_check = equity(connection_check)
