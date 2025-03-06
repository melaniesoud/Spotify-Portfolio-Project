
import numpy as np
import matplotlib.pyplot as plt

column_names = ['title', 'artist(s)', 'release', 'num_of_streams', 'bpm', 'key', 'mode', 'danceability', 'valence', 'energy', 'acousticness', 'instrumentalness', 'liveness', 'speechiness']
data = np.genfromtxt('spotify_data.csv', delimiter = ',', skip_header = True, dtype = str)

# DEFINE FUNCTIONS
def feature_stats(input_value):
    '''
    The purpose of this function is to take in an input value that corresponds to a position in each row in the given data set 
    under spotify_data.csv in order to create a new array with all of the corresponding data from the row value inputted. That inputted value/position of data in each row in the data set
    are then compiled into an array where the maximum, minimum, average, and index of the highest value in the array are found. A for loop
    is created to go through each row in the data set and to take the column values to do calculations. Each calculation (maximum, minimum, average, index of song with the highest value) are assigned a variable
    which is set to 0 outside of the for loop. Once the value is calculated, the variables outside of the for loop are updated, and then these variables are reassigned more appropriate names according to the purpose of the calculation.
    
    
    Paramaters: input_value (int): This comes from the main function. This input_value is named "selection" in the main function and is what is taken in for the function. That selection value is used to indicate the column in each row in the data set.
    
    Return: index_highest_value (int): This is the index of the song with the highest value.
    
     '''
    import math    # Import math in order to use math.floor to round down the float that would be outputed when the mean value is calculated.
    a = 0          # Set a variable a equal to 0 outside of the for loop. This will be updated with the minimum value calculated within the for loop.
    b = 0          # Set a variable b equal to 0 outside of the for loop. This will be updated with the maximum value calculated within the for loop.
    c = 0          # Set a variable c equal to 0 outside of the for loop. This will be updated with the mean/average value calculated within the for loop.
    d = 0          # Set a variable d equal to 0 outside of the for loop. This will be updated with the index value of the song with maximum value calculated within the for loop.
    for row in data:    # Create a for loop that goes through each column of each row within the data set.
        converted_data_feature = np.array([row[input_value] for row in data], dtype='int') # This line of code is used to take in the input value as the column number in each row in the data set, and to take those values from that column of each row and compile it into a new array. The data type is also converted to integers and this new array is called: converted_data_feature.
        a = min(converted_data_feature)     # With the new array that was created from the column values(converted_data_feature), the minimum value is found and is labeled as the variable a. This updates the value of a outside the for loop above it.
        b = max(converted_data_feature)     # With the new array that was created from the column values(converted_data_feature), the maximum value is found and is labeled as the variable b. This updates the value of b outside the for loop above it.
        c = sum(converted_data_feature)/len(converted_data_feature)   # With the new array that was created from the column values (converted_data_feature), the average/mean value is found by taking the sum of all the column values and dividing it by the length of the array. This value is labeled as the variable c. This updates the value of c outside the for loop above it.
        d = np.where(converted_data_feature == b)           # With the new array that was created from the column values (converted_data_feature), the index value of the row containing the maximum value is found and is labeled as the variable d. This updates the value of d outside the for loop above it.
    
    highest_value = b           # The variable b is renamed as highest_value.
    lowest_value = a            # The variable a is renamed as lowest_value.
    mean_value = math.floor(c)  # The value for variable c is rounded down in order to obtain the desired answer in an integer, not a float, and this value is renamed mean_value.
    index_highest_value = d     # The variable d is renamed as index_highest_value.

    print(f'Highest value: {highest_value}') # The desired output statement for highest_value is printed.
    print(f'Lowest value: {lowest_value}')   # The desired output statement for lowest_value is printed.
    print(f'Mean value: {mean_value}')       # The desired output statement for mean_value is printed.
    return index_highest_value               # The index value is returned.
   

