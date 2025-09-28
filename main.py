#!/usr/bin/env python3
"""
Hotel Management System - Command Line Interface
"""
import sys
from datetime import datetime, timedelta
from hotel_manager import HotelManager


class HotelCLI:
    """Command line interface for the hotel management system"""
    
    def __init__(self):
        self.hotel_manager = HotelManager()
    
    def run(self):
        """Main CLI loop"""
        print("=" * 50)
        print("Welcome to Hotel Management System v1.1")
        print("=" * 50)
        
        while True:
            self.show_main_menu()
            choice = input("\nEnter your choice: ").strip()
            
            if choice == "1":
                self.customer_menu()
            elif choice == "2":
                self.room_menu()
            elif choice == "3":
                self.booking_menu()
            elif choice == "4":
                self.review_menu()
            elif choice == "5":
                self.show_statistics()
            elif choice == "6":
                print("Thank you for using Hotel Management System!")
                break
            else:
                print("Invalid choice. Please try again.")
    
    def show_main_menu(self):
        """Display main menu"""
        print("\n" + "=" * 30)
        print("MAIN MENU")
        print("=" * 30)
        print("1. Customer Management")
        print("2. Room Management")
        print("3. Booking Management")
        print("4. Review Management")
        print("5. Show Statistics")
        print("6. Exit")
    
    def customer_menu(self):
        """Customer management menu"""
        while True:
            print("\n" + "-" * 30)
            print("CUSTOMER MANAGEMENT")
            print("-" * 30)
            print("1. Add Customer")
            print("2. List Customers")
            print("3. View Customer Details")
            print("4. Update Customer")
            print("5. Back to Main Menu")
            
            choice = input("\nEnter your choice: ").strip()
            
            if choice == "1":
                self.add_customer()
            elif choice == "2":
                self.list_customers()
            elif choice == "3":
                self.view_customer_details()
            elif choice == "4":
                self.update_customer()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")
    
    def room_menu(self):
        """Room management menu"""
        while True:
            print("\n" + "-" * 30)
            print("ROOM MANAGEMENT")
            print("-" * 30)
            print("1. Add Room")
            print("2. List All Rooms")
            print("3. List Available Rooms")
            print("4. Update Room Price")
            print("5. Toggle Room Availability")
            print("6. Back to Main Menu")
            
            choice = input("\nEnter your choice: ").strip()
            
            if choice == "1":
                self.add_room()
            elif choice == "2":
                self.list_rooms(available_only=False)
            elif choice == "3":
                self.list_rooms(available_only=True)
            elif choice == "4":
                self.update_room_price()
            elif choice == "5":
                self.toggle_room_availability()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")
    
    def booking_menu(self):
        """Booking management menu"""
        while True:
            print("\n" + "-" * 30)
            print("BOOKING MANAGEMENT")
            print("-" * 30)
            print("1. Create Booking")
            print("2. List All Bookings")
            print("3. View Booking Details")
            print("4. Customer Bookings")
            print("5. Check In")
            print("6. Check Out")
            print("7. Cancel Booking")
            print("8. Back to Main Menu")
            
            choice = input("\nEnter your choice: ").strip()
            
            if choice == "1":
                self.create_booking()
            elif choice == "2":
                self.list_bookings()
            elif choice == "3":
                self.view_booking_details()
            elif choice == "4":
                self.view_customer_bookings()
            elif choice == "5":
                self.check_in_booking()
            elif choice == "6":
                self.check_out_booking()
            elif choice == "7":
                self.cancel_booking()
            elif choice == "8":
                break
            else:
                print("Invalid choice. Please try again.")
    
    def review_menu(self):
        """Review management menu"""
        while True:
            print("\n" + "-" * 30)
            print("REVIEW MANAGEMENT")
            print("-" * 30)
            print("1. Add Review")
            print("2. List All Reviews")
            print("3. View Reviews for Booking")
            print("4. Back to Main Menu")
            
            choice = input("\nEnter your choice: ").strip()
            
            if choice == "1":
                self.add_review()
            elif choice == "2":
                self.list_reviews()
            elif choice == "3":
                self.view_booking_reviews()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")
    
    def add_customer(self):
        """Add a new customer"""
        try:
            name = input("Enter customer name: ").strip()
            email = input("Enter customer email: ").strip()
            phone = input("Enter customer phone: ").strip()
            
            if not all([name, email, phone]):
                print("Error: All fields are required.")
                return
            
            customer = self.hotel_manager.add_customer(name, email, phone)
            print(f"Customer added successfully! ID: {customer.customer_id}")
        except Exception as e:
            print(f"Error adding customer: {e}")
    
    def list_customers(self):
        """List all customers"""
        customers = self.hotel_manager.list_customers()
        if not customers:
            print("No customers found.")
            return
        
        print(f"\n{'ID':<37} {'Name':<20} {'Email':<25} {'Phone':<15}")
        print("-" * 97)
        for customer in customers:
            print(f"{customer.customer_id:<37} {customer.name:<20} {customer.email:<25} {customer.phone:<15}")
    
    def view_customer_details(self):
        """View customer details"""
        customer_id = input("Enter customer ID: ").strip()
        customer = self.hotel_manager.get_customer(customer_id)
        
        if not customer:
            print("Customer not found.")
            return
        
        print(f"\nCustomer Details:")
        print(f"ID: {customer.customer_id}")
        print(f"Name: {customer.name}")
        print(f"Email: {customer.email}")
        print(f"Phone: {customer.phone}")
        print(f"Created: {customer.created_at}")
        
        # Show customer bookings
        bookings = self.hotel_manager.get_customer_bookings(customer_id)
        print(f"\nBookings ({len(bookings)}):")
        if bookings:
            for booking in bookings:
                print(f"  - Booking {booking.booking_id[:8]}... Room {booking.room_number} ({booking.status})")
    
    def update_customer(self):
        """Update customer information"""
        customer_id = input("Enter customer ID: ").strip()
        customer = self.hotel_manager.get_customer(customer_id)
        
        if not customer:
            print("Customer not found.")
            return
        
        print(f"Current customer: {customer.name} ({customer.email})")
        name = input("Enter new name (or press Enter to keep current): ").strip()
        email = input("Enter new email (or press Enter to keep current): ").strip()
        phone = input("Enter new phone (or press Enter to keep current): ").strip()
        
        try:
            updated_customer = self.hotel_manager.update_customer(
                customer_id, 
                name if name else None,
                email if email else None,
                phone if phone else None
            )
            if updated_customer:
                print("Customer updated successfully!")
        except Exception as e:
            print(f"Error updating customer: {e}")
    
    def add_room(self):
        """Add a new room"""
        try:
            room_number = input("Enter room number: ").strip()
            room_type = input("Enter room type (Single/Double/Suite): ").strip()
            price = float(input("Enter price per night: ").strip())
            capacity = int(input("Enter room capacity: ").strip())
            
            room = self.hotel_manager.add_room(room_number, room_type, price, capacity)
            print(f"Room {room.room_number} added successfully!")
        except ValueError as e:
            print(f"Error: Invalid input - {e}")
        except Exception as e:
            print(f"Error adding room: {e}")
    
    def list_rooms(self, available_only=False):
        """List rooms"""
        rooms = self.hotel_manager.list_rooms(available_only)
        if not rooms:
            status = "available" if available_only else ""
            print(f"No {status} rooms found.")
            return
        
        title = "Available Rooms" if available_only else "All Rooms"
        print(f"\n{title}:")
        print(f"{'Room #':<8} {'Type':<10} {'Price/Night':<12} {'Capacity':<9} {'Status':<12}")
        print("-" * 55)
        
        for room in rooms:
            status = "Available" if room.is_available else "Occupied"
            print(f"{room.room_number:<8} {room.room_type:<10} ${room.price_per_night:<11.2f} {room.capacity:<9} {status:<12}")
    
    def update_room_price(self):
        """Update room price"""
        room_number = input("Enter room number: ").strip()
        room = self.hotel_manager.get_room(room_number)
        
        if not room:
            print("Room not found.")
            return
        
        try:
            print(f"Current price: ${room.price_per_night}")
            new_price = float(input("Enter new price per night: ").strip())
            
            updated_room = self.hotel_manager.update_room_price(room_number, new_price)
            if updated_room:
                print(f"Room {room_number} price updated to ${new_price}!")
        except ValueError:
            print("Error: Invalid price format.")
        except Exception as e:
            print(f"Error updating room price: {e}")
    
    def toggle_room_availability(self):
        """Toggle room availability"""
        room_number = input("Enter room number: ").strip()
        room = self.hotel_manager.get_room(room_number)
        
        if not room:
            print("Room not found.")
            return
        
        new_status = not room.is_available
        updated_room = self.hotel_manager.update_room_availability(room_number, new_status)
        if updated_room:
            status = "Available" if new_status else "Unavailable"
            print(f"Room {room_number} is now {status}!")
    
    def create_booking(self):
        """Create a new booking"""
        try:
            # Show available rooms first
            print("\nAvailable Rooms:")
            self.list_rooms(available_only=True)
            
            customer_id = input("\nEnter customer ID: ").strip()
            room_number = input("Enter room number: ").strip()
            
            print("Enter dates in YYYY-MM-DD format:")
            check_in = input("Check-in date: ").strip()
            check_out = input("Check-out date: ").strip()
            
            booking = self.hotel_manager.create_booking(customer_id, room_number, check_in, check_out)
            if booking:
                print(f"Booking created successfully!")
                print(f"Booking ID: {booking.booking_id}")
                print(f"Total Price: ${booking.total_price}")
        except Exception as e:
            print(f"Error creating booking: {e}")
    
    def list_bookings(self):
        """List all bookings"""
        bookings = self.hotel_manager.list_bookings()
        if not bookings:
            print("No bookings found.")
            return
        
        print(f"\nAll Bookings:")
        print(f"{'Booking ID':<37} {'Customer ID':<37} {'Room':<6} {'Check-in':<12} {'Check-out':<12} {'Status':<12} {'Price':<10}")
        print("-" * 140)
        
        for booking in bookings:
            print(f"{booking.booking_id:<37} {booking.customer_id:<37} {booking.room_number:<6} {booking.check_in_date[:10]:<12} {booking.check_out_date[:10]:<12} {booking.status:<12} ${booking.total_price:<9}")
    
    def view_booking_details(self):
        """View booking details"""
        booking_id = input("Enter booking ID: ").strip()
        booking = self.hotel_manager.get_booking(booking_id)
        
        if not booking:
            print("Booking not found.")
            return
        
        customer = self.hotel_manager.get_customer(booking.customer_id)
        room = self.hotel_manager.get_room(booking.room_number)
        
        print(f"\nBooking Details:")
        print(f"Booking ID: {booking.booking_id}")
        print(f"Customer: {customer.name if customer else 'Unknown'} ({booking.customer_id})")
        print(f"Room: {booking.room_number} ({room.room_type if room else 'Unknown'})")
        print(f"Check-in: {booking.check_in_date}")
        print(f"Check-out: {booking.check_out_date}")
        print(f"Total Price: ${booking.total_price}")
        print(f"Status: {booking.status}")
        print(f"Created: {booking.created_at}")
    
    def view_customer_bookings(self):
        """View bookings for a specific customer"""
        customer_id = input("Enter customer ID: ").strip()
        customer = self.hotel_manager.get_customer(customer_id)
        
        if not customer:
            print("Customer not found.")
            return
        
        bookings = self.hotel_manager.get_customer_bookings(customer_id)
        
        print(f"\nBookings for {customer.name}:")
        if not bookings:
            print("No bookings found for this customer.")
            return
        
        for booking in bookings:
            print(f"  - {booking.booking_id[:8]}... Room {booking.room_number} ({booking.status}) - ${booking.total_price}")
    
    def check_in_booking(self):
        """Check in a booking"""
        booking_id = input("Enter booking ID: ").strip()
        booking = self.hotel_manager.check_in_booking(booking_id)
        
        if booking:
            print(f"Booking {booking_id[:8]}... checked in successfully!")
        else:
            print("Booking not found or cannot be checked in.")
    
    def check_out_booking(self):
        """Check out a booking"""
        booking_id = input("Enter booking ID: ").strip()
        booking = self.hotel_manager.check_out_booking(booking_id)
        
        if booking:
            print(f"Booking {booking_id[:8]}... checked out successfully!")
        else:
            print("Booking not found or cannot be checked out.")
    
    def cancel_booking(self):
        """Cancel a booking"""
        booking_id = input("Enter booking ID: ").strip()
        booking = self.hotel_manager.cancel_booking(booking_id)
        
        if booking:
            print(f"Booking {booking_id[:8]}... cancelled successfully!")
        else:
            print("Booking not found or cannot be cancelled.")
    
    def add_review(self):
        """Add a review"""
        try:
            customer_id = input("Enter customer ID: ").strip()
            booking_id = input("Enter booking ID: ").strip()
            rating = int(input("Enter rating (1-5): ").strip())
            comment = input("Enter comment: ").strip()
            
            review = self.hotel_manager.add_review(customer_id, booking_id, rating, comment)
            if review:
                print(f"Review added successfully! ID: {review.review_id}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error adding review: {e}")
    
    def list_reviews(self):
        """List all reviews"""
        reviews = self.hotel_manager.list_reviews()
        if not reviews:
            print("No reviews found.")
            return
        
        print(f"\nAll Reviews:")
        print(f"{'Review ID':<37} {'Customer ID':<37} {'Rating':<7} {'Comment':<50}")
        print("-" * 135)
        
        for review in reviews:
            comment = review.comment[:47] + "..." if len(review.comment) > 50 else review.comment
            print(f"{review.review_id:<37} {review.customer_id:<37} {review.rating}/5    {comment:<50}")
    
    def view_booking_reviews(self):
        """View reviews for a booking"""
        booking_id = input("Enter booking ID: ").strip()
        reviews = self.hotel_manager.get_booking_reviews(booking_id)
        
        if not reviews:
            print("No reviews found for this booking.")
            return
        
        print(f"\nReviews for booking {booking_id[:8]}...:")
        for review in reviews:
            customer = self.hotel_manager.get_customer(review.customer_id)
            print(f"  - {customer.name if customer else 'Unknown'}: {review.rating}/5 stars")
            print(f"    \"{review.comment}\"")
            print(f"    ({review.created_at[:10]})")
    
    def show_statistics(self):
        """Show hotel statistics"""
        customers = self.hotel_manager.list_customers()
        rooms = self.hotel_manager.list_rooms()
        available_rooms = self.hotel_manager.list_rooms(available_only=True)
        bookings = self.hotel_manager.list_bookings()
        reviews = self.hotel_manager.list_reviews()
        avg_rating = self.hotel_manager.get_average_rating()
        
        # Calculate booking statistics
        active_bookings = [b for b in bookings if b.status in ['confirmed', 'checked_in']]
        total_revenue = sum(b.total_price for b in bookings if b.status != 'cancelled')
        
        print(f"\n" + "=" * 40)
        print("HOTEL STATISTICS")
        print("=" * 40)
        print(f"Total Customers: {len(customers)}")
        print(f"Total Rooms: {len(rooms)}")
        print(f"Available Rooms: {len(available_rooms)}")
        print(f"Total Bookings: {len(bookings)}")
        print(f"Active Bookings: {len(active_bookings)}")
        print(f"Total Reviews: {len(reviews)}")
        print(f"Average Rating: {avg_rating}/5.0")
        print(f"Total Revenue: ${total_revenue:.2f}")
        print(f"Occupancy Rate: {((len(rooms) - len(available_rooms)) / len(rooms) * 100) if rooms else 0:.1f}%")


def main():
    """Main entry point"""
    cli = HotelCLI()
    try:
        cli.run()
    except KeyboardInterrupt:
        print("\n\nExiting Hotel Management System. Goodbye!")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()