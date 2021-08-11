import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june']

days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please, pick a city from (chicago, new york, washington)").lower()
        if city not in CITY_DATA:
            print("Invalid city, please try again")           
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please, pick a month from juanuray to june, you can also display all by typing 'all': ").lower()
        if (month != 'all') and (month not in months):
            print("Invalid month, please choose from january to june, you can also display all by typing 'all'")
        else:
            break
                  

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Pick a day of the week or type 'all' to display all days: ").lower()
        if day != 'all' and day not in days:
            print("Invalid day, please try again")
        else:
            break

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
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Loading data into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month from Start Time to create a month column
    df['month'] = df['Start Time'].dt.month
    
    # extract day from Start Time to create day column
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter by month if applicable
    if month != 'all':
        # use the index months list to get the corresponding int
        month = months.index(month) + 1
        # filter by months to create the new data frame
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
                  
    return df

def display_raw_data(df):
    """ Displaying rows of data based on user's input """
    i = 0
    raw = input("Would you like to display the first 5 rows of data? yes/no").lower() 
    pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df[i:i+5]) 
            raw = input("Would you like to display the following 5 rows of data? yes/no").lower()
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month: ", common_month)              

    # TO DO: display the most common day of week

    common_day = df['day_of_week'].mode()[0]
    print("The most common day: ", common_day)
                  
    # TO DO: display the most common start hour
    # Create an hour column from Start Time
    df['hour'] = df['Start Time'].dt.hour
    # Calculation
    common_hour = df['hour'].mode()[0]
    print("The most common hour: ", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print("The most common start station: ", common_start)
    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('The most common end station: ', common_end)

    # TO DO: display most frequent combination of start station and end station trip
    common_combination = df.groupby(['Start Station','End Station']).size().idxmax()[0]
    print('The most frequent combination of start-end station: ', common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total travel time: ', int(total_time/3600), ' hours')

    # TO DO: display mean travel time
    time_mean = df['Trip Duration'].mean()
    print('Average traveling time: ', time_mean/3600, ' hours')
                  
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df['User Type'].value_counts()

    print('Counts of user types: ', user_types_count)

    # TO DO: Display counts of gender
    # No gender column in washington file. Using if statement to avoid errors. 
    if 'Gender' in df:             
        gender_count = df['Gender'].value_counts()
        print('Counts of gender: ', gender_count)

    # TO DO: Display earliest, most recent, and most common year of birth
    # No birth year column in washington file. Using if statemtment to avoid errors.              
    if 'Birth Year' in df: 
        earliest_birth_year =int(df['Birth Year'].min())
        print('Earliest birth year: ', earliest_birth_year)          
        recent_birth_year = int(df['Birth Year'].max())
        print('Most recent birth year: ', recent_birth_year)
        common_birth_year = int(df['Birth Year'].mode()[0])
        print('Most common birth year: ', common_birth_year)
                  
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

             
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        while restart.lower() != 'yes' and restart.lower() != 'no':
            print("Invalid input, please make sure you type either 'yes' or 'no'.")
            restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
    

if __name__ == "__main__":
    main()
