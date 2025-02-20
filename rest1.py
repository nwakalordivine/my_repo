balance =5000
set_pin=4000

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
                Bank_names = ["1>Access Bank", "2>Guaranty Trust Bank", "3>United Bank for Africa","4>First City Monument Bank","\n\n#>Next"]
                print(Bank_names)
                bank_1=input("\n")
                if bank_1=="#":                
                    Bank_names_2=["5>Stanbic IBTC Bank","6>Fidelity Bank","7>Sterling Bank","8>Wema Bank","\n\n#>Next"]
                    print(Bank_names_2)
                    bank_2=input("\n")
                    if bank_2=="#": 
                        Bank_names_3=["9>Unity Bank","10>eystone Bank"]
                        print(Bank_names_3)
                        bank_3=input("")
                        if bank_3 != 9 and bank_3 != 10:
                          print("Invalid Entry")
                        continue
                    elif bank_2 != 5 and bank_2 != 6 and bank_2 != 7 and bank_2 != 8:
                        print("Invalid Entry")
                        continue
                elif bank_1 != 1 and bank_1 != 2 and bank_1 != 3 and bank_1 != 4:
                        print("Invalid Entry")
                        continue    
                fee=20
                total=amount+fee

                print(f"\nTransferring N{amount}.00 to {recievers_account}.\n")
                print(f"Fee: N{fee}\nTotal: N{total}.00\n")

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
        # display the options
option_2(balance, set_pin)