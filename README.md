# 5-4-Automobile-Costs
 Calculates and displays total monthly  and annual car costs

## Scope
 Write a program that asks the user to enter the monthly costs for the following expenses incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires, and maintenance. The program should then display the total monthly cost and total annual cost of these expenses.

 *Hint*: Ask for all of the inputs for the expenses in the main function. Then, send those to a showExpenses function to calculate and print the results.

### Sample Run
    Enter the monthly loan amount:  750
    Enter the monthly insurance amount:  150
    Enter the monthly gas amount:  300
    Enter the monthly oil amount:  35
    Enter the monthly tires amount:  20
    Enter the monthly maintenance amount:  200
    Total monthly expense: $1,455.00
    Total annual expense: $17,460.00
### Pseudocode
#### Main function
    START
      INPUT monthly_loan
      INPUT monthly_insurance
      INPUT monthly_gas
      INPUT monthly_oil
      INPUT monthly_tires
      INPUT monthly_maintenance
      CALL show_expenses
    END

#### show_expenses function
    START
      Pass In: monthly_loan, monthly_insurance, monthly_gas, monthly_oil, monthly_tires, monthly_maintenance
      CALCULATE monthly_total
        Sum all values passed to function
      PRINT monthly_total
      CALCULATE yearly_total
        Multiply monthy_total by 12
      PRINT yearly_total
    END
