import pypyodbc

mySQLServer = "CPMPUTERNAME\SQLNAME"
myDatabase = "DBNAME"

connection = pypyodbc.connect('Driver={SQL Server};'
							'Server=' + mySQLServer + ';'
							'Database=' + myDatabase + ';')

cursor = connection.cursor()

mySQLQuery = ("""
		SELECT CompanyName, ContactName, Country
		From dbo.Customers
		WHERE Country = 'Canada'
	""")

cursor.execute(mySQLQuery)
results = cursor.fetchall()

print(results)
for row in results:
	companyname = row[0]
	contactname = row[1]
	countryname = row[2]

	print(companyname + ' : ' + contactname + ' : ' + countryname)

connection.close()
