import re
file = open('2-1-input.txt')

lines = file.read()
patt = re.compile(r'(\d+)[-](\d+)\s([a-z]):\s(.*)\n')
matches = patt.findall(lines)

valid_passwords = 0
for match in matches:
    pos1 = int(match[0])
    pos2 = int(match[1])
    char = match[2]
    password = match[3]

    # Didn't read full question lol, here's the XOR gate that we're looking for.
    if (char == password[pos1 - 1] or char == password[pos2 - 1]) and not (char == password[pos1 - 1] and char == password[pos2 - 1]):
        valid_passwords += 1

print(valid_passwords)