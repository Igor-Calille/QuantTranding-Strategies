import plotly.graph_objects as go
import pandas as pd

class dashboard():
    def __init__(self):
        pass

    def plot_portfolio_price(self, data):

        data['date'] = pd.to_datetime(data['date'])

        fig = go.Figure()

        fig.add_trace(go.Scatter(x=data['date'], y=data['current_value'], mode='lines+markers', name='Portfolio Value'))

        fig.update_layout(
            title='Portfolio Value Over Time',
            xaxis_title='Date',
            yaxis_title='Portfolio Value (USD)',
            xaxis=dict(tickformat='%Y-%m-%d')
        )

        fig.show()
