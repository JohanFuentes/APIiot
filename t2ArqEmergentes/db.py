import sqlite3
DATABASE_NAME = "games.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS admin(
            name TEXT NOT NULL PRIMARY KEY,
			password TEXT NOT NULL
        )""",
        """CREATE TABLE IF NOT EXISTS company(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            company_name TEXT NOT NULL,
			company_api_key TEXT NOT NULL,
            company_admin TEXT NOT NULL
        )""",
        """CREATE TABLE IF NOT EXISTS location(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_api_key TEXT NOT NULL,
            location_name TEXT NOT NULL,
			location_country TEXT NOT NULL,
			location_city TEXT NOT NULL,
            location_meta TEXT NOT NULL
        )""",
        """CREATE TABLE IF NOT EXISTS sensor(
            location_id INTEGER,
            sensor_id INTEGER PRIMARY KEY AUTOINCREMENT,
			sensor_name TEXT NOT NULL,
			sensor_category TEXT NOT NULL,
            sensor_meta TEXT NOT NULL,
			sensor_api_key TEXT NOT NULL
        )"""
    ]
    
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)

