import create_tables
import fill_tables
import print_tables
import reports
import time
from datetime import date


# bacchus_wine_db_init.sql needs to be run first

# functions are in separate files and call them from main.py

def date_stamp():
    today = date.today()
    date_ran = today.strftime("%B %d, %Y")
    print("This report was generated on:", date_ran, "\n")


print("\n\nI will load and display the tables for you...\n\n")

# Pause for two seconds for dramatic effect
time.sleep(3)

# create_tables.drop_tables()
create_tables.create_tables()

# fill the tables
fill_tables.fill_tables()

# create the foreign keys
create_tables.foreign_key_constraints()

# print all of the tables and their contents
print_tables.print_tables()

# run the reports
while True:
    choice = input("Please Chose a report to look at. 'employee' for employee time, 'wine orders' for wine orders "
                   "over 1200, 'supply' to see supply orders or q to quit:\n ").lower()
    # Use an if-else statement to call the appropriate function
    if choice == 'employee':
        reports.employee_time()
        date_stamp()
    elif choice == 'wine orders':
        reports.wine_orders()
        date_stamp()
    elif choice == 'supply':
        reports.inventory()
        date_stamp()
    elif choice == 'q':
        print("Goodbye!")
        quit()
    else:
        print("Invalid choice. Please try again.")
