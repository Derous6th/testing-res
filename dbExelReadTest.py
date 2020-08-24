from pandas import read_excel
from pyodbc import connect

df = read_excel('database.xlsx')
print(df.columns)

#[ 'Row ID', 'Order ID', 'Order Date', 'Ship Date', 'Ship Mode',
#'Customer ID', 'Customer Name', 'Segment', 'Country', 'City', 'State',
# 'Postal Code', 'Region', 'Product ID', 'Category', 'Sub-Category',
# 'Product Name', 'Sales', 'Quantity', 'Discount', 'Profit']


a = []
for i in df.index:
    #print(df['Order ID'][i], df['Order Date'][i], df['Ship Mode'][i], df['CustomerID'][i], df['Customer Name'][i])
    a.append((df['Order ID'][i],
    df['Order Date'][i],
    df['Ship Mode'][i],
    df['Customer ID'][i], 
    df['Customer Name'][i]))

db = connect('Driver={SQL Server};Server=PM408-15\\MSSQLSERVER2014;DATABASE=Store;Trusted_connection=True')
cur = db.cursor()
sql = 'INSERT INTO DataRaw(OrderID, OrderDate, ShipMode, CustomerId, CustomerName) VALUES (?, ?, ?, ?, ?)'
cur.executemany(sql, a)
db.commit()
cur.close()
db.close()