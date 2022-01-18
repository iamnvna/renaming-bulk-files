import os

def main():
    i = 0;
    path = "C:/Users/cobbi/Desktop/Learn/renaming-bulk-files/Path/"
    for all in os.listdir(path):
        nameformat = "WillinPains_" + str(i) + ".jpg"
        source = path + all
        destination = path + nameformat
        os.rename(source, destination)
        i += 1

if __name__ == "__main__":
    main()

## Commentary
"""
Line 1:
    The os library is imported to allow the code access the system's OS
    and perform some functions.

Line 3:
    The main function is defined to hold the block of code to execute
    the required task.

Line 4:
    i is a global variable defined outside the for loop to allow for
    increments by one as the loop continues to run.

Line 5:
    The path to the folder where the files to be renamed are located is 
    passed into the declared variable, path.

Line 6:
    The for loop is created using functions of the os library to iterate
    all the files in the folder.

Line 7:
    The specified naming convention or format is assigned to the variable
    name format.
    
Line 8: 
    The source variable holds the absolute path to a file in the folder 
    or directory at each iteration.

Line 9:
    The destination variable holds the absolute path to a file in the folder
    or directory after it has been renamed. The destination path is concatenated
    with the nameformat variable after each iteration.

Line 10: 
    The os library function rename is used to rename all source paths (files) 
    to the destination paths (files)

Line 11:
    This is an increment operator to help run through the loop. Note: i is the
    global variable declared in line 4.
    
Line 13: 
    The if condition statement here crosschecks to be sure if the code is 
    imported or not. Since the __name__ variable returns __main__ by default, 
    this block of code would run because the boolean function above results
    to true. 
"""