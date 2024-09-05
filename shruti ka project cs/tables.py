import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="")
mycursor=mydb.cursor()
mycursor.execute("create database sscontractors")


#table1 for mason labour

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="sscontractors")
mycursor=mydb.cursor()
mycursor.execute("create table mason_labour(name varchar(100),age varchar(100),weight varchar(100),adhaar_card_no varchar(100),bank_account_details varchar(100))")

#table2 for carpenter labour

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="sscontractors")
mycursor=mydb.cursor()
mycursor.execute("create table carpenter_labour(name varchar(100),age varchar(100),working_experience varchar(100),adhaar_card_no varchar (100),bank_account_details varchar(100))")

#table3 for customer info.

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="sscontractors")
mycursor=mydb.cursor()
mycursor.execute("create table customer_info(name_of_company varchar(100),years_worked varchar(100),no_of_labours_working varchar(100),no_of_projects_done varchar(100),profit varchar(100))")

#table4 for male labour

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="sscontractors")
mycursor=mydb.cursor()
mycursor.execute("create table male_labour(name varchar(100),age varchar(100),weight varchar(100),adhaar_card_no varchar(100),bank_account_details varchar(100))")

#table5 for female labour

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="sscontractors")
mycursor=mydb.cursor()
mycursor.execute("create table female_labour(name varchar(100),age varchar(100),weight varchar(100),adhaar_card_no varchar(100),bank_account_details varchar(100))")
