'''
Created on 30-Sep-2019

@author: sneha
'''
import db as conencion
cursor=conencion.cur
def savetodb(item):
    query="insert into items(name) values(%s)"
    cursor.execute(query,(item))
    return conencion.db.commit()
    

def getitem(id):
    if(id):
        query="select * from items where id =(%s)"
        cursor.execute(query,(id))
    else:
        query="select * from items "
        cursor.execute(query)
    print("getting item ")
    result=[]
    for each in cursor.fetchall():
        result.append({"id":each[0],"name":each[1]})
    return {'result':result}
    
    
    