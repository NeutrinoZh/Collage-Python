import math

class Ship:
    def __init__(self, x = 0, y = 0, title='Ship', max_velocity=100000, team_size=5):
        self.x = x
        self.y = y
        self.title = title
        self.max_velocity = max_velocity
        self.team_size = team_size

    def moveUp(self):
        self.y += 1

    def __str__(self):
        return f'''
    "{self.title}"
    position: [{self.x}, {self.y}];
    max velocity: {self.max_velocity} km/h;
    team size: {self.team_size} people;
                '''

    def dist(self, ship):
        return math.sqrt(self.x * ship.x + self.y * ship.y)

class Spacecraft(Ship):
    def __init__(self, x=0, y=0, title='Ship', max_velocity=100000, team_size=5, galaxy='Milky Way'):
        super().__init__(x=x, y=y, title=title, max_velocity=max_velocity, team_size=team_size)
        self.galaxy = galaxy

class Spaceship(Spacecraft):
    pass

class TransportSpaceship(Spaceship):
    def __init__(self, x=0, y=0, title='Ship', max_velocity=100000, team_size=5, galaxy='Milky Way', lifting_сapacity=10000):
        super().__init__(x=x, y=y, title=title, max_velocity=max_velocity, team_size=team_size, galaxy=galaxy)
        self.lifting_сapacity = lifting_сapacity

class ExcursionSpaceship(Spaceship):
    def __init__(self, x=0, y=0, title='Ship', max_velocity=100000, team_size=5, galaxy='Milky Way', seats=50):
        super().__init__(x=x, y=y, title=title, max_velocity=max_velocity, team_size=team_size, galaxy=galaxy)
        self.seats = seats

class ResearchSpaceship(Spaceship):
    def __init__(self, x=0, y=0, title='Ship', max_velocity=100000, team_size=5, galaxy='Milky Way', maxFlightRange=1000000):
        super().__init__(x=x, y=y, title=title, max_velocity=max_velocity, team_size=team_size, galaxy=galaxy)
        self.maxFlightRange = maxFlightRange

class BattleSpaceship(Spaceship):
    def __init__(self, x=0, y=0, title='Ship', max_velocity=100000, team_size=5, galaxy='Milky Way', attack=90):
        super().__init__(x=x, y=y, title=title, max_velocity=max_velocity, team_size=team_size, galaxy=galaxy)
        self.attack = attack

class Fleet:
    def __init__(self):
        self.ships = []

    def add(self, ship):
        self.ships.append(ship)
    
    def __getitem__(self, key):
        return self.ships[key]

    def __str__(self):
        string = '-' * 15 + '\n'
        for i, ship in enumerate(self.ships):
            string += f'ship number {i}: {ship}\n'
        return string