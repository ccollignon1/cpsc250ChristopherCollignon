highway_number = int(input())

if (highway_number % 2) > 0:
    direction = 'north/south'
else:
    direction = 'east/west'

if highway_number > 99:
    if highway_number % 100 == 0:
        print(highway_number, "is not a valid interstate highway number.")
    else:
        print("I-" + str(highway_number) + " is auxiliary, serving I-" + str(highway_number % 100) + ", going",
              direction + ".")

elif highway_number > 0:
    print("I-" + str(highway_number) + " is primary, going", direction + ".")
else:
    print(highway_number, "is not a valid interstate highway number.")
