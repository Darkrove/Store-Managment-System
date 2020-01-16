import sys
import random
from datetime import date
from datetime import datetime
import time
from getpass import getpass

def_all_products = [
    [1, 'Sugar Bag', 20, 200], 
    [2, 'Premium Almonds', 100, 300], 
    [3, 'Desi Ghee', 200, 475], 
    [4, 'Olive Oil', 100, 200], 
    [5, 'Basmati Rice', 200, 475],
    [6, 'Mixed Fruit Jam', 100, 200],
    [7, 'Nescafe Coffee', 50, 400]
]
rem=[]
all_products=[
    [1, 'Sugar Bag', '5 kg', 20, 224], 
    [2, 'Premium Almonds', '250 g', 100, 345], 
    [3, 'Desi Ghee', '1 l', 200, 532], 
    [4, 'Olive Oil', '500 ml', 100, 229], 
    [5, 'Basmati Rice', '5 kg', 200, 599],
    [6, 'Mixed Fruit Jam', '1.04 kg', 100, 250],
    [7, 'Nescafe Coffee', '200 g', 50, 474]
    ]
idp=7
all_employee={
    1: {
        'first': 'Ajit',
        'last': 'Salaria', 
        'age': '20', 
        'salary': '15000',
        'contact': '8433624344',
        'sal_stat': 'Paid'
        },
    2: {
        'first': 'Carpe',
        'last': 'King', 
        'age': '35', 
        'salary': '17000',
        'contact': '9930965816',
        'sal_stat': 'Paid'
        }
    }
ide=2
prod_list=['sugar bag','premium almonds','desi ghee','olive oil','basmati rice','mixed fruit jam','nescafe coffee']
customer_list=[]
basket=[]
def cls():
    print("\n" * 50)
def logo():
    cls()
    print("""\t╔═══════════════════════════════════════════════════════════════════════════════════════╗
\t║  ███   ███   ████ █████  ████     █   █ █████ █   █ █████     █   █  ███  ████  █████ ║
\t║ █   █ █   █ █       █   █         ██ ██   █   ██  █   █       ██ ██ █   █ █   █   █   ║
\t║ █   █ █████  ███    █    ███      █ █ █   █   █ █ █   █       █ █ █ █████ ████    █   ║
\t║ █   █ █   █     █   █       █     █   █   █   █  ██   █       █   █ █   █ █ █     █   ║
\t║  ███  █   █ ████  █████ ████      █   █ █████ █   █ █████     █   █ █   █ █  █    █   ║
\t╚═══════════════════════════════════════════════════════════════════════════════════════╝\n\n""")

def banner():
    logo()
    print("\t╔═══════════════════════════════════╗")
    print("\t║\t1.Stock Details             ║")
    print("\t║\t2.Employee Details          ║")
    print("\t║\t3.Financial Details         ║")
    print("\t║\t4.Sales Details             ║")
    print("\t║\t5.Reminder                  ║")
    print("\t║\t6.Cashier Interface         ║")
    print("\t║\t7.Exit                      ║")
    print("\t╚═══════════════════════════════════╝")

def stockdetails():
    logo()
    print("\t╔═══════════════════════════════════╗")
    print("\t║\tSTOCK DETAILS               ║")
    print("\t╠═══════════════════════════════════╣")
    print("\t║\t1.Add Item                  ║")
    print("\t║\t2.Remove Item               ║")
    print("\t║\t3.Show All Products         ║")
    print("\t║\t4.Return to main menu       ║")
    print("\t╚═══════════════════════════════════╝")

def salesdetails():
    logo()
    print("\t╔═══════════════════════════════════╗")
    print("\t║\tSALES DETAILS               ║")
    print("\t╠═══════════════════════════════════╣")
    print("\t║\t1.Product sales             ║")
    print("\t║\t2.Customer details          ║")
    print("\t║\t3.Return to main menu       ║")
    print("\t╚═══════════════════════════════════╝")
    
def employeedetails():
    logo()
    print("\t╔═══════════════════════════════════╗")
    print("\t║\tEMPLOYEE DETAILS            ║")
    print("\t╠═══════════════════════════════════╣")
    print("\t║\t1.Add Employee              ║")
    print("\t║\t2.Remove Employee           ║")
    print("\t║\t3.Show All Employee         ║")
    print("\t║\t4.Return to main menu       ║")
    print("\t╚═══════════════════════════════════╝")
    
