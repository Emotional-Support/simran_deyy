num = int(input("Enter a number: "))
num_list = [str(k) for k in range(num, 0, -1)]
for i in range(num + 1):
    x = ""
    y = " "
    for n in range(i + 1):
        x += num_list[n]
    y = y * (num - (i + 1))
    print(y + x)
#    print(y + x)

# num = int(input("Enter a number: "))

# for i in range(1, num + 1):
#     x = ""
#     y = " " * (num - i)
#     for n in range(num, num - i, -1):
#         x += str(n)
#     print(y + x)
