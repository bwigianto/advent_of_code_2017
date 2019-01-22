def power(x, y, serial):
    return (int((((x + 10) * y + serial) * (x + 10))/100) % 10) - 5

serial = 6303
xysize_power = {}

def power_size(x, y, size, serial):
    if (x, y, size) in xysize_power:
        return xysize_power[(x, y, size)]
    if size == 1:
        ans = power(x, y, serial)
        xysize_power[(x, y, size)] = ans
        return ans
    bottom_left = sum([power_size(x + i, y + size - 1, 1, serial) for i in range(size)])
    top_right   = sum([power_size(x + size - 1, y + i, 1, serial) for i in range(size)])
    ans = power_size(x, y, size - 1, serial) + bottom_left + top_right + power_size(x + size - 1, y + size - 1, 1, serial)
    xysize_power[(x, y, size)] = ans
    return ans

max_coordinates = (1, 1, 1)
max_power = - float("inf")
for size in range(1, 301):
    print(size)
    for x in range(1, 301 - size):
        for y in range(1, 301 - size):
            p = power_size(x, y, size, serial)
            if p > max_power:
                max_power = p
                max_coordinates = (x, y, size)

print(max_coordinates)
print(max_power)
        
