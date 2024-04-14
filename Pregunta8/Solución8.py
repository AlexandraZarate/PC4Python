import requests
import sqlite3
from datetime import datetime

def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        bitcoin_price_usd = data["bpi"]["USD"]["rate_float"]
        return bitcoin_price_usd
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None

def store_bitcoin_price(cursor, conn):
    bitcoin_price = get_bitcoin_price()
    if bitcoin_price is not None:
        date = datetime.now().strftime('%Y-%m-%d')
        cursor.execute('''CREATE TABLE IF NOT EXISTS bitcoin (
                            precio REAL,
                            moneda TEXT,
                            fecha TEXT
                          )''')
        cursor.execute('''INSERT INTO bitcoin (precio, moneda, fecha)
                          VALUES (?, ?, ?)''', (bitcoin_price, 'USD', date))
        conn.commit()
    else:
        print("No se pudo obtener el precio de Bitcoin.")

def calculate_cost_in_pen_and_eur(cursor):
    cursor.execute('''SELECT precio FROM bitcoin ORDER BY fecha DESC LIMIT 1''')
    bitcoin_price = cursor.fetchone()[0]

    # Consultar tipo de cambio de PEN y EUR del último registro de la tabla sunat_info
    cursor.execute('''SELECT compra, venta FROM sunat_info ORDER BY fecha DESC LIMIT 1''')
    pen_eur_exchange_rate = cursor.fetchone()

    if bitcoin_price is not None and pen_eur_exchange_rate is not None:
        pen_exchange_rate, eur_exchange_rate = pen_eur_exchange_rate
        cost_in_pen = 10 * bitcoin_price * pen_exchange_rate
        cost_in_eur = 10 * bitcoin_price * eur_exchange_rate
        print(f"El costo de comprar 10 bitcoins en PEN es: {cost_in_pen:.2f} PEN")
        print(f"El costo de comprar 10 bitcoins en EUR es: {cost_in_eur:.2f} EUR")
    else:
        print("No se pudo calcular el costo en PEN y EUR.")

def main():
    try:
        # Conexión a la base de datos
        conn = sqlite3.connect('base.db')
        cursor = conn.cursor()

        # Almacenar el precio del bitcoin en la tabla bitcoin
        store_bitcoin_price(cursor, conn)

        # Calcular el costo de comprar 10 bitcoins en PEN y EUR
        calculate_cost_in_pen_and_eur(cursor)

    except sqlite3.Error as e:
        print("Error al interactuar con la base de datos:", e)

    finally:
        # Cerrar la conexión a la base de datos
        conn.close()

if __name__ == "__main__":
    main()
