birth = input ("What is your birthday? Type like this: DD/MM/YYYY ").split("/")
print(birth)

age = list(str(2025 - int(birth[2])))
number_candles = int(age[1])

candles = "i" * number_candles if number_candles > 0 else "_"

print (f"_{candles}_\n"
      "|:H:a:p:p:y:|\n"
    "__|___________|__\n"
   "|^^^^^^^^^^^^^^^^^|\n"
   "|:B:i:r:t:h:d:a:y:|\n"
   "|                 |\n"
   "~~~~~~~~~~~~~~~~~~~\n")

