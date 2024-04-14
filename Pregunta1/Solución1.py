import requests

def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        bitcoin_price_usd = data["bpi"]["USD"]["rate_float"]
        return bitcoin_price_usd
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None

def main():
    n_bitcoins = float(input("Ingrese la cantidad de bitcoins que posee: "))
    bitcoin_price = get_bitcoin_price()

    if bitcoin_price is not None:
        cost_in_usd = n_bitcoins * bitcoin_price
        print(f"El costo actual de {n_bitcoins} bitcoins es: ${cost_in_usd:,.4f}")
    else:
        print("No se pudo obtener el precio de Bitcoin.")

if __name__ == "__main__":
    main()


