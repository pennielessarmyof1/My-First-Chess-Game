#First we will learn how to create a grid.
# A chessboard is 64 squares and we need to create a grid
# to represent each square. 

#In order to create a grid we have to create a nested-list.
# A nested-list is a list with other lists as its elements.
# The best way to think about nested lists is as a table.

#Understand that grids can be referenced or known as either
# a grid, table, or nested list. They are all the same but 
# for Clarity I will refer to them as tables.

#Tables represent a vital foundational aspect of coding. 
# Not everything is a table but most everything that you work 
# with is some type or form of a nested list. The code that we
# create is meant to populate, update, and transform these nested 
# lists and our ability to manipulate them ultimately determines 
# what we are able to create. 

#Lets start with a simple 3x3 structure. We refer to it as a structure
# because although we are creating a 3x3 table the first row of our
# table typically represents our column names. It is not uniform to 
# always have your first row represent your column names but it is 
# best practice because it allows others to easily understand what each
# row of data contains. 

student_data =[
        ['Name', 'Group', 'Age'],
        ['John', 'A', '25'],
        ['Mary', 'B', '27'] 
        ]

print(student_data)

# We use the '=' sign to designate a variable. Variables
# can be named anything. They are simply used to easily reference 
# the items that they represent and to provide a descriptive name that 
# indicates what kind of data the variable holds. Inside of variables 
# we can store integers, strings, floats, booleans, lists, tuples, 
# dictionaries, sets, objects, functions, placeholders, and 
# even create custom class types. 
#       *It is important to note that variables can be reassigned 
#       each time you use the '=' sign. Each time you do, you are 
#       re-declaring your variable. Be mindful not to frequently 
#       overwrite or accidentally erase your variable by declaring it     
#       multiple times.

# The first set of brackets[] designates the overall list. Each consecutive
# bracket represents a smaller list inside of that overall list.

# So here we can interpret this code as us having created a 
# nested-list entitled student_data in which each list inside represents a row 
# in the table and the first row represents the column names 
# in your table.

# We use print() to display the output of our code to the screen.

# Next, try creating your own 3x3 table or recreate student_data with more columns
# and rows or completely different data. Experiment and create what you want in 
# order to test what is possible and what is not.