def add_item():
    global idp
    username = input("\n\t\tEnter Admin UserID: ")
    password = getpass("\t\tEnter Password: ")
    if username == "Admin" and password == "Password":
        logo()
        print("\t\tAdding New Product")
        name=input("\n\t\tEnter Name Of Product: ").strip().capitalize()
        while(True):      
            pri=input("\t\tEnter Price: ")
            if(pri.isdigit()):
                break
            else:
                print("\t\tInvalid input")
                continue
        while(True):      
            quan=input("\t\tEnter Quantity: ")
            quan=quan.strip()
            ltc1=quan[len(quan)-1]
            ltc2=quan[len(quan)-2]+quan[len(quan)-1]
            if( ltc2=="ml" or ltc2=="kg"):
                qval=quan[slice(0,quan.index(ltc2))].strip()
                if(qval.isdigit()):
                    break
                elif(int(float(qval))!=float(qval)):
                    break
                else:
                    print("\t\tInvalid input")
                    continue
            elif(ltc1=="g" or ltc1=="l"):
                qval=quan[slice(0,quan.index(ltc1))].strip()
                if(qval.isdigit()):
                    break
                elif(int(float(qval))!=float(qval)):
                    break
                else:
                    print("\t\tInvalid input")
                    continue
            else:
                print("\t\tInvalid input")
                continue
        while(True):      
            ava=input("\t\tAvailable Stock: ")
            if(ava.isdigit()):
                break
            else:
                print("\t\tInvalid input")
                continue
        
        all_products.append([idp+1,name, quan, int(ava), int(pri)])
        def_all_products.append([idp+1,name, quan,int(ava),int(pri)])
        idp+=1
        prod_list.append(name.lower())
        print("\t\tItem Added Successfully.")
    else:
        print("\t\tIncorrect username and password")
    w8=input("\n\t\tpress ENTER to continue.")

def remove_item():
    username = input("\n\t\tEnter Admin UserID: ")
    password = getpass("\t\tEnter Password: ")
    if username == "Admin" and password == "Password":
        item_list()
        while(True):
            idofpro =input("\n\t\tEnter Product ID you wish to get removed(enter \'0\' to exit this menu): ")
            if(idofpro.isdigit()):
                k=0
                if(int(idofpro)==0):
                    break
                for i in range(0,len(all_products)):
                    if(int(idofpro)!=all_products[i][0]):
                        k+=1    
                if(k==len(all_products)):
                    print("\t\tID unavailable")
                    continue
                else:
                    for i in range(0,len(all_products)):
                        if(int(idofpro)==all_products[i][0]):
                            all_products.pop(i)
                            def_all_products.pop(i)
                            prod_list.pop(i)
                            break
                    print("\t\tItem removed Successfully.")
                    break
            else:
                print("\t\tInvalid input")
                continue
    else:
        print("\t\tIncorrect username and password")
    w8=input("\n\t\tpress ENTER to continue.") 

def item_list():
    logo()
    print("\t╔═══════════════╦════════════════════LIST OF ITEMS══════╦═══════════════╦═══════════════╗")
    print("\t║\t ID\t║ NAME\t\t\t║ PRICE\t\t║ QUANTITY\t║ IN STOCK\t║")
    print("\t╠═══════════════╬═══════════════════════╬═══════════════╬═══════════════╬═══════════════╣")
    for product_dict in all_products:
            print("\t║\t",product_dict[0],"\t║", product_dict[1]," " * (15-len(product_dict[1])),"\t║",product_dict[4],"\t\t║", product_dict[2]," " * (8-len(product_dict[2])),"\t║", product_dict[3],"\t\t║")
    print("\t╚═══════════════╩═══════════════════════╩═══════════════╩═══════════════╩═══════════════╝")
def stock():
    while True:
        stockdetails()
        option1=0
        while(True):      
            opt = input("\n\t\tSelect Option: ")
            if(opt.isdigit()):
                if(int(opt)!=1 and int(opt)!=2 and int(opt)!=3 and int(opt)!=4):
                    print("\t\tOption unavailable")
                    continue
                else:
                    option1=int(opt)
                    break
            else:
                print("\t\tInvalid input")
                continue
        if option1 == 1:
            add_item()
        elif option1 == 2:
            remove_item()
        elif option1 == 3:
            item_list()
            w8=input("\n\t\tpress ENTER to continue.")
        elif option1 == 4:
            break
        
