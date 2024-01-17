# Quantitative Trading Strategy - RSI Mean Reversion

## Overview

This Python script implements a trading strategy based on Relative Strength Index (RSI) mean reversion. RSI is a momentum oscillator that measures the speed and change of price movements. The strategy aims to capture potential price reversals by identifying overbought or oversold conditions in the market.

## Performance Statistics

### Sharpe Ratio

The Sharpe Ratio is a measure of risk-adjusted returns. For the implemented strategy:

- Sharpe Ratio: 0.0462

### Maximum Drawdown

Maximum Drawdown represents the maximum loss from a peak to a trough of the portfolio. For the implemented strategy:

- Maximum Drawdown: -0.1442

### Annualized Return

The Annualized Return provides an annualized measure of performance. For the implemented strategy:

- Annualized Return: 0.0462

## Visualization

Here is the cumulative returns and net gains/losses comparison graph:

![Strategy Performance](/Figure_1.png)

## How to Run

To run the script locally without using the QuantConnect API, follow these steps:

1. Install necessary Python modules: pandas, numpy, matplotlib, talib, seaborn.
2. Adjust the code to accept data from your preferred data source.
3. Run the script.

## Additional Notes

- Customize parameters such as RSI period, RSI entry threshold, and initial investment as needed.
- The script includes visualizations of cumulative returns and net gains/losses for easy performance analysis.

Feel free to explore and modify the script to suit your preferences and data sources.
