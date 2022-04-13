n = input()
alphabet = [-1] * 26

for i in range(len(n)):
    if alphabet[ord(n[i]) - 97] == -1:
        alphabet[ord(n[i]) - 97] = i

for j in alphabet:
    print(j, end=' ')