def age_stats(input_value):
    '''
    The purpose of this function is to take in an input value and use that value as the column number in each row in the data set in order to 
    execute calculations with the values in that column. A for loop is created to go through each row in the data set in order to create a new array with the column values. 
    Within the for loop, the maximum and minimum values are found, including the index of the row with the minimum value corresponding to the column. The difference between the minimum and maximum values
    is used to find the span of years of the songs within the spotify data. This value (for the span of years) is printed within an output statement. The index is used to give the Artist name, Key, and mode of the oldest song (minimum value) in the spotify data. 
    These values are also printed in an output statement.
    
    Parameters: input_value (int): This input value comes from selection in the main function. It is used to find the column position in the rows of the data set.
    
    Return: None (nothing is returned) 
    
    '''
    oldest_year = 0          # Set a variable oldest_year equal to 0 outside of the for loop. This will be updated with the minimum value calculated within the for loop.
    recent_year = 0          # Set a variable recent_year equal to 0 outside of the for loop. This will be updated with the maximum value calculated within the for loop.
    index_oldest_song = 0    # Set a variable index_oldest_year equal to 0 outside of the for loop. This will be updated with the index value of the oldest song (minimum) calculated within the for loop.
    for row in data:         # Create a for loop for each row in the data set in order to go through each row to create an array with the column values.
        converted_data_age = np.array([row[input_value] for row in data], dtype='int')   # This line of code is used to take in the input value as the column number in each row in the data set, and to take those values from that column of each row and compile it into a new array. The data type is also converted to integers and this new array is called: converted_data_age.
        oldest_year = min(converted_data_age)   # With the new array that was created from the column values(converted_data_age), the minimum value is found and is labeled as oldest_year. This updates the value of oldest_year outside the for loop above it.
        recent_year = max(converted_data_age)   # With the new array that was created from the column values(converted_data_age), the maximum value is found and is labeled as recent_year. This updates the value of recent_year outside the for loop above it.
        index_oldest_song = np.where(converted_data_age == oldest_year)  # With the new array that was created from the column values(converted_data_age), the index of oldest_song is found and is labeled as index_oldest_song. This updates the value of index_oldest_song outside the for loop above it.
    
    span_years = recent_year - oldest_year  # The span of years for the songs within the spotify data is calculated by fidning the difference between recent_year and oldest_year.

    print(f'Span of years: {span_years}')   # Print the desired output statement for span_years.
    artist = data[index_oldest_song, 1]     # The artist of the oldest song is found by taking a point in the data set by having the value of the row and column number (with the artist name) in square brackets (data[row, column]).
    key = data[index_oldest_song, 5]        # The key of the oldest song is found by taking a point in the data set by having the value of the row (the index of the oldest song) and column number (with the key) in square brackets (data[row, column]).
    mode = data[index_oldest_song, 6]       # The mode of the oldest song is found by taking a point in the data set by having the value of the row (the index of the oldest song) and column number (with the mode) in square brackets (data[row, column]).
    print(f'Artist of oldest song: {artist[0,0]}')   # The desired output statement is printed as the artist data in the fomrat of a 1 by 1 matrix (represented by artist[0,0]).
    print(f'Key and mode of oldest song: {key[0,0]} {mode[0,0]}')  # The desired output statement is printed as the key and mode data in the fomrat of a 1 by 1 matrix (represented by key[0,0] and mode[0,0]).

