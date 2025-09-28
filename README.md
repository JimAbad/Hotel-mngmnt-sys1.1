# Hotel Management System v1.1

A comprehensive hotel management application that handles customer bookings, room management, and customer reviews.

## Features

- **Customer Management**: Add, update, and manage customer information
- **Room Management**: Track rooms, prices, availability, and capacity
- **Booking System**: Create, manage, check-in/check-out bookings
- **Review System**: Customers can leave reviews and ratings for their stays
- **Statistics**: View hotel occupancy, revenue, and rating statistics
- **Data Persistence**: All data is saved to JSON files for persistent storage

## Installation & Usage

### Prerequisites
- Python 3.6 or higher

### Running the Application

1. Clone this repository:
```bash
git clone <repository-url>
cd Hotel-mngmnt-sys1.1
```

2. Run the application:
```bash
python main.py
```

3. Follow the interactive CLI menu to manage your hotel.

### Running Tests

To run the basic functionality tests:
```bash
python test_hotel.py
```

## System Architecture

The system is built with the following components:

- **`models.py`**: Data models for Customer, Room, Booking, and Review
- **`data_manager.py`**: Handles JSON file-based data persistence
- **`hotel_manager.py`**: Core business logic and operations
- **`main.py`**: Command-line interface for user interaction
- **`test_hotel.py`**: Basic tests for system functionality

## Data Models

### Customer
- Customer ID (unique identifier)
- Name, email, phone
- Creation timestamp

### Room
- Room number (unique identifier)
- Room type (Single, Double, Suite)
- Price per night
- Capacity
- Availability status
- Amenities list

### Booking
- Booking ID (unique identifier)
- Customer ID and Room number references
- Check-in and check-out dates
- Total price
- Status (confirmed, checked_in, checked_out, cancelled)

### Review
- Review ID (unique identifier)
- Customer ID and Booking ID references
- Rating (1-5 stars)
- Comment text
- Creation timestamp

## CLI Menu Structure

### Main Menu
1. Customer Management
2. Room Management
3. Booking Management
4. Review Management
5. Show Statistics
6. Exit

### Customer Management
- Add new customers
- List all customers
- View customer details and booking history
- Update customer information

### Room Management
- Add new rooms
- List all rooms or available rooms only
- Update room prices
- Toggle room availability

### Booking Management
- Create new bookings
- List all bookings
- View booking details
- Check-in/check-out guests
- Cancel bookings

### Review Management
- Add reviews for completed stays
- List all reviews
- View reviews for specific bookings

### Statistics Dashboard
- Total customers, rooms, bookings
- Occupancy rate
- Total revenue
- Average customer rating

## Example Usage

1. **Add a Customer**: Create customer profiles with contact information
2. **Add Rooms**: Set up your hotel rooms with different types and prices
3. **Create Booking**: Reserve rooms for customers with check-in/out dates
4. **Check-in/Check-out**: Manage guest arrivals and departures
5. **Add Reviews**: Collect customer feedback and ratings
6. **View Statistics**: Monitor hotel performance and metrics

## Data Storage

All data is stored in JSON files in a `data/` directory:
- `customers.json`: Customer information
- `rooms.json`: Room details and availability
- `bookings.json`: Booking records
- `reviews.json`: Customer reviews

## Error Handling

The system includes comprehensive error handling for:
- Invalid date formats
- Non-existent customers or rooms
- Double booking attempts
- Invalid rating values
- Data validation errors

## Future Enhancements

Potential features for future versions:
- Web-based user interface
- Database backend (PostgreSQL, MySQL)
- Payment processing integration
- Email notifications
- Advanced reporting and analytics
- Multi-hotel support
- Staff management
- Maintenance scheduling