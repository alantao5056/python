def cough_def(func):

  def func_wrapper():
    # code before function
    print('*cough*')
    func()
    print('*cough*')
    # code after function

  return func_wrapper

@cough_def
def question():
  print('can you give me a discount on that?')

@cough_def
def answer():
  print("it's only 50p cheapstake")

question()
answer()