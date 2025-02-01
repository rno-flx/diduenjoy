
import mysql.connector

def addIntoDatabase(data):
    conn = mysql.connector.connect(
        user='root', password='root', host='127.0.0.1', database='init.sql'
    )
    mycursor = conn.cursor()
    for item in data:
        sql = "INSERT INTO public.items (id, name, price, ref, packageId, warranty, duration) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (item['name'], item['price'], item['ref'], item['packageId'], item['warranty'], item['duration'])
        mycursor.execute(sql, val)
    conn.commit()
    mycursor.close()
    conn.close()
    pass
