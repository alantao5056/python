age = 25;
num = 0;

while num < age:
  # block of code
  if num == 0:
    num += 1;
    continue;
  if num % 2 == 0:
    print(num);
  if num > 10:
    break;
  num += 1;