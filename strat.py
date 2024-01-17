import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import talib
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns


date_column_name = 'date'  # Replace with the actual column name for the date
# Set dark theme style
sns.set(style="darkgrid")

# Function to implement the trading strategy
def rsi_mean_reversion_strategy(data, initial_investment=100000, rsi_period=2, rsi_entry_threshold=10):
    # Check if the dataset is not empty
    if data.empty:
        return data

    # Calculate the RSI
    data['RSI'] = talib.RSI(data['close'], timeperiod=rsi_period)

    # Define entry signals
    data['Entry Signal'] = (data['RSI'] < rsi_entry_threshold)

    # Define conditions for exit signal, implement your exit strategy here
    # For demonstration, we're using: today's close > yesterday's high
    data['Exit Signal'] = (data['close'] > data['high'].shift(1))

    # Check if there are enough rows to calculate percentage changes
    if len(data) > 1:
        # Calculate daily returns
        data['Daily Returns'] = data['close'].pct_change()

        # Calculate strategy returns
        data['Strategy Returns'] = data['Daily Returns'] * data['Entry Signal'].shift(1)

        # Calculate cumulative returns for the strategy
        data['Cumulative Strategy Returns'] = (1 + data['Strategy Returns']).cumprod() * initial_investment

    return data

# Load your QQQ dataset with pandas from the same directory
qqq_data = pd.read_csv('QQQ_raw.csv', parse_dates=['date'])


# Specify the desired date range
start_date = '2000-01-03'
end_date = '2024-01-03'

# Filter QQQ data based on the date range
qqq_data = qqq_data[(qqq_data['date'] >= start_date) & (qqq_data['date'] <= end_date)]


# Specify the initial investment amount
initial_investment = 1000

# Run the strategy function on filtered QQQ data
rsi_strategy_result = rsi_mean_reversion_strategy(qqq_data, initial_investment=initial_investment)

# Load S&P 500 data (assuming you have a CSV file named 'sp500.csv')
sp500_data = pd.read_csv('sp500.csv', parse_dates=['date'], dayfirst=False)
sp500_data['date'] = pd.to_datetime(sp500_data['date'], format='%m/%d/%Y')

# Filter S&P 500 data based on the date range
sp500_data = sp500_data[(sp500_data['date'] >= start_date) & (sp500_data['date'] <= end_date)]



# Check if the dataset is not empty before proceeding
if not sp500_data.empty:
    # Calculate daily returns for S&P 500
    sp500_data['Daily Returns'] = sp500_data['close'].pct_change()

    # Calculate cumulative returns for Buy and Hold (S&P 500)
    sp500_data['Cumulative Buy and Hold Returns'] = (1 + sp500_data['Daily Returns']).cumprod() * initial_investment

    # Check if there are enough rows to calculate strategy returns
    if len(rsi_strategy_result) > 1:
        # Calculate cumulative returns for the strategy
        rsi_strategy_result['Cumulative Strategy Returns'] = (1 + rsi_strategy_result['Strategy Returns']).cumprod() * initial_investment


        # Calculate the Sharpe Ratio
        sharpe_ratio = rsi_strategy_result['Strategy Returns'].mean() / rsi_strategy_result['Strategy Returns'].std()
        print("Sharpe Ratio:", sharpe_ratio)

        # Calculate the Maximum Drawdown
        cumulative_strategy_returns = rsi_strategy_result['Cumulative Strategy Returns']
        max_drawdown = (cumulative_strategy_returns / cumulative_strategy_returns.cummax() - 1).min()
        print("Maximum Drawdown:", max_drawdown)


        # Calculate the Sharpe Ratio
        sharpe_ratio = rsi_strategy_result['Strategy Returns'].mean() / rsi_strategy_result['Strategy Returns'].std()
        print("Sharpe Ratio:", sharpe_ratio)

        # Convert the date column to datetime and set it as the index for both dataframes
        rsi_strategy_result[date_column_name] = pd.to_datetime(rsi_strategy_result[date_column_name], format='%m/%d/%Y')
        rsi_strategy_result.set_index(date_column_name, inplace=True)

        sp500_data['date'] = pd.to_datetime(sp500_data['date'], format='%m/%d/%Y')
        sp500_data.set_index('date', inplace=True)

        # Plotting the equity curves
        plt.figure(figsize=(12, 8))

        plt.subplot(2, 1, 1)
        plt.plot(rsi_strategy_result.index, rsi_strategy_result['Cumulative Strategy Returns'], label='QQQ RSI(2) Strategy Returns', linewidth=2)
        plt.plot(sp500_data.index, sp500_data['Cumulative Buy and Hold Returns'], label='Buy and Hold (S&P 500) Returns', linewidth=2, linestyle='--')
        plt.legend()
        plt.title('Cumulative Returns Comparison')
        plt.xlabel('Date')
        plt.ylabel('Cumulative Returns')

        # Format x-axis ticks to show only years
        plt.gca().xaxis.set_major_locator(mdates.YearLocator(base=1))
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

        plt.subplot(2, 1, 2)
        plt.plot(rsi_strategy_result.index, rsi_strategy_result['Cumulative Strategy Returns'] - sp500_data['Cumulative Buy and Hold Returns'], label='Net Gains/Losses', linewidth=2, color='orange')
        plt.legend()
        plt.title('Net Gains/Losses Comparison')
        plt.xlabel('Date')
        plt.ylabel('Net Gains/Losses')

        plt.tight_layout()

        # Show the dark-themed plot
        plt.show()


    else:
        print("Not enough data points to calculate strategy returns.")
else:
    print("S&P 500 dataset is empty after filtering.")


print("Number of data points in QQQ dataset:", len(rsi_strategy_result))

print("QQQ dataset information:")
print(qqq_data.head())
print(qqq_data.columns)


