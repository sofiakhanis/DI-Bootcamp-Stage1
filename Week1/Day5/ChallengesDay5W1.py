#challenge 1

def string_input ():
    string = str(input("Write different words, separate them by ', ': ").split(", "))
    string.sort()
    print (', '.join(string)) 
string_input() 

#challenge 2

def input_string ():
    user_string = input("Write a sentence: ").split()
    max_length = 0
    longest_word = ''
    for word in user_string:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)
    print(longest_word)
input_string ()