def add_employee():
    global ide
    username = input("\n\t\tEnter Admin UserID: ")
    password = getpass("\t\tEnter Password: ")
    if username == "Admin" and password == "Password":
        logo()
        print("\t\tAdding New Employee")
        while(True):      
            first=input("\n\t\tEnter First Name Of Employee: ").capitalize()
            if(first.isalpha()):
                break
            else:
                print("\t\tInvalid input")
                continue
        while(True):      
            last=input("\t\tEnter Last Name Of Employee: ").capitalize()
            if(last.isalpha()):
                break
            else:
                print("\t\tInvalid input")
                continue
        while(True):      
            age=input("\t\tAge: ")
            if(age.isdigit()):
                if(int(age)<18 or int(age)>70):
                    print("\t\tAge requirements of 18-70 are not met.");
                    continue
                else:
                    break
            else:
                print("\t\tInvalid input")
                continue
        while(True):      
            sal=input("\t\tSalary: ")
            if(sal.isdigit()):
                break
            else:
                print("\t\tInvalid input")
                continue
        while(True):      
            con=input("\t\tContact: ")
            if(con.isdigit() and len(con)==10):
                break
            else:
                print("\t\tInvalid input")
                continue
        all_employee[ide+1] = {'first': first, 'last': last, 'age': age, 'salary': sal, 'contact': con,'sal_stat': 'Pending'}
        ide+=1
        print("\t\tEmployee Data Added Successfully")
        w8=input("\n\t\tpress ENTER to continue.")
    else:
        print("\t\tIncorrect username and password") 

def remove_employee():
    username = input("\n\t\tEnter Admin UserID: ")
    password = getpass("\t\tEnter Password: ")
    if username == "Admin" and password == "Password":
        emp_list()
        while(True):
            idofemp = input("\n\t\tEnter Employee ID you wish to get removed(enter \'0\' to exit this menu): ")
            if(idofemp.isdigit()):
                if(int(idofemp)==0):
                    break
                if(int(idofemp) not in all_employee.keys()):   
                    print("\t\tID unavailable")
                    continue
                else:
                    del all_employee[int(idofemp)]
                    print("\t\tEmployee Data removed Successfully")
                    break
            else:
                print("\t\tInvalid input")
                continue
    else:
        print("\t\tIncorrect username and password")
        
    w8=input("\n\t\tpress ENTER to continue.")

def emp_list():
    logo()
    print("\t╔═══════════════LIST OF EMPLOYEE═══════════════╗")
    for id, emp_dict in all_employee.items():
        print("\t║                                              ║")                                         
        print("\t║\tID: ", id,"                                ║")
        print("\t║\tFULL NANE: ", emp_dict['first']+' '+emp_dict['last']," " *(24-len(emp_dict['first']+emp_dict['last'])),"║")
        print("\t║\tAGE: ",emp_dict['age'],"                              ║")
        print("\t║\tSALARY: ",emp_dict['salary']," " *(28-len(emp_dict['salary'])),"║")
        print("\t║\tCONTACT NUMBER: ",emp_dict['contact']+"            ║")
    print("\t╚══════════════════════════════════════════════╝")
        
def employee():
    option2=0
    while(True):
        employeedetails()
        while True:
            opt = input("\n\t\tSelect Option: ")
            if(opt.isdigit()):
                if(int(opt)!=1 and int(opt)!=2 and int(opt)!=3 and int(opt)!=4):
                    print("\t\tOption unavailable")
                    continue
                else:
                    option2=int(opt)
                    break
            else:
                print("\t\tInvalid input")
                continue
        if option2 == 1:
            add_employee()     
        elif option2 == 2:
            remove_employee()
        elif option2 == 3:
            emp_list()
            w8=input("\n\t\tpress ENTER to continue.")
        elif option2 == 4:
            break   
#finance module

