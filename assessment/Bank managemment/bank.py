import pymysql

# ------------------ Create Database ------------------
def create_database():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password=""
    )
    cur = conn.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS bank_db")
    conn.commit()
    conn.close()

# ------------------ DB Connection ------------------
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="bank_db",
        cursorclass=pymysql.cursors.DictCursor
    )

# ------------------ Base Class ------------------
class Person:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

# ------------------ Customer Class ------------------
class Customer(Person):
    def __init__(self, name, email, password, account_no, balance):
        super().__init__(name, email, password)
        self.account_no = account_no
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            return False
        self.__balance -= amount
        return True

# ------------------ Setup DB Tables ------------------
def create_tables():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100) UNIQUE,
            password VARCHAR(100),
            account_no INT UNIQUE,
            balance FLOAT
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS bankers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100) UNIQUE,
            password VARCHAR(100)
        )
    """)
    conn.commit()
    conn.close()

# ------------------ Customer Logic ------------------
def register_customer():
    conn = get_connection()
    cur = conn.cursor()
    print("\n--- Customer Registration ---")
    name = input("Name: ")
    email = input("Email: ")
    password = input("Password: ")
    acc_no = int(input("Account No: "))
    balance = float(input("Initial Balance: "))

    try:
        cur.execute("INSERT INTO customers (name, email, password, account_no, balance) VALUES (%s, %s, %s, %s, %s)",
                    (name, email, password, acc_no, balance))
        conn.commit()
        print("Registered Successfully!")
    except:
        print("Email or Account No already exists.")
    finally:
        conn.close()

def login_customer():
    conn = get_connection()
    cur = conn.cursor()
    print("\n--- Customer Login ---")
    email = input("Email: ")
    password = input("Password: ")
    cur.execute("SELECT * FROM customers WHERE email=%s AND password=%s", (email, password))
    user = cur.fetchone()
    conn.close()

    if user:
        print("Login Successful!")
        return Customer(user['name'], user['email'], user['password'], user['account_no'], user['balance'])
    else:
        print("Invalid Credentials!")
        return None

def deposit_money(customer):
    conn = get_connection()
    cur = conn.cursor()
    amount = float(input("Enter amount to deposit: "))
    customer.deposit(amount)
    cur.execute("UPDATE customers SET balance=%s WHERE account_no=%s", (customer.get_balance(), customer.account_no))
    conn.commit()
    conn.close()
    print("Deposit Successful!")

def withdraw_money(customer):
    conn = get_connection()
    cur = conn.cursor()
    amount = float(input("Enter amount to withdraw: "))
    if customer.withdraw(amount):
        cur.execute("UPDATE customers SET balance=%s WHERE account_no=%s", (customer.get_balance(), customer.account_no))
        conn.commit()
        print("Withdrawal Successful!")
    else:
        print("Insufficient Balance!")
    conn.close()

def view_balance(customer):
    print(f" Current Balance: ₹{customer.get_balance()}")

# ------------------ Banker Logic ------------------
def register_banker():
    conn = get_connection()
    cur = conn.cursor()
    print("\n--- Banker Registration ---")
    name = input("Name: ")
    email = input("Email: ")
    password = input("Password: ")

    try:
        cur.execute("INSERT INTO bankers (name, email, password) VALUES (%s, %s, %s)",
                    (name, email, password))
        conn.commit()
        print("Banker Registered!")
    except:
        print("Email already exists.")
    finally:
        conn.close()

def login_banker():
    conn = get_connection()
    cur = conn.cursor()
    print("\n--- Banker Login ---")
    email = input("Email: ")
    password = input("Password: ")
    cur.execute("SELECT * FROM bankers WHERE email=%s AND password=%s", (email, password))
    result = cur.fetchone()
    conn.close()
    return bool(result)

def view_all_customers():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT name, email, account_no, balance FROM customers")
    data = cur.fetchall()
    conn.close()
    print("\n--- All Customers ---")
    for cust in data:
        print(f"Name: {cust['name']}, Email: {cust['email']}, Acc No: {cust['account_no']}, Balance: ₹{cust['balance']}")

def delete_customer():
    conn = get_connection()
    cur = conn.cursor()
    acc_no = int(input("Enter Account No to delete: "))
    confirm = input("Are you sure? (Y/N): ").strip().upper()
    if confirm == "Y":
        cur.execute("DELETE FROM customers WHERE account_no=%s", (acc_no,))
        conn.commit()
        print("Customer Deleted.")
    else:
        print("Cancelled.")
    conn.close()

def update_customer():
    conn = get_connection()
    cur = conn.cursor()
    acc_no = int(input("Enter Account No to update: "))
    print("Leave blank to skip:")
    name = input("New Name: ")
    password = input("New Password: ")

    if name:
        cur.execute("UPDATE customers SET name=%s WHERE account_no=%s", (name, acc_no))
    if password:
        cur.execute("UPDATE customers SET password=%s WHERE account_no=%s", (password, acc_no))
    conn.commit()
    conn.close()
    print("Customer Updated.")

# ------------------ Main Program ------------------
create_database()
create_tables()

while True:
    print("""
======== Bank Management System ========

1. Banker
2. Customer
3. Exit
""")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        while True:
            print("""
--- Banker Menu ---
1. Register
2. Login
3. Back
""")
            ch = input("Enter choice: ")
            if ch == "1":
                register_banker()
            elif ch == "2":
                if login_banker():
                    while True:
                        print("""
-- Banker Operations --
1. View All Customers
2. Update Customer
3. Delete Customer
4. Back
""")
                        op = input("Enter choice: ")
                        if op == "1":
                            view_all_customers()
                        elif op == "2":
                            update_customer()
                        elif op == "3":
                            delete_customer()
                        elif op == "4":
                            break
                        else:
                            print("Invalid Choice")
                else:
                    print("Login Failed!")
            elif ch == "3":
                break
            else:
                print("Invalid Option!")

    elif choice == "2":
        while True:
            print("""
--- Customer Menu ---
1. Register
2. Login
3. Back
""")
            c = input("Enter choice: ")
            if c == "1":
                register_customer()
            elif c == "2":
                customer = login_customer()
                if customer:
                    while True:
                        print("""
-- Customer Operations --
1. Deposit
2. Withdraw
3. View Balance
4. Back
""")
                        op = input("Enter choice: ")
                        if op == "1":
                            deposit_money(customer)
                        elif op == "2":
                            withdraw_money(customer)
                        elif op == "3":
                            view_balance(customer)
                        elif op == "4":
                            break
                        else:
                            print("Invalid Option!")
            elif c == "3":
                break
            else:
                print("Invalid Choice!")

    elif choice == "3":
        print(" Thank you for using the Jaypalsinh's Bank Management System!! ")
        break
    else:
        print(" Invalid Input. Try again. ")
