import requests

url = "https://currency-converter5.p.rapidapi.com/currency/convert"

querystring = {"format":"json","from":"AUD","to":"CAD","amount":"1","language":"en"}

headers = {
	"x-rapidapi-key": "1146a909c1msh0d3fcafbd793c83p1d4b63jsn178a843fa214",
	"x-rapidapi-host": "currency-converter5.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
