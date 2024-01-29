"""

import sqlite3

database_name = 'db.sqlite3'
connection = sqlite3.connect(database_name)
cursor = connection.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

for table in tables:
    table_name = table[0]
    print(f"\nTable: {table_name}\n{'=' * 20}")
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    print("Columns:")
    for column in columns:
        print(f"  {column[1]} - {column[2]} - {column[3]} - {column[4]}")#column0?
    cursor.execute(f"SELECT * FROM {table_name};")
    rows = cursor.fetchall()
    print("\nData:")
    for row in rows:
        print(row)
connection.close()

"""

import os
import sys
import django
from . import models
from . import uygulama


sys.path.append('DOSYAYOLU')


os.environ.setdefault('DJANGO_SETTINGS_MODULE', uygulama.settings')
django.setup()

from app import models

def check_database():
    try:
        models_list = [
            models.Category,
            models.ComponentDocumentLink,
            models.Component,
            models.DocumentType,
            models.Document,
            models.LocationType,
            models.Location,
            models.Manufacturer,
            models.Package,
            models.PurchaseDetail,
            models.Purchase,
            models.Supplier,
            models.StockMovement,
        ]

        for model in models_list:
            model_name = model.__name__
            if model.objects.exists():
                print(f"{model_name} modeli veritabanında mevcut.")
            else:
                print(f"{model_name} modeli veritabanında bulunamadı.")
    except Exception as e:
        print(f"Hata: {e}")
if __name__ == '__main__':
    check_database()


#  python3 databasekontrol.py