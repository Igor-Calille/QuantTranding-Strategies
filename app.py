import pandas as pd
import StockIntegration as si
import Estrategias.CombinacaoIndicadoresTecnicos as cit
import BackTesting as bt
import dashboard as db

data = si.yfinance().get_data_yfinance('TSLA', '2019-01-01')

data = cit.MeanReversion().MR_1(data, media_movel=[20], rsi_periodo=[14], bollinger_periodo=[20])
#data = cit.MomentumTrading().MT_1(data)


data.to_csv('output/data.csv', index=False)


data, count_signals = bt.BackTesting().backtest_signals_date_rpt(data, '2019-01-01', 10000)

precison, count = bt.precision().check_precision(data)

print(f"Total de sinais: {count_signals}")
print("resultado final: ",data['current_value'].iloc[-1])
print("precision: ", precison)
print("count successful: ", count)

db.dashboard().plot_portfolio_price(data)