def finance_menu():
    while(True):
        opt=""
        cho=""
        logo()
        print("\t╔═══════════════════════════════════╗")
        print("\t║\tFINANCIAL DETAILS           ║")
        print("\t╠═══════════════════════════════════╣")
        print("\t║\t1. Profit and loss report   ║")
        print("\t║\t2. Employee Salary Status   ║")
        print("\t║\t3. Return to main menu      ║")
        print("\t╚═══════════════════════════════════╝")
        while(True):      
            opt=input("\n\t\tEnter option: ")
            if(opt.isdigit()):
                if(int(opt)!=1 and int(opt)!=2 and int(opt)!=3):
                    print("\t\tOption unavailable")
                    continue
                else:
                    break
            else:
                print("\t\tInvalid input")
                continue

        if(opt=="1"):
            PnL_report()
        elif(opt=="2"):
            EmpSalStat()
        elif(opt=="3"):
            break
            
        logo()
        while(True):
            cho=input("\t\tDo you wish to check Financial details again?(Y/N):")
            if(cho.isalpha()):
                if(cho!="Y" and cho!="N" and cho!="y" and cho!="n"):
                    print("\t\tOption unavailable")
                    continue
                else:
                    break
            else:
                print("\t\tInvalid input")
                continue
        if(cho=="N" or cho =="n"):
            break

def PnL_report():
    fl=0
    logo()
    print("\t╔═════════════════════════════════════════════════════════════════════════════════╗")
    print("\t║\t\t\t\tProfit and loss report\t\t\t\t  ║")
    
    for i in range(0,len(all_products)):
        if(def_all_products[i][2]!=all_products[i][3]):
            fl=1
            print("\t╠═══════════════════════╦════════════════════╦══════════════════╦═════════════════╣")
            print("\t║\tProduct_ID\t║ Product name       ║ Quantity sold\t║ Total amount    ║")
            print("\t╠═══════════════════════╬════════════════════╬══════════════════╬═════════════════╣")
            break
    
    rev=0
    cogd=0
    inval=0
    oe=1500
    inct=0
    for i in range(0,len(all_products)):
        inval=inval+def_all_products[i][2]*def_all_products[i][3]
        if all_products[i][3] != def_all_products[i][2]:
            n=def_all_products[i][2]-all_products[i][3]
            print("\t║\t",all_products[i][0],"\t\t║",all_products[i][1]," "*(17-len(all_products[i][1])),"║",n,"\t\t║",n*all_products[i][4]," "*(14-len(str(n*all_products[i][4]))),"║")
            rev=rev+n*all_products[i][4]
            cogd=cogd+n*def_all_products[i][3]
    if(fl==1):
        print("\t╚═══════════════════════╩════════════════════╩══════════════════╩═════════════════╝")
    else:
        print("\t╚═════════════════════════════════════════════════════════════════════════════════╝")
    gp=rev-cogd
    oi=gp-oe
    print("\n\t\tRevenue                  = ₹",rev)
    print("\n\t\tCost of Goods sold       = ₹",cogd)
    print("\n\t\tGross profit             = ₹",gp)
    if(cogd!=0 and inval!=0):
        print("\n\t\tGross profit %           =  ",float((int(gp*10000/cogd))/100.0))
        print("\n\t\tTotal profit %           =  ",float((int(gp*10000/inval))/100.0))
    print("\n\t\tOperating income         = ₹",oi)
    
    day = date.today()
    today = day.strftime("%m")
    if(today=="03"):
        print("\n\t\tIncome before Income tax = ₹",oi)
        if(oi<250000):
            inct=0
        elif(oi<500000):
            inct=0.05*oi
        elif(oi<1000000):
            inct=12500+0.2*(oi-500000)
        ni=oi-inct
        print("\n\t\tIncome Taxes             = ₹",float((int(inct*100))/100.0))
        print("\n\t\tNet Income               = ₹",float((int(ni*100))/100.0))
    w8=input("\n\t\tpress ENTER to continue.")

