'''
#Railway Reservation Management System
#OOP(Object-Oriented Programming)
class Passenger:

    def __init__(self, passenger_id, name, age, gender):

        self.passenger_id = passenger_id
        self.name = name
        self.age = age
        self.gender = gender

passenger1 = Passenger("p1", "Eramani" , 23 , "Female")
    
print(passenger1.passenger_id)
print(passenger1.name)
print(passenger1.age)
print(passenger1.gender)
'''
# ============================================================
# RAILWAY RESERVATION SYSTEM
# ============================================================
#
# CONCEPTS USED:
#
# 1. OOP
#    - Passenger Class
#    - Train Class
#    - Ticket Class
#    - RailwayReservationSystem Class
#
# 2. Lists
#    - Booked Passengers
#    - Waiting List
#
# 3. Dictionaries
#    - Trains
#    - Passengers
#    - Tickets
#
# 4. Functions
#    - Add Train
#    - Register Passenger
#    - Search Train
#    - Book Ticket
#    - Calculate Fare
#    - Cancel Ticket
#    - Reallocate Seat
#
# 5. Conditional Statements
#    - Seat Available
#    - Train Found
#    - Ticket Found
#
# 6. Loops
#    - for Loop
#    - while Loop
#
# 7. Exception Handling
#    - try-except
#
# 8. Basic Modules
#    - datetime
#
# 9. TXT File Handling
#    - railway_records.txt
#
# ============================================================


# ============================================================
# BASIC MODULES
# ============================================================

from datetime import datetime


# ============================================================
# TXT FILE HANDLING
# ============================================================

def save_to_file(data):
    """
    This function saves railway activities
    into railway_records.txt
    """

    try:
        with open("railway_records.txt", "a") as file:
            file.write(data + "\n")

    except Exception as error:
        print("File Error:", error)


# ============================================================
# OOP
# ============================================================


# ============================================================
# PASSENGER CLASS
# ============================================================

class Passenger:

    def __init__(self, passenger_id, name, age, gender):

        self.passenger_id = passenger_id
        self.name = name
        self.age = age
        self.gender = gender


    def display_details(self):

        print("\n----- PASSENGER DETAILS -----")

        print("Passenger ID :", self.passenger_id)
        print("Name         :", self.name)
        print("Age          :", self.age)
        print("Gender       :", self.gender)


# ============================================================
# TRAIN CLASS
# ============================================================

class Train:

    def __init__(
        self,
        train_no,
        name,
        source,
        destination,
        total_seats,
        fare
    ):

        self.train_no = train_no
        self.name = name
        self.source = source
        self.destination = destination
        self.total_seats = total_seats
        self.fare = fare


        # ====================================================
        # LISTS
        # ====================================================

        # List to store confirmed passengers
        self.booked_passengers = []

        # List to store waiting passengers
        self.waiting_list = []


    # ========================================================
    # FUNCTIONS
    # DISPLAY TRAIN
    # ========================================================

    def display_train(self):

        print("\n==============================")
        print("TRAIN DETAILS")
        print("==============================")

        print("Train Number :", self.train_no)
        print("Train Name   :", self.name)
        print("Source       :", self.source)
        print("Destination  :", self.destination)
        print("Total Seats  :", self.total_seats)
        print("Fare         :", self.fare)

        print(
            "Available Seats :",
            self.available_seats()
        )


    # ========================================================
    # FUNCTIONS
    # SEAT AVAILABILITY
    # ========================================================

    def available_seats(self):

        available = (
            self.total_seats
            -
            len(self.booked_passengers)
        )

        return available


    # ========================================================
    # FUNCTIONS
    # TICKET BOOKING
    # ========================================================

    def book_ticket(self, passenger):


        # ====================================================
        # CONDITIONAL STATEMENT
        # SEAT AVAILABLE
        # ====================================================

        if self.available_seats() > 0:


            # Add passenger to booked passengers list

            self.booked_passengers.append(
                passenger
            )


            print(
                "\nTicket Booked Successfully!"
            )


            return "CONFIRMED"


        else:


            # Add passenger to waiting list

            self.waiting_list.append(
                passenger
            )


            print(
                "\nSeats Not Available!"
            )

            print(
                "Passenger Added to Waiting List."
            )


            return "WAITING"


    # ========================================================
    # FUNCTIONS
    # TICKET CANCELLATION
    # ========================================================

    def cancel_ticket(self, passenger_id):


        # ====================================================
        # FOR LOOP
        # ====================================================

        for passenger in self.booked_passengers:


            # =================================================
            # CONDITIONAL STATEMENT
            # =================================================

            if passenger.passenger_id == passenger_id:


                # Remove passenger

                self.booked_passengers.remove(
                    passenger
                )


                print(
                    "\nTicket Cancelled Successfully!"
                )


                # Reallocate seat

                return self.reallocate_seat()


        return None


    # ========================================================
    # FUNCTIONS
    # SEAT REALLOCATION
    # ========================================================

    def reallocate_seat(self):


        # Check waiting list

        if len(self.waiting_list) > 0:


            # Get first passenger from waiting list

            passenger = self.waiting_list.pop(0)


            # Add passenger to confirmed list

            self.booked_passengers.append(
                passenger
            )


            print(
                "\nSeat Reallocated!"
            )


            print(
                passenger.name,
                "moved from Waiting to Confirmed."
            )


            return passenger


        return None


    # ========================================================
    # FUNCTIONS
    # DISPLAY BOOKED PASSENGERS
    # ========================================================

    def display_booked_passengers(self):

        print("\n----- BOOKED PASSENGERS -----")


        if len(self.booked_passengers) == 0:

            print(
                "No Confirmed Passengers."
            )


        else:


            # FOR LOOP

            for passenger in self.booked_passengers:

                print(
                    passenger.passenger_id,
                    "-",
                    passenger.name
                )


    # ========================================================
    # FUNCTIONS
    # DISPLAY WAITING LIST
    # ========================================================

    def display_waiting_list(self):

        print("\n----- WAITING LIST -----")


        # CONDITIONAL STATEMENT

        if len(self.waiting_list) == 0:

            print(
                "Waiting List is Empty."
            )


        else:


            # FOR LOOP

            position = 1

            for passenger in self.waiting_list:

                print(
                    "Position:",
                    position,
                    "|",
                    passenger.passenger_id,
                    "-",
                    passenger.name
                )

                position += 1


