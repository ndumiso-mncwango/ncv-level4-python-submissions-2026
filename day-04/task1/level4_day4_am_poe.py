with open("names.txt", "w") as f:
    f.write("Ndumiso\n")
    f.write("Samkelo\n")
    f.write("Luyanda\n")
    f.write("Ntwenhle\n")
    f.write("Mandisa\n")
with open("names.txt") as f:
    for line in f:
        print(line.strip().upper())
with open("names.txt", "a") as f:
    f.write("Nokuphumula\n")
with open("names.txt") as f:
    print(len(f.readline().strip()))
try:
    with open("nothing.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("File does not seem to exist")

    
    