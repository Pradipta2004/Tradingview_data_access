from tvDatafeed import TvDatafeedLive, Interval

# Function to print the live price of an asset
def print_live_price(symbol, exchange, interval):
    # Initialize TvDatafeedLive without login
    tvl = TvDatafeedLive()

    # Create a Seis (Symbol-Exchange-Interval-Set) for the asset
    seis = tvl.new_seis(symbol, exchange, interval)

    # Define a consumer function to print the live price
    def live_price_consumer(seis, data):
        print(f"Live Price Update - {seis.symbol} on {seis.exchange} ({seis.interval.name}): {data.close[0]}")

    # Register the consumer function with the Seis
    seis.new_consumer(live_price_consumer)

    # Keep the program running to receive live updates
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Live price feed stopped.")

# Main function to run the live price feed
def main():
    # Specify the symbol, exchange, and interval for the asset
    symbol = 'NIFTY'
    exchange = 'NSE'
    interval = Interval.in_1_minute

    print("Starting live price feed...")
    print_live_price(symbol, exchange, interval)

# Run the program
if __name__ == "__main__":
    main()
