#!/usr/bin/env python3
"""
Hotel Management System - Basic Tests
"""
import os
import tempfile
import shutil
from datetime import datetime, timedelta
from hotel_manager import HotelManager


def test_hotel_management_system():
    """Run basic tests for hotel management system"""
    print("Running Hotel Management System Tests...")
    print("=" * 50)
    
    # Create a temporary directory for test data
    test_data_dir = tempfile.mkdtemp()
    
    try:
        # Initialize hotel manager with test data directory
        hotel_manager = HotelManager()
        hotel_manager.data_manager.data_dir = test_data_dir
        hotel_manager.data_manager.customers_file = os.path.join(test_data_dir, "customers.json")
        hotel_manager.data_manager.rooms_file = os.path.join(test_data_dir, "rooms.json")
        hotel_manager.data_manager.bookings_file = os.path.join(test_data_dir, "bookings.json")
        hotel_manager.data_manager.reviews_file = os.path.join(test_data_dir, "reviews.json")
        hotel_manager.data_manager._initialize_files()
        hotel_manager._initialize_default_rooms()
        
        test_count = 0
        passed_count = 0
        
        # Test 1: Add Customer
        test_count += 1
        print(f"\nTest {test_count}: Adding Customer")
        try:
            customer = hotel_manager.add_customer("John Doe", "john@example.com", "123-456-7890")
            assert customer.name == "John Doe"
            assert customer.email == "john@example.com"
            print("✓ PASSED: Customer added successfully")
            passed_count += 1
        except Exception as e:
            print(f"✗ FAILED: {e}")
        
        # Test 2: List Customers
        test_count += 1
        print(f"\nTest {test_count}: Listing Customers")
        try:
            customers = hotel_manager.list_customers()
            assert len(customers) == 1
            assert customers[0].name == "John Doe"
            print("✓ PASSED: Customer listed successfully")
            passed_count += 1
        except Exception as e:
            print(f"✗ FAILED: {e}")
        
        # Test 3: List Rooms
        test_count += 1
        print(f"\nTest {test_count}: Listing Rooms")
        try:
            rooms = hotel_manager.list_rooms()
            assert len(rooms) == 5  # Default rooms
            available_rooms = hotel_manager.list_rooms(available_only=True)
            assert len(available_rooms) == 5
            print("✓ PASSED: Rooms listed successfully")
            passed_count += 1
        except Exception as e:
            print(f"✗ FAILED: {e}")
        
        # Test 4: Create Booking
        test_count += 1
        print(f"\nTest {test_count}: Creating Booking")
        try:
            check_in = datetime.now().date().isoformat()
            check_out = (datetime.now().date() + timedelta(days=2)).isoformat()
            
            booking = hotel_manager.create_booking(
                customer.customer_id, "101", check_in, check_out
            )
            assert booking.customer_id == customer.customer_id
            assert booking.room_number == "101"
            assert booking.status == "confirmed"
            print("✓ PASSED: Booking created successfully")
            passed_count += 1
        except Exception as e:
            print(f"✗ FAILED: {e}")
        
        # Test 5: Room Availability After Booking
        test_count += 1
        print(f"\nTest {test_count}: Room Availability After Booking")
        try:
            room = hotel_manager.get_room("101")
            assert room.is_available == False
            available_rooms = hotel_manager.list_rooms(available_only=True)
            assert len(available_rooms) == 4
            print("✓ PASSED: Room availability updated correctly")
            passed_count += 1
        except Exception as e:
            print(f"✗ FAILED: {e}")
        
        # Test 6: Add Review
        test_count += 1
        print(f"\nTest {test_count}: Adding Review")
        try:
            review = hotel_manager.add_review(
                customer.customer_id, booking.booking_id, 5, "Excellent stay!"
            )
            assert review.rating == 5
            assert review.comment == "Excellent stay!"
            print("✓ PASSED: Review added successfully")
            passed_count += 1
        except Exception as e:
            print(f"✗ FAILED: {e}")
        
        # Test 7: List Reviews
        test_count += 1
        print(f"\nTest {test_count}: Listing Reviews")
        try:
            reviews = hotel_manager.list_reviews()
            assert len(reviews) == 1
            assert reviews[0].rating == 5
            
            booking_reviews = hotel_manager.get_booking_reviews(booking.booking_id)
            assert len(booking_reviews) == 1
            print("✓ PASSED: Reviews listed successfully")
            passed_count += 1
        except Exception as e:
            print(f"✗ FAILED: {e}")
        
        # Test 8: Check-in Booking
        test_count += 1
        print(f"\nTest {test_count}: Check-in Booking")
        try:
            checked_in_booking = hotel_manager.check_in_booking(booking.booking_id)
            assert checked_in_booking.status == "checked_in"
            print("✓ PASSED: Booking checked in successfully")
            passed_count += 1
        except Exception as e:
            print(f"✗ FAILED: {e}")
        
        # Test 9: Check-out Booking
        test_count += 1
        print(f"\nTest {test_count}: Check-out Booking")
        try:
            checked_out_booking = hotel_manager.check_out_booking(booking.booking_id)
            assert checked_out_booking.status == "checked_out"
            
            # Room should be available again
            room = hotel_manager.get_room("101")
            assert room.is_available == True
            print("✓ PASSED: Booking checked out successfully")
            passed_count += 1
        except Exception as e:
            print(f"✗ FAILED: {e}")
        
        # Test 10: Average Rating
        test_count += 1
        print(f"\nTest {test_count}: Calculate Average Rating")
        try:
            avg_rating = hotel_manager.get_average_rating()
            assert avg_rating == 5.0
            print("✓ PASSED: Average rating calculated correctly")
            passed_count += 1
        except Exception as e:
            print(f"✗ FAILED: {e}")
        
        # Test Results
        print(f"\n" + "=" * 50)
        print(f"TEST RESULTS: {passed_count}/{test_count} tests passed")
        if passed_count == test_count:
            print("🎉 ALL TESTS PASSED!")
        else:
            print(f"⚠️  {test_count - passed_count} tests failed")
        print("=" * 50)
        
        return passed_count == test_count
        
    finally:
        # Clean up test data directory
        shutil.rmtree(test_data_dir)


if __name__ == "__main__":
    success = test_hotel_management_system()
    if not success:
        exit(1)