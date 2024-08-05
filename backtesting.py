import pandas as pd

class BackTesting():
    def __init__(self):
        pass

    def backtest_signals_date_rpt(self, data, date, initial_capital, risk_per_trade=1.0, slippage=0.0):
        cash = initial_capital
        current_value = initial_capital
        position = 0
        date = pd.to_datetime(date)
        count_signals = 0
        up_slippage = 1 + slippage
        down_slippage = 1 - slippage
        
        # Iniciando a coluna do valor da carteira
        data['current_value'] = initial_capital

        for index, row in data.iterrows():
            if pd.to_datetime(row['date']) >= date:
                
                buy_price = row['close'] * up_slippage
                sell_price = row['close'] * down_slippage
                amount_to_risk = cash * risk_per_trade

                if row['signal'] == 1 and cash > 0:
                    #shares_to_buy = (amount_to_risk / buy_price) * abs(row['bollinger_low_proportion_20'])
                    shares_to_buy = (amount_to_risk / buy_price) 
                    position += shares_to_buy
                    cash -= shares_to_buy * buy_price
                    count_signals += 1

                elif row['signal'] == -1 and position > 0:
                    #shares_to_sell = position * abs(row['bollinger_high_proportion_20'])
                    shares_to_sell = position
                    cash += shares_to_sell * sell_price
                    position -= shares_to_sell
                    count_signals += 1

                current_value = cash + position * row['close']
                data.at[index, 'current_value'] = current_value
            else:
                if index > 0:
                    data.at[index, 'current_value'] = data.at[index-1, 'current_value']
                else:
                    data.at[index, 'current_value'] = initial_capital
        
        # Preenchendo os valores restantes após a última trade
        for index in range(len(data)-1):
            if data.at[index+1, 'current_value'] == initial_capital:
                data.at[index+1, 'current_value'] = data.at[index, 'current_value']
        
        return data, count_signals
    
class precision():
    def  __init__(self):
        pass

    def check_precision(self, data):

        count_successful_signal = 0
        total_signals = 0
        
        for index in range(len(data) - 1):
            current_row = data.iloc[index]
            next_row = data.iloc[index + 1]

            if current_row['signal'] == 1 and next_row['close'] > current_row['close']:
                count_successful_signal += 1
            elif current_row['signal'] == -1 and next_row['close'] < current_row['close']:
                count_successful_signal += 1

            if current_row['signal'] == 1 or current_row['signal'] == -1:
                total_signals += 1

        precision = count_successful_signal / total_signals if total_signals > 0 else 0

        return precision, count_successful_signal


