import changocoin as cc

def upload_blockchain(blockchain):
    csv = input("Please enter the name of the CSV file with the transactions: ")
    blockchain = cc.upload_blockchain(csv)
    if len(blockchain) == 0:
        print("The file name doesn't exist, please try again")
    else:
        print("The following blockchain was uploaded with their corresponding hashes per transaction (from the csv file)")
        for transaction in blockchain:
            print(transaction["Hash"])
    return blockchain

def add_transaction(blockchain):
    pass
def add_block(blockchain):
    pass
def nt_sender_recipient(blockchain):
    pass
def view_transaction(blockchain):
    pass
def validate_block(blockchain):
    pass
def find_transactions(blockchain):
    pass
def transaction_max_value(blockchain):
    pass
def account_balance(blockchain):
    pass

def menu():
    print("\nOptions")
    print("1. Upload a file wtih the transactions(copy blockchain) .csv")
    print("2. Add a new transaction")
    print("3. Add a new block")
    print("4. See the number of transactions with a specific sender or recipient account")
    print("5. View transaction information")
    print("6. Validate block")
    print("7. Find transactions with a specific sender or recipient account")
    print("8. See the  transaction with the maximum value")
    print("9. Calculate account balance")
    print("10. Exit")

def main():
    execute = True
    blockchain = []
    while execute:
        menu()
        option = int(input("Please select an option: "))
        if option == 1:
            blockchain = upload_blockchain(blockchain)
        elif option == 2:
            add_transaction(blockchain)
        elif option == 3:
            add_block(blockchain)
        elif option == 4:
            nt_sender_recipient(blockchain)
        elif option == 5:
            view_transaction(blockchain)
        elif option == 6:
            validate_block(blockchain)
        elif option == 7:
            find_transactions(blockchain)
        elif option == 8:
            transaction_max_value(blockchain)
        elif option == 9:
            account_balance(blockchain)
        elif option == 10:
            execute = False
        else:
            print("Pls select a correct option")

if __name__=="__main__":
    main()