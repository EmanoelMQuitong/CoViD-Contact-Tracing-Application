
pos = -1

def search(modified, n):
    i = 0
    while i< len(modified):
        if modified[i] == n:
            globals()['pos'] = i
            return pos
        i = i+1

    return print("Not Found")



list = [5,8,4,6,9,2]
n = 'JUAN DELA CRUZ'

file_path = "Stored Informations.txt"
file =open(file_path, "r")
lines = file.readlines()
modified = []

# Process the lines outside the 'with' block if needed
for line in lines:
    modified.append(line.strip())  # Use strip() to remove newline characters


search(modified, n)
print('\n')
print(modified)

new = modified
newer = new[pos]
print('hi')
print(new)
print('hello')