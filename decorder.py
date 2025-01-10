def decorator(func):
  def inner1():
    print("Hello, this is before function execution")
    func()
    print("This is after function execution")
  return inner1
def function():
     print("This is inside the function !!")
function_used = decorator(function)
function_used()