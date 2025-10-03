"""1. Write code that asks the user for their name, then opens a file called name.txt and writes that name to it. Use open and close for this question."""
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

"""In the same file, but as if it were a separate program, write code that opens "name.txt" and reads the name (as above) then prints (note the exact output),
Hi Bob! (or whatever the name is in the file). Do not simply print the user's input variable!
Use open and close for this question."""

with open("name.txt","r") as in_file:
    print(f"Hi {in_file.read().strip()}!")