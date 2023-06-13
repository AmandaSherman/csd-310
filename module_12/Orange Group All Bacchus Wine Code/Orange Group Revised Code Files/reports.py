import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="bacchus_user",
    password="mysqltest",
    database="bacchus_wine"
)
mycursor = mydb.cursor()


def wine_orders():
    print("\n***WINE ORDER REPORT***\n")
    # Execute the script using the cursor
    mycursor.execute(
        "select w.name, w.onhand_quantity, wo.total_cost, wo.order_date, wo.wine_order_id"
        " from wine w inner join wine_order_details wod on w.wine_id = wod.wine_id "
        "inner join wine_order wo on wod.wine_order_id = wo.wine_order_id order by w.name")

    # Fetch and print the results
    results = mycursor.fetchall()
    for row in results:
        print(
            f"Wine Name: {row[0]}\nOnhand Quantity: {row[1]}\nTotal Cost: {row[2]}\nOrder Date: {row[3]}\nWine Order ID: {row[4]}\n"
        )


def employee_time():
    print("\n***EMPLOYEE TIME REPORT***\n")

    mycursor.execute(
        'select first_name, last_name, etw.date, '
        'timestampdiff(minute,etw.clock_in_shift,etw.clock_out_shift)/60 as "Total Shift (Hr)", '
        'timestampdiff(minute,etw.clock_out_break,etw.clock_in_break) as "Break (Min)", '
        'timestampdiff(minute,etw.clock_out_lunch,etw.clock_in_lunch) as"Lunch (Min)", '
        '((timestampdiff(minute,etw.clock_in_shift,etw.clock_out_shift)) '
        '-(timestampdiff(minute,etw.clock_out_break,etw.clock_in_break)) '
        '-(timestampdiff(minute,etw.clock_out_lunch,etw.clock_in_lunch)))/60 as "Total Worked (Hr)" '
        'from employee e '
        'inner join employee_time_worked etw '
        'on e.employee_id = etw.employee_id'
    )

    timeworked = mycursor.fetchall()

    for employee in timeworked:
        print(
            '''First Name: {}\nLast Name: {}\nDate: {}\nHours Worked: {}\n'''.format(employee[0], employee[1], employee[2],
                                                                                 employee[3]))


def inventory():
    print("\n***SUPPLY ORDERS REPORT***\n")

    mycursor.execute('''select s.name, so.supply_order_id, so.total_cost, so.order_date,
    so.order_estimated_delivery_date,so.order_actual_delivery_date,
    (timestampdiff(DAY,so.order_estimated_delivery_date,so.order_actual_delivery_date))
    as "Actual vs Estimated Delivery" from supplier s inner join supply_order so
    on s.supplier_id = so.supplier_id;''')

    details = mycursor.fetchall()

    for detail in details:
        print('''Supplier: {}\nSupply Order ID: {}\nCost: ${}\nOrder Date: {}\nEstimated Delivery: {}\nActual Delivery: {}\nActual VS. Estimated Delivery: {} Days\n'''.format(detail[0], detail[1], detail[2], detail[3], detail[4], detail[5],
                                                      detail[6]))