def EmpSalStat():
    logo()
    f=False
    print("\t╔═══════════════LIST OF EMPLOYEE═══════════════╗")
    for id, emp_dict in all_employee.items():
        print("\t║                                              ║")                                         
        print("\t║\tID: ", id,"                                ║")
        print("\t║\tFULL NANE: ", emp_dict['first']+' '+emp_dict['last']," " *(24-len(emp_dict['first']+emp_dict['last'])),"║")
        print("\t║\tSALARY STATUS: ",emp_dict['sal_stat']," " *(21-len(emp_dict['sal_stat'])),"║")
    print("\t╚══════════════════════════════════════════════╝")
    while(True):
        cho=input("\n\n\t\tDo you wish to update it?(Y/N):")
        if(cho.isalpha()):
             if(cho!="Y" and cho!="N" and cho!="y" and cho!="n"):
                print("\t\tOption unavailable")
                continue
             else:
                 break
        else:
            print("\t\tInvalid input")
            continue
    print("\n")
    if(cho=='y' or cho=='Y'):
        for id, emp_dict in all_employee.items():
            print("\t\tID: ", id)
            print("\t\tFULL NANE: ", emp_dict['first']+' '+emp_dict['last'])
            print("\t\tSALARY STATUS: ",emp_dict['sal_stat'])
            while(True):
                ss=input("\n\t\tSalary Status (Paid/Pending):")
                if(ss.isalpha()):
                    if(ss.casefold()!="paid" and ss.casefold()!="pending"):
                        print("Option unavailable")
                        continue
                    else:
                        break
                else:
                    print("Invalid input")
                    continue
            emp_dict['sal_stat']=ss.capitalize()
    if('Employee salary(s) pending' in rem):
        f=True
    for id,emp_dict in all_employee.items():
        if(emp_dict['sal_stat']=="Pending" and f==False):
            rem.append("Employee salary(s) pending")
            break
    w8=input("\n\t\tpress ENTER to continue.")
    
def EmpSalRef():
    day = date.today()
    today = day.strftime("%d")
    if(today=="01"):
        for i in range(0,len(emp_dets)):
            emp_dets[i][2]="Pending"

#Reminder module
def Reminder():
    logo()
    f=False
    rem.clear() 
    lstk="Stock running low for:"
    if('Employee salary(s) pending' in rem):
        f=True
    for id,emp_dict in all_employee.items():
        if(emp_dict['sal_stat']=="Pending" and f==False):
            rem.append("Employee salary(s) pending")
            break 
    day = date.today()
    today = day.strftime("%m")
    f=False
    if(today=="03"):
        for i in range(0,len(rem)):
            if(rem[i]=="Income Tax Payment Month"):
                f=True
                break;
        if(f==False):
            rem.append("Income Tax Payment Month")
    for i in range(0,len(all_products)):
        if(all_products[i][3]<16):
            lstk=lstk+", "+all_products[i][1];
    if(len(lstk)>22):
        rem.append(lstk)
    if(len(rem)==0):
        print("\n\t\tNo reminders!")
    else:
        print("\n\t\tHere are your reminder(s):")
        for i in range(0,len(rem)):
            print("\t\t",i+1,".",rem[i])
    w8=input("\n\t\tpress ENTER to continue.")
    
def generate_bill(name,AMOUNT,contact_c):
    print("═══════════════════════════════════════════════════════════════════════════════════════")
    str3="OASIS MINI MART"
    str4="samaralishaikh212@gmail.com"
    print(str3.center(84))
    print(str4.center(80))
    print("═══════════════════════════════════════════════════════════════════════════════════════")
    print("Bill:{} \tDate:{}".format(int(random.random()*100000), str(datetime.now())))
    print("Customer Name: ",name)
    print("Contact Number: ",contact_c)
    print("Item List: \n")
    for i in range(0,len(basket)):
        print("Item: ", basket[i][0],"\tQty:", basket[i][1],"\tPrice: ", basket[i][2])
    print("═══════════════════════════════════════════════════════════════════════════════════════")
    print("Total: \t\t\t\t\t₹",AMOUNT)
    print("═══════════════════════════════════════════════════════════════════════════════════════")
    
    