# DEFINE MAIN CODE
def main():
    ''' 

    The purpose of this function is to ask the user to input a certain value, and to take that input value to find certain data from the spotify_data.csv.
    A while loop is created in order to keep prompting the user to input a value after the desired output is outputted, except for when the input is equal to -1. Since the 
    while loop condition is selection cannot equal to -1, when the selection does equal to -1, the loop is broken and the code exits the loop. Then, an if statement outside of the while loop is run where the code runs to output a graph. Finally, the code ends and the user is not repromted to input a value.
    When the selection is equal to 2, the input value of 2 is the input for age_stats() which outputs the span of years and the artist, key, and mode of the odlest song.
    When the selection is equal to 0, 1, 5, and 6, the input message is reprompted. 
    When the selection is equal to 3, 4, and 7 to 13, that value becomes the input value for feauture_stats() and the column number of the rows within the data set. The highest, lowest, and mean values are printed while the index is of the song with the highest value is returned.
    When the user inputs an invalid input, an error message is outputted and the input massage is repromted.
    
    Parameters: selection (int): this input value is inputed by the user, which then tells the program what it has to do.
    
    Return: None (returns nothing)
    
    '''
    print("Spotify Statistics\n")  # Welcome statement is printed.
    print("Song analysis options: ")        # Print statement in quotations.
    for menu, option in enumerate(column_names):  # enumerate numbers each menu option starting from 0.
         print(menu, option)                      # The menu options are printed.
    print("Choose -1 to end the program.")        # The condition regarding inputting -1 is printed.
    
    selection = 0  # Outside of the While loop, user input selection is set to 0, which will later be updated each time the user is repromted to input a number.
    while (selection != -1):     # States the conditions that the code will run in the While loop while the selection is not equal to -1. If the selection does equal to -1, the while loop is broken and the code runs and if statement outside of the while loop in order to output a Danceability vs BPM graph. Tnen the code ends and the user is not reprompted to input a value.
        selection = int(input("\nPlease enter a song feature to analyze: ")) # Selection is equal to the integer inputted by the user. An input statement is printed to prompt the user to input an integer value.
        if (selection == -1):    # If-else statements are used to take in the user input and output the desired data. This if statement runs on the condition that selection equals -1.
            break                # Once the desired output (graph) is outputted, break the the code and the loop is exited. This results in the code ending. 

        elif (selection == 2):   # If-else statements are used to take in the user input and output the desired data. This if statement runs on the condition that selection equals 2.
            age_stats(selection) # the age_stats() function is called and the input of 2 is taken into the function to print the desired data on span of years and oldest song artist, key, and mode.
            
        elif (selection == 3) or (selection == 4) or (selection >=7 and selection <=13):  # If-else statements are used to take in the user input and output the desired data. This if statement runs on the condition when selection equals 3, 4, or 7 to 13.
            song_index = data[feature_stats(selection), 0]                                # This section of code takes the input value into the function feature_stats() and the input value corresponds to the column value for the rows in the data set to output the desired data. This line of code finds the song at the returned index value. The format is data[row, column] so the index value returned by feature_stats(selection) is the row value, while 0 is the column value, which is the song name. This is labeled as song_index which mean the song at that certain index value.
            print(f'Top song in selected feature: {song_index[0, 0]}')   # An output statement is printed with song_index (song name) being formatted as a 1 by 1 matrix (represented as [0,0]).             

        elif (selection == 0) or (selection == 1) or (selection == 5) or (selection == 6):  # If-else statements are used to take in the user input and output the desired data. This if statement runs on the condition that selection equals 0, 1, 5, or 6.
           pass     # When the selection (user input) is 0, 1, 5, or 6, pass is used to remain in the loop but just reprompt the user to input a value for selection.

        else:       # This else statement is for when the user inputs seomthing that is not in the conditions of the previous if-else statements.
            print('You must enter a valid menu option.\n')  # An error message is outputted, telling the user to input a valid menu option.
            continue # The code is continued in order to repromt the user to input a value for the menu options.
    
            
    if (selection == -1): # Since the While loop ran on the condition that selection does not equal -1, when the code does equal to -1, the While loop was broken, leaving the while loop and instead, running the code in this if statement. 

        for row in data:  # This ensure that the desired values are found within the columns for each row in the data set.
            bpm = np.array([row[column_names.index('bpm')] for row in data], dtype='float')              # Using the provided code above, a new array is formed for BPM and the inputted column value for row in data is the index value for the column name: 'bpm'. The data will be in the new array as a float type.
            dance = np.array([row[column_names.index('danceability')] for row in data], dtype='float')   # Using the provided code above, a new array is formed for Danceability and the inputted column value for row in data is the index value for the column name: 'danceability'. The data will be in the new array as a float type.

        plt.scatter(bpm, dance, s=5, label = 'Song stats')   # This creates a scatter plot with bpm in the x-axis, danceability on the y-axis, a font size of 5, and the label for the legend.
        plt.xlabel('BPM')           # Labels the x-axis as 'BPM'.
        plt.ylabel('Danceability')  # Labels the y-axis as 'Danceability'.
        plt.title('Danceability vs. Beats per Minute')  # Labels the title of the graph as 'Danceability vs. Beats per Minute.' 
        plt.legend(loc='upper right')    # The location of the legend is positioned at the upper-right corner.
        plt.show()                       # The graph is shown.
            
    # Create and print danceability vs. bpm plot
