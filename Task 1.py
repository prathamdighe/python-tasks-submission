try:
    file = open("Sample.txt", "r")
    print("reading lines:")
    lines = file.readlines()
    print("Reading file content")

    for i, line in enumerate(lines, 1):
        print(f'line {i}: "{line.strip()}"')

    file.close()

except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
