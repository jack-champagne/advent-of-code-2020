import re
file = open('2.txt')

lines = file.read()
patt = re.compile(r'(\d+)[-](\d+)\s([a-z]):\s(.*)\n')
matches = patt.findall(lines)

valid_passwords = 0
for match in matches:
    min = int(match[0])
    max = int(match[1])
    char = match[2]
    password = match[3]
    # print("Min: " + min + "\t\t Max: " + max + " \t\t Char: " + char + "\t P: " + password)
    letter_patt = re.compile(char)
    p_mat_size = len(letter_patt.findall(password))
    if min <= p_mat_size <= max:
        valid_passwords += 1

print(valid_passwords)