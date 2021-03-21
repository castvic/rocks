#   Functions for rocks.py  
# 
#   Overall TODOs
#   TODO:   Create function to process input to identify characters
#           that are invalid input and return an error (error handling)
#           in general
#   TODO:   Add a ground tracking list to improve performance
#   TODO:   Make world expandable to a dynamic width
#   TODO:   Fix variable names for those that should be private
#   TODO:   Fix Table handling - Misread rules on how tables are
#           handled and assumed restriction was applied only to
#           columnd
#   
#   Take string text input and convert it to an array that represents
#   a world and return resultant array
def convert_to_world(text):
    col1 = []
    col2 = []
    col3 = []
    col4 = []
    for line in text.splitlines():
        for col in range(0,4):
            length = len(line)
            if col >= length:
                if col == 1:
                    col2.insert(0, " ")
                    col3.insert(0, " ")
                    col4.insert(0, " ")
                if col == 2:
                    col3.insert(0, " ")
                    col4.insert(0, " ")
                if col == 3:
                    col4.insert(0, " ") 
            elif col == 0 and col < length:
                col1.insert(0,line[col])
            elif col == 1 and col < length:
                col2.insert(0,line[col])
            elif col == 2 and col < length:
                col3.insert(0,line[col])
            elif col == 3 and col < length:
                col4.insert(0,line[col])
    world = [col1, col2, col3, col4]
    return world

# Apply the rules for handling gravity by removing " " elements in
# list and adding the " " (air) elemnts back on top return 
# resultant world
# 
# TODO: Fix table handling to apply to whole world rather than just
#       Column

def apply_gravity(world):
    new_world = []
    for column in world:
        if column.count("T") == 0:
            column = remove_air(column)
            column = combine_dots(column)
        elif column.count("T") == 1:
            table_location = column.index("T")
            below_table = column[0:table_location]
            below_table = remove_air(below_table)
            below_table = combine_dots(below_table)
            above_table = column[table_location:len(column)]
            above_table = remove_air(above_table)
            above_table = combine_dots(above_table)
            column = below_table + above_table
        new_world.append(column)
    return new_world

# Remove air " " from list and return list
def remove_air(column):
    length = len(column)
    new_list = []
    for value in column:
        if value != " ":
            new_list.append(value)
    for position in range(len(new_list), length):
        new_list.append(" ")
    return new_list

# Take the input of a column list and return a list that has rocks
# combined into ":"
def combine_dots(column):
    length = len(column)
    skip = False
    for position in range(0, length):
        if skip == False:
            if column[position] == "." and column[position+1] == ".":
                column[position] = ":"
                column[position+1] = " "
                skip = True
        else:
            skip = False
    column = remove_air(column)    
    for position in range (len(column), length):
        column.append(" ")
    return column

# Take in a world array and and return a string formatted world
def world_to_string(world):
    world_string = ""
    column_heights = columns_max_height(world)
    tallest_height = columns_tallest(column_heights)

    for height in range(tallest_height, 0, -1):
        for column in world:
            col_length = len(column)
            if height > col_length:
                world_string = world_string + " "
            else:
                world_string = world_string + column[height - 1]
        if height > 1:
            world_string = world_string + "\n"
    return world_string

# Find height for each column in array and return a list of heights
def columns_max_height(world):
    col_heights = []
    for column in world:
        col_heights.append(len(column))
    return col_heights

# Find the largest column in a list of column heights and return 
# an integer value of the tallest
def columns_tallest(column_heights):
    column_heights.sort()
    return column_heights[-1]


#
# Takes in two array worlds and stacks them on top of eachother
# to return a pre-gravity world.
def stack_worlds(original_world, new_world):
    result =[]
    for col in range(0,4):
        new_column = original_world[col] + new_world[col]
        result.append(new_column)
    return result


# testing functions
# 
# world = []
# text='''. .
# . .
#  :T.
# . .
# .'''

# world = convert_to_world(text)
# worlds = [world]
# print("Next Function")
# #print(world)
# newworld = apply_gravity(world)
# new_world_string = world_to_string(newworld)
# print(new_world_string)