# ============================================================
# TICKET CLASS
# ============================================================

class Ticket:


    # Class Variable

    ticket_counter = 1001


    def __init__(
        self,
        passenger,
        train,
        status
    ):


        self.ticket_no = (
            Ticket.ticket_counter
        )


        Ticket.ticket_counter += 1


        self.passenger = passenger

        self.train = train

        self.status = status


        # ====================================================
        # DATETIME MODULE
        # ====================================================

        self.booking_date = datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )


    # ========================================================
    # FUNCTION
    # DISPLAY TICKET
    # ========================================================

    def display_ticket(self):

        print("\n==============================")
        print("RAILWAY TICKET")
        print("==============================")

        print("Ticket Number :", self.ticket_no)

        print("Passenger ID  :",
              self.passenger.passenger_id)

        print("Passenger Name :",
              self.passenger.name)

        print("Train Number :",
              self.train.train_no)

        print("Train Name :",
              self.train.name)

        print("Source :",
              self.train.source)

        print("Destination :",
              self.train.destination)

        print("Fare : Rs.",
              self.train.fare)

        print("Status :",
              self.status)

        print("Booking Date :",
              self.booking_date)


# ============================================================
# RAILWAY RESERVATION SYSTEM CLASS
# ============================================================

class RailwayReservationSystem:


    def __init__(self):


        # ====================================================
        # DICTIONARIES
        # ====================================================


        # Dictionary to store trains

        self.trains = {}


        # Dictionary to store passengers

        self.passengers = {}


        # Dictionary to store tickets

        self.tickets = {}


        # Passenger counter

        self.passenger_counter = 1


    # ========================================================
    # FUNCTION
    # ADD TRAIN
    # ========================================================

    def add_train(self):


        # ====================================================
        # EXCEPTION HANDLING
        # ====================================================

        try:

            print("\n----- ADD TRAIN -----")


            train_no = input(
                "Enter Train Number: "
            )


            # CONDITIONAL STATEMENT

            if train_no in self.trains:

                print(
                    "Train Already Exists!"
                )

                return


            name = input(
                "Enter Train Name: "
            )


            source = input(
                "Enter Source: "
            )


            destination = input(
                "Enter Destination: "
            )


            total_seats = int(
                input(
                    "Enter Total Seats: "
                )
            )


            fare = float(
                input(
                    "Enter Fare: "
                )
            )


            # =================================================
            # OBJECT CREATION
            # =================================================

            train = Train(

                train_no,
                name,
                source,
                destination,
                total_seats,
                fare

            )


            # =================================================
            # DICTIONARY
            # STORE TRAIN
            # =================================================

            self.trains[train_no] = train


            print(
                "\nTrain Added Successfully!"
            )


            # TXT FILE HANDLING

            save_to_file(

                "Train Added: "
                + train_no
                + " - "
                + name

            )


        except ValueError:

            print(
                "Invalid Input!"
            )


    # ========================================================
    # FUNCTION
    # DISPLAY ALL TRAINS
    # ========================================================

    def display_all_trains(self):


        if len(self.trains) == 0:

            print(
                "No Trains Available!"
            )


        else:


            # FOR LOOP

            for train in self.trains.values():

                train.display_train()


    # ========================================================
    # FUNCTION
    # PASSENGER REGISTRATION
    # ========================================================

    def register_passenger(self):


        try:

            print(
                "\n----- PASSENGER REGISTRATION -----"
            )


            name = input(
                "Enter Passenger Name: "
            )


            age = int(
                input(
                    "Enter Passenger Age: "
                )
            )


            gender = input(
                "Enter Gender: "
            )


            # Create Passenger ID

            passenger_id = (
                "P"
                +
                str(self.passenger_counter)
            )


            # Increase counter

            self.passenger_counter += 1


            # =================================================
            # OBJECT CREATION
            # =================================================

            passenger = Passenger(

                passenger_id,
                name,
                age,
                gender

            )


            # =================================================
            # DICTIONARY
            # STORE PASSENGER
            # =================================================

            self.passengers[
                passenger_id
            ] = passenger


            print(
                "\nPassenger Registered Successfully!"
            )


            print(
                "Passenger ID:",
                passenger_id
            )


            # TXT FILE HANDLING

            save_to_file(

                "Passenger Registered: "
                +
                passenger_id
                +
                " - "
                +
                name

            )


            return passenger


        except ValueError:

            print(
                "Invalid Age!"
            )


            return None


    # ========================================================
    # FUNCTION
    # TRAIN SEARCH
    # ========================================================

    def search_train(self):


        source = input(
            "Enter Source: "
        )


        destination = input(
            "Enter Destination: "
        )


        found = False


        # ====================================================
        # FOR LOOP
        # ====================================================

        for train in self.trains.values():


            # =================================================
            # CONDITIONAL STATEMENT
            # =================================================

            if (

                train.source.lower()
                ==
                source.lower()

                and

                train.destination.lower()
                ==
                destination.lower()

            ):


                train.display_train()


                found = True


        if found == False:

            print(
                "No Train Found!"
            )


    # ========================================================
    # FUNCTION
    # CHECK SEAT AVAILABILITY
    # ========================================================

    def check_seat_availability(self):


        train_no = input(
            "Enter Train Number: "
        )


        # CONDITIONAL STATEMENT

        if train_no in self.trains:


            train = self.trains[train_no]


            print(
                "\nAvailable Seats:",
                train.available_seats()
            )


        else:

            print(
                "Train Not Found!"
            )


    # ========================================================
    # FUNCTION
    # TICKET BOOKING
    # ========================================================

    def book_ticket(self):


        print(
            "\n----- TICKET BOOKING -----"
        )


        # Display Trains

        for train in self.trains.values():

            print(

                train.train_no,
                "-",
                train.name

            )


        train_no = input(
            "Enter Train Number: "
        )


        # CONDITIONAL STATEMENT

        if train_no not in self.trains:

            print(
                "Train Not Found!"
            )

            return


        # Get train object

        train = self.trains[train_no]


        # Register Passenger

        passenger = self.register_passenger()


        if passenger is None:

            return


        # Book Ticket

        status = train.book_ticket(
            passenger
        )


        # ====================================================
        # OBJECT CREATION
        # ====================================================

        ticket = Ticket(

            passenger,
            train,
            status

        )


        # ====================================================
        # DICTIONARY
        # STORE TICKET
        # ====================================================

        self.tickets[
            ticket.ticket_no
        ] = ticket


        # Display Ticket

        ticket.display_ticket()


        # TXT FILE HANDLING

        save_to_file(

            "Ticket Booked: "
            +
            str(ticket.ticket_no)
            +
            " | Passenger: "
            +
            passenger.name
            +
            " | Status: "
            +
            status

        )


    # ========================================================
    # FUNCTION
    # FARE CALCULATION
    # ========================================================

    def calculate_fare(self):


        try:

            train_no = input(
                "Enter Train Number: "
            )


            if train_no not in self.trains:

                print(
                    "Train Not Found!"
                )

                return


            number_of_passengers = int(

                input(
                    "Enter Number of Passengers: "
                )

            )


            train = self.trains[
                train_no
            ]


            # =================================================
            # ARITHMETIC OPERATOR
            # =================================================

            total_fare = (

                train.fare
                *
                number_of_passengers

            )


            print(
                "\nFare Per Passenger:",
                train.fare
            )


            print(
                "Total Fare:",
                total_fare
            )


        except ValueError:

            print(
                "Invalid Input!"
            )


    # ========================================================
    # FUNCTION
    # DISPLAY WAITING LIST
    # ========================================================

    def show_waiting_list(self):


        train_no = input(
            "Enter Train Number: "
        )


        if train_no in self.trains:


            train = self.trains[
                train_no
            ]


            train.display_waiting_list()


        else:

            print(
                "Train Not Found!"
            )


    # ========================================================
    # FUNCTION
    # TICKET CANCELLATION
    # ========================================================

    def cancel_ticket(self):


        try:

            ticket_no = int(

                input(
                    "Enter Ticket Number: "
                )

            )


            # =================================================
            # CONDITIONAL STATEMENT
            # TICKET FOUND
            # =================================================

            if ticket_no not in self.tickets:

                print(
                    "Ticket Not Found!"
                )

                return


            # Get Ticket Object

            ticket = self.tickets[
                ticket_no
            ]


            train = ticket.train


            passenger_id = (

                ticket.passenger.passenger_id

            )


            # If confirmed ticket

            if ticket.status == "CONFIRMED":


                promoted_passenger = train.cancel_ticket(

                    passenger_id

                )


                # Update waiting passenger ticket

                if promoted_passenger is not None:


                    for other_ticket in self.tickets.values():

                        if (

                            other_ticket.passenger.passenger_id
                            ==
                            promoted_passenger.passenger_id

                        ):

                            other_ticket.status = "CONFIRMED"

                            break


            # If waiting ticket

            elif ticket.status == "WAITING":


                for passenger in train.waiting_list:


                    if (

                        passenger.passenger_id
                        ==
                        passenger_id

                    ):


                        train.waiting_list.remove(
                            passenger
                        )


                        print(
                            "Waiting Ticket Cancelled!"
                        )


                        break


            # Delete Ticket

            del self.tickets[
                ticket_no
            ]


            print(
                "Ticket Cancelled Successfully!"
            )


            # TXT FILE HANDLING

            save_to_file(

                "Ticket Cancelled: "
                +
                str(ticket_no)

            )


        except ValueError:

            print(
                "Invalid Ticket Number!"
            )


    # ========================================================
    # FUNCTION
    # TICKET SUMMARY
    # ========================================================

    def ticket_summary(self):


        print(
            "\n----- TICKET SUMMARY -----"
        )


        if len(self.tickets) == 0:

            print(
                "No Tickets Available!"
            )


        else:


            # FOR LOOP

            for ticket in self.tickets.values():

                print("\nTicket Number:",
                      ticket.ticket_no)

                print("Passenger:",
                      ticket.passenger.name)

                print("Train:",
                      ticket.train.name)

                print("Status:",
                      ticket.status)

                print("Fare:",
                      ticket.train.fare)


