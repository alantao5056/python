class Planet:

  shape = 'round'

  def __init__(self, name, radius, gravity, system):
    self.name = name
    self.radius = radius
    self.gravity = gravity
    self.system = system

  def orbit(self):
    return f'{self.name} is orbiting in the {self.system}'

  @classmethod
  def commons (cls):
    return f'All plantes are {cls.shape} because of gravity'

  @staticmethod
  def spin (speed = '2000 miles per hour'):
    return f'the planet spins at {speed}'

# hoth = Planet('Hoth', 200000, 5.5, 'Hoth System')
# print(f'Name is: {hoth.name}')
# print(f'Radius is: {hoth.radius}')
# print(f'the gravity is: {hoth.gravity}')
# print(hoth.orbit())

naboo = Planet('Naboo', 300000, 8, 'Naboo System')
# print(f'Name: {naboo.name}')
# print(f'Radius: {naboo.radius}')
# print(f'Gravity: {naboo.gravity}')
# print(naboo.orbit())

print(Planet.spin('a very high speed'))
