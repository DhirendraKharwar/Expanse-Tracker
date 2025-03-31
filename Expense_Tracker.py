'''
Add expense
    1. input the data from the user
    2. store it in the dictionary
    3. print successful added massege
'''
def add_expense(expenses):
    date = input("Enter Date YYYY-MM-DD: ")
    category= input("Enter the Category: ")
    amount = float(input("Enter the expense amount: "))
    description= input("Enter the description: ")
    
    exp = {'date':date,'category':category,'amount':amount,'description':description}
    expenses.append(exp)
    print("Recorded successfully.")
    
'''
View Expense Record
    1. If record is not found give the messege
    2. print the records from the dictionary
'''
def view_expense(expenses):
    if not expenses:
        print("No record found.\n Thank You!")
    print("  Date               Category               Amount               Description")
    print("-"*50)
    for exp in expenses:
        print(f"  {exp['date']}               {exp['category']}               {exp['amount']:.2f}               {exp['description']}")
    print("-"*50)
    
'''
Set the Budget
'''
def set_budget():
    return float(input("Enter your monthly budget: "))

'''
Track the expense recods and budget
'''
def track_budget(expenses, budget):
    total_spent = sum(exp['amount'] for exp in expenses)
    print(f"Total Spent: Rs. {total_spent:.2f}")
    if total_spent>budget:
        print("Warning: You have exceeded budget!")
        print(f"Exceeded Amount: Rs. {total_spent-budget:.2f}")
    else:
        print(f"Remaining Budget: Rs. {budget-total_spent:.2f}")


'''
Call all the functions here to navigate all the activity in this expese tracker
'''
def main():
    expenses = []
    budget = set_budget()
    while True:
        print("Epense Tracker is here")
        print("1. Add expense records.")
        print("2. View expense records.")
        print("3. Track budget.")
        print("4. Exit")
        
        choise = int(input("Enter your choise: "))
        
        if choise==1:
            add_expense(expenses)
        elif choise==2:
            view_expense(expenses)
        elif choise==3:
            track_budget(expenses,budget)
        elif choise==4:
            print("Exit done.")
            exit()
        else:
            print("Please correct your choise, try again.")
        
if __name__=="__main__":
    main()
