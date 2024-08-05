import pandas as pd
import StockIntegration as si
import Estrategias.CombinacaoIndicadoresTecnicos as cit
import BackTesting as bt


data = si.yfinance().get_data_yfinance('AAPL', '2021-01-01')

data = cit.MeanReversion().MR_1(data, media_movel=[20], rsi_periodo=[14], bollinger_periodo=[20])

data.to_csv('output/data.csv', index=False)


data, count_signals = bt.BackTesting().backtest_signals_date_rpt(data, '2024-01-01', 10000)

print(f"Total de sinais: {count_signals}")
print("resultado final: ",data['current_value'].iloc[-1])