import os

for i in range(1, 101):
    os.rename(f"gugu_{i}_result.txt", f"gugu_{i}_dan.txt")
