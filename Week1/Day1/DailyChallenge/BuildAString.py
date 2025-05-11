string = input("Type the string (exactly 10 characters long!): ")
if len(string) < 10:
    print ("String not long enough.")
elif len(string) > 10:
    print ("String too long.")
else:
    print ("Perfect string!")
    print (string[0], string [9])
    for s in range(1, len(string) + 1):
        print (string [:s])
