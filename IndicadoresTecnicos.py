
class IndicadoresTecnicos():
    def __init__(self):
        pass

    def computar_media_movel(self, data, periodo):
        return data.rolling(window=periodo).mean()
    
    def computar_RSI(self, data, periodo=14):
        delta = data.diff().dropna()
        gain = (delta.where(delta>0, 0)).rolling(window=periodo).mean()
        loss = (-delta.where(delta<0, 0)).rolling(window=periodo).mean()
        RS = gain/loss

        return 100 - (100/(1+RS))
    
    def computar_Bollinger_Bands(self, data, periodo=20, desvio_padrao=2):
        rolling_mean = data.rolling(window=periodo).mean()
        rolling_std = data.rolling(window=periodo).std()
        bollinger_high = rolling_mean + (desvio_padrao * rolling_std)
        bollinger_low = rolling_mean - (desvio_padrao * rolling_std)

        return bollinger_high, bollinger_low
