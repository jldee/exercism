"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.
    
    Attributes:
        (class) total_aliens_created (int): Total number of Alien instances.
        x_coordinate (int): Position on the x-axis.
        y_coordinate (int): Position on the y-axis.
        health (int): Number of health points.

    Methods:
        hit(): Decrement Alien health by one point.
        is_alive(): Return a boolean for if Alien is alive (if health is > 0).
        teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
        collision_detection(other): Implementation TBD.

    """
    total_aliens_created = 0

    def __init__(self, x, y):
            self.x_coordinate = x
            self.y_coordinate = y
            self.health = 3
            self.alive = True
            Alien.total_aliens_created += 1
    
    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
             return -1
        
    def is_alive(self):
        if self.health <= 0:
              self.alive = False
        return self.alive

    def teleport(self, x, y):
        self.x_coordinate += x
        self.y_coordinate += y
        return self.x_coordinate, self.y_coordinate

    def collision_detection(self, other_object):

         pass

def new_aliens_collection(alien_start_positions):

    alien_collection = []

    for position in alien_start_positions:
        x = position[0]
        y = position[1]
        alien_collection.append(Alien(x, y))

    return alien_collection