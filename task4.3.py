list_input = input("Enter the list:").split(" ")
list_1 = list(map(int, list_input))
if max(list_1) <= 0:
    print(1)
else:
  for item in range(1, max(list_1)):
    if item not in list_1:
        print(item)
        break

