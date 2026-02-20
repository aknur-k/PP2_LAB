def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")



def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")
#keyword only

