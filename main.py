import requests

API_KEY = 'c13a5d2ecf7cc6b8c50c06d7e1dfce22'
STOCKS = ['AAPL', 'GOOGL', 'AMZN', 'TSLA', 'FB', 'TWTR', 'UBER', 'LYFT', 'SNAP', 'SHOP']


def get_value(stock):
    url = f'https://financialmodelingprep.com/api/v3/quote-short/{stock}?apikey={API_KEY}'
    response = requests.get(url)
    return float(response.json()[0].get('price'))


if __name__ == '__main__':
    values = sum([get_value(stock) for stock in STOCKS])
    print(values)
