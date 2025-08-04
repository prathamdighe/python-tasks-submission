file = open("output.txt", "w")
lines_from_input = input("Enter text to write to the file: ")
write = file.writelines(lines_from_input)
file.close()
print("Data successfully written to output.txt \n")

file = open("output.txt", "a")
lines_from_input = input("Enter additional text to append: ")
append = file.writelines("\n" + lines_from_input)
file.close()
print("Data successfully appended ")


file = open("output.txt", "r")
print("File content of output.txt")
lines = file.readlines()
print("Reading file content")

for i, line in enumerate(lines, 1):
    print(f'line {i}: "{line.strip()}"')
file.close()
