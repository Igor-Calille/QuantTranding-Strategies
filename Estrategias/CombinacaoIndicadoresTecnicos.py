
from typing import List, Union
import pandas as pd
import IndicadoresTecnicos as it

"""
Descrição: Baseia-se na suposição de que os preços de um ativo tendem a voltar à sua média histórica.
Aplicação: Compra de ativos subvalorizados (abaixo da média) e venda de ativos sobrevalorizados (acima da média).
Indicadores Usados: Bollinger Bands, Média Móvel, RSI (Relative Strength Index).
"""
class MeanReversion():
    def __init__(self):
        pass

    def MR_1(self, data, media_movel: Union[List[int], None]=[20], rsi_periodo: Union[List[int], None]=[14], bollinger_periodo: Union[List[int], None]=[20]):

        if media_movel is not None:
            if not isinstance(media_movel, list):
                raise ValueError("media_movel deve ser uma lista de inteiros")
            else:
                for periodo in media_movel:
                    data[f"MM_{periodo}"] = it.IndicadoresTecnicos().computar_media_movel(data['close'], periodo)
                    data[f'MM_proportion_{periodo}'] = (data[f'MM_{periodo}'] - data['close']) / data['close'] 

        if rsi_periodo is not None:
            if not isinstance(rsi_periodo, list):
                raise ValueError("rsi_periodo deve ser uma lista de inteiros")
            else:
                for periodo in rsi_periodo:
                    data[f'RSI_{periodo}'] = it.IndicadoresTecnicos().computar_RSI(data['close'], periodo)

        if bollinger_periodo is not None:
            if not isinstance(bollinger_periodo, list):
                raise ValueError("bollinger_periodo deve ser uma lista de inteiros")
            else:
                for periodo in bollinger_periodo:
                    bollinger_high, bollinger_low = it.IndicadoresTecnicos().computar_Bollinger_Bands(data['close'], periodo)
                    data[f'bollinger_high_{periodo}'] = bollinger_high
                    data[f'bollinger_low_{periodo}'] = bollinger_low
                    data[f'bollinger_low_proportion_{periodo}'] = (data[f'bollinger_low_{periodo}'] - data['close']) / data['close']
                    data[f'bollinger_high_proportion_{periodo}'] = (data[f'bollinger_high_{periodo}'] - data['close']) / data['close']

        for index, row in data.iterrows():
            if row['close'] < row['bollinger_low_20'] and row['RSI_14'] < 30 and row['MM_20'] > row['close']:
                data.at[index, 'signal'] = 1
            elif row['close'] > row['bollinger_high_20'] and row['RSI_14'] > 70 and row['MM_20'] < row['close']:
                data.at[index, 'signal'] = -1

        return data



"""
Descrição: Tenta capitalizar as tendências de alta ou baixa dos preços.
Aplicação: Compra de ativos que têm mostrado desempenho positivo e venda de ativos que têm mostrado desempenho negativo.
Indicadores Usados: Médias Móveis, Índice de Força Relativa (RSI), MACD (Moving Average Convergence Divergence).
"""
class MomentumTrading():
    def __init__(self):
        pass

"""
Descrição: Envolve a identificação de preços anômalos entre ativos relacionados e a execução de operações para explorar essas ineficiências.
Aplicação: Pairs trading (negociação em pares), market neutral strategies.
Indicadores Usados: Cointegração, Correlação, Regressão Linear.
"""
class StatisticalArbitrage():
    def __init__(self):
        pass

"""
Descrição: Baseia-se na identificação e no seguimento de tendências de mercado de longo prazo.
Aplicação: Compra de ativos em tendência de alta e venda de ativos em tendência de baixa.
Indicadores Usados: Médias Móveis, SAR Parabólico, ADX (Average Directional Index).
"""
class TrendFollowing():
    def __init__(self):
        pass