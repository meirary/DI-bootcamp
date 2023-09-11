matrix = [
        ["7","i","i"],
        ["T","s","x"],
        ["h","%","?"],
        ["i","","#"],
        ["s","M",""],
        ["$","a",""],
        ["#","t","%"],
        ["^","r","!"],
    ]

decoded_message = ""

num_rows = len(matrix)
num_cols = len(matrix[0])

for col in range(num_cols):
    column_text = ""
    for row in range(num_rows):
        char = matrix[row][col]
        if char.isalpha():
            column_text += char 
        else:
            column_text += " "  
    
    decoded_message += column_text + ""  

print(decoded_message)
