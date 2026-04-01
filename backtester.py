import yfinance as yf
import pandas as pd

def run_backtest(df, initial_cash):
    cash = initial_cash
    position = 0 #number of shares
    portfolio_values = []
    for index, row in df.iterrows():
        signal = int(row['Signal'])
        price = float(row['Close'])
        
        #Buy
        if signal == 1 and cash > 0:
            position = cash / price #buy as many shares as possible
            cash = 0
            print(f"BUY at {price:.2f}")
        
        #Sell
        elif signal == -1 and position > 0:
            cash = position * price
            position = 0
            print(f"SELL at {price:.2f}")
        total_value = cash + (position * price)
        portfolio_values.append(total_value)
    
    final_value = cash + (position + float(df.iloc[-1]['Close']))
    profit = float(final_value - initial_cash)
    
    return final_value, profit, portfolio_values