# "a" - Append - will append to the end of the file

# "w" - Write - will overwrite any existing content

with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read())



with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read())


f = open("myfile.txt", "x")

# "x" - Create - will create a file, returns an error if the file exists