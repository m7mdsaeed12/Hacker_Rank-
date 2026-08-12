def string1 (string, position, character):
    return string [ :position] + character + string [position + 1: ]

s = input()
position, character = input().split()
position = int(position)
print(string1(s, position, character))