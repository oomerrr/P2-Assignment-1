A="AIRPLANE MANAGEMENT SYSTEM"
C="====================================================================================="
print(A)
print(C)

flights = {}

###OTHER FUNCTIONS

def loginpage():
    users=["user","admin"]
    passwords=["user123","admin123"]
    username = input("username: ")           
    while username not in users:                                                
        print("Enter a valid username.")
        username = input("username: ")
    password=input("password: ")
    while password not in passwords:                                                
        print("Enter a valid password.")
        password = input("password: ")
    if username == "user" and password == "user123":
        user_page()                                                                                                                      # Call the user-specific function
    elif username == "admin" and password == "admin123":
        admin_page()                                                                                                                     # Call the admin-specific function
    else:
        print("Invalid credentials.")

import sys
def more_options1():                                                                                                                #function to return to main page of user                                                       
    print("")
    
    opt1=input("More Options(Y for yes /N for no): ")                       
    while opt1 not in ["y","Y","N","n"]:
        print("Invalid choice, please enter Y or N")
        opt1=input("More Options(Y/N): ")

    if opt1.upper() == "Y":                                                    
        print("")
        
        user_page()

    elif opt1.upper() == "N":
        print("")
        print("Thank you, GOODBYE")
        print("")
        
        sys.exit()         

def more_options2():                                                                                                              #function to return to main page of admin                                                         
    print("")
    
    opt1=input("More Options(Y for yes /N for no): ")                       
    while opt1 not in ["y","Y","N","n"]:
        print("Invalid choice, please enter Y or N")
        opt1=input("More Options(Y/N): ")

    if opt1.upper() == "Y":                                                    
        print("")
        
        admin_page()

    elif opt1.upper() == "N":
        print("")
        print("Thank you, GOODBYE")
        print("")
        
        sys.exit()

def display_seats(seats):
    print("Seating arrangement:")
    for row in seats:
        for seat in row:
            print(seat, end=' ')
        print()  

###ADMIN FUNCTIONS

def add_flight():
    flight_name = input("Enter the flight name: ")
    if flight_name in flights:
        print("Flight already exists.")
        more_options2()
    
    rows = int(input("Enter the number of rows: "))     
    columns = int(input("Enter the number of columns: "))  

    seats = []
    for row in range(rows):
        row_seats = []
        for column in range(columns):
            row_seats.append('*')
        seats.append(row_seats)
    departure_date = input("Enter departure date: ")
    arrival_time = input("Enter arrival time: ")
    departure_time = input("Enter departure time: ")

    flights[flight_name] = {'seats': seats,'rows': rows,'columns': columns,'departure_date': departure_date,'arrival_time': arrival_time,'departure_time': departure_time}
    
    print(f"Flight '{flight_name}' created successfully")
    more_options2()
    
def modify_flight():
    flight_name = input("Enter the flight name to modify: ")
    if flight_name in flights:
        print("Options for modifying flight:")
        print("1. Set departure date")
        print("2. Set arrival time")
        print("3. Set departure time")
        print("4. Edit seat layout")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            new_departure_date = input("Enter new departure date: ")
            flights[flight_name]['departure_date'] = new_departure_date
            print("Departure date updated.")
            more_options2()
        elif choice == "2":
            new_arrival_time = input("Enter new arrival time: ")
            flights[flight_name]['arrival_time'] = new_arrival_time
            print("Arrival time updated.")
            more_options2()
        elif choice == "3":
            new_departure_time = input("Enter new departure time: ")
            flights[flight_name]['departure_time'] = new_departure_time
            print("Departure time updated.")
            more_options2()
        elif choice == "4":
            num_rows = int(input("Enter the number of rows: "))     
            num_columns = int(input("Enter the number of columns: "))

            num_rows = flights[flight_name]['rows']
            num_columns = flights[flight_name]['columns']

            seats = []
            for row in range(rows):
                row_seats = []
                for column in range(columns):
                    row_seats.append('*')
                seats.append(row_seats)

            flights[flight_name]['seats'] = seats
            print("Seat layout updated.")
            display_seats(seats)
            more_options2()
            
        else:
            print("Invalid choice.")
            more_options2()
    else:
        print(f"Flight '{flight_name}' not found.")
        more_options2()
        
       
            
    
   


