import math
 #exercise 1
C = 50
H = 30
D = input ("Write a number: ").split(", ")
for one in D:
    calculation = math.sqrt(2*C*int(one)/H)
    print (int(calculation))


#exercise 2
q = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 

print(q)
print(sorted(q, reverse=True))
print ([sum(q)])
print ([q [0], q [-1]])

r = []
for i in q:
    if i > 50:
        r.append(i)
print (r)

t = []
for u in q:
    if u <10:
        t.append(u)
print (t)

s = []
for p in q:
    k = (p**2)
    s.append(k)
print (s)

aver = sum (q)/len(q) 
print (aver)

print (max(q))
print (min(q))

#exercise 3

text_online = "Instead of using pre-defined lists of numbers, ask the user for 10 numbers between -100 and 100. Ask the user for an integer between -100 and 100 repeat this question 10 times. Each number should be added into a variable that you created earlier."

charac_count = len(text_online)
print (charac_count)

sentence = text_online.split(". ") #to count sentences
print (len(sentence))

wordes = text_online.split() #to count words
for i in wordes:
    averg = len(wordes) / len(sentence) #average words in sentences
print (int(averg)) 

aa = [] #non white-space characters 
for f in text_online:
    if f != " ":
       aa.append(f)
print(len(aa))

nonunique_word = ["user", "number", "of", "the", "and"]

rtl = []
for wf in wordes:
    if wf not in nonunique_word:
        rtl.append(wf) 
print (len(rtl))    






