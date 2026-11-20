#function that determines the initial amount using facility code and time
def amount_due(facility_code, hours):
    match facility_code:
        case "squa":
            amnt_due = 13.0 * hours
        case "swim":
            amnt_due = 12.00 * hours
        case "gym":
            amnt_due = 11.00 * hours
        case "wei":
            amnt_due = 8.00 * hours
       
    return amnt_due

#function that calculates and returns the amount that is inclusive of VAT
def final_amount_due(amount):
    final_amount = amount + (amount * 0.14) # or final_amount_due = amount * 1.14
    return final_amount

#void procedure that displays the output for the program
def display(name, final_amount):
    print(f"{name},",f"the mount due: R{final_amount:.2f}")

#method main
def process_payment():
    codes = ["wei","squa","swim","gym"]
    name = input("Enter the name of the member: ")
    print("Facility Codes:")
    Facilities = { "Squash": "squa",
                   "Swimming Pool": "swim",
                   "Gymnasium": "gym",
                   "Weights": "wei"}
    print(Facilities)
    code = input("Enter the facility code: ")
    while code not in codes:
        print("Invalid code")
        code = input("Enter the facility code: ")
    time = input("Enter the time in hours: ")
    amount = amount_due(code,float(time))
    display(name,final_amount_due(amount))
#calling the method main to run the program
process_payment()

