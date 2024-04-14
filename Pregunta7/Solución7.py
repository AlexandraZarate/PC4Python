import requests
import sqlite3

# Obtener los datos del API
url = "https://api.apis.net.pe/v1/tipo-cambio-sunat?month=3&year=2023"
response = requests.get(url)
data = response.json()

# Crear una base de datos y una tabla
conn = sqlite3.connect('base.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS sunat_info (
                    compra REAL,
                    venta REAL,
                    origen TEXT,
                    moneda TEXT,
                    fecha TEXT
                  )''')

# Insertar los datos en la tabla
for registro in data:
    compra = registro['compra']
    venta = registro['venta']
    origen = registro['origen']
    moneda = registro['moneda']
    fecha = registro['fecha']
    cursor.execute('''INSERT INTO sunat_info (compra, venta, origen, moneda, fecha)
                      VALUES (?, ?, ?, ?, ?)''', (compra, venta, origen, moneda, fecha))

# Confirmar los cambios
conn.commit()

# Mostrar el contenido de la tabla
cursor.execute('''SELECT * FROM sunat_info''')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Cerrar la conexión
conn.close()
