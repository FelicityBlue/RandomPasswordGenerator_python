import pandas as pd
import random as rd

# read csv
df = pd.read_csv(r'password_codes.csv')

# Generate a list
characters = []


def random_char_generator(column_num, end):
    # Generate random numbers for row index
    rand_num = rd.randint(0, end)

    # adding entries to the list called characters
    if column_num == 2:

        # add this to get rid of decimal place
        addChar = int(df.iloc[rand_num, column_num])
    else:
        addChar = df.iloc[rand_num, column_num]

    # Add the character to the list
    characters.append(addChar)


for column in range(0, 4):
    for i in range(0, 3):
        random_char_generator(column, df.iloc[:, column].count() - 1)

password = ""
for i in range(0, len(characters)):
    # Get a random index & add the entry to the string
    length = len(characters) - 1
    num = rd.randint(0, length)
    password += str(characters[num])

    # remove the entry in the characters
    characters.pop(num)
    length -= 1

# Print the password for the user
print("The password: " + password)
