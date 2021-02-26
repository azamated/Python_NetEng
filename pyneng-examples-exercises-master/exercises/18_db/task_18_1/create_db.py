# -*- coding: utf-8 -*-
import sqlite3
import os
import sys

#Creating DB function
def create_db(db_name):
	if os.path.isfile(db_name):
		print ("DB is alredy created")		
	else:	
		try:
			conn = sqlite3.connect(db_name)
			print ("SQLITE verison is: " + sqlite3.version)
			print ("Creating DB ...")
	
		except Error as e:
			print(e)
	
		finally:
			if conn:
				conn.close()
		print ("DONE!!!")

#Create tables function
def create_tables(db_name, tables_schema):
	with open(tables_schema) as f:
		conn = sqlite3.connect(db_name)
		try:
			conn.executescript(f.read())
			print ('Creating tables >>>')
			print ('DONE!!!')
		
		except sqlite3.OperationalError as e:
			print (e)
		
		finally:
			if conn:
				conn.close()	
		

if __name__ == '__main__':
	create_db(r"dhcp_snooping.db")
	create_tables('dhcp_snooping.db', 'dhcp_snooping_schema.sql')
	
	
	
	
	
	
