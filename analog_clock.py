import tkinter as tk
import datetime
import math


class AnalogClock:
    """
    A simple analog clock using Tkinter.
    This class creates an analog clock with hour, minute, and second hands,
    as well as tick marks and numbers for each hour.
    """

    def __init__(self, root):
        """Initialize the clock and set up the canvas."""
        self.root = root
        self.root.title("Analog Clock")
        self.canvas_size = 400  # Size of the canvas
        self.center = self.canvas_size // 2  # Center point of the clock
        self.radius = self.canvas_size // 2 - 20  # Radius of the clock face

        # Create canvas
        self.canvas = tk.Canvas(
            root, width=self.canvas_size, height=self.canvas_size, bg="white"
        )
        self.canvas.pack()

        # Draw clock face
        self.draw_clock_face()

        # Create clock hands
        self.hour_hand = self.canvas.create_line(0, 0, 0, 0, width=4, fill="black")
        self.minute_hand = self.canvas.create_line(0, 0, 0, 0, width=2, fill="black")
        self.second_hand = self.canvas.create_line(0, 0, 0, 0, width=1, fill="red")

        # Start updating the clock
        self.update_clock()

    def draw_clock_face(self):
        """Draws the clock face, including the outer circle, tick marks, and numbers."""
        # Draw outer circle
        self.canvas.create_oval(
            self.center - self.radius,
            self.center - self.radius,
            self.center + self.radius,
            self.center + self.radius,
            width=2,
        )

        # Draw hour markers and numbers
        for hour in range(1, 13):
            angle = math.radians(hour * 30 - 90)

            # Draw tick marks
            x_inner = self.center + (self.radius - 15) * math.cos(angle)
            y_inner = self.center + (self.radius - 15) * math.sin(angle)
            x_outer = self.center + self.radius * math.cos(angle)
            y_outer = self.center + self.radius * math.sin(angle)
            self.canvas.create_line(x_inner, y_inner, x_outer, y_outer, width=2)

            # Draw numbers
            num_x = self.center + (self.radius - 30) * math.cos(angle)
            num_y = self.center + (self.radius - 30) * math.sin(angle)
            self.canvas.create_text(
                num_x, num_y, text=str(hour), font=("Arial", 16, "bold")
            )

    def update_clock(self):
        """Updates the clock hands to reflect the current time."""
        now = datetime.datetime.now()
        hours = now.hour % 12
        minutes = now.minute
        seconds = now.second

        # Calculate angles for each hand
        hour_angle = math.radians((hours * 30) + (minutes * 0.5) - 90)
        minute_angle = math.radians((minutes * 6) + (seconds * 0.1) - 90)
        second_angle = math.radians(seconds * 6 - 90)

        # Update hand positions
        self.update_hand(self.hour_hand, hour_angle, length=50)
        self.update_hand(self.minute_hand, minute_angle, length=70)
        self.update_hand(self.second_hand, second_angle, length=90)

        # Schedule next update in 1 second
        self.root.after(1000, self.update_clock)

    def update_hand(self, hand, angle, length):
        """Moves a clock hand to a new position based on the given angle."""
        x = self.center + length * math.cos(angle)
        y = self.center + length * math.sin(angle)
        self.canvas.coords(hand, self.center, self.center, x, y)


if __name__ == "__main__":
    root = tk.Tk()
    clock = AnalogClock(root)
    root.mainloop()