def remove_flight():
    if len(flights)<1:
        print("NO FLIGHTS AVAILABLE TO REMOVE")
    else:
        print("Available flights:")
        for flight_name in flights:
            print(f"- {flight_name}") 
        
        flight_name = input("Enter the flight name to remove: ")
        if flight_name in flights:
            del flights[flight_name]
            print(f"Flight '{flight_name}' deleted successfully.")
        else:
            print(f"Flight '{flight_name}' not found.")
    more_options2() 

          
### USER FUNCTIONS

def book_flight():
    if len(flights)<1:
        print("NO FLIGHTS AVAILABLE FOR BOOKING")
    else:
        print("Available flights:")
        for flight_name in flights:
            print(f"--> {flight_name}")

        flight_name = input("Enter the name of the flight you want to book: ")
        if flight_name not in flights:
            print("Flight not found.")
            more_options1()
            return
        

        flight_info = flights[flight_name]
        rows = flight_info['rows']
        columns = flight_info['columns']
        seats = flight_info['seats']
        display_seats(seats)
        row_choice = int(input("Enter the row number you want to book: "))
        while row_choice < 1 or row_choice > rows:
           print("Invalid row  number.")
           row_choice = int(input("Enter the row number you want to book: "))
           
        column_choice = int(input("Enter the column number you want to book: "))   
        while column_choice < 1 or column_choice > columns:
            print("Invalid  column number.")
            column_choice = int(input("Enter the seat number you want to book: ")) 
            
        if seats[row_choice - 1][column_choice - 1] == 'X':
            print("This seat is already booked.")
        else:
            seats[row_choice - 1][column_choice - 1] = 'X'
            print(f"Seat row{row_choice}-seat{column_choice} booked successfully!")
            save_flight_data()
            print(C)
            booker=input("PLEASE WRITE YOUR FULL NAME: ")
            print("here is your ticket, safe travels :)")
            print(f"NAME:{booker}")
            print(f"AIRLINE: {flight_name }")
            print(f"SEAT DETAILS: row{row_choice}-seat{column_choice}")
            save_ticket(flight_name, booker, row_choice, column_choice)
    more_options1()

def cancel_flight():
    if len(flights)<1:
        print("NO FLIGHTS AVAILABLE TO CANCEL")
    else:
        print("Available flights:")
        for flight_name in flights:
            print(f"--> {flight_name}")

        flight_name = input("Enter the name of the flight you want to book: ")
        if flight_name not in flights:
            print("Flight not found.")
            more_options1()
            return
       

        flight_info = flights[flight_name]
        rows = flight_info['rows']
        columns = flight_info['columns']
        seats = flight_info['seats']
        display_seats(seats)
        row_choice = int(input("Enter the row number of your seat: "))
        while row_choice < 1 or row_choice > rows:
           print("Invalid row  number.")
           row_choice = int(input("Enter the row number of your seat: "))
           
        column_choice = int(input("Enter the seat number you want to cancel: "))   
        while column_choice < 1 or column_choice > columns:
            print("Invalid  column number.")
            column_choice = int(input("Enter the seat number you want to cancel: "))
        if seats[row_choice - 1][column_choice - 1] == '*':
            print("This seat is not booked.")
        else:
            seats[row_choice - 1][column_choice - 1] = '*'
            print(f"Seat row{row_choice}-seat{column_choice} cancelled successfully!")
            save_flight_data()
    more_options1()
    
