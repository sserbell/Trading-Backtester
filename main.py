from data_fetcher import get_historical_data
from strategy import add_moving_averages, generate_signals
from backtester import run_backtest
import matplotlib.pyplot as plt

user_ticker = input("Please input a ticker you would like to test on: ")
start_date = input("Please enter a start date (YYY-MM-DD): ")
end_date = input("Please enter an end date (YYY-MM-DD): ")

ticker = user_ticker.strip().upper()
data = get_historical_data(ticker,start_date, end_date)
data = add_moving_averages(data, short_window = 10, long_window = 50)
data = generate_signals(data)
data = data.dropna()

final_value, profit, portfolio_values = run_backtest(data, 1000)
print("\nFinal Portfolio Value:", round(final_value, 2))
print("Total Profit:", round(profit, 2))

import matplotlib.pyplot as plt

plt.plot(portfolio_values)
plt.title("Portfolio Value Over Time")
plt.xlabel("Time")
plt.ylabel("Portfolio Value")
plt.show()

