length = int(input("Enter password length: "))
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*()_-+=<>?/"
all_chars = letters + digits + symbols
password = ""
index = 0
for i in range(length):
    index = (i * 7 + 13) % len(all_chars)
    password += all_chars[index]
print("Generated Password:", password)