# def greet(name = 'ryu', time = 'morning'):
#   print(f'good {time} {name}, hope you are well');

# name = input('Enter your name: ');
# time = input('Enter the time of day: ')

# greet('shaun', 'afternoon');

def area(radius):
  return 3.1416 * radius * radius;

def vol(area, length):
  print(area * length);

radius = int(input('Enter a radius: '));
length = int(input('Enter a length: '));

vol(area(radius), length);