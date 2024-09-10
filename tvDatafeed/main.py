from tvDatafeed import TvDatafeed, Interval
#from tvDatafeed import TvDatafeedLive

# username = 'YourTradingViewUsername'
# password = 'YourTradingViewPassword'

#tvl = TvDatafeedLive()

# username = 'YourTradingViewUsername'
# password = 'YourTradingViewPassword'

tv = TvDatafeed()

# index
nifty_index_data = tv.get_hist(symbol='NIFTY',exchange='NSE',interval=Interval.in_daily,n_bars=1000)

# # futures continuous contract
# nifty_futures_data = tv.get_hist(symbol='NIFTY',exchange='NSE',interval=Interval.in_1_hour,n_bars=1000,fut_contract=1)

# # crudeoil
# crudeoil_data = tv.get_hist(symbol='CRUDEOIL',exchange='MCX',interval=Interval.in_1_hour,n_bars=5000,fut_contract=1)

# # downloading data for extended market hours
# extended_price_data = tv.get_hist(symbol="EICHERMOT",exchange="NSE",interval=Interval.in_1_hour,n_bars=500, extended_session=False)
print(nifty_index_data)
nifty_index_data.to_csv("nifty.csv")
