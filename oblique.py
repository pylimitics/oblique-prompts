#!/usr/bin/env python3
"""
Oblique Products
A simple app that displays thought-provoking prompts to stimulate creative thinking
about networking and security product requirements. Based on Oblique Strategies by Brian Eno and Peter Schmidt
"""

import tkinter as tk
import random
from typing import List


class ObliqueStrategiesApp:
    """Main application window for displaying oblique product strategies."""
    
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Oblique Products")
        
        # Set window size and position
        window_width = 600
        window_height = 400
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        # Configure background
        self.root.configure(bg='#2c3e50')
        
        # Strategies list
        self.strategies: List[str] = [
            "Networks don't connect everything",
            "Scale down, not up",
            "A datacenter is a single point of failure",
            "A single point can be success",
            "Organizations have blind spots",
            "Use tiny data",
            "Protocols are lock-ins",
            "Addressing needs a list",
            "Not all who wander are lost",
            "Roaming finds places without addresses",
            "Not every location has an address",
            "When is an individual greater than a group",
            "Frameworks require reframing",
            "Inference needs data",
            "Context contains organizations",
            "Control is an illusion",
            "Nomads find oases",
            "A board has only two dimensions",
            "Nobody can keep up",
            "The first dashboards were just for mud",
            "Off-road networking",
            "Free range addressing",
            "Are protocols alive",
            "Connections are reversible",
            "A fractal is a way of seeing infinity",
            "Scale can have emergent properties",
            "What we call random is just patterns we can't decipher",
            "Wonders spring from simple rules",
            "Order is repetition of units.",
            "Connecting = emergence",
            "Scaling is not a goal, it's a method",
            "Ask a different question",
            "Understand the solution, not the problem",
            "Protocol > prodedure",
            "Take a different route",
            "Simplicity is complex",
            "Simplicity is a byproduct, not a goal"
        ]
        
        # Shuffle strategies for variety
        random.shuffle(self.strategies)
        self.current_index = 0
        
        # Create main frame
        self.main_frame = tk.Frame(root, bg='#2c3e50')
        self.main_frame.pack(expand=True, fill='both')
        
        # Create label for displaying text
        self.text_label = tk.Label(
            self.main_frame,
            text=self.strategies[self.current_index],
            font=('Helvetica', 24, 'normal'),
            fg='#ecf0f1',
            bg='#2c3e50',
            wraplength=550,
            justify='center',
            cursor='hand2'
        )
        self.text_label.pack(expand=True)
        
        # Create instruction label
        self.instruction_label = tk.Label(
            self.main_frame,
            text="Click anywhere to see another strategy; Q to quit",
            font=('Helvetica', 11, 'italic'),
            fg='#95a5a6',
            bg='#2c3e50'
        )
        self.instruction_label.pack(side='bottom', pady=20)
        
        # Bind click events
        self.root.bind('<Button-1>', self.next_strategy)
        self.text_label.bind('<Button-1>', self.next_strategy)
        
        # Bind keyboard shortcuts
        self.root.bind('<space>', self.next_strategy)
        self.root.bind('<Return>', self.next_strategy)
        self.root.bind('q', lambda e: self.root.quit())
        self.root.bind('<Escape>', lambda e: self.root.quit())
    
    def next_strategy(self, event=None):
        """Display the next strategy in the list."""
        self.current_index = (self.current_index + 1) % len(self.strategies)
        
        # Add a subtle fade effect by briefly changing opacity
        self.text_label.config(fg='#7f8c8d')
        self.root.after(50, lambda: self.text_label.config(fg='#ecf0f1'))
        
        # Update text
        self.text_label.config(text=self.strategies[self.current_index])


def main():
    """Initialize and run the application."""
    root = tk.Tk()
    app = ObliqueStrategiesApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
