import pyorient
import sys

client = pyorient.OrientDB("localhost", 2424)
session_id = client.connect("root", "admin")
db_name = "soufun"
db_username = "admin"
db_password = "admin"

if client.db_exists( db_name, pyorient.STORAGE_TYPE_MEMORY ):
	client.db_open( db_name, db_username, db_password )
	print db_name + " opened successfully"
else:
	print "database [" + db_name + "] does not exist! session ending..."
	sys.exit()

lat1 = 22.532498
lat2 = 22.552317

lng1 = 114.044329
lng2 = 114.076644

query = 'SELECT FROM Listing WHERE latitude BETWEEN {} AND {} AND longitude BETWEEN {} AND {}'

records = client.command(query.format(lat1, lat2, lng1, lng2))

numListings = len(records)

print 'received ' + str(numListings) + ' records'

sumPrice = 0
minPrice = 1000000
maxPrice = 1

for record in records:
	print record.price

        sumPrice += record.price
        averagePrice = sumPrice / numListings
        
        if record.price < minPrice:
            minPrice = record.price
            
        if record.price > maxPrice:
            
            maxPrice = record.price

# [PRINT OUT THE RESULTING VALUES BY CONCATENATING THEM TO THESE LINES TO CHECK YOUR WORK]

print 'min price: ' + str(minPrice)
print 'max price: ' + str(maxPrice)
print 'average price: ' + str(averagePrice)

client.db_close()
