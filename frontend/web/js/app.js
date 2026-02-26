'use strict';

class BookingFlow {
    constructor() {
        this.bookings = [];
    }

    addBooking(bookingData) {
        this.bookings.push(bookingData);
        console.log('Booking added:', bookingData);
    }

    viewBookings() {
        console.log('Current bookings:', this.bookings);
    }

    removeBooking(bookingId) {
        this.bookings = this.bookings.filter(booking => booking.id !== bookingId);
        console.log('Booking removed:', bookingId);
    }
}

// Example usage:
const bookingFlow = new BookingFlow();

// Adding a booking
bookingFlow.addBooking({ id: 1, user: 'John Doe', destination: 'Paris', date: '2026-03-01' });

// Viewing all bookings
bookingFlow.viewBookings();

// Removing a booking
bookingFlow.removeBooking(1);