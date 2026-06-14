#!/usr/bin/python3
output = ""
for c in range(97, 123):
    if c != 101 and c != 113:
        output += chr(c)
print("{}".format(output), end="")
