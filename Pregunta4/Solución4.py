import requests

def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        bitcoin_price_usd = data["bpi"]["USD"]["rate_float"]
        return bitcoin_price_usd
    except Exception as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None

def save_price_to_txt(price, filename):
    try:
        with open(filename, "w") as file:
            file.write(str(price))
        print("Precio de Bitcoin almacenado en el archivo:", filename)
    except Exception as e:
        print("Error al guardar el precio de Bitcoin en el archivo:", e)

def main():
    bitcoin_price = get_bitcoin_price()

    if bitcoin_price is not None:
        save_price_to_txt(bitcoin_price, "bitcoin_price.txt")
    else:
        print("No se pudo obtener el precio de Bitcoin.")

if __name__ == "__main__":
    main()
