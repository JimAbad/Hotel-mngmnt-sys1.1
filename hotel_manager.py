"""
Hotel Management System - Core Business Logic
"""
from datetime import datetime, timedelta
from typing import List, Optional
import uuid
from models import Customer, Room, Booking, Review
from data_manager import DataManager


class HotelManager:
    """Main hotel management system class"""
    
    def __init__(self):
        self.data_manager = DataManager()
        self._initialize_default_rooms()
    
    def _initialize_default_rooms(self):
        """Initialize some default rooms if none exist"""
        existing_rooms = self.data_manager.get_all_rooms()
        if not existing_rooms:
            default_rooms = [
                Room("101", "Single", 100.0, 1),
                Room("102", "Single", 100.0, 1),
                Room("201", "Double", 150.0, 2),
                Room("202", "Double", 150.0, 2),
                Room("301", "Suite", 250.0, 4),
            ]
            for room in default_rooms:
                self.data_manager.save_room(room)
    
    # Customer Management
    def add_customer(self, name: str, email: str, phone: str) -> Customer:
        """Add a new customer"""
        customer_id = str(uuid.uuid4())
        customer = Customer(customer_id, name, email, phone)
        self.data_manager.save_customer(customer)
        return customer
    
    def get_customer(self, customer_id: str) -> Optional[Customer]:
        """Get customer by ID"""
        return self.data_manager.get_customer(customer_id)
    
    def list_customers(self) -> List[Customer]:
        """List all customers"""
        return self.data_manager.get_all_customers()
    
    def update_customer(self, customer_id: str, name: str = None, 
                       email: str = None, phone: str = None) -> Optional[Customer]:
        """Update customer information"""
        customer = self.data_manager.get_customer(customer_id)
        if customer:
            if name:
                customer.name = name
            if email:
                customer.email = email
            if phone:
                customer.phone = phone
            self.data_manager.save_customer(customer)
            return customer
        return None
    
    # Room Management
    def add_room(self, room_number: str, room_type: str, 
                 price_per_night: float, capacity: int) -> Room:
        """Add a new room"""
        room = Room(room_number, room_type, price_per_night, capacity)
        self.data_manager.save_room(room)
        return room
    
    def get_room(self, room_number: str) -> Optional[Room]:
        """Get room by number"""
        return self.data_manager.get_room(room_number)
    
    def list_rooms(self, available_only: bool = False) -> List[Room]:
        """List all rooms or only available ones"""
        if available_only:
            return self.data_manager.get_available_rooms()
        return self.data_manager.get_all_rooms()
    
    def update_room_availability(self, room_number: str, is_available: bool) -> Optional[Room]:
        """Update room availability status"""
        room = self.data_manager.get_room(room_number)
        if room:
            room.is_available = is_available
            self.data_manager.save_room(room)
            return room
        return None
    
    def update_room_price(self, room_number: str, new_price: float) -> Optional[Room]:
        """Update room price"""
        room = self.data_manager.get_room(room_number)
        if room:
            room.price_per_night = new_price
            self.data_manager.save_room(room)
            return room
        return None
    
    # Booking Management
    def create_booking(self, customer_id: str, room_number: str, 
                      check_in_date: str, check_out_date: str) -> Optional[Booking]:
        """Create a new booking"""
        # Validate customer exists
        customer = self.data_manager.get_customer(customer_id)
        if not customer:
            raise ValueError("Customer not found")
        
        # Validate room exists and is available
        room = self.data_manager.get_room(room_number)
        if not room:
            raise ValueError("Room not found")
        if not room.is_available:
            raise ValueError("Room is not available")
        
        # Calculate total price (simple calculation for now)
        try:
            check_in = datetime.fromisoformat(check_in_date)
            check_out = datetime.fromisoformat(check_out_date)
            if check_out <= check_in:
                raise ValueError("Check-out date must be after check-in date")
            
            nights = (check_out - check_in).days
            total_price = nights * room.price_per_night
        except ValueError as e:
            raise ValueError(f"Invalid date format: {e}")
        
        # Create booking
        booking_id = str(uuid.uuid4())
        booking = Booking(booking_id, customer_id, room_number, 
                         check_in_date, check_out_date, total_price)
        
        # Mark room as unavailable and save booking
        room.is_available = False
        self.data_manager.save_room(room)
        self.data_manager.save_booking(booking)
        
        return booking
    
    def get_booking(self, booking_id: str) -> Optional[Booking]:
        """Get booking by ID"""
        return self.data_manager.get_booking(booking_id)
    
    def list_bookings(self) -> List[Booking]:
        """List all bookings"""
        return self.data_manager.get_all_bookings()
    
    def get_customer_bookings(self, customer_id: str) -> List[Booking]:
        """Get all bookings for a customer"""
        return self.data_manager.get_customer_bookings(customer_id)
    
    def cancel_booking(self, booking_id: str) -> Optional[Booking]:
        """Cancel a booking"""
        booking = self.data_manager.get_booking(booking_id)
        if booking and booking.status != "cancelled":
            booking.status = "cancelled"
            # Make room available again
            room = self.data_manager.get_room(booking.room_number)
            if room:
                room.is_available = True
                self.data_manager.save_room(room)
            self.data_manager.save_booking(booking)
            return booking
        return None
    
    def check_in_booking(self, booking_id: str) -> Optional[Booking]:
        """Check in a booking"""
        booking = self.data_manager.get_booking(booking_id)
        if booking and booking.status == "confirmed":
            booking.status = "checked_in"
            self.data_manager.save_booking(booking)
            return booking
        return None
    
    def check_out_booking(self, booking_id: str) -> Optional[Booking]:
        """Check out a booking"""
        booking = self.data_manager.get_booking(booking_id)
        if booking and booking.status == "checked_in":
            booking.status = "checked_out"
            # Make room available again
            room = self.data_manager.get_room(booking.room_number)
            if room:
                room.is_available = True
                self.data_manager.save_room(room)
            self.data_manager.save_booking(booking)
            return booking
        return None
    
    # Review Management
    def add_review(self, customer_id: str, booking_id: str, 
                   rating: int, comment: str) -> Optional[Review]:
        """Add a review for a booking"""
        # Validate rating
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5")
        
        # Validate customer exists
        customer = self.data_manager.get_customer(customer_id)
        if not customer:
            raise ValueError("Customer not found")
        
        # Validate booking exists and belongs to customer
        booking = self.data_manager.get_booking(booking_id)
        if not booking:
            raise ValueError("Booking not found")
        if booking.customer_id != customer_id:
            raise ValueError("Booking does not belong to this customer")
        
        # Check if customer has already reviewed this booking
        existing_reviews = self.data_manager.get_booking_reviews(booking_id)
        customer_reviews = [r for r in existing_reviews if r.customer_id == customer_id]
        if customer_reviews:
            raise ValueError("Customer has already reviewed this booking")
        
        # Create review
        review_id = str(uuid.uuid4())
        review = Review(review_id, customer_id, booking_id, rating, comment)
        self.data_manager.save_review(review)
        
        return review
    
    def get_review(self, review_id: str) -> Optional[Review]:
        """Get review by ID"""
        return self.data_manager.get_review(review_id)
    
    def list_reviews(self) -> List[Review]:
        """List all reviews"""
        return self.data_manager.get_all_reviews()
    
    def get_booking_reviews(self, booking_id: str) -> List[Review]:
        """Get all reviews for a booking"""
        return self.data_manager.get_booking_reviews(booking_id)
    
    def get_average_rating(self) -> float:
        """Get average rating across all reviews"""
        reviews = self.data_manager.get_all_reviews()
        if not reviews:
            return 0.0
        total_rating = sum(review.rating for review in reviews)
        return round(total_rating / len(reviews), 2)