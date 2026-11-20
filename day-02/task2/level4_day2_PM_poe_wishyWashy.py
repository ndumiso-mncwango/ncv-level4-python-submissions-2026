import random 
def generate_minutes():
    minutes = random.randint(30,180)
    return minutes

def calc_amount(machine_type, minutes):
    hours = minutes/60.0
    if machine_type == "A":
        cost = 50 + (hours * 30)
    elif machine_type == "B":
        cost = 62.5 + (hours * 36.25)
    elif machine_type == "C":
        cost = 74.87 + (hours * 40.5)
    return cost
def calc_total_amount(amount):
    vat_amount = amount * 0.14
    total = amount + vat_amount
    return vat_amount, total
def display_summary(payments):
    num_customers_processed = len(payments)
    total_payable = 0
    lowest = payments[0]
    highest = payments[0]
    
    for n in range(num_customers_processed):
        total_payable += payments[n]
    average = total_payable/num_customers_processed
    
    for n in range(num_customers_processed):
        if payments[n] > highest:
            highest = payments[n]
        if payments[n] < lowest:
            lowest = payments[n]
    print(f"Number of Customers: {num_customers_processed}")
    print(f"Total Payable: R{total_payable:.2f}")
    print(f"Average: {average:.2f}")
    print(f"Highest: {highest:.2f}")
    print(f"Lowest: {lowest:.2f}")
    #return num_customers_processed, total_payable,average,highest,lowest
def process_payments():
    num_customers = input("Enter the number of customers to process: ")
    #validating number of customers input
    while not num_customers.isdigit():
        num_customers = input("Enter valid number of customers: ")
    payments = []
    
    num_customers = int(num_customers)
    for n in range(num_customers):
        cust_name = input("Enter the customer name: ")
        machine_type = input("Enter the machine type (A, B or C): ").upper()
        #validating machine type input
        machine_types = ["A","B","C"]
        while machine_type not in machine_types:
            machine_type = input("Invalid machine type, enter valid machine type: ").upper()
        minutes = generate_minutes()
        amount = calc_amount(machine_type, minutes)
        VAT, total_payable = calc_total_amount(amount)
        payments.append(total_payable)
        print(f"Customer Name: {cust_name}")
        print(f"Machine Type: {machine_type}")
        print(f"Duration: {minutes}")
        print(f"Amount before VAT: R{amount:.2f}")
        print(f"VAT Amount: R{VAT:.2f}")
        print(f"Total Payable: R{total_payable:.2f}")
        print("--------------------------------------------")
        print("--------------------------------------------")
    
    display_summary(payments)
process_payments()        
    

