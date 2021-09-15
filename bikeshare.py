import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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


    city = input('Would you like to see the data for Chicago, New York or Washington? ').lower()
    while city not in ['Chicago', 'New York', 'Washington']:
        print('Please try again')
        city = input('Would you like to see the data for Chicago, New York or Washington? ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Which month would you like to see (January - June)? ').title()
    while month not in ['January', 'February', 'March', 'April', 'May', 'June', 'All']:
        print('Please try again')
        month = input('Which month would you like to see (January - June)? ').title()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Which day of the week would you like to see?').title()
    while day not in ['All', 'Sunday' 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']:
        print('Please try again')
        day = input('Which day of the week would you like to see? ').title()
        weekdays = def choice(prompt, choices)

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

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'All':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'All':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    pop_month = df.loc[:,'month'].mode()[0]
    print('The most popular month is: {}'.format(pop_month))

    # TO DO: display the most common day of week
    pop_day = df.loc[:, 'day_of_week'].mode()[0]
    print('The most popular day is: {}'.format(pop_day))

    # TO DO: display the most common start hour
    pop_hour = df.loc[:, 'hour'].mode()[0]
    print('The most popular hour is: {}'.format(pop_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    pop_start = df.loc[:, 'Start Station'].mode()[0]
    print('The most popular start station is: {}'.format(pop_start))

    # TO DO: display most commonly used end station
    pop_end = df.loc[:, 'End Station'].mode()[0]
    print('The most popular end station is: {}'.format(pop_end))

    # TO DO: display most frequent combination of start station and end station trip
    df['start_end'] = df['Start Station'] + ' - ' + df['End Station']
    pop_start_end = df.loc[:, 'start_end'].mode()[0]
    print('The most popular start and end station combination is: {}'.format(pop_start_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_trip_time = df.loc[:, 'Trip Duration'].sum()
    print('The total travel time is: {}'.format(tot_trip_time))

    # TO DO: display mean travel time
    mean_trip_time = df.loc[:, 'Trip Duration'].mean()
    print('The mean travel time is: {}'.format(mean_trip_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    try:
        """Displays statistics on bikeshare users."""
        print('\nCalculating User Stats...\n')
        start_time = time.time()

    # TO DO: Display counts of user types
        user_types = df.loc[:, 'User Type'].value_counts()
        print('\nUser Types: \n{}'.format(user_types))

    # TO DO: Display counts of gender
        gender_types = df.loc[:, 'Gender'].value_counts()
        print('\nGender types: \n{}'.format(gender_types))

    # TO DO: Display earliest, most recent, and most common year of birth
        early_year = df.loc[:, 'Birth Year'].min()
        recent_year = df.loc[:, 'Birth Year'].max()
        common_year = df.loc[:, 'Birth Year'].mode()
        print('\nThe earliest year of birth is {}'.format(int(early_year)))
        print('\nThe most recent year of birth is {}'.format(int(recent_year)))
        print('\nThe most common year of birth is {}'.format(int(common_year)))

        print("\nThis took %s seconds." % (time.time() - start_time))
    except:
        print('\nThis is all of user info available for the selected city')

    finally:
        print('-'*40)

view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
start_loc = 0
while(   ): #add into it.
    print(df.iloc[   ] #add into it.
    start_loc += 5
    view_data = input("Do you wish to continue?: ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
