import pandas as pd
import StockIntegration as si
import Estrategias.CombinacaoIndicadoresTecnicos as cit


data = si.yfinance().get_data_yfinance('AAPL', '2021-01-01')

data = cit.MeanReversion().MR_1(data, media_movel=[20], rsi_periodo=[14], bollinger_periodo=[20])

data.to_csv('output/data.csv', index=False)