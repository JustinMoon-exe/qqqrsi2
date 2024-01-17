        plt.figure(figsize=(12, 8))

        plt.subplot(2, 1, 1)
        plt.plot(rsi_strategy_result.index, rsi_strategy_result['Cumulative Strategy Returns'], label='Strategy Returns', linewidth=2)
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
