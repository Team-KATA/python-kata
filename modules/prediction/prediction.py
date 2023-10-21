import pandas as pd

# from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from pmdarima import auto_arima

# 상대경로
def load_csv(_file_name, _index_col):
    df = pd.read_csv(_file_name)
    df.set_index(_index_col)
    return df

def defferencing_data(_df, _col):
    diff_df = _df.copy()
    diff_df = diff_df[_col].diff().dropna()
    return diff_df

def optimize_order(_df):
    return auto_arima(_df,  seasonal=False, m=12, trace=True, suppress_warnings=True)

def train(_df, _col, _order):
    # ARIMA 모델 정의 및 학습
    model = SARIMAX(_df[_col], order=_order.order, seasonal_order=_order.seasonal_order)
    # 모델 훈련
    model_fit = model.fit()
    return model_fit

def forecast(_model, _start, _end):
    _forecast = _model.predict(start=_start, end=_end)
    _forecast.plot()
    return _forecast

def prediction(_df, _col, _index_col, _start):
    df = load_csv(_df, _index_col)
    diff_df = defferencing_data(df, _col)
    best_order = optimize_order(diff_df)
    model = train(df, _col, best_order)
    result = forecast(model, int(len(df)*_start), len(df)-1)
    return list(result)


result = prediction("arima_train - full.csv", "dew", "datetime", 0.98)
print(f'result : \n{result}')
    