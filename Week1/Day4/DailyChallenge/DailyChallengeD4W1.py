import re

MATRIX_STR = '''
7ii
Tsx
h%?
i #
sM 
$a 
#t%'''       

rows = MATRIX_STR.strip().split('\n')
num_columns = len(rows[0])
num_rows = len(rows)
column_text = ""
for col in range(num_columns):
    for row in range(num_rows):
        column_text += rows[row][col] 

decoded_message = re.sub(r'(?<=[A-Za-z])[^A-Za-z]+(?=[A-Za-z])', ' ', column_text) 
final_message = re.sub(r'^[^A-Za-z]+|[^A-Za-z]+$', '', decoded_message)     
print(final_message)
