

def power(x, y, serial):
    return (int((((x + 10) * y + serial) * (x + 10))/100) % 10) - 5

print(power(3, 5, 8))

serial = 6303
max_coordinates = (1, 1)
max_power = - float("inf")
for x in range(1, 298):
    for y in range(1, 298):
        p = 0
        for i in range(3):
            for j in range(3):
                p += power(x + i, y + j, serial)
        if p > max_power:
            max_power = p
            max_coordinates = (x, y)

print(max_coordinates)
print(max_power)
        
