import sqlite3

conection = sqlite3.connect('marketplace.db')

# print(conection)

# conection.close()

cursor = conection.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
    );
    """
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price TEXT NOT NULL,
    stock_count INTEGER DEFAULT 1,
    description TEXT
    );
    """
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    order_date TEXT,
    FOREIGN KEY (customer_id) REFERENCES users(id)
    );
    """
)

username = "dhh"
email = "madalina"
password = "1234"

user_sql = """
INSERT INTO users (username, email, password)
VALUES (?, ?, ?);

"""

cursor.execute(user_sql, (username, email, password))

conection.commit()



# tema
# Write a SQL statement to create a table called continents, with the following columns:
# continent_id
# continent_name

cursor = conection.cursor()

continent_name = "South America"
continent_code = "SA"
'''Africa
North America
Oceania
Antarctica
Asia
Europe
South America
AF
NA
OC
AN
AS
EU
SA'''

dictionar_tari = {
    'Africa': 'AF',
    'North America': 'NA',
    'Oceania': 'OC',
    'Antarctica': 'AN',
    'Asia': 'AS',
    'Europe': 'EU',
    'South America': 'SA'
}



cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS continents(
    continent_id INTEGER PRIMARY KEY AUTOINCREMENT,
    continent_name TEXT NOT NULL,
    continent_code TEXT NOT NULL
    );
    """)

for k, v in dictionar_tari.items():
    cursor.execute(
        f"""
        INSERT INTO continents (continent_code, continent_name)
        VALUES ("{v}", "{k}");
        """
    )


#
# cursor.execute(
#     """
#     INSERT INTO continents (continent_code, continent_name)
#     VALUES (?, ?);
#     """, (continent_code, continent_name)
# )

conection.commit()
conection.close()

# continent_code – 2 letters code, use this link
# Using the link above, write all SQL statements needed to add all the seven continents (INSERT).
# Write a SQL statement to create a table called countries, with the following columns:
# country_code – 2 letters code (e.g. RO, US, IT, etc)
# country_name
# continent_id – foreign key
# population – number
# Write a few SQL statements to add some countries. Here is a list of countries with their codes. Feel free to invent or approximate their populations, and use your geography knowledge for their continent. Add at least 10 countries, as diverse as possible (INSERT). Examples:
# – Romania, EU, 19mil
# – USA, NA, 330mil
# – France, EU, 70mil
# – Hungary, EU,  9mil
# – Canada, NA, 40mil
# – China, AS, 1450mil
# – Belgium, EU, 12mil
# –  Egypt, AF, 110mil
# – Australia, OC, 25mil


dictionar = {
    1: {
        'nume': 'Africa',
        'prescurtare': 'AF'
    },
    2: {
        'nume': 'oceania',
        'prescurtare': 'OC'
    }
}

dictionar.values() # lista
for val in dictionar.values():
    val['nume'] dictionar[2]['nume'] dictionar['oceania']

dropdown_facultati = {
    'https: twitter.com': 1
    'https://google.com': 2
    2: "cccccccccccccccccccc"
    3: "universitatea bucuresti" # in dropdown vor aparea valorile, deci asta e varianta corecta
}

nr = 1283456
string = "universitatea bucuresti"

print(nr.__sizeof__())
print(string.__sizeof__())
