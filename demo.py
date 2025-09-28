#!/usr/bin/env python3
"""
Hotel Management System - Quick Demo
Demonstrates the core functionality without user interaction
"""
from hotel_manager import HotelManager
from datetime import datetime, timedelta

def demo_hotel_system():
    """Demonstrate the hotel management system"""
    print("=" * 60)
    print("HOTEL MANAGEMENT SYSTEM v1.1 - DEMO")
    print("=" * 60)
    
    # Initialize the system
    hotel = HotelManager()
    
    print("\n1. INITIAL SYSTEM STATE")
    print("-" * 30)
    rooms = hotel.list_rooms()
    print(f"Available rooms: {len([r for r in rooms if r.is_available])}")
    print(f"Total rooms: {len(rooms)}")
    
    # Add some customers
    print("\n2. ADDING CUSTOMERS")
    print("-" * 30)
    customer1 = hotel.add_customer("Alice Johnson", "alice@email.com", "555-0101")
    customer2 = hotel.add_customer("Bob Smith", "bob@email.com", "555-0102")
    print(f"Added customer: {customer1.name} (ID: {customer1.customer_id[:8]}...)")
    print(f"Added customer: {customer2.name} (ID: {customer2.customer_id[:8]}...)")
    
    # Create bookings
    print("\n3. CREATING BOOKINGS")
    print("-" * 30)
    check_in = datetime.now().date().isoformat()
    check_out = (datetime.now().date() + timedelta(days=3)).isoformat()
    
    booking1 = hotel.create_booking(customer1.customer_id, "101", check_in, check_out)
    booking2 = hotel.create_booking(customer2.customer_id, "201", check_in, 
                                   (datetime.now().date() + timedelta(days=2)).isoformat())
    
    print(f"Booking 1: {customer1.name} → Room 101, ${booking1.total_price}")
    print(f"Booking 2: {customer2.name} → Room 201, ${booking2.total_price}")
    
    # Check room availability
    print("\n4. ROOM AVAILABILITY AFTER BOOKINGS")
    print("-" * 30)
    available_rooms = hotel.list_rooms(available_only=True)
    print(f"Available rooms: {len(available_rooms)} (Rooms: {', '.join([r.room_number for r in available_rooms])})")
    
    # Check in guests
    print("\n5. CHECKING IN GUESTS")
    print("-" * 30)
    hotel.check_in_booking(booking1.booking_id)
    hotel.check_in_booking(booking2.booking_id)
    print(f"{customer1.name} checked into Room 101")
    print(f"{customer2.name} checked into Room 201")
    
    # Add reviews
    print("\n6. ADDING CUSTOMER REVIEWS")
    print("-" * 30)
    review1 = hotel.add_review(customer1.customer_id, booking1.booking_id, 5, 
                              "Excellent service and comfortable room!")
    review2 = hotel.add_review(customer2.customer_id, booking2.booking_id, 4, 
                              "Great stay, would recommend to others.")
    print(f"{customer1.name}: {review1.rating}/5 - \"{review1.comment}\"")
    print(f"{customer2.name}: {review2.rating}/5 - \"{review2.comment}\"")
    
    # Check out one guest
    print("\n7. CHECKING OUT GUEST")
    print("-" * 30)
    hotel.check_out_booking(booking2.booking_id)
    print(f"{customer2.name} checked out of Room 201")
    
    # Show final statistics
    print("\n8. FINAL HOTEL STATISTICS")
    print("-" * 30)
    customers = hotel.list_customers()
    all_rooms = hotel.list_rooms()
    available_rooms = hotel.list_rooms(available_only=True)
    bookings = hotel.list_bookings()
    reviews = hotel.list_reviews()
    avg_rating = hotel.get_average_rating()
    total_revenue = sum(b.total_price for b in bookings if b.status != 'cancelled')
    
    print(f"Total customers: {len(customers)}")
    print(f"Total rooms: {len(all_rooms)}")
    print(f"Available rooms: {len(available_rooms)}")
    print(f"Total bookings: {len(bookings)}")
    print(f"Total reviews: {len(reviews)}")
    print(f"Average rating: {avg_rating}/5.0")
    print(f"Total revenue: ${total_revenue:.2f}")
    print(f"Occupancy rate: {((len(all_rooms) - len(available_rooms)) / len(all_rooms) * 100):.1f}%")
    
    print("\n" + "=" * 60)
    print("DEMO COMPLETED SUCCESSFULLY!")
    print("=" * 60)


if __name__ == "__main__":
    demo_hotel_system()