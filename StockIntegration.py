import yfinance as yf
from datetime import datetime

class yfinance():
    def __init__(self):
        pass

    def get_data_yfinance(self, symbol, start_date):
        
        data = yf.download(symbol, start=start_date)

        if data.empty:
            print("Stocks nao encontrados")
            return None
        else:
            print(f'Dados obtidos, total de linhas: {len(data)}')

        # Formatar dados
        data.reset_index(inplace=True)
        data = data.rename(columns={'Date': 'date', 'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close', 'Volume': 'volume', 'Adj Close': 'adj_close'})

        return data
    
    def get_data_yfinance_2H(symbol):
        data = yf.download(symbol, interval='1h')

        data_H = data.resample('2H').agg({
            'Open': 'first',
            'High': 'max',
            'Low': 'min',
            'Close': 'last',
            'Volume': 'sum'
        }) 

        data_H = data_H.dropna()

        data_H.reset_index(inplace=True)
        data_H = data_H.rename(columns={'Date': 'date', 'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close', 'Volume': 'volume', 'Adj Close': 'adj_close'})

        return data_H