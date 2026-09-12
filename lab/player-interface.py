# ==========================================
# CONCEPTUAL LEARNING NOTES: Build a Player Interface
# ==========================================
#
# 1. Abstract Base Classes (ABCs):
#    - Inheriting from `abc.ABC` allows you to define a blueprint class that cannot 
#      be instantiated directly, enforcing structure on child classes.
#    - Using the `@abstractmethod` decorator means any concrete child class (like 
#      Pawn) MUST implement that method, otherwise Python raises a TypeError upon 
#      instantiation.
#
# 2. Tuple Coordinate Arithmetic:
#    - In Python, adding two tuples together `(x1, y1) + (x2, y2)` concatenates them 
#      into `(x1, y1, x2, y2)` instead of performing vector addition.
#    - To properly move coordinates, you must sum them element-wise:
#      `position = (position[0] + choice[0], position[1] + choice[1])`
#
# 3. Method Overriding and super():
#    - Calling `super().__init__()` inside a child class ensures the parent class's 
#      initialization logic runs first, setting up shared attributes (`position`, `path`, etc.) 
#      before the child class modifies or extends them (like defining `self.moves`).
#
# 4. Extending List Attributes:
#    - Using the augmented assignment operator `+=` on a list (e.g., `self.moves += new_items`) 
#      calls `list.__iadd__`, which extends the existing list in place, rather than 
#      raising a TypeError like trying to add an integer (`+= 1`) to a list would.

from abc import ABC, abstractmethod
import random 

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0,0)
        self.path = [self.position]
    
    def make_move(self):
        choice = random.choice(self.moves)
        self.position = (self.position[0] + choice[0], self.position[1] + choice[1]) 
        self.path.append(self.position)
        return self.position 

    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [(0,1), (0,-1), (-1,0), (1,0)]
    
    def level_up(self):
        self.moves += [(1,1),(1,-1),(-1,1),(-1,-1)]
