# Declaring the function
def init():
    while True:
        try:
            productprice = int(raw_input("Price: $"))
            break
        except ValueError:
            print("Not an integer!")

# Setting the region (If input isn't one of the countries then it'll loop)
    while True:
        Region = raw_input("Enter country (US, CA, OTHER): ").lower()
        if Region not in ['us','ca','other']:
            print('Please enter one of the following countries! ')
        else:
            break

# Defining the region
    if Region == 'us':
        goatfee = 5 + ( 9.5 / 100 ) * productprice
        finalCost = productprice - goatfee
        paypalfee = ( 2.9 / 100 ) * finalCost
    elif Region == 'ca':
        goatfee = 20 + ( 9.5 / 100 ) * productprice
        finalCost = productprice - goatfee
        paypalfee = ( 2.9 / 100 ) * finalCost
    elif Region == 'other':
        goatfee = 30 + ( 9.5 / 100 ) * productprice
        finalCost = productprice - goatfee
        paypalfee = ( 2.9 / 100 ) * finalCost

# Print the results with one decimal place
    print("===================")
    print("===================")
    print("===================")
    print("Listing Price: $" + format(productprice, ",.1f"))
    print("Goat Commission: $" + format(goatfee, ",.1f"))
    print("Paypal Fees: $" + format(paypalfee, ",.1f"))
    print("Amount Paid: $" + format(finalCost, ",.1f"))


# Beginning of the script
if __name__ == "__main__":
    print("GOAT FEE CALCULATOR BY KENNY")

    # Calls the function
    init()

    # Function to re-use the calculator
    def again():
        while True:
            restart = raw_input('Would you like to use this again? "yes" or "no": ')
            if restart.lower() == 'yes':
                init()
            else:
                print("THANK YOU FOR USING ME")
                break
    # Calls the repeat function
    again()
