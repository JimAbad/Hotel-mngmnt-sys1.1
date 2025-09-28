"""
Hotel Management System - Data Models
"""
from datetime import datetime
from typing import List, Dict, Optional
import json


class Customer:
    """Represents a hotel customer"""
    
    def __init__(self, customer_id: str, name: str, email: str, phone: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.created_at = datetime.now().isoformat()
    
    def to_dict(self) -> Dict:
        """Convert customer to dictionary for JSON serialization"""
        return {
            'customer_id': self.customer_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'created_at': self.created_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Customer':
        """Create customer from dictionary"""
        customer = cls(data['customer_id'], data['name'], data['email'], data['phone'])
        customer.created_at = data['created_at']
        return customer


class Room:
    """Represents a hotel room"""
    
    def __init__(self, room_number: str, room_type: str, price_per_night: float, capacity: int):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.capacity = capacity
        self.is_available = True
        self.amenities = []
    
    def to_dict(self) -> Dict:
        """Convert room to dictionary for JSON serialization"""
        return {
            'room_number': self.room_number,
            'room_type': self.room_type,
            'price_per_night': self.price_per_night,
            'capacity': self.capacity,
            'is_available': self.is_available,
            'amenities': self.amenities
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Room':
        """Create room from dictionary"""
        room = cls(data['room_number'], data['room_type'], data['price_per_night'], data['capacity'])
        room.is_available = data.get('is_available', True)
        room.amenities = data.get('amenities', [])
        return room


class Booking:
    """Represents a hotel booking"""
    
    def __init__(self, booking_id: str, customer_id: str, room_number: str, 
                 check_in_date: str, check_out_date: str, total_price: float):
        self.booking_id = booking_id
        self.customer_id = customer_id
        self.room_number = room_number
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.total_price = total_price
        self.status = "confirmed"  # confirmed, checked_in, checked_out, cancelled
        self.created_at = datetime.now().isoformat()
    
    def to_dict(self) -> Dict:
        """Convert booking to dictionary for JSON serialization"""
        return {
            'booking_id': self.booking_id,
            'customer_id': self.customer_id,
            'room_number': self.room_number,
            'check_in_date': self.check_in_date,
            'check_out_date': self.check_out_date,
            'total_price': self.total_price,
            'status': self.status,
            'created_at': self.created_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Booking':
        """Create booking from dictionary"""
        booking = cls(data['booking_id'], data['customer_id'], data['room_number'],
                     data['check_in_date'], data['check_out_date'], data['total_price'])
        booking.status = data.get('status', 'confirmed')
        booking.created_at = data['created_at']
        return booking


class Review:
    """Represents a customer review"""
    
    def __init__(self, review_id: str, customer_id: str, booking_id: str, 
                 rating: int, comment: str):
        self.review_id = review_id
        self.customer_id = customer_id
        self.booking_id = booking_id
        self.rating = rating  # 1-5 stars
        self.comment = comment
        self.created_at = datetime.now().isoformat()
    
    def to_dict(self) -> Dict:
        """Convert review to dictionary for JSON serialization"""
        return {
            'review_id': self.review_id,
            'customer_id': self.customer_id,
            'booking_id': self.booking_id,
            'rating': self.rating,
            'comment': self.comment,
            'created_at': self.created_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Review':
        """Create review from dictionary"""
        review = cls(data['review_id'], data['customer_id'], data['booking_id'],
                    data['rating'], data['comment'])
        review.created_at = data['created_at']
        return review