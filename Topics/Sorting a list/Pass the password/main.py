# the follwing line reads the list from the input, do not modify it, please
passwords = input().split()

passwords.sort(key=len)
for password, length in zip(passwords, list(map(len, passwords))):
    print(password, length)
