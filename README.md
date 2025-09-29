# Hotel & Restaurant Management System (MERN)

## Project Overview

This is a **MERN stack** (MongoDB, Express, React, Node.js) application for managing a hotel and restaurant system.
It supports two admin roles: `restaurantAdmin` and `hotelAdmin`. Each admin has their own dashboard and must log in to access it.

---

## Key Features & Structure

### Backend (`/backend`)
- **Express server** connects to MongoDB Atlas using a connection string in `.env` (`MONGO_URI`).
- **User model** (`User.js`):
	- Fields: `username`, `email`, `password` (hashed), `role` (`restaurantAdmin` or `hotelAdmin`).
- **Routes** (`userRoutes.js`):
	- `/api/users/register`: Register a new admin (choose role).
	- `/api/users/login`: Login, returns JWT and role.
	- JWT secret is set via `.env` (`JWT_SECRET`).
- **Error handling**: Registration returns clear errors for missing fields, duplicates, or validation issues.

### Frontend (`/frontend`)
- **React app** with React Router for navigation.
- **Pages/Components**:
	- `Home.js`: Welcome page with links to Login and Register.
	- `RegisterPage.js`: Register as an admin (choose role).
	- `LoginPage.js`: Login, redirects to the correct dashboard based on role.
	- `RestaurantAdminDashboard.js` and `HotelAdminDashboard.js`: Separate dashboards for each admin type.
	- `LogoutButton.js`: Logs out and redirects to login.
	- `ProtectedRoute.js`: Protects routes, checks for valid JWT and correct role, redirects to login if not authenticated or authorized.
- **JWT & role** are stored in `localStorage` after login.
- **Role-based routing**: Only the correct admin can access their dashboard, and you cannot bypass login by typing the URL.

---

## How to Start Collaborating

1. **Clone the repository** and open it in VS Code.
2. **Install dependencies**:
	 - In the root:  
		 `npm install`
	 - In `/frontend`:  
		 `npm install`
	 - In `/backend`:  
		 `npm install`
3. **Set up environment variables**:
	 - In `/backend`, create a `.env` file with:
		 ```
		 MONGO_URI=your_mongodb_atlas_connection_string
		 JWT_SECRET=your_jwt_secret
		 ```
4. **Start the servers**:
	 - Backend:  
		 `npm start` (from `/backend`)
	 - Frontend:  
		 `npm start` (from `/frontend`)
5. **Register an admin** (restaurant or hotel) at `/register`, then log in at `/login`.
6. **Code organization**:
	 - Frontend components are in `/frontend/src/`.
	 - Backend models and routes are in `/backend/`.
	 - Add new features by creating new components, routes, or models as needed.

---

## How to Help/Contribute

- **Frontend**: Add new pages, improve dashboards, enhance UI, or add features (e.g., restaurant/hotel management tools).
- **Backend**: Add new models (e.g., Restaurant, Hotel, Menu), create new API endpoints, improve authentication, or add business logic.
- **Testing**: Add unit or integration tests.
- **Documentation**: Update the README with setup instructions, API docs, or usage guides.


---



