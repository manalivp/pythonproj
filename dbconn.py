import mysql.connector
import pandas as pd
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="manali",
  database="DA"
)
print(dataBase)
