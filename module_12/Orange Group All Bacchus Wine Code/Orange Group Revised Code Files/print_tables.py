import mysql.connector

def print_tables():

    db = mysql.connector.connect(
        user="bacchus_user",
        password="mysqltest",
        host="localhost",
        database="bacchus_wine"
    )

    cursor = db.cursor()


    # print supplier table
    cursor.execute("SELECT * FROM supplier;")

    results = cursor.fetchall()

    print("\n***Suppliers***")

    for tables in results:
        print(
            f"Supplier ID: {tables[0]}\nName: {tables[1]}\nAddress: {tables[2]}\nAddress2: {tables[3]}\nZip code: {tables[4]}\nFirst name: {tables[5]}\nLast name: {tables[6]}\nPhone: {tables[7]}\nEmail: {tables[8]}\nOrder Method: {tables[9]}\nMisc: {tables[10]}\nActive: {tables[11]}\n")
        print("\n")


    # print supplies table
    cursor.execute("SELECT * FROM supplies;")

    results = cursor.fetchall()

    print("\n***Supplies***")

    for tables in results:
        print(
            f"Supply ID: {tables[0]}\nName: {tables[1]}\nDescription: {tables[2]}\nAvailable: {tables[3]}\nCost: {tables[4]}\nSupplier ID: {tables[5]}")
        print("\n")


    # print supply_order_details table
    cursor.execute("SELECT * FROM supply_order_details;")

    results = cursor.fetchall()

    print("\n***Supply Order Details")

    for tables in results:
        print(
            f"Supply Order ID: {tables[0]}\nSupply ID: {tables[1]}\nQuantity Ordered: {tables[2]}\n")


    # print supply_order table
    cursor.execute("SELECT * FROM supply_order;")

    results = cursor.fetchall()

    print("\n***Supply Order***")

    for tables in results:
        print(
            f"Supply Order ID: {tables[0]}\nTotal Cost: {tables[1]}\nOrder Date: {tables[2]}\nOrder Method: {tables[3]}\nTracking Number: {tables[4]}\nCarrier: {tables[5]}\nEstimated Delivery Date: {tables[6]}\nActual Delivery Date: {tables[7]}\nSupplier ID: {tables[8]}\n")


    # print wine table
    cursor.execute("SELECT * FROM wine;")

    results = cursor.fetchall()

    print("\n***Wine***")

    for tables in results:
        print(
            f"Wine ID: {tables[0]}\nName: {tables[1]}\nStyle {tables[2]}\nOn-Hand: {tables[3]}\nBatch ID: {tables[4]}\nCost: {tables[5]}\n")


    # # print batch table
    cursor.execute("SELECT * FROM batch;")

    results = cursor.fetchall()

    print("\n***Batch***")

    for tables in results:
        print(
            f"Batch ID: {tables[0]}\nBottled On: {tables[1]}\nExpiration: {tables[2]}\nBatch Quantity: {tables[3]}\nWine ID: {tables[4]}\n")


    # print wine_order table
    cursor.execute("SELECT * FROM wine_order;")

    results = cursor.fetchall()

    print("\n***Wine Orders***")

    for tables in results:
        print(
            f"Wine Order ID: {tables[0]}\nTotal Cost: {tables[1]}\nOrder Date: {tables[2]}\nOrder Method: {tables[3]}\nEstimated Delivery Date: {tables[4]}\nActual Delivery Date: {tables[5]}\nDistributor ID: {tables[6]}\n")


    # print wine_order_details table
    cursor.execute("SELECT * FROM wine_order_details;")

    results = cursor.fetchall()

    print("\n***Wine Order Details***")

    for tables in results:
        print(
            f"Wine Order ID: {tables[0]}\nWine ID{tables[1]}\nQuantity Ordered: {tables[2]}\n")


    # print distributor table
    cursor.execute("SELECT * FROM distributor;")

    results = cursor.fetchall()

    print("\n***Distributors***")

    for tables in results:
        print(
            f"Distributor ID: {tables[0]}\nName: {tables[1]}\nAddress 1: {tables[2]}\nAddress 2: {tables[3]}\nZip Code: {tables[4]}\nFirst Name: {tables[5]}\nLast Name: {tables[6]}\nPhone: {tables[7]}\nEmail: {tables[8]}\nActive: {tables[9]}\n")


    # print wine_distributor_details table
    cursor.execute("SELECT * FROM wine_distributor_details;")

    results = cursor.fetchall()

    print("\n***Wine Distributor Details***")

    for tables in results:
        print(
            f"Wine ID: {tables[0]}\nDistributor ID: {tables[1]}\n")


    # print employee table
    cursor.execute("SELECT * FROM employee;")

    results = cursor.fetchall()

    print("\n***Employee***")

    for tables in results:
        print(
            f"Employee ID: {tables[0]}\nFirst Name: {tables[1]}\nLast Name: {tables[2]}\nHire Date: {tables[3]}\nStart Date: {tables[4]}\nActive: {tables[5]}\nDepartment ID: {tables[6]}\nPosition ID: {tables[7]}\n")


    # print employee_time_worked table
    cursor.execute("SELECT * FROM employee_time_worked;")

    results = cursor.fetchall()

    print("\n***Employee Time Worked***")

    for tables in results:
        print(
            f"Date: {tables[0]}\nClock In: {tables[1]}\nClock Out: {tables[2]}\nStart Break: {tables[3]}\nEnd Break: {tables[4]}\nStart Lunch: {tables[5]}\nEnd Lunch: {tables[6]}\nEmployee ID: {tables[7]}\n")


    # print positions table
    cursor.execute("SELECT * FROM positions;")

    results = cursor.fetchall()

    print("\n***Positions***")

    for tables in results:
        print(
            f"Position ID: {tables[0]}\nTitle: {tables[1]}\nPay: {tables[2]}\nHourly(1)/Salary(0): {tables[3]}\nSupervisor Y(1)/N(0): {tables[4]}\n")


    # print zip_lookup table
    cursor.execute("SELECT * FROM zip_lookup;")

    results = cursor.fetchall()

    print("\n***Zipcode Lookup***")

    for tables in results:
        print(
            f"Zip Code: {tables[0]}\nCity: {tables[1]}\nState: {tables[2]}\nCountry: {tables[3]}\n")


    # print department table
    cursor.execute("SELECT * FROM department;")

    results = cursor.fetchall()

    print("\n***Departments***")

    for tables in results:
        print(
            f"Department ID: {tables[0]}\nName: {tables[1]}\nDepartment Head: {tables[2]}\n")


    # print employee_alternate table
    cursor.execute("SELECT * FROM employee_alternate;")

    results = cursor.fetchall()

    print("\n***Employee Alternate***")

    for tables in results:
        print(
            f"Address 1: {tables[0]}\nAddress 2: {tables[1]}\nZip Code: {tables[2]}\nPhone: {tables[3]}\nEmail: {tables[4]}\nTermination Date: {tables[5]}\nTermination Reason: {tables[6]}\nEligible For Rehire Y(1)/N(0): {tables[7]}\nSSN: {tables[8]}\nDOB: {tables[9]}\nEmployee ID: {tables[10]}\n")