def show_flights():
    if len(flights) < 1:
        print("NO FLIGHTS AVAILABLE")
    else:
        print("Available flights:")
        for flight_name in flights:
            print(f"- {flight_name}")           

        flight_name = input("Enter the name of the flight you want to see: ")
        if flight_name not in flights:
            print("Flight not found.")
            more_options1()
            return

        flight_info = flights[flight_name]
        rows = flight_info['rows']
        columns = flight_info['columns']
        seats = flight_info['seats']
        departure_date = flight_info['departure_date']
        arrival_time = flight_info['arrival_time']
        departure_time = flight_info['departure_time']

        print(f"Flight Name '{flight_name}':")
        print(f"Departure Date: {departure_date}")
        print(f"Arrival Time: {arrival_time}")
        print(f"Departure Time: {departure_time}")
        display_seats(seats)

    more_options1()





##File handling functions


def load_flight_data():
    try:
        with open("flights.txt", "r") as file:
            for line in file:
                data = line.strip().split('/')
                flight_name = data[0]
                row = int(data[1])
                column = int(data[2])
                date = int(data[3])
                departure = str(data[4])
                arrival = str(data[5])
                
                seats = [['*' for i in range(column)] for j in range(row)]
                
                for i in range(5, len(data)):
                    seat_info = data[i].split('-')
                    row_num = int(seat_info[0])
                    col_num = int(seat_info[1])
                    seats[row_num - 1][col_num - 1] = 'X'
                
                flights[flight_name] = {'seats': seats, 'rows': row, 'columns': column,}

    except FileNotFoundError:
        pass

def save_flight_data():
    with open("flights.txt", "a") as file:
        for flight_name, data in flights.items():
            rows = data['rows']
            columns = data['columns']
            seats = data['seats']
            date = data['departure_date']
            arrival = data['arrival_time']
            departure = data['departure_time']
            file.write(f"{flight_name}/{rows}/{columns}/{date}/{departure}/{arrival}")
            for row in range(rows):
                for col in range(columns):
                    if seats[row][col] == 'X':
                        file.write(f"/{row+1}-{col+1}")
            file.write("\n")

def save_ticket(name, booker, row, column):
    with open("tickets.txt", "a") as file:
        file.write(f"{name}/{booker}/{row}/{column}")

    




### MAIN pages functions    


def admin_page():
    print("")
    print(C)
    print("WELCOME ADMIN")
    print("  1.ADD A FLIGHT ")
    print("  2.MODIFY A FLIGHT ")
    print("  3. REMOVE A FLIGHT")
    print("  4.BACK TO LOGIN")
    print("")
    choice = input("Enter the corresponding number of your choice: ")
    print(C) 
    while choice not in ["1","2", "3","4"]:
        print("Invalid choice,Enter a valid option.")
        choice = input("Enter your choice: ")
    if choice == "1":
        add_flight()
        pass
    elif choice == "2":
        modify_flight()
        pass
    elif choice == "3":
        remove_flight()                                             
        pass
    elif choice=="4":
        loginpage()
        pass
    


def user_page():
   print("")
   print(C)
   print("WELCOME USER")
   print("  1.BOOK A TICKET ")
   print("  2. CANCEL A BOOKING")
   print("  3. SHOW AVAILBLE FLIGHTS")
   print("  4.BACK TO LOGIN") 
   print("")
   choice = input("Enter the corresponding number of your choice: ")
   print(C) 
   while choice not in ["1","2", "3","4"]:
       print("Invalid choice,Enter a valid option.")
       choice = input("Enter the corresponding number of your choice: ")
   if choice == "1":
        book_flight()
        pass
   elif choice == "2":
        cancel_flight()
        pass
   elif choice == "3":
        show_flights()
        pass 
   elif choice=="4":
        loginpage()
        pass 




def loginpage():
    users=["user","admin"]
    passwords=["user123","admin123"]
    username = input("username: ")           
    while username not in users:                                                
        print("Enter a valid username.")
        username = input("username: ")
    password=input("password: ")
    while password not in passwords:                                                
        print("Enter a valid password.")
        password = input("password: ")
    if username == "user" and password == "user123":
        user_page()  
    elif username == "admin" and password == "admin123":
        admin_page()  
    else:
        print("Invalid username or password.")
        loginpage()

load_flight_data()
loginpage()       