def cashier():
    global basket
    basket=[]
    item_list()
    while True:
        fl=0
        user_answr = input("\n\tEnter Product ID (Type 'quit' to end): ").lower().strip()
        while user_answr != "quit":
            if(user_answr.isdigit()):
                user_answer=int(user_answr)
                k=0
                for i in range(0,len(all_products)):
                    if(int(user_answer)!=all_products[i][0]):
                        k+=1    
                if(k==len(all_products)):
                    print("\t\tID unavailable")
                    fl=1
                    break
                else:
                    while True:
                        user_qt = input("\tEnter Product quantiy : ")
                        if(user_qt.isdigit()):
                            user_qty=int(user_qt)
                            break
                        else:
                            print("\tInvalid input\n")
                    g=""
                    for i in range(0,len(all_products)):
                        if(all_products[i][0]==user_answer):
                            g=all_products[i][1].lower()
                    if(all_products[prod_list.index(g)][3]<user_qty):
                        user_answr=input("\tInsufficient quantity\n\n\tEnter Product ID (Type 'quit' to end): ").lower().strip()
                        continue
                    else:
                        
                        all_products[prod_list.index(g)][3]-=user_qty
                        t=0
                        for item in basket:
                            if(item[0]==user_answer):
                                item[1]+=user_qty
                                t=1
                                break
                        if(t==0):    
                            basket.append([g,user_qty])
                    user_answr=input("\n\tEnter Product ID (Type 'quit' to end) : ").lower().strip()
            else:
                user_answr=input("\t\tInvalid input\n\n\tEnter Product ID (Type 'quit' to end) : ")
        if(fl==1):
            continue
        print("\n\t═════════════════════════════════════════════════════════════════════════════════════════")
        print("\t  Cart: ",("Empty" if len(basket)==0 else basket))
        print("\t═════════════════════════════════════════════════════════════════════════════════════════")
        while True:
            answer = input("\tAny more products? (Type yes/no): ").strip().lower()
            if(answer!="no" and answer!="yes"):
                print("\tInvalid option")
            else:
                break
        if answer=="no":
            break
        
def customer():
    while True:
        address=[]
        total=[]
        logo()
        name = input("\tEnter Customer's name (Enter 'Q' to exit menu): ").capitalize().strip()
        if(name=="Q"):
            return
        while True:
                    contact_c = input("\tEnter Customer's contact number: ")
                    if(contact_c.isdigit()):
                        contact_c=int(contact_c)
                        if(len(str(abs(contact_c)))!=10):
                            print("\tInvalid number")
                        else:
                            break
                    else:
                        print("\tInvalid Number")
        cashier()
        if(len(basket)>0):
            for i in range(0,len(basket)):
                for j in range(len(all_products)):
                    if(basket[i][0].casefold()==all_products[j][1].casefold()):
                        total.append(all_products[j][4]*basket[i][1])
                        basket[i].append(all_products[j][4])
                
            amount_to_pay = sum(total)
            while True:
                place=input("\n\tHome delievery? (Type 'yes/no'): ").strip().lower()
                if(place!="no" and place!="yes"):
                    print("\tInvalid option")
                else:
                    break    
            if place == "yes":
                print("\tEnter customer's address")
                address.append(input("\tFlat/House No.: "))
                address.append(input("\tBuilding : "))
                address.append(input("\tSociety : "))
                address.append(input("\tArea : "))
                print("\n\tHome delivery charges = Rs.50")
                AMOUNT = amount_to_pay + 50
            else:
                address.append("")
                AMOUNT = amount_to_pay
              
            print("\n\t══════════════════════════════════════")
            print("\t  Total amount : Rs.",AMOUNT)
            print("\t══════════════════════════════════════")
            while True:
                way=input("\n\tPayment Method (card or cash): ").strip().lower()
                if(way!="card" and way!="cash"):
                    print("\tInvalid option")
                else:
                    break
            if way=="card":
                print("\n\tSwipe customer's card")
            print("\n\n")
            generate_bill(name,AMOUNT,contact_c)
            customer_list.append([name,basket,AMOUNT,address,way,contact_c])
            address=[]
            total=[]
        w8=input("\n\t\tpress ENTER to continue.")
        time.sleep(1)        
        
#sales module
def sales():
    while True:
        salesdetails()
        option1=0
        while(True):      
            opt = input("\n\t\tSelect Option: ")
            if(opt.isdigit()):
                if(int(opt)!=1 and int(opt)!=2 and int(opt)!=3):
                    print("\t\tOption unavailable")
                    continue
                else:
                    option1=int(opt)
                    break
            else:
                print("\t\tInvalid input")
                continue
        if option1 == 1:
            prod_sales()
        elif option1 == 2:
            customer_dtls()
        elif option1 == 3:
            break

