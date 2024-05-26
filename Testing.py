# temporary challenge projects for learning
# and strengthening fundamental knowledge


# Challenge 1
# make a program that returns int values into string written version
# Example:
# input: 1234
# output: One Two Three Four

# Step 1 define dictionary with num for keys and the string for the value
nums = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    0: "Zero",
}

# request input
user_input = int(input("Phone: "))
# loop through input and display
for num in list(str(user_input)):
    num = int(num)
    print(f"{nums[num]} ")
