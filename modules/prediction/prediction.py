import pandas as pd

# from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from pmdarima import auto_arima

# 상대경로
def load_csv(_file_name: str, _index_col: str):
    df = pd.read_csv(_file_name)
    df.set_index(_index_col)
    return df

def defferencing_data(_df, _col: str):
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

def forecast(_model: SARIMAX, _start: int, _amount: int) -> pd.core.series.Series:
    _forecast = _model.predict(start=_start, end=_amount)
    return _forecast

def prediction(_df: str, _col: str, _index_col: str, _amount: float):
    df = load_csv(_df, _index_col)
    diff_df = defferencing_data(df, _col)
    best_order = optimize_order(diff_df)
    model = train(df, _col, best_order)

    result = forecast(model, len(df), int(len(df)+_amount))

    # df[_col].plot()
    # result.plot()

    return result


# result = prediction("/workspace/Forage/python-kata/modules/prediction/arima_train - full.csv", "dew", "datetime", 10)
# print(f'result : \n{result}')