def prod_sales():
    logo()
    fl=0
    print("\t╔═════════════════════════════════════════════════════════════════════════════════╗")
    print("\t║\t\t\t\t    Product sales     \t\t\t\t  ║")
    for i in range(0,len(all_products)):
        if(def_all_products[i][2]!=all_products[i][3]):
            fl=1
            print("\t╠═══════════════════════╦════════════════════╦══════════════════╦═════════════════╣")
            print("\t║\tProduct_ID\t║ Product name       ║ Quantity sold\t║ Total amount    ║")
            print("\t╠═══════════════════════╬════════════════════╬══════════════════╬═════════════════╣")
            break
   
    rev=0
    inval=0
    prod_uns=[]
    prod_sol=[]
    fmax=[]
    pmax=[]
    for i in range(0,len(all_products)):
        inval=inval+def_all_products[i][2]*def_all_products[i][3]
        if all_products[i][3] != def_all_products[i][2]:
            n=def_all_products[i][2]-all_products[i][3]
            print("\t║\t",all_products[i][0],"\t\t║",all_products[i][1]," "*(17-len(all_products[i][1])),"║",n,"\t\t║",n*all_products[i][4]," "*(14-len(str(n*all_products[i][4]))),"║")
            rev=rev+n*all_products[i][4]
        else:
            prod_uns.append(all_products[i][1])
    if(fl==1):
        print("\t╚═══════════════════════╩════════════════════╩══════════════════╩═════════════════╝")
    else:
        print("\t╚═════════════════════════════════════════════════════════════════════════════════╝")
    print("\n\t\tTotal value of products sold = ₹",rev)
    for i in range(0,len(customer_list)):
        for j in range(0,len(customer_list[i][1])):
            prod_sol.append(customer_list[i][1][j][0])
    for i in prod_sol:
        fmax.append(prod_sol.count(i))
    for i in range(0,len(fmax)):
        if(fmax[i]==max(fmax)):
            if(prod_sol[i] not in pmax):
                pmax.append(prod_sol[i])
    print("\n\t\tMost famous product(s)       = ",pmax if len(pmax)>0 else "None")
    print("\n\t\tUnsold Products :");
    for i in prod_uns:
        print("\t\t",i)
    w8=input("\n\t\tpress ENTER to continue.")

def customer_dtls():
    logo()
    print("\t╔═════════════════════════════════════════════════════════════════════════════════╗")
    print("\t║\t\t\t\tCustomer Details      \t\t\t\t  ║")
    print("\t╚═════════════════════════════════════════════════════════════════════════════════╝")
    if(len(customer_list)>0):
        k=1
        for i in customer_list:
            print("\n\t\t",k,".")
            print("\t\tName :",i[0])
            print("\t\tProducts purchasesd [Product name, Quantity, Product value]:")
            for j in i[1]:
                print("\t\t",j)
            print("\t\tAmount purchased : Rs.",i[2])
            print("\t\tAddress :","Unavailable" if len(i[3])==1 else i[3])
            print("\t\tContact number: ",i[5])
            print("\t\tMethod of payment :",i[4])
            k+=1
    else:
        print("\n\t\tNo customers")
    w8=input("\n\t\tpress ENTER to continue.")
                
EmpSalRef()            
while True:
    banner()
    while(True):
        cho = input("\n\t\tEnter choice: ")
        if(cho.isdigit()):
            if(int(cho)>7):
                print("\t\tOption unavailable")
                continue
            else:
                choice=int(cho)
                break
        else:
            print("\t\tInvalid input")
            continue
    if choice == 1:
        stock()
    elif choice == 2:
        employee()
    elif choice == 3:
        finance_menu()
    elif choice == 4:
        sales()    
    elif choice == 5:
        Reminder()
    elif choice == 6:
        customer()
    elif choice == 7:
        logo() 
        print("""
\t════════════════════════════════════════════════════════════════════════════════════════
\t\t\t\t\t───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
\t\t\t\t\t───█▒▒░░░░░░░░░▒▒█───
\t\t\t\t\t────█░░█░░░░░█░░█────
\t\t\t\t\t─▄▄──█░░░▀█▀░░░█──▄▄─
\t\t\t\t\t█░░█─▀▄░░░░░░░▄▀─█░░█)
\t\t\t\t\t****SYSTEM CLOSED****
\t════════════════════════════════════════════════════════════════════════════════════════
""")
        time.sleep(5)
        break
   
