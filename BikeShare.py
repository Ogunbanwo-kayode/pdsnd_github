CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():


    print('Hello! Let\'s explore some US bikeshare data!')
    city = ""
    while city not in CITY_DATA.keys():
        
        print("Would you like to see data for Chicago, New York City, or Washington?")
        city = input().lower()
        print("your entry: ", city.title()) #this would display the result in title case

        if city not in CITY_DATA.keys():
            print("\nOops!!! That\'s not a valid a city name, please check your input")
            print("\nRestarting..............................")
            
    print(f"\nLooks like you want to hear about {city.title()}! If this is not true, please restart the program now")

    print("-" *100)

    # get user input for month (all, january, february, ... , june)
    month_info = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, "all" : 7}
    month = ''
    while month not in month_info.keys():
        print("\nWould you like to filter the data by month: (e.g May or may) OR by all i.e to apply no filter" )
        print("\nAvailable months are:\nJanuary, February,......June. Note: only full month name is allowed here")
        month = input().lower()
        print("You entry: ", month)

        if month not in month_info.keys():
            print("\nInvalid input. Please try again in the accepted input format.")
            print("\nRestarting..............")
            
        if month == "all":
            print(f"\nYou have chosen to view {month.title()} monthly information")
        else:
            print(f"\nYou have chosen {month.title()} as your preferred month.")
    

        
        



    print("*" * 40)


    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_info = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    while day not in day_info:
        print("\nPlease enter a day in the week of your choice for which you're seeking the data:")
        print("\nAccepted input:\nDay name; not case sensitive (e.g. monday or MONDAY).\nDay name in title case (e.g. Monday).")
        print("\n(You can also put 'all' or 'All' to view data for all days in a week.)")
        day = input().lower()
        print(day.title()) ## this would display the chosen day in title case
    

        if day not in day_info:
            print("\nInvalid input. Please try again in one of the accepted input formats.")
            print("\nRestarting................................................")  
        
        if day == "all":
            print(f"\nYou have chosen to view {day.title()} daily information") 
        
        else:
            print(f"\nYou have chosen {day.title()} as your preferred day.")

    


    print(f"\nYou have chosen to view data for city: {city.upper()}, month/s: {month.upper()} and day/s: {day.upper()}.")

    print('-'*40)
    return city, month, day
    
    


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    import pandas as pd
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df["Start Time"])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df["Start Time"].dt.month
    df['day_of_week'] = df["Start Time"].dt.dayofweek
    # Extract the hour from the start time column
    df["hour"] = df["Start Time"].dt.hour
   
    
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        #months = ['january', 'february', 'march', 'april', 'may', 'june']
        months = list({'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7})
        month = months.index(month) + 1
        
    
        # filter by month to create the new dataframe
        df = df[df["month"] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        days = list({"monday": 0, "tuesday": 1, 'wednesday' : 2, 'thursday' : 3, 'friday' : 4, 'saturday' : 5, 'sunday' : 6})
        day = days.index(day) + 1
        df = df[df["day_of_week"] == day]
    
    return df

## this is just a check for the above corrected functions

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel..........\n')
    import time
    start_time = time.time()

# display the most common month
    popular_month = df["month"].mode()[0]
    print(f"The Most Popular Month (1 = January,...,6 = June): {popular_month}")

# display the most common day of week
    popular_day_of_week = df["day_of_week"].mode()[0]
    print(f"\nMost Popular Day (Monday = 0,..... Sunday = 6): {popular_day_of_week}")

# display the most common start hour
    popular_hour = df["hour"].mode()[0]
    print(f"\nMost Popular Start Hour: {popular_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def station_stats(df):
    """Displays summary statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    import time
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df["Start Station"].mode()[0]
    print(f"\nMost Commonly Used Start Station: {popular_start_station}")

    # display most commonly used end station
    popular_end_station = df["End Station"].mode()[0]
    print(f"\nMost Commonly Used End Station: {popular_end_station}")


    # display most frequent combination of start station and end station trip
    df["Start To End"] = df["Start Station"].str.cat(df["End Station"], sep = " to ")
    start_to_end_combo = df["Start To End"].mode()[0]
    print(f"\nThe most frequent combination of start and end station trip: {start_to_end_combo}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def trip_duration_stats(df):
    """Displays summary statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration............\n')
    import time
    start_time = time.time()

    # display total travel time, also calculate the duration in minute, second and hour
    total_travel_time = df["Trip Duration"].sum()
    minute, second = divmod(total_travel_time, 60)
    hour, minute = divmod(minute, 60)
    print(f"The total travel time is {hour} hours, {minute} minutes and {second} seconds.")


    # display mean travel time, also calculate the mean travel time in minute, hour and second
    mean_travel_time = round(df["Trip Duration"].mean())
    avg_mins, avg_sec = divmod(mean_travel_time, 60)
    if avg_mins > 60:
        avg_hrs, avg_mins = divmod(avg_mins, 60)
        print(f"\nThe average travel time is {avg_hrs} hours, {avg_mins} minutes and {avg_sec} seconds.")
    else:
        print(f"\nThe average travel time is {avg_mins} minutes and {avg_sec} seconds.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    import time
    start_time = time.time()

    # Display counts of user types
    count_user_type = df["User Type"].value_counts()
    print(f"The count of each users types are displayed below:\n\n{count_user_type}")


    # Display counts of gender, since not all the df contain gender colume we may need to use the the try statement here
    try:
        count_gender = df["Gender"].value_counts()
        print(f"\nThe total count by gender are given below:\n\n{count_gender}")
    except:
        print("\nThere is no 'Gender' column found in this data.")


    # Display earliest, most recent, and most common year of birth
    try:
        earliest = round(df["Birth Year"].min())
        most_recent = round(df["Birth Year"].max())
        most_common_year = round(df["Birth Year"].mode()[0])
        print(f"\nThe earliest year of birth: {earliest}\n\nThe most recent year of birth: {most_recent}\n\nThe most common year of birth: {most_common_year}")
    except:
        print("No birth year information found in this data.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def show_raw_data(df):
    '''
    Displays the raw data used to compute the stats
    Input:
        the df with all the bikeshare data
    Returns: 
       none
    '''
    #drop all columns that were added to perform the required summary statistics
    df = df.drop(['month', 'day_of_week', 'hour'], axis = 1)
    row_index = 0

    display_data = input("\nWould you like to see 5 lines (rows) of the raw data used to compute the summary statistics? Please type 'yes' or 'no' \n")
    display_data = display_data.lower()
    while True:
        if display_data == 'no':
            return
        if display_data == 'yes':
            print(df[row_index: row_index + 5])
            row_index = row_index + 5
        display_data = input("\n Would you like to see five more rows of the data used to compute the stats? Please write 'yes' or 'no' \n").lower()
        
        print("-" * 80)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            
            
if __name__ == "__main__":
    main()
