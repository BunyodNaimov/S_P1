import requests
import json

url = "https://currency-converter18.p.rapidapi.com/api/v1/supportedCurrencies"


def currency_converter():
    from_currency = "USD"
    to_currency = "UZS"
    amount = "1"
    querystring = {"from": from_currency, "to": to_currency, "amount": amount}
    headers = {
        "x-rapidapi-key": "1146a909c1msh0d3fcafbd793c83p1d4b63jsn178a843fa214",
        "x-rapidapi-host": "currency-converter18.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = json.loads(response.text)
    # amount = data['result']
    print(data)


currency_converter()
