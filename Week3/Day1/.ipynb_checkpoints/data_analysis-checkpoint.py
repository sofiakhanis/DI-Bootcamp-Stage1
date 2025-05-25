import pandas as pd

#pd.Series
data = pd.Series ([1, 2, 3, 4])
print (data) 
#output:
#0    1
#1    2
#2    3
#3    4


#pd.Frame
data1 = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'Donna', 'Emily'],
    'Age': [28, 34, 29, 32, 25, 45],
    'City': ['New York', 'Paris', 'Berlin', 'London', 'Tokyo', 'Moscow']
}
accessed_to_data1 = pd.DataFrame(data1)
print (accessed_to_data1)
#output:
#    Name  Age      City
#0   John   28  New York
#1   Anna   34     Paris
#2  Peter   29    Berlin
#3  Linda   32    London
#4  Donna   25     Tokyo
#5  Emily   46    Moscow

ages = accessed_to_data1['Name'] #access to only one column
print (ages)

accessed_to_data1.sort_values (by='Age') #sort by 'Age' column increasing

print(accessed_to_data1[accessed_to_data1 ['Age'] > 30]) #access to specific condition
#output:
#    Name  Age    City
#1   Anna   34   Paris
#3  Linda   32  London
#5  Emily   45  Moscow

#THE DIFFERENCE

print(accessed_to_data1 ['Age'] > 30) 
#output: 
#0    False
#1     True
#2    False
#3     True
#4    False
#5     True
#Name: Age, dtype: bool

data2 = {
    'Book Title': ['The Great Gatsby', 'To Kill a Mockingbird', '1984', 'Pride and Prejudice', 'The Catcher in the Rye'],
    'Author': ['F. Scott Fitzgerald', 'Harper Lee', 'George Orwell', 'Jane Austen', 'J.D. Salinger'],
    'Genre': ['Classic', 'Classic', 'Dystopian', 'Classic', 'Classic'],
    'Price': [10.99, 8.99, 7.99, 11.99, 9.99],
    'Copies Sold': [500, 600, 800, 300, 450]
}

df = pd.DataFrame(data2)

print (df)

print(df.head(0)) #only first row

print (df.describe()) 
print (df.info()) #shows data about the frame

print (df.sort_values(by='Price'))
print (df.sort_values(by='Copies Sold'))

print(df[df.Genre == 'Classic']) #sort by specific word inside a column

print(df.groupby(by='Author')['Copies Sold'].sum()) #to group and show the table