# ============================================================
# MAIN FUNCTION
# ============================================================

def main():


    # ========================================================
    # OBJECT CREATION
    # ========================================================

    system = RailwayReservationSystem()


    # ========================================================
    # DEFAULT TRAIN OBJECTS
    # ========================================================

    train1 = Train(

        "12001",
        "Hyderabad Express",
        "Hyderabad",
        "Bangalore",
        3,
        500

    )


    train2 = Train(

        "12002",
        "Godavari Express",
        "Hyderabad",
        "Visakhapatnam",
        3,
        600

    )


    train3 = Train(

        "12003",
        "Charminar Express",
        "Hyderabad",
        "Chennai",
        3,
        700

    )


    # ========================================================
    # DICTIONARY
    # STORE DEFAULT TRAINS
    # ========================================================

    system.trains[
        train1.train_no
    ] = train1


    system.trains[
        train2.train_no
    ] = train2


    system.trains[
        train3.train_no
    ] = train3


    # ========================================================
    # WHILE LOOP
    # MAIN MENU
    # ========================================================

    while True:


        print("\n====================================")

        print(
            "RAILWAY RESERVATION SYSTEM"
        )

        print("====================================")


        print("1. Add Train")

        print("2. Display All Trains")

        print("3. Passenger Registration")

        print("4. Train Search")

        print("5. Seat Availability")

        print("6. Ticket Booking")

        print("7. Fare Calculation")

        print("8. Waiting List")

        print("9. Ticket Cancellation")

        print("10. Ticket Summary")

        print("11. Exit")


        choice = input(
            "\nEnter Your Choice: "
        )


        # ====================================================
        # CONDITIONAL STATEMENTS
        # MENU
        # ====================================================

        if choice == "1":

            system.add_train()


        elif choice == "2":

            system.display_all_trains()


        elif choice == "3":

            system.register_passenger()


        elif choice == "4":

            system.search_train()


        elif choice == "5":

            system.check_seat_availability()


        elif choice == "6":

            system.book_ticket()


        elif choice == "7":

            system.calculate_fare()


        elif choice == "8":

            system.show_waiting_list()


        elif choice == "9":

            system.cancel_ticket()


        elif choice == "10":

            system.ticket_summary()


        elif choice == "11":

            print(
                "\nThank You!"
            )

            print(
                "Railway Reservation System Closed."
            )

            break


        else:

            print(
                "Invalid Choice!"
            )


# ============================================================
# PROGRAM STARTING POINT
# ============================================================

if __name__ == "__main__":

    main()











 











