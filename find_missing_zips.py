import csv
from pyzipcode import ZipCodeDatabase
myzip = ZipCodeDatabase()
infile = open('ZIP_Locale_Detail.csv', mode='r')
missing_zips_file = open('missing_zips.txt', mode='w')
csvFile = csv.reader(infile)
for line in csvFile:
    try:
        testzip = myzip[line[4]]
    except:
        zip = line[4]
        zip_2 = line[9]
        state = line[8]
        city_split = line[7].split(' ')
        city_parts = [ city_word.capitalize() for city_word in city_split ]
        city = ' '.join(city_parts)
        csv_string = zip + ','+ zip_2 + ',' + city + ',' + state + '\n'
        len = missing_zips_file.write(csv_string)

