import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="bacchus_user",
    password="mysqltest",
    database="bacchus_wine"
)
mycursor = mydb.cursor()


def fill_tables():
    # fill supplier table
    supplier = ("INSERT INTO supplier (supplier_ID, name, Street_Address_1, Street_Address_2, Zip, Contact_First_Name,"
                "Contact_Last_Name, Phone_Number, Email_Address, Order_Method, Order_Method_Details, Active)"
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    values = [
        (1, 'Southern Glazer', '2400 SW 145th AVE', 'Suite200', 68111, 'Angel', 'Garay', '305-627-1202',
         'angel.garay@shws.com', 'online', 'these are details', 1),
        (2, 'Republic National', '1114 Baldwin ST', 'and a half', 50310, 'Damian', 'Brown', '254-568-1245',
         'damian.brown@repubnat.com', 'phone', 'these are details', 0),
        (3, 'Breakthru', '4587 Somewhere RD', None, 53188, 'Bob', 'Lasname', '896-456-2580',
         'blas@breakthru.com', 'post', 'prefers correspondence by mail', 1),
        (4, 'Young\'s market', '1 Young CIR', 'Suite 100', 27513, 'George', 'Young', '321-456-9870',
         'gyoung@youngsmarket.com', 'online', 'I\'m not really sure what should be here', 1)
    ]
    mycursor.executemany(supplier, values)
    mydb.commit()
    print(mycursor.rowcount, "rows were inserted into supplier table")

    # fill supplies table
    supplies = ("INSERT INTO supplies (Supply_ID, Name, Description, Onhand_Quantity, Unit_Price, Supplier_ID) "
                "VALUES (%s, %s, %s, %s, %s, %s)")
    values = [
        (1, 'Corks', 'Environment Friendly', 1548, 0.25, 1),
        (2, 'Bottles', '750 ML', 254, 1.20, 1),
        (3, 'Labels', 'Display Product on Bottle', 2455, 0.05, 4),
        (4, 'Tubing', 'For Processing', 25, 25.00, 3),
        (5, 'Vats', 'For Fermenting', 12, 2500.00, 3),
        (6, 'Boxes', 'Six(6) Bottle Size', 1258, 2.00, 4)
    ]
    mycursor.executemany(supplies, values)
    mydb.commit()
    print(mycursor.rowcount, "rows were inserted into supplies table")

    # fill supply_order_details table
    supply_order_details = ("INSERT INTO supply_order_details (Supply_Order_ID, Supply_ID, Quantity_Ordered)"
                            "VALUES (%s, %s, %s)")
    values = [
        (1111, 1, 10000),
        (2222, 2, 10000),
        (3333, 3, 10000),
        (4444, 4, 100),
        (5555, 5, 10),
        (6666, 6, 10000),
    ]
    mycursor.executemany(supply_order_details, values)
    mydb.commit()
    print(mycursor.rowcount, "rows were inserted into supply_order_details table")

    # fill supply_order table
    supply_order = ("INSERT INTO supply_order (supply_order_ID, total_cost, Order_date, Order_Method,"
                    "Order_tracking_number, Order_delivery_carrier, Order_Estimated_Delivery_date,"
                    " Order_Actual_Delivery_Date, Supplier_ID)"
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
    values = [
        (1111, 2500.00, '2022-04-21', 'Online', '33783220542444073463', 'USPS', '2022-04-26', '2022-04-26 14:00:00', 1,),
        (2222, 12000.00, '2022-05-21', 'Online', '33668316260356970224', 'USPS', '2022-05-26', '2022-05-25 14:30:00', 1,),
        (3333, 500.00, '2022-06-21', 'Phone', '81102417195194130687', 'UPS', '2022-06-26', '2022-06-28 16:00:00', 4,),
        (4444, 2500.00, '2022-08-21', 'Phone', '58613729517346820701', 'FEDEX', '2022-08-26', '2022-08-27 9:00:00', 3,),
        (5555, 25000.00, '2022-10-21', 'Phone', '71763449314037379282', 'FEDEX', '2022-10-26', '2022-10-24 11:00:00', 3,),
        (6666, 20000.00, '2022-11-21', 'Phone', '84904082002849849284', 'UPS', '2022-11-26', '2022-11-30 16:45:00', 4,),
    ]
    mycursor.executemany(supply_order, values)
    mydb.commit()
    print(mycursor.rowcount, "rows were inserted into supply_order table")

    # fill wine table
    wine = "INSERT INTO wine (Wine_ID, Name, Style, Onhand_Quantity, Batch_ID, Cost) VALUES (%s, %s, %s, %s, %s, %s)"
    values = [
        (1, 'Dark and Red', 'Merlot', 300, 2022010101, 15.00),
        (2, 'Crimson Silk', 'Cabernet', 257, 2022010102, 15.00),
        (3, 'Bright and Bold', 'Chablis', 124, 2022010103, 12.00),
        (4, 'Clean and Smooth', 'Chardonnay', 272, 2022010104, 8.00),
        (5, 'Rare Velvet', 'Chardonnay', 90, 2022042701, 25.00),
        (6, 'Anniversary Cask', 'Merlot', 37, 2022021401, 40.00)
    ]
    mycursor.executemany(wine, values)
    mydb.commit()
    print(mycursor.rowcount, "rows were inserted into wine table")


    # fill batch table
    batch = ("INSERT INTO batch (Batch_ID, Bottled_Date, Expiration_Date, Quantity, Wine_id) " \
            "VALUES (%s, %s, %s, %s, %s)")
    values = [
        (2022010101, '2022-08-01', '2024-08-01', 200, 1),
        (2022010102, '2022-10-01', '2023-10-01', 200, 2),
        (2022010103, '2022-02-02', '2023-02-02', 200, 3),
        (2022010104, '2022-02-02', '2023-02-02', 200, 4),
        (2022042701, '2022-03-01', '2023-03-01', 100, 5),
        (2022021401, '2022-12-01', '2024-12-01', 100, 6)
    ]
    mycursor.executemany(batch, values)
    mydb.commit()
    print(mycursor.rowcount, "rows were inserted into batch table")

    # fill wine_order table
    wine_order = ("INSERT INTO wine_order (Wine_Order_ID, Total_Cost, Order_Date, Order_Method, "
                  "Order_Estimated_Delivery_Date, Order_Actual_Delivery_Date, Distributor_ID)"
                  "VALUES(%s,%s,%s,%s,%s,%s,%s)")
    values = [
        (1154, 1500.00, '2022-06-24 11:20', 'Post', '2022-12-01', '2022-12-01 10:04', 441),
        (1155, 1500.00, '2022-02-10 14:14', 'Online', '2022-11-25', '2022-11-23 12:35', 342),
        (1156, 1200.00, '2021-11-15 15:10', 'Phone', '2022-11-13', '2022-11-17 09:10', 775),
        (1157, 800.00, '2022-07-10 09:20', 'Online', '2022-10-29', '2022-10-27 03:20', 889),
        (1158, 250.00, '2021-04-19 16:09', 'Post', '2022-11-16', '2022-11-16 02:15', 442),
        (1159, 1600.00, '2020-12-20 08:15', 'Phone', '2022-10-02', '2022-09-30 09:00', 332)
    ]
    mycursor.executemany(wine_order, values)
    mydb.commit()
    print(mycursor.rowcount, "rows were inserted into wine_order table")


    # fill wine_order_details table
    wine_order_details = "INSERT INTO wine_order_details (Wine_Order_ID, Wine_ID, Quantity_Ordered) VALUES(%s,%s,%s)"
    values = [
        (1154, 1, 100),
        (1155, 2, 100),
        (1156, 3, 100),
        (1157, 4, 100),
        (1158, 5, 10),
        (1159, 6, 40)
    ]
    mycursor.executemany(wine_order_details, values)
    mydb.commit()
    print(mycursor.rowcount, "rows were inserted into wine_order_details table")
    
    # fill distributor_table
    distributor = ("INSERT INTO distributor (Distributor_ID, Name, Street_Address_1, Street_Address_2, Zip, Contact_First_Name, Contact_Last_Name, "
                " Phone_Number, Email_Address, Active)"
                "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    values = [
        (441, 'Hy - vee Wine and Spirits', '14195 Corkey Road', None, 68111, 'Sally', 'Sanders', 7012329585, 'salsan@hyveeus.com', 1),
        (342, 'A1 Beer and Liquor','693343 Main Street' , None, 50310, 'John', 'Coleman', 6239256644, 'JColeman@a1liquors.com', 1),
        (775, 'Bakers Grocery', '4298 Merlot Place', None, 53188, 'Candace', 'Bidson', 5159544232, 'Bidson@bakersdillons.com', 1),
        (889, 'Wine Club Platinum', '9899 Rocket Road', None, 27513, 'Asher', 'Jones', 7128453980, 'AJones@wineclub.com', 1),
        (442, 'Wine Styles Club', '22 Canary Road', None, 52501, 'Katie', 'Brown', 3764548878, 'Brown@winestyles.com', 1),
        (332, 'Cheesecake Factory', '555 Cake Drive', None, 51537, 'Spencer', 'Hilgen', 5315585933, 'hilgen@cheesecake.com', 1)
     ]
    mycursor.executemany(distributor, values)
    mydb.commit()
    print(mycursor.rowcount, "rows were inserted into distributor table")

    # fill wine_distributor_details table
    wine_distributor_details = "INSERT INTO wine_distributor_details (Wine_ID, Distributor_ID) VALUES(%s,%s)"
    values = [
        (1,	441),
        (2,	441),
        (3,	441),
        (4,	441),
        (5,	441),
        (6,	441),
        (1, 342),
        (2,	342),
        (3, 342),
        (4,	342),
        (5,	342),
        (6,	342),
        (1,	775),
        (2,	775),
        (3,	775),
        (4,	775),
        (5,	775),
        (6,	775),
        (1,	889),
        (2,	889),
        (3,	889),
        (4,	889),
        (5,	889),
        (6,	889),
        (1,	442),
        (2,	442),
        (3,	442),
        (4,	442),
        (1,	332),
        (2,	332),
        (3,	332),
        (4,	332)
    ]
    mycursor.executemany(wine_distributor_details, values)
    mydb.commit()
    print(mycursor.rowcount, "rows were inserted into wine_distributor_details table")
    
    # fill employee table
    employee = ("INSERT INTO employee (Employee_ID, First_Name, Last_Name, Hire_Date, "
    "Start_Date, Active, Department_ID, Position_ID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)")
    values = [
        (6930090, 'Stan', 'Bacchus', '2019-12-04', '2019-12-04', 1, 1000, 100,),
        (1380275, 'Davis', 'Bacchus', '2019-12-04', '2019-12-04', 1, 1000, 100),
        (8613677, 'Elyse', 'Bailey', '1983-08-04', '1983-08-05', 1, 4000, 120),
        (4059962, 'Emmanuel', 'Ramsey', '2016-10-07', '2016-10-15', 1, 3000, 120),
        (1842386, 'Keira', 'Peck', '1992-08-25', '1992-08-26', 1, 6000, 200),
        (5937994, 'Mia', 'Frost', '1999-09-15', '1999-09-16', 1, 5000, 200),
        (9685338, 'Amaya', 'Hebert', '2014-01-14', '2014-01-15', 1, 2000, 200),
        (7480510, 'Roz', 'Murphy', '2010-03-10', '2010-03-15', 1, 3000, 220),
        (8995741, 'Bob', 'Ulrich', '2011-04-25', '2011-04-26', 1, 3000, 220),
        (5687918, 'Antwan', 'Cline', '1985-04-16', '1985-04-17', 1, 3000, 220),
        (3695025, 'Anyiah', 'Vincent', '1997-11-14', '1997-11-15', 1, 3000, 220),
        (5667699, 'Davian', 'Clark', '2003-04-28', '2003-04-29', 1, 3000, 220),
        (4180563, 'Deborah', 'Harrell', '2007-08-13', '2007-08-17', 1, 3000, 220),
        (9855487, 'Leon', 'Gibbins', '2022-05-19', '2022-05-26', 1, 3000, 220),
        (7767463, 'Henry', 'Doyle', '1982-04-02', '1982-04-03', 1, 5000, 300),
        (5939049, 'Sara', 'Esparza', '2020-01-22', '2020-01-26', 1, 2000, 320),
        (5823178, 'Jordyn', 'Aguilar', '2007-03-05', '2007-03-06', 1, 4000, 400),
        (7863543, 'Santiago', 'Branch', '2020-01-29', '2020-02-05', 1, 5000, 400),
        (4916879, 'Marley', 'Herring', '2007-09-27', '2007-09-28', 1, 5000, 420),
        (5307392, 'Vivian', 'Caldwell', '2011-07-27', '2011-07-28', 1, 4000, 420),
        (6383017, 'Janet', 'Collins', '2017-05-15', '2017-05-17', 1, 2000, 500),
        (2795091, 'Alisa', 'Franklin', '1988-06-16', '1988-06-17', 1, 2000, 500),
        (2799911, 'Trenton', 'Bird', '1990-12-14', '1990-12-15', 1, 2000, 500),
        (3021812, 'Adriana', 'Randolph', '2002-02-08', '2002-02-09', 1, 2000, 500),
        (7579383, 'Alexus', 'Calhoun', '2006-08-30', '2006-09-05', 1, 2000, 500),
        (1944186, 'Maria', 'Costanza', '1983-06-17', '1983-06-18', 1, 6000, 600),
        (1314667, 'Carlos', 'Horne', '1995-02-17', '1995-02-18', 1, 5000, 600),
        (4145223, 'Parker', 'Hart', '2006-11-02', '2006-11-03', 1, 5000, 600)
    ]
    mycursor.executemany(employee, values)
    mydb.commit()
    print(mycursor.rowcount, "rows were insert into employee table")

    # fill employee time worked table
    employee_time_worked = ("INSERT INTO employee_time_worked (Date, Clock_In_Shift , Clock_Out_Shift "
                            ", Clock_Out_Break , Clock_In_Break , Clock_Out_Lunch , "
                            "Clock_In_Lunch, Employee_ID)"
                            "VALUES(%s, %s, %s, %s, %s, %s, %s, %s)")
    values = [
        ('2022-11-01', '07:00:00', '11:00:00', None, None, None, None, '4916879'),
        ('2022-11-02', '07:00:00', '12:00:00', '10:00:00', '10:15:00', None, None, '5307392'),
        ('2022-11-03', '08:00:00', '16:00:00', '11:00:00', '11:15:00', '13:00:00', '13:30:00', '6383017'),
        ('2022-11-04', '10:00:00', '15:00:00', '13:00:00', '13:15:00', None, None, '2795091'),
        ('2022-11-05', '10:00:00', '18:00:00', '13:00:00', '13:15:00', '15:00:00', '15:30:00', '2799911'),
        ('2022-11-06', '11:00:00', '19:00:00', '14:00:00', '14:15:00', '16:00:00', '16:30:00', '3021812'),
        ('2022-11-07', '13:00:00', '17:00:00', None, None, None, None, '7579383'),
        ('2022-11-08', '13:00:00', '21:00:00', '16:00:00', '16:15:00', '18:00:00', '18:30:00', '1944186'),
        ('2022-11-09', '15:00:00', '20:00:00', '18:00:00', '18:15:00', None, None, '1314667'),
        ('2022-11-10', '17:00:00', '21:00:00', None, None, None, None, '4145223'),
    ]
    mycursor.executemany(employee_time_worked, values)
    mydb.commit()
    print(mycursor.rowcount, "rows were inserted into employee_time_worked table")

    # fill positions table
    positions = "INSERT INTO positions (Position_ID, Position_Title, Pay_Grade, Hourly, Supervisory) VALUES (%s,%s,%s,%s,%s)"

    values = [
        (100, 'Owner', None, 0,1),
        (120, 'Administrative Assistant', 20, 1, 0),
        (200, 'Sales', 30, 0, 1),
        (220, 'Marketing', 25, 0, 0),
        (300, 'Production Manager', 23, 1, 1),
        (320, 'Production Laborer', 20, 1, 0),
        (400, 'Maintenance', 20, 1, 0),
        (420, 'Environmental', 15, 1, 0),
        (500, 'Accounting / Payroll', 30, 1, 0),
        (600, 'Logistics', 25, 1, 0),
    ]
    mycursor.executemany(positions, values)
    mydb.commit()
    print(mycursor.rowcount, "rows were inserted into positions table")

    # fill zip code table
    zip_lookup = "INSERT INTO zip_lookup(Zip, City, State, Country) VALUES (%s,%s,%s,%s)"
    values = [
        (68111, 'Omaha', 'NE', 'USA'),
        (50310, 'Des Moines', 'IA', 'USA'),
        (53188, 'Waukesha', 'WI', 'USA'),
        (27513, 'Cary', 'NC', 'USA'),
        (52501, 'Ottumwa', 'IA', 'USA'),
        (51537, 'Harlan', 'IA', 'USA')
    ]
    mycursor.executemany(zip_lookup, values)
    mydb.commit()
    print(mycursor.rowcount, "rows were inserted into zip table")

    # fill department table
    department = "INSERT INTO department (Department_ID, Department_Name, Department_Head) VALUES (%s,%s,%s)"
    values = [
        (1000, 'Owners', 6930090),
        (2000, 'Finance', 6383017),
        (3000, 'Marketing', 748051),
        (4000, 'Facilites', 5307392),
        (5000, 'Production', 7767463),
        (6000, 'Distribution', 1944186)
    ]
    mycursor.executemany(department, values)
    mydb.commit()
    print(mycursor.rowcount, "rows were inserted into department table")

    # fill employee_alternate
    employee_alternate = "INSERT INTO employee_alternate (Street_Address_1, Street_Address_2, Zip, Phone_Number, Email_Address, Term_Date, Term_Reason, Rehireable, SSN, DOB, Employee_ID) VALUES (%s, %s,%s,%s,%s, %s,%s,%s,%s, %s,%s)"
    values = [
    ('3924 Rose Stree',	None, 68111, '402-966-8247', 'Stantheman@gmail.com', None, None, None, 748149274, '1984-11-11', 6930090),
    ('3205 Pearcy Avenue','Apt 10', 68111, '402-826-5015', 'Dbaccu80@yahoo.com',	None, None,	None, 251345289, '1965-04-12', 1380275),
    ('826 Westport Avenue',	None, 68111, '402-372-6785', 'Jcollinshi@yahoo.com',	None, None, None, 634587654, '1996-09-23', 6383017),
    ('70 East Marlborough Avenue', None, 50310,	'515-392-9069',	'Rozzu4@gmail.com',	None, None, None, 214375683, '1990-10-03', 7480510),
    ('7123 S. Glenwood St',	None, 53188, '262-601-9735', 'BobbyUl@gmail.com', None, None, None, 963620155, '1994-04-20', 8995741),
    ('446 North Ave', 'Apt 2', 27513, '919-195-2072', 'Doyleman@hotmail.com',	None, None, None, 135249771, '1983-07-20', 7767463),
    ('7603 Third Dr', 'Apt 3', 52501, '641-209-9539', 'Dogloverxooxxo@aol.com', None, None, None, 912662242, '1986-07-09', 1944186),
    ('9423 Belmont Street',	None, 51537, '712-712-7573', 'Catlady44Elyse@gmail.com',	None, None, None, 289979667, '1974-05-23', 8613677),
    ('12 Pineknoll St',	None, 68111, '402-817-7588', 'Clineantwan@gmail.com', None, None, None, 645881321, '1997-06-23', 5687918),
    ('3 West Street', None,	50310, '515-738-5018', 'AFrankhappy111@icloud.com', None, None, None,91220286, '2001-12-26', 2795091),
    ('27 Old Colonial Ave',	None, 53188, '262-523-9023', 'TBird@icloud.com',	None, None, None, 338355472, '1976-10-02', 2799911),
    ('167 Pine St',	'Suite 100', 27513, '919-577-9325', 'Keirasmail@gmail.com',	None, None,	None, 817261829, '1979-08-29', 1842386),
    ('7172 NW. Saxon Ave',	None, 52501, '641-538-0399', 'C4Horne@yahoo.com', None, None, None, 373644533, '1977-06-15', 1314667),
    ('69 Sutor Ave', None, 51537, '712-575-5087', 'Vinanyiah@aol.com', None, None, None, 844236731, '1986-02-13', 3695025),
    ('700 Valley Farms Ave', None, 68111, '402-335-8005', 'Frosty0mia@icloud.com', None, None, None, 635478765, '1992-04-16', 5937994),
    ('80 SE. Hillside Road', None, 50310, '515-253-1609', 'Adrianadolph@hotmail.com',	None, None, None, 475645765, '1983-01-04', 3021812),
    ('7272C Linden Rd',	None, 53188, '262-858-7453', 'daviclark4312@aol.com', None, None, None, 870978909, '2000-09-17', 5667699),
    ('9684 Lees Creek Ave',	None, 27513, '919-304-6304', 'lexicalhoun99@gmail.com', None, None, None, 125432454, '1999-01-30', 7579383),
    ('796 Plymouth Street',	None, 52501, '641-712-6123', 'Parker7Hart@icloud.com', None,	None, None,	745667546, '1992-03-15', 4145223),
    ('82 Roosevelt St',	None, 51537, '712-433-1562', 'Jord10A@aol.com', None, None, None, 987689879, '1996-10-24', 5823178),
    ('415 West Henry Smith St', None, 68111, '402-674-8021', 'DH4632@gmail.com',	None, None, None, 346554634, '1991-05-23', 4180563),
    ('9774 Birch Hill Rd', None, 50310, '515-452-2415',	'herringml76@yahoo.com', None, None, None, 323243324, '1993-07-09', 4916879),
    ('215 Brookside Avenue', None, 53188, '262-848-0672', 'mscaldwel@gmail.com', None, None, None, 524323453, '1995-10-02', 5307392),
    ('7874 Sunbeam Avenue',	None, 27513, '919-845-9528', 'alherb2060@icloud.com', None, None, None, 634536455, '1998-01-21', 9685338),
    ('7848 S. Clark St', None, 52501, '641-525-3606', 'Ramseyem49@hotmail.com', None,	None, None,	689575689, '1989-05-04', 4059962),
    ('827 NE. Vine St',	None, 51537, '712-657-6502', 'Sparzasar0u@icloud.com', None, None, None, 678586756, '1988-12-13', 5939049),
    ('7 North Bear Hill Ave', None, 68111, '402-177-4774', 'branchbrantiago@gmail.com', None, None, None, 520296509, '1987-03-26', 7863543),
    ('70 North Summerhouse Street',	None, 50310, '515-974-2114', 'leonbig7474@aol.com', None, None, None, 980123098, '1985-09-13', 9855487),
    ]
    mycursor.executemany(employee_alternate, values)
    mydb.commit()
    print(mycursor.rowcount, "rows were inserted into employee_alternate table")