#Take text input and arrange in array
def convert_to_world(text, world):
    col1 = []
    col2 = []
    col3 = []
    col4 = []
    for line in text.splitlines():
        print(line)
        for col in range(0,4):
            length = len(line)
            print(col)
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
    print(new_world)
    return new_world

def remove_air(column):
    length = len(column)
    new_list = []
    for value in column:
        if value != " ":
            new_list.append(value)
    for position in range(len(new_list), length):
        new_list.append(" ")
    return new_list

def combine_dots(column):
    print(column)
    length = len(column)
    skip = False
    for position in range(0, length):
        #print(column[position])
        if skip == False:
            #print(column[position])
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
world = []
text='''. .
. .
 :T.
. .
.'''

world = convert_to_world(text, world)
print("Next Function")
print(world)
newworld = apply_gravity(world)



