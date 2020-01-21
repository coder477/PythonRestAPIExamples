'''
Created on 30-Sep-2019

@author: sneha
'''

import pymysql.cursors
import pymysql.connections


db=pymysql.connect(
    host="localhost",
    db="tcart_db",
    user="root",
    password="root")

cur=db.cursor()