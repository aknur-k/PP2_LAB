def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")



def my_function(name, /):
  print("Hello", name)

my_function("Emil")
#positional only
