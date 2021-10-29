from ships import *

test = Ship()
print(test)
test.moveUp()
print(test)

test = Fleet()

test.add(Ship(7, 2, 'Milky Way', 865633, 9))
test.add(Spacecraft(5, 3, 'Earth', 50000, 3))
test.add(Spaceship(0, 0, 'New Horizons', 456000, 8, 'Andromeda'))
test.add(ResearchSpaceship(6, 0, 'Mars', 115000, 4))
test.add(TransportSpaceship(2, 7, 'NeutrinoZh', 3587153, 9))
test.add(ExcursionSpaceship(6, 5, 'Second life'))
test.add(BattleSpaceship(7, 1, 'Future now', team_size=4))

print(test)

test[0].moveUp()
test[4].moveUp()
test[3].moveUp()

print(test)

print(test[0].dist(test[1])) 