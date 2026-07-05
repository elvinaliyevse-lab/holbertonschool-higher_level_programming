#!/usr/bin/python3
"""Print the ASCII alphabet in reverse alternating lower/upper."""
print("{}".format(
    ''.join(
        (chr(ord('a') + i) if i % 2 else chr(ord('A') + i))
        for i in range(25, -1, -1)
    )
), end="")
