import pandas as pd 
import json 
import sqlite3
import requests 
from sqlalchemy import create_engine


with open("C:/Users/User/OneDrive/Documents/test2/books.json") as f:

    data = json.loads(f)
##data = json.load(f.text)
#
df = pd.DataFrame(data)
#print(df.head())
##df.columns()
engine = create_engine("sqllite:///C:/Users/User/OneDrive/Documents/test2/db.sqlite3")
df.to_sql('books2', engine)
##sql connection 
#
#con = sqlite3.connect("C:/Users/User/OneDrive/Documents/test2/db.sqlite3")
#cur = con.cursor() 
#df.to_sql("books2",con)
