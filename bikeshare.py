# Explore US Bikeshare Data - Udacity PDSND Project
# Created by Craig Hoopes on 10/10/2018 using Python 3.7

import time
import pandas as pd
import numpy as np
from datetime import timedelta

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

valid_months = ['january', 'february', 'march', 'april', 'may', 'june']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    month = "all"
    day = "all"

    print("\nHello! Let's explore some US bikeshare data!")

    # Get user input for city (chicago, new york city, washington).
    while True:
        city = input("\nWould you like to see data for Chicago, New York City, or Washington?\n")
        city = city.lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print("Please enter a valid city.\n")
            continue
        else:
            break

    while True:
        time_filter = input("\nWould you like to filter the data by month, day, or not at all?  Type \"all\" for no filter.\n")
        time_filter = time_filter.lower()
        if time_filter not in ('month', 'day', 'all'):
            print("Please enter a valid selection.\n")
            continue
        else:
            break

    # Get user input for month (january, february, ... , june)
    if time_filter == "month":
        while True:
            month = input("\nWhich month?  January, February, March, April, May, or June?\n")
            month = month.lower()
            if month not in valid_months:
                print("Please enter a valid month.\n")
                continue
            else:
                break

    # Get user input for day of week (monday, tuesday, ... sunday)
    if time_filter == "day":
        while True:
            day = input("\nWhich day?  Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n")
            day = day.lower()
            if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
                print("Please enter a valid day.\n")
                continue
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
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Filter by month if applicable
    if month != 'all':
<<<<<<< HEAD
        # Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
||||||| merged common ancestors
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
=======
        # use the index of the months list to get the corresponding int
        months = valid_months
>>>>>>> refactoring
        month = int(months.index(month) + 1)

        # Filter by month to create the new dataframe
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'all':
        # Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    months = valid_months
    popular_month = (months[df['month'].mode()[0] - 1]).title()
    print("Most popular month for traveling: ", popular_month)

    # Display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("Most popular day for traveling: ", popular_day)

    # Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_start_hour = df['hour'].mode()[0]
    print("Most popular hour of the day to start traveling: ", popular_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Most popular start station: ", popular_start_station)

    # Display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("Most popular end station: ", popular_end_station)

    # Display most frequent combination of start station and end station trip
    popular_trip = (df["Start Station"] + " to " + df["End Station"]).mode()[0]
    print("Most popular trip from start to end: ", popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_seconds = df['Trip Duration'].sum()
    tot_m, tot_s = divmod(total_seconds, 60)
    tot_h, tot_m = divmod(tot_m, 60)
    tot_d, tot_h = divmod(tot_h, 24)
    tot_w, tot_d = divmod(tot_d, 7)
    print("The total travel time is: {} seconds ({})".format(total_seconds, ("%dw %dd %dh %dm %ds" % (tot_w, tot_d, tot_h, tot_m, tot_s))))

    # Display mean travel time
    mean_seconds = df['Trip Duration'].mean()
    avg_m, avg_s = divmod(mean_seconds, 60)
    avg_h, avg_m = divmod(avg_m, 60)
    print("The average travel time is: {} seconds ({})".format(mean_seconds, ("%dh %dm %ds" % (avg_h, avg_m, avg_s))))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("\nNumber of users by type:\n")
    print(user_types)

    # Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print("\nNumber of users by gender:\n")
        print(gender)
    else:
        print("\nNo gender data available.\n")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = int(df['Birth Year'].describe()["min"])
        latest_year = int(df['Birth Year'].describe()["max"])
        popular_year = int(df['Birth Year'].mode()[0])
        print("\nAge data:\n")
        print("Oldest user was born in {}.".format(earliest_year))
        print("Youngest user was born in {}.".format(latest_year))
        print("Most popular birth year for users is {}.".format(popular_year))
    else:
        print("\nNo age data available.\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """Displays five lines of raw data at a time if user chooses."""

    count = 0

    view = input("\nWould you like to view the raw data? Enter yes or no.\n")
    if view.lower() == 'yes':
        print(df[count:count+5])
        count += 5
        while True:
            cont_view = input("\nView more? Enter yes or no.\n")
            if cont_view.lower() == 'yes':
                print(df[count:count+5])
                count += 5
            else:
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
