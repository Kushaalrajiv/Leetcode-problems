total = 0
s = input("Enter a Roman numeral: ")
key_values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

for i in range(len(s) - 1):
    if key_values[s[i]] < key_values[s[i + 1]]:
        total -= key_values[s[i]]
    else:
        total += key_values[s[i]]
    print(total)
total += key_values[s[-1]]#last character

print(total)
