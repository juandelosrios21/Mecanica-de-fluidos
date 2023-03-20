import pandas as pd
import yfinance as yf

# Definimos los símbolos de las compañías que nos interesan
tickers = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'AMZN']

# Definimos la fecha de inicio y fin del período que nos interesa
start_date = '2022-01-01'
end_date = '2022-12-31'

# Obtenemos los precios de las acciones de cada compañía en el período especificado
prices = pd.DataFrame()
for ticker in tickers:
    data = yf.download(ticker, start=start_date, end=end_date)['Adj Close']
    data.name = ticker
    prices = pd.concat([prices, data], axis=1)

# Agregamos las fechas como la primera columna del DataFrame
prices.insert(0, 'Fecha', prices.index)

# Guardamos los precios en un archivo Excel
prices.to_excel('precios_acciones.xlsx', index=False)
