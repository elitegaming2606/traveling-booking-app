package backend.java.services.bookingengine;

import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpStatus;

@RestController
@RequestMapping("/api/booking")
public class BookingController {

    @PostMapping
    public ResponseEntity<String> createBooking(@RequestBody Booking booking) {
        // Logic to create booking
        return new ResponseEntity<>("Booking created successfully!", HttpStatus.CREATED);
    }

    @GetMapping("/{id}")
    public ResponseEntity<Booking> getBooking(@PathVariable Long id) {
        // Logic to retrieve booking by id
        Booking booking = new Booking(id, "Example Name", "Example Date"); // Placeholder
        return new ResponseEntity<>(booking, HttpStatus.OK);
    }

    @PutMapping("/{id}")
    public ResponseEntity<String> updateBooking(@PathVariable Long id, @RequestBody Booking booking) {
        // Logic to update booking
        return new ResponseEntity<>("Booking updated successfully!", HttpStatus.OK);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<String> deleteBooking(@PathVariable Long id) {
        // Logic to delete booking
        return new ResponseEntity<>("Booking deleted successfully!", HttpStatus.NO_CONTENT);
    }
}

class Booking {
    private Long id;
    private String name;
    private String date;

    public Booking(Long id, String name, String date) {
        this.id = id;
        this.name = name;
        this.date = date;
    }
    // Getters and setters...
}