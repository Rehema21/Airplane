import csv
import random

#  maximum number of seats on the plane
MAX_SEATS = 100


csv_file_path = 'records.csv'

# Read existing bookings and calculate remaining available seats
def get_available_seats():
    pass
#     try:
#         with open(csv_file_path, 'r') as file:
#             reader = csv.reader(file)
#             bookings = list(reader)
#             booked_seats = sum(int(row[3]) for row in bookings[1:])  # Assuming 'num_tickets' is in the 4th column
#             available_seats = MAX_SEATS - booked_seats
#             return available_seats
#     except FileNotFoundError:
#         return MAX_SEATS
#
# # Function to book tickets for a customer
def book_ticket(first_name, last_name, passport_number, num_tickets):
    available_seats = get_available_seats()

    # Check if there are enough available seats
    if num_tickets > available_seats:
        print(f"Error: Not enough seats available. Only {available_seats} seats left.")
        return

    # Generate a random ticket number for the booking
    ticket_number = random.randint(1000, 9999)

    # Append booking details to the CSV file
    with open(csv_file_path, 'a', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name', 'passport_number', 'num_tickets', 'ticket_number']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header if the file is empty
        csvfile.seek(0, 2)  # Move to the end of the file
        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow({
            'first_name': first_name,
            'last_name': last_name,
            'passport_number': passport_number,
            'num_tickets': num_tickets,
            'ticket_number': ticket_number
        })

    print(f"Booking successful! Ticket number: {ticket_number}. Seats remaining: {available_seats - num_tickets}")

def cancel_ticket():
    pass

def view_available_sits():
    available_seats = get_available_seats()
    print(f"Seats remaining: {available_seats}")

def update_booking():
    pass

def ticket_information():
    pass

menu = {
    '1': "Book a Ticket.",
    '2': "Cancel Ticket.",
    '3': "View available seats.",
    '4': "Update a booking",
    '5': "View Ticket information",
    '6': "Quit"
}
# MENU
while True:
    # Get and sort the keys of the menu
    options = sorted(menu.keys())

    # Display the menu
    for entry in options:
        print(entry, menu[entry])

    # Get user input
    selection = input("Please Select: ")

    if selection == '1':
        book_ticket()
    elif selection == '2':
        cancel_ticket()
    elif selection == '3':
        view_available_sits()
    elif selection == '4':
        update_booking()
    elif selection == '5':
        ticket_information()

    elif selection == '6':
        print("Exiting the program...")
        break
    else:
        print("Unknown Option Selected!")

# Function to display remaining seats
# def display_remaining_seats():
#     available_seats = get_available_seats()
#     print(f"Seats remaining: {available_seats}")


# if __name__ == '__main__':
#     # Simulate customer input for booking
#     first_name = input("Enter first name: ")
#     last_name = input("Enter last name: ")
#     passport_number = input("Enter passport number: ")
#     num_tickets = int(input("Enter number of tickets to book: "))
#
#     # Book tickets
#     book_ticket(first_name, last_name, passport_number, num_tickets)
#
#     # Display the remaining seats
#     display_remaining_seats()
