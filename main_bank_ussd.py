# a program to replicate Moniepoint ussd code operate
# line 189!!!
# start

# input the code
print("REGISTRATION FORM!")
balance = int(input("input your Virtual Bank Amount (VBA) Balance!: "))
while True:
    Register_number=input("Register a number to your bank\n")
    if not Register_number.isdigit():
        print("Invalid entry, Only numbers can be set as PIN!")
        continue
    elif len(Register_number)!=11:
            print("Invalid input; number input must be 11!")
            continue
    print("Pick your mobile line")
    i=1
    line=["MTN","AIRTEL","GLO","9MOBILE"]
    for li in line:
        print(f"{i}>{li}")
        i+=1
    line_input=int(input("\n"))-1
    if line_input not in [0,1,2,3,]:
        print("Invalid input!")
        continue
    while True:
        set_pin=input("kindly set your Transaction PIN (pin must contain 4 digits): ")
        if not set_pin.isdigit():
            print("Invalid entry, Only numbers can be set as PIN!")
            continue
        elif len(set_pin)!=4:
            print("Invalid pin count")
            continue
        else:
            print("To end this program after any transaction, simply input 'quit', thankyou!\n")
            print("\n\nSTART\n")
            code=input("Input code (the code for this bank is '*5573#'): ")
            print("\n")

        def option_1(balance, set_pin):
            while True:
                try:
                    amount = int(input("Enter amount.\n"))
                    while amount < 100:
                        amount = int(input("Low amount (limit: 100.00): Enter amount again.\n"))

                    recievers_account = input("Enter recipient's account number.\n")
                    if len(recievers_account) != 10:
                        print("Invalid account number. Please try again.")
                        continue  

                    print(f"\nTransferring N{amount}.00 to {recievers_account}.\n")
                    print(f"Fee: N0.00\nTotal: N{amount}.00\n")

                    pin_entry = input("Enter PIN. Press 0 to go back.\n")
                    if pin_entry == "0":
                        continue  
                    elif pin_entry == set_pin:
                        if amount > balance:
                            print("Insufficient funds!")
                            continue 
                        else:
                            balance -= amount
                            print(f"Your Transaction was Successful.\nYour updated balance is: N{balance}")
                            break  
                    else:
                        print("Incorrect PIN! Try again.")

                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            return balance  
            

        def option_2(balance, set_pin):
            while True:
                try:
                    amount = int(input("Enter amount.\n"))
                    while amount < 100:
                        amount = int(input("Low amount (limit: 100.00): Enter amount again.\n"))

                    recievers_account = input("Enter recipient's account number.\n")
                    if len(recievers_account) != 10:
                        print("Invalid account number. Please try again.")
                        continue 
                    print("\nSelect recipient's bank.\n")
                    Bank_names = ["Access Bank", "Guaranty Trust Bank", "United Bank for Africa","First City Monument Bank"]
                    i=1
                    for bank in Bank_names:
                            print(f"{i}>{bank}")
                            i+=1
                    print("\n\n#>Next")
                    bank_1=input("\n")
                    if bank_1=="#":      
                        Bank_names_2=["Stanbic IBTC Bank","Fidelity Bank","Sterling Bank","Wema Bank"]
                        i=5
                        for bank in Bank_names_2:
                            print(f"{i}>{bank}")
                            i+=1
                        print("\n\n#>Next")
                        bank_2=input("\n")
                        if bank_2=="#": 
                            Bank_names_3=["Unity Bank","eystone Bank"]
                            i=9
                            for bank__ in Bank_names_3:
                                print(f"{i}>{bank__}")
                                i+=1
                            
                            bank_3=input("\n")
                            if bank_3 not in ["9","10"]:
                                print("Invalid Entry")
                                continue
                            selected_bank=Bank_names_3[int(bank_3)-9]

                        elif bank_2 not in ["5","6","7","8"]:
                            print("Invalid Entry")
                            continue
                        else:
                            selected_bank=Bank_names_2[int(bank_2)-5]
                        
                    elif bank_1 not in ["1","2","3","4"]:
                            print("Invalid Entry")
                            continue    
                    else:
                        selected_bank=Bank_names[int(bank_1)-1]

                    fee=20
                    total=amount+fee

                    print(f"\nTransferring N{amount}.00 to {recievers_account}. ({selected_bank})\n")
                    print(f"Fee: N{fee}\nTotal: N{total}.00\n")

                    pin_entry = input("Enter PIN. Press 0 to go back.\n")
                    if pin_entry == "0":
                        continue  
                    elif pin_entry == set_pin:
                        if amount > balance:
                            print("Insufficient funds!")
                            continue 
                        else:
                            amount+=fee
                            balance -= amount
                            print(f"Your Transaction was Successful.\nYour updated balance is: N{balance}")
                            break  
                    else:
                        print("Incorrect PIN! Try again.")

                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            return balance   
        
        def option_3(balance,set_pin,Register_number,line_input):
            while True:
                try:
                    print("\nBuy airtime\n\n")
                    for_whom=["For yourself","For others"]
                    i=1
                    for person in for_whom:
                        print(f"{i}>{person}")
                        i+=1
                    opt = input("\n")
                    if opt=="1":
                        amount=int(input("\nEnter amount.\n"))
                        discount=10
                        Total=amount-discount
                        print(f"Buying N{amount}.00 {line[line_input]} airtime for {Register_number}.\n\nDiscount: N{discount}.00\nTotal: {Total}.00\n\nEnter PIN:\nPress 0 to go back.")
                        response=input("")
                        if response == "0":
                            continue

                        elif response != set_pin:
                            print("Invalid pin input")
                            continue
                        
                        if Total>balance:
                            print("Insufficient funds")
                            continue

                        balance-=Total
                        print(f"You've succefully purchased N{amount}.00 airtime,\nYour Updated balance is {balance}")
                        break
                except ValueError:
                    print("Invalid input.")
            return balance
        
       
        def option_4(balance, set_pin, Register_number, line_input):
            while True:
                # all code in this program was write by Nwakalor Ejike Divine
                try:
                    print("\nBuy data\n\n")
                    for_whom = ["For yourself", "For others"]
                    i = 1
                    for person in for_whom:
                        print(f"{i}>{person}")
                        i += 1
                    opt = input("\n")
                    
                    if opt == "1":
                        recipient_number = Register_number
                        recipient_line = line_input
                    elif opt == "2":
                        recipient_number = input("Enter recipient's phone number: ")
                        if recipient_number == Register_number:
                            print("Sorry your number can't be input here!")
                            continue

                        elif not recipient_number.isdigit() or len(recipient_number) != 11:
                            print("Invalid phone number. Must be 11 digits.")
                            continue
                        
                        print("Pick recipient's mobile line")
                        i = 1
                        line = ["MTN", "AIRTEL", "GLO", "9MOBILE"]
                        for li in line:
                            print(f"{i}>{li}")
                            i += 1
                        recipient_line = int(input("\n")) - 1
                        if recipient_line not in [0, 1, 2, 3]:
                            print("Invalid input!")
                            continue
                    else:
                        print("Invalid selection.")
                        continue
                    
                    print("Select data plan group\n\n")
                    data_bundles = ["Monthly", "Weekly", "Daily"]
                    i = 1
                    for bundle in data_bundles:
                        print(f"{i}>{bundle}")
                        i += 1
                    data_bun = input("\n")
                    
                    if data_bun not in ["1", "2", "3"]:
                        print("Invalid input!")
                        continue
                    
                    data_plans = {
                        "MTN": {"1": ["1.8GB - N1,500", "2.7GB - N2,000"], "2": ["750MB - N500", "1.5GB - N1,000"], "3": ["100MB - N100", "200MB - N200"]},
                        "AIRTEL": {"1": ["2GB - N1,500", "3GB - N2,000"], "2": ["1GB - N500", "2GB - N1,000"], "3": ["150MB - N100", "300MB - N200"]},
                        "GLO": {"1": ["2.5GB - N1,500", "4GB - N2,000"], "2": ["1.2GB - N500", "2.4GB - N1,000"], "3": ["200MB - N100", "400MB - N200"]},
                        "9MOBILE": {"1": ["2GB - N1,500", "3.5GB - N2,000"], "2": ["800MB - N500", "1.5GB - N1,000"], "3": ["120MB - N100", "250MB - N200"]}
                    }
                    
                    network = ["MTN", "AIRTEL", "GLO", "9MOBILE"][recipient_line]
                    print(f"\nSelect {network} {data_bundles[int(data_bun) - 1]} plan:\n")
                    i = 1
                    for plan in data_plans[network][data_bun]:
                        print(f"{i}>{plan}")
                        i += 1
                    plan_choice = input("\n")
                    
                    if plan_choice not in ["1", "2"]:
                        print("Invalid input!")
                        continue
                    
                    selected_plan = data_plans[network][data_bun][int(plan_choice) - 1]
                    plan_price = int(selected_plan.split(" - N")[-1].replace(",", ""))
                    
                    print(f"\nBuying {selected_plan} data plan for {recipient_number} ({network}).\n\nTotal: N{plan_price}.00\n\nEnter PIN:\nPress 0 to go back.")
                    response = input("")
                    
                    if response != set_pin:
                        print("Invalid PIN!")
                        continue
                    elif response == "0":
                        continue
                    if plan_price > balance:
                        print("Insufficient funds!")
                        continue
                    
                    balance -= plan_price
                    print(f"You have successfully purchased {selected_plan} for {recipient_number},\nYour updated balance is N{balance}.")
                    break
                
                except ValueError:
                    print("Invalid input.")
            
            return balance
        
        def option_5(balance, set_pin):
            while True:
                print("\nTo view your current bank balance, kindly input your PIN below:")
                balance_check = input("\n")
                
                if balance_check == set_pin:
                    print(f"\nYour current account balance is N{balance}.")
                    return balance 
                else:
                    print("Invalid PIN! Please try again.\n")

        def option_6(set_pin):
            while True:
                print("Change PIN,\n\nKindly input your current PIN:\n")
                pin_change=input("")
                if pin_change!=set_pin:
                    print("Invalid PIN input")
                    continue
                print("\nEnter new pin below")
                new_pin=input("")
                if not new_pin.isdigit():
                    print("Invalid entry, Only numbers can be set as PIN!")
                    continue
                elif len(new_pin)!=4:
                    print("Invalid pin count")
                    continue
                print(f"You have succefully updated your PIN to {new_pin}")
                set_pin=new_pin
                return set_pin
        import sys

        def option_7(set_pin):
            while True:
                print("\nBlock Account\n\nEnter your PIN to proceed:\n")
                pin_input = input("")
                
                if pin_input != set_pin:
                    print("Invalid PIN! Please try again.\n")
                    continue
                
                print("\nAre you sure you want to block your account?\n1> Yes\n2> No")
                confirm = input("\n")
                
                if confirm == "1":
                    print("\nYour account has been successfully blocked!\n")
                    sys.exit() 
                elif confirm == "2":
                    print("\nAccount blocking canceled.\n")
                    return "Active"
                else:
                    print("Invalid selection! Try again.\n")

        while code == "*5573#":
                print("Welcome to Moniepoint\n\n")
                options=["Send to Moniepoint", "Send to other banks", "Buy airtime", "Buy data", "Check balance", "Change pin", "Block account"]
                i=1
                for opt in options:
                    print(f"{i}>{opt}")
                    i+=1
                entry=input("\n").lower()
                if entry == "1":
                    balance=option_1(balance,set_pin)
                elif entry == "2":
                    balance=option_2(balance, set_pin)
                elif entry == "3":
                    balance=option_3(balance,set_pin,Register_number,line_input)
                elif entry == "4":
                    balance=option_4(balance, set_pin, Register_number, line_input)
                elif entry == "5":
                    balance=option_5(balance,set_pin)
                elif entry == "6":
                    set_pin=option_6(set_pin)
                elif entry == "7":
                    option_7(set_pin)
                else:
                    if entry == "quit":
                        print(f"Okay thank you for using our services\nyour current balance is {balance}")
                        break       
        else:
                print("invalid input, try again!")
