# 5-4 Automobile Costs
# Shaun Hayworth
# CIS 2
# 11-03-2019
# Source code and revision history are available at https://github.com/SCHayworth/5-4-Automobile-Costs

# Program calculates the total monthly and yearly costs for an automobile given the following monthly costs:
#   loan payment, insurance, gas, oil, tires, maintenence.

# Define the main function
# Mainline program logic
def main():

    # Prompt user for individual monthly costs
    monthly_loan = float(input('Enter the monthly loan amount: ')) # Monthly loan payment
    monthly_insurance = float(input('Enter the monthly insurance amount: ')) # Monthly insurance premium
    monthly_gas = float(input('Enter the monthly gas amount: ')) # Monthly fuel cost
    monthly_oil = float(input('Enter the monthly oil amount: ')) # Monthly oil cost
    monthly_tires = float(input('Enter the monthly tires amount: ')) # Monthly tire care cost
    monthly_maintenance = float(input('Enter the monthly maintenence amount: ')) # Monthly maintenance cost

    # Call the show_expenses function and pass the monthly costs to it
    show_expenses(monthly_loan, monthly_insurance, monthly_gas, monthly_oil, monthly_tires, monthly_maintenance)

# Define the show_expenses function
# Calculates monthly and yearly auto costs, and accepts an arbitrary number of arguments
def show_expenses(*expenses):

    # Get the total number of arguments passed
    expense_count = len(expenses)

    # If there are arguments passed, add them to the total until there are no more arguments to add.
    # Otherwise, set monthly_total to 0.
    if expense_count > 0 :
        monthly_total = 0
        for elem in expenses :
            monthly_total += elem
    else:
        monthly_total = 0

    # Display the monthly and yearly expenses.
    print(f'Total monthly expense: ${monthly_total:,.2f}')
    print(f'Total annual expense: ${monthly_total * 12:,.2f}')

# Call the main function to execute the program.
main()
