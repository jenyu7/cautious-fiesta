'''
Jen Yu
HW #09: No Treble
Software Development Pd7
2017-10-15
'''
import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

#Create a table with the specified name and column number
def create_table(table_name, num_c):
    return "CREATE TABLE " + table_name + " (" + num_c + ")"

#fill the table with contents of the inputted csv file
def populate(csv_file, table_name):
    f = open(csv_file, 'rU')
    read = csv.DictReader(f)
    for row in read:
        #insert into the table each comma separated value in the row
        j = "INSERT INTO " + table_name + " VALUES ("
        for field in row:
            j += '"' + row[field] + '",'
        j = j[0:-1]
        j += ")"
        c.execute(j)
    f.close()

#create the table 
c.execute(create_table("courses", "code TEXT, mark INTEGER, id INTEGER"))
c.execute(create_table("peeps", "name TEXT, age INTEGER, id INTEGER"))
#insert the values in the csv file
populate("courses.csv", "courses")
populate("peeps.csv", "peeps")

#==========================================================
db.commit() #save changes
db.close()  #close database
