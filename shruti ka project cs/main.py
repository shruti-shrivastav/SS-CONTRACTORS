print("**--------------------------------------------- SS CONTRACTORS ---------------------------------------------**")

c="y"
while c=="y":
    print("1.mason labour details")
    print("2.carpenter labour details")
    print("3.customer info details")
    print("4.male labours details")
    print("5.female labour details")
    print("6.Exit")
    print("\n")
    choice=int(input("enter your choice:"))
    print("\n")
    if choice==1:
        def mld():
            x="a"
            while x=="a":
                print("1.add mason labour details")
                print("2.update mason labour details")
                print("3.display mason labour details")
                print("4.search mason labour details")
                print("5.delete mason labour details")
                print("6.Exit")
                print("\n")
                b=int(input("enter your choice"))
                print("\n")
                if b==1:
                    addmld()
                elif b==2:
                    upmld()
                elif b==3:
                    dismld()
                elif b==4:
                    sermld()
                elif b==5:
                    delmld()
                else:
                    print("returning to main menu...")
                    break
        def addmld():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="sscontractors")
                mycursor=mydb.cursor()
                name=input("Enter name:")
                age=input('Enter age:')
                weight=input("Enter Weight:")
                acn=input("Enter adhaar card number:")
                bad=input('Enter account number:')
                mycursor.execute("""INSERT INTO mason_labour(name,age,weight,adhaar_card_no,bank_account_details)VALUES(%s,%s,%s,%s,%s)""",(name,age,weight,acn,bad))
                print('Record Inserted')
                mydb.commit()
            except Exception as e:
                print('unable to insert record')
                print(e)
        def upmld():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd='',db='sscontractors')
                mycursor=mydb.cursor()
                name=input("Enter name:")
                age=input('Enter age:')
                weight=input("Enter Weight:")
                acn=input("Enter adhaar card number:")
                bad=input('Enter account number:')
                mycursor.execute("""UPDATE mason_labour SET age=%s,weight=%s,adhaar_card_no=%s,bank_account_details=%s WHERE name=%s""",(age,weight,acn,bad,name))
                print('Record Updated')
                mydb.commit()
            except Exception as e:
                print('Unable to update record')
                print(e)
        def dismld():
            import mysql.connector
            from tabulate import tabulate
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd='',db='sscontractors')
                mycursor=mydb.cursor()
                mycursor.execute("select * from mason_labour")
                results=mycursor.fetchall()
                print(tabulate(results,headers=["name","age","weight","adhaar_card_no","bank_account_details"],tablefmt="fancy_grid"))
                print('Record displayed')
                mydb.commit()
            except Exception as e:
                print('Unable to display record')
                print(e)
        def sermld():
            import mysql.connector
            from tabulate import tabulate
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="sscontractors")
                mycursor=mydb.cursor()
                name=input("Enter mason labour name:")
                mycursor.execute("""Select * from mason_labour WHERE name=%s""",(name,))
                result=mycursor.fetchall()
                print(tabulate(result,headers=["name","age","weight","adhaar_card_no","bank_account_details"],tablefmt="fancy_grid"))
                print("record displayed")
                mydb.commit()
            except Exception as e:
                print("unable to search record")
                print(e)
        def delmld():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="sscontractors")
                mycursor=mydb.cursor()
                name=input("Enter name:")
                mycursor.execute("""DELETE FROM mason_labour WHERE name=%s""",(name,))
                print("record deleted")
                mydb.commit()
            except Exception as e:
                print("unable to delete record")
                print(e)
        mld()

    if choice==2:
        def cld():
            y="b"
            while y=="b":
                print("1.add carpenter labour details")
                print("2.update carpenter labour details")
                print("3.display carpenter labour details")
                print("4.search carpenter labour details")
                print("5.delete carpenter labour details")
                print("6.Exit")
                print("\n")
                c=int(input("enter your choice"))
                print("\n")
                if c==1:
                    addcld()
                elif c==2:
                    upcld()
                elif c==3:
                    discld()
                elif c==4:
                    sercld()
                elif c==5:
                    delcld()
                else:
                    print("returning to main menu...")
                    break
        def addcld():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="sscontractors")
                mycursor=mydb.cursor()
                name=input("Enter name:")
                age=input("Enter age:")
                we=input("Enter working experience:")
                acn=input("Enter adhaar card number:")
                bad=input("Enter account number:")
                mycursor.execute("""INSERT INTO carpenter_labour(name,age,working_experience,adhaar_card_no,bank_account_details)VALUES(%s,%s,%s,%s,%s)""",(name,age,we,acn,bad))
                print("Record Inserted")
                mydb.commit()
            except Exception as e:
                print("unable to insert record")
                print(e)
        def upcld():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="sscontractors")
                mycursor=mydb.cursor()
                name=input("Enter name:")
                age=input("Enter age:")
                we=input("Enter working experience:")
                acn=input("Enter adhaar card number:")
                bad=input("Enter account number:")
                mycursor.execute("""UPDATE carpenter_labour SET age=%s,working_experience=%s,adhaar_card_no=%s,bank_account_details=%s WHERE name=%s""",(age,we,acn,bad,name))
                print("Record updated")
                mydb.commit()
            except Exception as e:
                print("Unable to update record")
                print(e)
        def discld():
            import mysql.connector
            from tabulate import tabulate
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="sscontractors")
                mycursor=mydb.cursor()
                mycursor.execute("select * from carpenter_labour")
                results=mycursor.fetchall()
                print(tabulate(results,headers=["name","age","working_experience","adhaar_card_no","bank_account_details"],tablefmt="fancy_grid"))
                print("Record displayed")
                mydb.commit()
            except Exception as e:
                print("Unable to display record")
                print(e)
        def sercld():
            import mysql.connector
            from tabulate import tabulate
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="sscontractors")
                mycursor=mydb.cursor()
                name=input("Enter name:")
                mycursor.execute("""Select * from carpenter_labour WHERE name=%s""",(name,))
                result=mycursor.fetchall()
                print(tabulate(result,headers=["name","age","working_experience","adhaar_card_no","bank_account_details"],tablefmt="fancy_grid"))
                print("Record displayed")
                mydb.commit()
            except Exception as e:
                print("Unable to search record")
                print(e)
        def delcld():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="sscontractors")
                mycursor=mydb.cursor()
                name=input("Enter name:")
                mycursor.execute("""DELETE from carpenter_labour WHERE name=%s""",(name,))
                print("Record deleted")
                mydb.commit()
            except Exception as e:
                print("Unable to delete record")
                print(e)
        cld()
    if choice==3:
        def cid():
            z="c"
            while z=="c":
                print("1.add customer info details")
                print("2.update customer info details")
                print("3.display customer info details")
                print("4.search customer info details")
                print("5.delete customer info details")
                print("6.Exit")
                print("\n")
                d=int(input("enter your choice"))
                print("\n")
                if d==1:
                    addcid()
                elif d==2:
                    upcid()
                elif d==3:
                    discid()
                elif d==4:
                    sercid()
                elif d==5:
                    delcid()
                else:
                    print("Returning to main menu...")
                    break
        def addcid():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="sscontractors")
                mycursor=mydb.cursor()
                noc=input("Enter name of company:")
                yw=input("Enter years worked:")
                nolw=input("Enter number of labours working:")
                nopd=input("Enter number of projects done:")
                profit=input("Enter profit:")
                mycursor.execute("""INSERT INTO customer_info(name_of_company,years_worked,no_of_labours_working,no_of_projects_done,profit)VALUES(%s,%s,%s,%s,%s)""",(noc,yw,nolw,nopd,profit))
                print("Record Inserted")
                mydb.commit()
            except Exception as e:
                print("Unable to insert record")
                print(e)
        def upcid():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="sscontractors")
                mycursor=mydb.cursor()
                noc=input("Enter name of company:")
                yw=input("Enter years worked:")
                nolw=input("Enter number of labours working:")
                nopd=input("Enter number of projects done:")
                profit=input("Enter profit:")
                mycursor.execute("""UPDATE customer_info SET years_worked=%s,no_of_labours_working=%s,no_of_projects_done=%s,profit=%s WHERE name_of_company=%s""",(yw,nolw,nopd,profit,noc))
                print("Record updated")
                mydb.commit()
            except Exception as e:
                print("Unable to update record")
                print(e)
        def discid():
            import mysql.connector
            from tabulate import tabulate
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="sscontractors")
                mycursor=mydb.cursor()
                mycursor.execute("select * from customer_info")
                results=mycursor.fetchall()
                print(tabulate(results,headers=["name_of_company","years_worked","no_of_labours_working","no_of_projects_done","profit"],tablefmt="fancy_grid"))
                print("Record displayed")
                mydb.commit()
            except Exception as e:
                print("Unable to display record")
                print(e)
        def sercid():
            import mysql.connector
            from tabulate import tabulate
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="sscontractors")
                mycursor=mydb.cursor()
                noc=input("Enter name of company:")
                mycursor.execute("""Select * from customer_info WHERE name_of_company=%s""",(noc,))
                results=mycursor.fetchall()
                print(tabulate(results,headers=["name_of_company","years_worked","no_of_labours_working","no_of_projects_done","profit"],tablefmt="fancy_grid"))
                print("Record displayed")
                mydb.commit()
            except Exception as e:
                print("Unable to search record")
                print(e)
        def delcid():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="sscontractors")
                mycursor=mydb.cursor()
                noc=input("Enter name of company:")
                mycursor.execute("""DELETE FROM company_info WHERE name_of_company=%s""",(noc,))
                print("Record deleted")
                mydb.commit()
            except Exception as e:
                print("Unable to delete record")
                print(e)
        cid()
    if choice==4:
        def mlds():
            w="d"
            while w=="d":
                print("1.add male labour details")
                print("2.update male labour details")
                print("3.display male labour details")
                print("4.search male labour details")
                print("5.delete male labour details")
                print("6.Exit")
                print("\n")
                e=int(input("Enter your choice"))
                print("\n")
                if e==1:
                    addmlds()
                elif e==2:
                    upmlds()
                elif e==3:
                    dismlds()
                elif e==4:
                    sermlds()
                elif e==5:
                    delmlds()
                else:
                    print("Returning to main menu...")
                    break
        def addmlds():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="sscontractors")
                mycursor=mydb.cursor()
                name=input("Enter name:")
                age=input("Enter age:")
                weight=input("Enter weight:")
                acn=input("Enter adhaar card no:")
                bad=input("Enter account no:")
                mycursor.execute("""INSERT INTO male_labour(name,age,weight,adhaar_card_no,bank_account_details)VALUES(%s,%s,%s,%s,%s)""",(name,age,weight,acn,bad))
                print("Record inserted")
                mydb.commit()
            except Exception as e:
                print("Unable to insert record")
                print(e)
        def upmlds():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="sscontractors")
                mycursor=mydb.cursor()
                name=input("Enter name:")
                age=input("Enter age:")
                weight=input("Enter weight:")
                acn=input("Enter adhaar card no:")
                bad=input("Enter account no:")
                mycursor.execute("""UPDATE male_labour SET age=%s,weight=%s,adhaar_card_no=%s,bank_account_details=%s WHERE name=%s""",(age,weight,acn,bad,name))
                print("Record updated")
                mydb.commit()
            except Exception as e:
                print("Unable to update record")
                print(e)
        def dismlds():
            import mysql.connector
            from tabulate import tabulate
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="sscontractors")
                mycursor=mydb.cursor()
                mycursor.execute("select * from male_labour")
                results=mycursor.fetchall()
                print(tabulate(results,headers=["name","age","weight","adhaar_card_no","bank_account_details"],tablefmt="fancy_grid"))
                print("Record displayed")
                mydb.commit()
            except Exception as e:
                print("Unable to display record")
                print(e)
        def sermlds():
            import mysql.connector
            from tabulate import tabulate
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="sscontractors")
                mycursor=mydb.curosr()
                name=input("Enter name:")
                mycursor.execute("""Select * from male_labour WHERE name=%s""",(name,))
                results=mycursor.fetchall()
                print(tabulate(results,headers=["name","age","weight","adhaar_card_no","bank_account_details"],tablefmt="fancy_grid"))
                print("Record displayed")
                mydb.commit()
            except Exception as e:
                print("Unable to search record")
                print(e)
        def delmlds():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="sscontractors")
                mycursor=mydb.cursor()
                name=input("Enter name:")
                mycursor.execute("""DELETE FROM male_labour WHERE name=%s""",(name,))
                print("Record deleted")
                mydb.commit()
            except Exception as e:
                print("Unable to delete record")
                print(e)
        mlds()
    if choice==5:
        def fld():
            s="e"
            while s=="e":
                print("1.add female labour details")
                print("2.update female labour details")
                print("3.display female details")
                print("4.search female details")
                print("5.delete female details")
                print("6.Exit")
                print("\n")
                f=int(input("Enter your choice:"))
                print("\n")
                if f==1:
                    addfld()
                elif f==2:
                    upfld()
                elif f==3:
                    disfld()
                elif f==4:
                    serfld()
                elif f==5:
                    delfld()
                else:
                    print("Returning to main menu...")
                    break
        def addfld():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="sscontractors")
                mycursor=mydb.cursor()
                name=input("Enter name:")
                age=input("Enter age:")
                weight=input("Enter weight:")
                acn=input("Enter adhaar card number:")
                bad=input("Enter account number:")
                mycursor.execute("""INSERT INTO female_labour(name,age,weight,adhaar_card_no,bank_account_details)VALUES(%s,%s,%s,%s,%s)""",(name,age,weight,acn,bad))
                print("Record inserted")
                mydb.commit()
            except Exception as e:
                print("Unable to insert record")
                print(e)
        def upfld():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="sscontractors")
                mycursor=mydb.cursor()
                name=input("Enter name:")
                age=input("Enter age:")
                weight=input("Enter weight:")
                acn=input("Enter adhaar card number:")
                bad=input("Enter account number:")
                mycursor.execute("""UPDATE female_labour SET age=%s,weight=%s,adhaar_card_no=%s,bank_account_details=%s WHERE name=%s""",(age,weight,acn,bad,name))
                print("Record updated")
                mydb.commit()
            except Exception as e:
                print("Unable to update record")
                print(e)
        def disfld():
            import mysql.connector
            from tabulate import tabulate
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="sscontractors")
                mycursor=mydb.cursor()
                mycursor.execute("select * from female_labour")
                results=mycursor.fetchall()
                print(tabulate(results,headers=["name","age","weight","adhaar_card_no","bank_account_details"],tablefmt="fancy_grid"))   
                print("Record displayed")
                mydb.commit()
            except Exception as e:
                print("Unable to display record")
                print(e)  
        def serfld():
            import mysql.connector
            from tabulate import tabulate
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="sscontractors")
                mycursor=mydb.cursor()
                name=input("Enter name:")
                mycursor.execute("""Search * from female_labour WHERE name=%s""",(name,))
                results=mycursor.fetchall()
                print(tabulate(results,headers=["name","age","weight","adhaar_card_no","bank_account_details"],tablefmt="fancy_grid"))
                print("Record displayed")
                mydb.commit()
            except Exception as e:
                print("Unable to search record")
                print(e)
        def delfld():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="sscontraactors")
                mycursor=mydb.cursor()
                name=input("Enter name:")
                mycursor.exeute("""DELETE FROM female_labour WHERE name=%s""",(name,))
                print("Record deleted")
                mydb.commit()
            except Exception as e:
                print("Unable to delete record")
                print(e)
        fld()
    if choice==6:
        exit() 

    else:
        print("choice dosnt exist")     

    
        









        



        

