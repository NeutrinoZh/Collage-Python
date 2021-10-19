for i in range(1, 16, 2):
    print(f"{' ' * (16 - i)} {'X' * i * 2}")
for i in reversed(range(3, 16, 2)):
    print(f"{' ' * (16 - i)} {'X' * i * 2}")