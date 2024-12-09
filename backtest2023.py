import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import random

def get_portfolio_return():
    num_stocks = int(input("How many stocks in portfolio? "))
    tickers = []
    weights = []

    for i in range(num_stocks):
        ticker = input(f"Enter the ticker symbol for stock {i + 1} for example TSLA, NVDA: ")
        weight = float(input(f"Enter the weight for stock {i + 1} (in percentage, like 20 for 20%): ")) / 100  # Convert to decimal
        tickers.append(ticker)
        weights.append(weight)

    start_date = '2023-01-03'
    end_date = '2023-12-29'
    
    # Stock data for the specified period
    price_data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    
    # Daily price changes in percentage
    returns = price_data.pct_change(fill_method=None).dropna()

    # Portfolios return based on weights
    portfolio_return = (returns * weights).sum(axis=1)
    
    # Calculate total portfolio return for the year 2023
    total_return = (1 + portfolio_return).prod() - 1

    # Show total portfolio return
    print(f"Your total portfolio return for 2023: {total_return:.2%}")
    
    # Random colors for the pie chart
    colors = [f'#{random.randint(0, 0xFFFFFF):06x}' for _ in range(len(tickers))]

    # Pie chart for portofolios weights
    plt.figure(figsize=(10, 6))
    plt.pie(weights, labels=tickers, autopct='%1.1f%%', startangle=90, colors=colors)
    plt.title('Portfolio allocation at the start of 2023')
    plt.show()

    # Bar chart for individual stock returns
    stock_returns_2023 = (price_data.iloc[-1] / price_data.iloc[0] - 1) * 100
    stock_returns_2023 = stock_returns_2023.sort_values(ascending=False)

    # Coloring the bars
    colors = ['green' if return_ >= 0 else 'red' for return_ in stock_returns_2023]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(stock_returns_2023.index, stock_returns_2023, color=colors)
    
    # Line showing portofolios total return
    plt.axhline(y=total_return * 100, color='blue', linestyle='--', label=f'Total Portfolio Return: {total_return * 100:.2f}%')
    
    # Annotate the total portfolio return
    plt.text(len(stock_returns_2023) - 1, total_return * 100, f'{total_return * 100:.2f}%', color='blue', va='center', ha='left', fontsize=12)

    plt.title('Stock Returns in 2023')
    plt.ylabel('Return (%)')
    plt.xlabel('Stock')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

get_portfolio_return()
