"""
Hotel Management System - Data Manager
Handles data persistence using JSON files
"""
import json
import os
from typing import List, Dict, Optional
from models import Customer, Room, Booking, Review


class DataManager:
    """Manages data persistence for the hotel management system"""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self.ensure_data_directory()
        
        # File paths for different data types
        self.customers_file = os.path.join(data_dir, "customers.json")
        self.rooms_file = os.path.join(data_dir, "rooms.json")
        self.bookings_file = os.path.join(data_dir, "bookings.json")
        self.reviews_file = os.path.join(data_dir, "reviews.json")
        
        # Initialize empty data files if they don't exist
        self._initialize_files()
    
    def ensure_data_directory(self):
        """Create data directory if it doesn't exist"""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
    
    def _initialize_files(self):
        """Initialize JSON files with empty arrays if they don't exist"""
        files = [self.customers_file, self.rooms_file, self.bookings_file, self.reviews_file]
        for file_path in files:
            if not os.path.exists(file_path):
                with open(file_path, 'w') as f:
                    json.dump([], f)
    
    def _load_json(self, file_path: str) -> List[Dict]:
        """Load data from JSON file"""
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def _save_json(self, file_path: str, data: List[Dict]):
        """Save data to JSON file"""
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    # Customer operations
    def save_customer(self, customer: Customer):
        """Save a customer to the data store"""
        customers = self._load_json(self.customers_file)
        # Update existing customer or add new one
        for i, existing in enumerate(customers):
            if existing['customer_id'] == customer.customer_id:
                customers[i] = customer.to_dict()
                break
        else:
            customers.append(customer.to_dict())
        self._save_json(self.customers_file, customers)
    
    def get_customer(self, customer_id: str) -> Optional[Customer]:
        """Get a customer by ID"""
        customers = self._load_json(self.customers_file)
        for customer_data in customers:
            if customer_data['customer_id'] == customer_id:
                return Customer.from_dict(customer_data)
        return None
    
    def get_all_customers(self) -> List[Customer]:
        """Get all customers"""
        customers = self._load_json(self.customers_file)
        return [Customer.from_dict(data) for data in customers]
    
    # Room operations
    def save_room(self, room: Room):
        """Save a room to the data store"""
        rooms = self._load_json(self.rooms_file)
        # Update existing room or add new one
        for i, existing in enumerate(rooms):
            if existing['room_number'] == room.room_number:
                rooms[i] = room.to_dict()
                break
        else:
            rooms.append(room.to_dict())
        self._save_json(self.rooms_file, rooms)
    
    def get_room(self, room_number: str) -> Optional[Room]:
        """Get a room by room number"""
        rooms = self._load_json(self.rooms_file)
        for room_data in rooms:
            if room_data['room_number'] == room_number:
                return Room.from_dict(room_data)
        return None
    
    def get_all_rooms(self) -> List[Room]:
        """Get all rooms"""
        rooms = self._load_json(self.rooms_file)
        return [Room.from_dict(data) for data in rooms]
    
    def get_available_rooms(self) -> List[Room]:
        """Get all available rooms"""
        rooms = self.get_all_rooms()
        return [room for room in rooms if room.is_available]
    
    # Booking operations
    def save_booking(self, booking: Booking):
        """Save a booking to the data store"""
        bookings = self._load_json(self.bookings_file)
        # Update existing booking or add new one
        for i, existing in enumerate(bookings):
            if existing['booking_id'] == booking.booking_id:
                bookings[i] = booking.to_dict()
                break
        else:
            bookings.append(booking.to_dict())
        self._save_json(self.bookings_file, bookings)
    
    def get_booking(self, booking_id: str) -> Optional[Booking]:
        """Get a booking by ID"""
        bookings = self._load_json(self.bookings_file)
        for booking_data in bookings:
            if booking_data['booking_id'] == booking_id:
                return Booking.from_dict(booking_data)
        return None
    
    def get_all_bookings(self) -> List[Booking]:
        """Get all bookings"""
        bookings = self._load_json(self.bookings_file)
        return [Booking.from_dict(data) for data in bookings]
    
    def get_customer_bookings(self, customer_id: str) -> List[Booking]:
        """Get all bookings for a specific customer"""
        bookings = self.get_all_bookings()
        return [booking for booking in bookings if booking.customer_id == customer_id]
    
    # Review operations
    def save_review(self, review: Review):
        """Save a review to the data store"""
        reviews = self._load_json(self.reviews_file)
        # Update existing review or add new one
        for i, existing in enumerate(reviews):
            if existing['review_id'] == review.review_id:
                reviews[i] = review.to_dict()
                break
        else:
            reviews.append(review.to_dict())
        self._save_json(self.reviews_file, reviews)
    
    def get_review(self, review_id: str) -> Optional[Review]:
        """Get a review by ID"""
        reviews = self._load_json(self.reviews_file)
        for review_data in reviews:
            if review_data['review_id'] == review_id:
                return Review.from_dict(review_data)
        return None
    
    def get_all_reviews(self) -> List[Review]:
        """Get all reviews"""
        reviews = self._load_json(self.reviews_file)
        return [Review.from_dict(data) for data in reviews]
    
    def get_booking_reviews(self, booking_id: str) -> List[Review]:
        """Get all reviews for a specific booking"""
        reviews = self.get_all_reviews()
        return [review for review in reviews if review.booking_id == booking_id]