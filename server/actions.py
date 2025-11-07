import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

connection = mysql.connector.connect(
    host="localhost",
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DB")
)
cursor = connection.cursor()

def checkDbConnection():
    try:
        cursor.execute("Select * from contentType;")
    except:
        return "Connection Error"

def addNewContentType(contentTypeID,contentTypeName):

    #validate that content type does not already exist
    checkStatement = "SELECT * FROM contentType WHERE contentTypeName = %s"
    args = [contentTypeName]
    cursor.execute(checkStatement,args)
    results = cursor.fetchone()
    if results:
        return f"{contentTypeName} already exisits and is content type ID {results[0]}"
    else:
        addStatement = "insert into contentType (contentTypeID, contentTypeName) VALUES (%s,%s)"
        args = (contentTypeID,contentTypeName)
        cursor.execute(addStatement,args)
        connection.commit()
        return "200"
    
def addNewContent(contentName,contentType):


    #validate that content type does not already exist
    checkStatement = "SELECT * FROM content WHERE contentName = %s"
    args = [contentName]
    cursor.execute(checkStatement,args)
    results = cursor.fetchone()
    if results:
        return f"{contentName} already exisits"
    else:
        addStatement = "insert into content(contentName, contentType) VALUES (%s,%s)"
        args = [contentName,contentType]
        cursor.execute(addStatement,args)
        connection.commit()
        return "200"

def addDrink(drinkName):
    #validate that content type does not already exist
    checkStatement = "SELECT * FROM drink WHERE drinkName = %s"
    args = [drinkName]
    cursor.execute(checkStatement,args)
    results = cursor.fetchone()
    if results:
        return f"{drinkName} already exisits"
    else:
        addStatement = "insert into drink(drinkName) VALUES (%s)"
        args = [drinkName]
        cursor.execute(addStatement,args)
        connection.commit()
        return "200"
    
def addFormula(drinkName,contentName,quantity):
    #validate that content type does not already exist
    checkStatement = "SELECT * FROM formula WHERE drinkName = %s AND contentName = %s"
    args = [drinkName,contentName]
    cursor.execute(checkStatement,args)
    results = cursor.fetchone()
    if results:
        return f"{contentName} already exisits for {drinkName}"
    else:
        addStatement = "insert into formula(drinkName,contentName,quantity) VALUES (%s,%s,%s)"
        args = [drinkName,contentName,quantity]
        cursor.execute(addStatement,args)
        connection.commit()
        return "200"
    
def getAllFormulas():
    #get formulas for all drinks for the main page
    query = "SELECT * FROM formula"
    cursor.execute(query)
    results = cursor.fetchall()
    return results

def getFormula(drinkName):
    #pull the ingredients for a drink
    query = "SELECT * FROM formula WHERE drinkName = %s"
    args = [drinkName]
    cursor.execute(query,args)
    results = cursor.fetchall()
    return results


