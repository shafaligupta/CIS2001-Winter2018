def fahrenheit_to_celcius_temp(fValue):
    celcius = (fValue-32)/1.8
    return celcius

def celcius_to_fahrenheit(cValue):
    fahrenheit = (cValue*1.8)+32
    return fahrenheit

def number_of_payments( monthly_rate, payment_amount, loan_balance ):
    current_balance = loan_balance

    if monthly_rate >= 1:
        monthly_rate /= 100
    payments = 0
    while current_balance > 0:
        payments += 1
        current_balance += current_balance * monthly_rate
        current_balance -= payment_amount

    return payments

def calculate_payment_amount( monthly_rate, number_of_payments, loan_balance ):
    if monthly_rate >= 1:
        monthly_rate /= 100

    payment = ( monthly_rate * loan_amount ) \
              / ( 1 - ( 1 + monthly_rate )**-number_of_payments)

    return payment

choice = ""

while choice != "5":
    print("Welcome to lab 1, please select an option:")
    choice = input("1 - Convert Fahrenheit to Celsius\n"
                   "2 - Convert Celsius to Fahrenheit\n"
                   "3 - Calculate number of payments needed given a rate and amount\n"
                   "4 - Calculate the payment requirement given a rate and number of payments\n"
                   "5 - Quit\n")

    print("You chose the option:", choice)

    if choice == "1":
        temp_in_fahrenheit = float(input("Enter the temp in Fahrenheit: "))
        print( fahrenheit_to_celcius_temp( temp_in_fahrenheit ))
    elif choice == "2":
        temp_in_celsius = float(input("Enter the temp in Celsius: "))
        print(celcius_to_fahrenheit(temp_in_celsius))
    elif choice =="3":
        monthly_rate = float(input("Enter the APR of the loan: ")) / 12
        payment_amount = float(input("Enter the monthly payment amount: "))
        loan_amount = float(input("Enter the loan amount: "))
        print( "It will take",
               number_of_payments( loan_amount, payment_amount, monthly_rate)
               , "payments to pay off the loan")

    elif choice == "4":
        monthly_rate = float(input("Enter the APR of the loan: ")) / 12
        number_of_payments = float(input("Enter the number of payments to be made: "))
        loan_amount = float(input("Enter the loan amount: "))
        print(calculate_payment_amount(monthly_rate, number_of_payments, loan_amount) )
    elif choice != "5":
        print("PLease enter a number 1-5")