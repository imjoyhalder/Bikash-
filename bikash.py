  # Here make a Bkash System
import time 
dail = input("To open Bikash dail *247# :  ")
pin = 1234
balance = 1000
count1 = 0
count = 0
while True:
    if dail == "*247#":
        print("""
            Bkash
            1.Send Money
            2.Send Money to Non-Bkash User
            3.Mobile Recharge
            4.Payment
            5.Cash out 
            6.Pay Bill
            7.NGO Bill
            8.Download App
            9.My bkash
            10.Reset PIN
            0.Main menu

            """)
        
        choice = int(input("Send: "))
            
            #send money
        if choice == 1:
            account = str(input("Enter Receiver bKash Account Number: "))
            if len(account) == 11:
                amount = int(input("Enter Amount: "))
                if balance >= amount:
                    calcul = 0.005 * amount
                    calculate = balance - (calcul+amount)
                    if calculate>0:
                        print("Send Money")
                        print(f"TO: {account}")
                        print(f"Amount {amount} tk")
                        while True:
                            user_pin = int(input("Enter PIN for Confirm: "))
                            if pin != user_pin:
                                count += 1
                                print("Invalid PIN")
                                if count == 3:
                                    print("Your account have been block")
                                    time.sleep(86400)
                                    break
                            if pin == user_pin:
                                print(f"{amount} tk Send money Successful\n")
                                print(f"Now your main balance is {calculate:.1f} tk")
                                break
                    #else:
                        #print("Invalid PIN Please try again")
                        #break
                    else:
                        print("Insufficient Balance")
                else:
                    print("Insufficient Balance")
                    break
            else:
                print("Please Enter right number")
                break
            

            # Send money to Non bkash user
        elif choice == 2:
            account = str(input("Enter Receiver bKash Account Number: "))
            if len(account) == 11:
                amount = int(input("Enter Amount: "))
                if balance >= amount:
                    calcul = 0.005 * amount
                    calculate = balance - (calcul+amount)
                    if calculate>0:
                        print("Send Money")
                        print(f"TO: {account}")
                        print(f"Amount {amount} tk")
                        while True:
                            user_pin = int(input("Enter PIN for Confirm: "))
                            if pin != user_pin:
                                count += 1
                                print("Invalid PIN")
                                if count == 3:
                                    print("Your account have been block for 24 hour")
                                    time.sleep(86400)
                                    break
                            if pin == user_pin:
                                print(f"{amount} tk Send money Successful\n")
                                print(f"Now your main balance is {calculate} tk")
                                break
                    else:
                        print("Insufficient Balance")
                else:
                    print("Insufficient Balance")
                    break
            else:
                print("Please Enter Right Number")    

                # Mobile Recharge
        elif choice == 3:
            print("""
                1.Grammen
                2.Robi
                3.Airtle
                4.Taletok
                5.Banglalink
                    """)
            re_choice = int(input("Enter your choice: "))
            if re_choice  in (1,2,3,4,5):
                re_account = input("Enter your recharge account number: ")
                if len(re_account) == 11:
                    re_amount = int(input("Amount: "))
                    if re_amount >= 10:
                        if balance >= re_amount:
                            print(f"Recharge {re_amount} tk")
                            print(f"Number: {re_account} ")
                            cla = balance - re_amount
                            while True:
                                re_pin = int(input("Enter PIN for Confirm: "))
                                if pin != re_pin:
                                    count += 1
                                    print("Invalid PIN")
                                    if count == 3:
                                        print("Your account have been block for 24 hours")
                                        time.sleep(86400)
                                if pin == re_pin:
                                    print(f"{re_amount} tk Recharge Successful\n")
                                    print(f"Now your main balance is {cla} tk")
                                    break
                        else:
                            print("Insufficient Balance")
                            break
                    else:
                        print("You can not recharge less than 10 tk")
                        break
                else:
                    print("Please enter Right Number")
                    break
            else: 
                print("Enter Right Choice")
                break

                #Payment
        elif choice == 4:
            payment_number = ["01721030209","01308807152","01732163043","01726512383","017409955560"]
            account_n = input(str("Enter 11 digits Rechiver account number: "))
            if account_n in payment_number:
                if len(account_n) == 11:
                        amount2 = int(input("Enter Amount: "))
                        if amount2>1:
                            if balance >= amount2:
                                calcul = 0.01 * amount2
                                calculate = balance - (calcul+amount2)
                                if calculate>0:
                                    print("Payment")
                                    print(f"TO: {account_n}")
                                    print(f"Amount {amount2} tk")
                                    while True:
                                        user_pin = int(input("Enter PIN for Confirm: "))
                                        if pin != user_pin:
                                            count += 1
                                            print("Invalid PIN")
                                            if count == 3:
                                                print("Your account have been block for 24 hours")
                                                time.sleep(86400)
                                                break
                                        if pin == user_pin:
                                            print(f"{amount2} tk Payment  Successful\n")
                                            print(f"Now your main balance is {calculate} tk")
                                            break
                                else:
                                    print("Insufficient Balance")
                                    break        
                            else:
                                print("Insufficient Balance")
                                break
                        else:
                            print("You can not payment less than 1 tk")  
                            break  
                else:
                    print("Please Enter Right number")
                    break
            else:
                ("There have no Payment number which is you enter here")
                break




        elif choice == 5:
            print("""
                    1.From Agent
                    2.From ATM
                    3.Priyo Agent number
                    """)

            option = int(input("Send: "))
            if option == 2:
                amount = int(input("Amount: "))
                if amount<=25000:
                    if balance> amount :
                        if amount>=50:
                                calcul = 0.015 * amount
                                cal = balance - (calcul+amount)
                                print("Cash out form ATM")
                                print(f"Amount {amount} tk")
                                while True:
                                        user_pin = int(input("Enter PIN for Confirm: "))
                                        if pin != user_pin:
                                            count += 1
                                            print("Invalid PIN")
                                            if count == 3:
                                                print("Your account have been block for 24 hours")
                                                time.sleep(86400)
                                                break
                                        if pin == user_pin:
                                            print(f"{amount} tk Cashout Successful from ATM")
                                            print(f"Now Balance is {cal}")
                        else:
                            print("You can not cash out less than 50 tk")
                    else:
                        print("Insufficient Balance")  
                else:
                    print("In 24 hours you can not cash out more than 25000 tk")        
                                  
                

            if option == 1:
                payment_number = ["01721030209","01308807152","01732163043","01726512383","017409955560"]
                account_n = input(str("Enter 11 digits Bkash Agent number: "))
                if account_n in payment_number and len(account_n) == 11:
                    amount = int(input("Amount: "))
                    if balance >25000:
                        print("In 24 hours you can not cashout more than 25000 tk")
                        break
                    if balance>= amount :
                        if amount>=50:
                            calcul = 0.02 * amount
                            cal = balance - (calcul+amount)
                            print(f"Amount {amount} tk")
                            print(f"Bkash Agent Number: {account_n} ")
                            while True:
                                user_pin = int(input("Enter PIN for Confirm: "))
                                if pin != user_pin:
                                    count += 1
                                    print("Invalid PIN")
                                    if count == 3:
                                        print("Your account have been block for 24 hours")
                                        time.sleep(86400)
                                        break
                                if pin == user_pin:
                                    print(f"{amount} tk Cashout Successful")
                                    print(f"Now Balance is {cal} tk")
                                    break
                        else:
                            print("You can not Cash out less than 50 tk")
                            break            
                    else:                
                        print("Insufficient Balance")
                        break  
                else:
                    print("Please Enter wright number And")
                    print("There have no Agent number which you enter")
                    break
                
            
            if option == 3:
                payment_number = ["01721030209","01308807152","017409955560"]
                account_n = input(str("Enter 11 digits Priyo Agent number: "))
                if account_n in payment_number and len(account_n) == 11:
                    amount = int(input("Amount: "))
                    if balance <25000:
                        print("In 24 hours you can not cashout more than 25000 tk")
                        break
                    if balance>= amount :
                        if amount>=50:
                            calcul = 0.015 * amount
                            cal = balance - (calcul+amount)
                            print(f"Amount {amount} tk")
                            print(f"Priyo Agent Number: {account_n} ")
                            while True:
                                user_pin = int(input("Enter PIN for Confirm: "))
                                if pin != user_pin:
                                    count += 1
                                    print("Invalid PIN")
                                    if count == 3:
                                        print("Your account have been block for 24 hours")
                                        time.sleep(86400)
                                        break
                                if pin == user_pin:
                                    print(f"{amount} tk Cashout Successful")
                                    print(f"Now Balance is {cal} tk")
                                    break
                        else:
                            print("You can not Cash out less than 50 tk")
                            break            
                    else:                
                        print("Insufficient Balance")
                        break  
                else:
                    print("Please Enter right number")
                    break

                       
        elif choice == 6:
            print("""
                Pay Bill
                1.Electricity Bill
                2.Gas Bill
                3.Water Bill
                4.Inernet Bill
                5.Tv
                6.City Services
                7.Education Services
                8.Financila Services
                """)
            options = int(input("Send: "))
            pay_bill = ["01740995732","01726512383","01799353514","013628236963","01936951365",
            "01308807152","01721030209","01740995732","01740995560","01775784567","01389639450",
            "01467395385","01367975134","01765870954","01578654567","015098123","01756487965"]
            if options == 1:
                account_n = str(input("Enter Electricity Bill Payment number: "))
                if account_n in pay_bill and len(account_n) == 11:
                    amount4 = int(input("Amount: "))    
                    if balance >= amount4:
                        calcul = 0.005 * amount4
                        cal = balance - (calcul+amount4)
                        print(f"Amount {amount4} tk")
                        print(f"Electricity Bill pay Number: {account_n} ")
                        while True:
                            user_pin = int(input("Confirm PIN: "))
                            if pin != user_pin:
                                count += 1
                                print("Invalid PIN")
                                if count == 3:
                                    print("Your account have been block for 24 hours")
                                    time.sleep(86400)
                                    break
                            if pin == user_pin:
                                print(f"{amount4} tk Electricity Bill Pay Successful\n")
                                print(f"Now your account balance is {cal} tk")
                                break
                    else:
                        print("Insufficient Balance")
                        break
                else:
                    print("Please Enter Right Number\n")
                    print(f"{account_n} this number is not found in Electricity pay bill number")
                    break



            if options == 2:
                account_n = input("Enter Gas Bill Payment number: ")
                if account_n in pay_bill:
                    amount4 = int(input("Amount: "))    
                    if balance >= amount4:
                        calcul = 0.005 * amount
                        cal = balance - (calcul+amount)
                        print(f"Amount {amount} tk")
                        print(f"Priyo Agent Number: {account_n} ")
                        while True:
                            user_pin = int(input("Confirm PIN: "))
                            if pin != user_pin:
                                count += 1
                                print("Invalid PIN")
                                if count == 3:
                                    print("Your account have been block for 24 hours")
                                    time.sleep(86400)
                                    break
                            if pin == user_pin:
                                print(f"{amount4} tk Gas Bill Pay Successful")
                                print(f"Now your account balance is {cal}")
                                break
                    else:
                        print("Insufficient Balance")
                        break
                else:
                    print(f"{account_n} this number is not found in Gas pay bill number")
                    break



                
            if options == 3:
                account_n = input("Enter Water Bill Payment number: ")
                if account_n in pay_bill:
                    amount4 = int(input("Amount: "))    
                    if balance >= amount4:
                        calcul = 0.005 * amount4
                        cal = balance - (calcul+amount4)
                        print(f"Amount {amount4} tk")
                        print(f"Water Bill pay Number: {account_n} ")
                        while True:
                            user_pin = int(input("Confirm PIN: "))
                            if pin != user_pin:
                                count += 1
                                print("Invalid PIN")
                                if count == 3:
                                    print("Your account have been block for 24 hours")
                                    time.sleep(86400)
                                    break
                            if pin == user_pin:
                                print(f"{amount4} tk Water Bill Pay Successful")
                                print(f"Now your account balance is {cal}")
                                break
                    else:
                        print("Insufficient Balance")
                        break
                else:
                    print(f"{account_n} this number is not found in Water pay bill number")
                    break



            if options == 4:
                account_n = input("Enter Internet Bill Payment number: ")
                if account_n in pay_bill:
                    amount4 = int(input("Amount: "))    
                    if balance >= amount4:
                        calcul = 0.005 * amount4
                        cal = balance - (calcul+amount4)
                        print(f"Amount {amount4} tk")
                        print(f"Internet Bill pay Number: +088{account_n} ")
                        while True:
                            user_pin = int(input("Confirm PIN: "))
                            if pin != user_pin:
                                count += 1
                                print("Invalid PIN")
                                if count == 3:
                                    print("Your account have been block for 24 hours")
                                    time.sleep(86400)
                                    break
                            if pin == user_pin:
                                print(f"{amount4} tk Internet Bill Pay Successful")
                                print(f"Now your account balance is {cal}")
                                break
                    else:
                        print("Insufficient Balance")
                        break
                else:
                    print(f"{account_n} this number is not found in Internet pay bill number")
                    break



                
            if options == 5:
                account_n = input("Enter TV Bill Payment number: ")
                if account_n in pay_bill:
                    amount4 = int(input("Amount: "))    
                    if balance >= amount4:
                        calcul = 0.005 * amount4
                        cal = balance - (calcul+amount4)
                        print(f"Amount {amount4} tk")
                        print(f"Tv Bill pay Number: +88{account_n} ")
                        while True:
                                user_pin = int(input("Confirm PIN: "))
                                if pin != user_pin:
                                    count += 1
                                    print("Invalid PIN")
                                    if count == 3:
                                        print("Your account have been block for 24 hours")
                                        time.sleep(86400)
                                        break
                                if pin == user_pin:
                                    print(f"{amount4} tk TV Bill Pay Successful")
                                    print(f"Now your account balance is {cal} tk")
                                    break
                    else:
                        print("Insufficient Balance")
                        break
                else:
                    print(f"{account_n} this number is not found in TV pay bill number")
                    break



                
            if options == 7:
                print("It's temporary stop")
                break
                
            if options == 8:
                print("Please go to Bkash app for Education Services")
                break
            if options == 9:
                print("Please go to Bkash app for Financila Services")
        if choice == 7:
            print("Please go to bKash app for NGO pay")
        if choice == 8:
            print("Please Download Bkash App from Google play sotore")
        elif choice == 9:
            print("""
                bKash
                1 Check Balance
                2 Request Statement
                3 Change PIN
                4 Save priyo Number
                5 Help line
                0 Main Menu
                """)
            option = int(input("Send: "))
            if option == 3:
                 while True:
                        re_pin = int(input("Enter PIN for Confirm: "))
                        if pin != re_pin:
                            count += 1
                            print("Invalid PIN")
                            if count == 3:
                                print("Your account have been block for 24 hours")
                                time.sleep(86400)
                                break
                            if pin == re_pin:
                                new_pin = int(input("Confirm PIN: "))
                                renew_pin = int(input("Confirm Your new PIN: "))
                                if new_pin == renew_pin:
                                    print("Your PIN changed Successfuly")
                                    break
                                else:
                                    print("Does not match PIN")
                                    break
            if option == 2:
                print("Found Nothing please try other")

            if option == 1:
                while True:
                    re_pin = int(input("Confirm PIN: "))
                    if pin != re_pin:
                        count += 1
                        print("Invalid PIN")
                        if count == 3:
                            print("Your account have been block for 24 hours")
                            time.sleep(86400)
                            break
                    else:
                        print(f"Your account Balance {balance} tk")
                        break
                    
            if option == 4:
                priyo_number = str(input("Enter your Priyo number: "))
                if len(priyo_number) == 11:
                    pin1 = int(input("Confirm PIN: "))
                    if pin == pin1:
                        print("Your priyo number Save Successfuly")
                    if pin != pin1:
                        print("Invalid PIN")
                        count += 1
                        if count == 3:
                            print("You account have been Block for 24 hours")
                            time.sleep(86400)
                            break
                else:
                    print("Please Enter Right Number")
                    break

            if option == 5:
                print("Help line number - 16247")

            if option == 0:
                pass

        elif choice == 10:
            while True:
                re_pin = int(input("Enter PIN for Confirm: "))
                if pin != re_pin:
                    count += 1
                    print("Invalid PIN")
                    if count == 3:
                        print("Your account have been block for 24 hours")
                        time.sleep(86400)
                        break
                if pin == re_pin:
                    new_pin = int(input("Enter New PIN: "))
                    renew_pin = int(input("Confirm Your new PIN: "))
                    if new_pin == renew_pin:
                        print("Your PIN changed Successfuly")
                        time.sleep(100000)
                        break
                    else:
                        print("Does not match PIN")
                        break
                
        elif choice == 0:
            pass

        else:
            print("\n")
            break
    else:
        print("Invalid MMI Code or connection problem")
        break
                    
                        
    
                

                
                        


                
































