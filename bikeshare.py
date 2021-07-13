import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities=['chicago','new york city','washington']
months=['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December','All']
days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        city=str(input('What city you are interested in? Chicago, New York City or Washington? ')).lower()
        if city not in cities:
            print('Invalid city name')
        else:
            break

    while True:
        month=str(input('If you would like to filter by month, type out the month and if not, type out "all"\n')).title()
        if month not in months:
            print('Invalid month name')
        else:
            break

    while True:
        day=str(input('If you would like to filter by month, type out the month and if not, type out "all"\n')).title()
        if day not in days:
            print('Invalid day')
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
                      
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'All':
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'All':
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month']= df['Start Time'].dt.month
    df['day_of_week']= df['Start Time'].dt.weekday_name
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    month_mode=df['month'].mode()[0]
    print('The most common month: ' + months[month_mode-1])
    
    print('The most common day: ' + df['day_of_week'].mode()[0])
    
    df['hour'] = df['Start Time'].dt.hour
    print('The most common start hour: ' + format(df['hour'].mode()[0]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    print('The most common start station: ' + df['Start Station'].mode()[0])
    
    print('The most common end station: ' + df['End Station'].mode()[0])
    
    most_common_combination = df['Start Station'].map(str) + ' to ' + df['End Station']
    print('The most popular combination: ' + most_common_combination.mode()[0])
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    total_m, total_s = divmod(df['Trip Duration'].sum(), 60)
    total_h, total_m = divmod(total_m, 60)
    print ('Total travel time: ',total_h,' hours, ', total_m,' minutes, and ', total_s,' seconds.')
    
    mean_m, mean_s = divmod(df['Trip Duration'].mean(), 60)
    mean_h, mean_m = divmod(mean_m, 60)
    print ('Mean travel time: ',mean_h,' hours, ', mean_m,' minutes, and ', mean_s,' seconds.')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    print('The user can be broken down into \n{}'.format(df['User Type'].value_counts()))
    
    if('Gender' not in df):
        print('Sorry! There is not any available gender data for this City')
    else:
        print('The genders are \n{}'.format(df['Gender'].value_counts()))
    
    if ('Birth Year' not in df):
        print('Sorry! There is not any available gender data for this City')
    else:
        print('The Earliest birth year: {}'.format(df['Birth Year'].min()))
        print('The most recent birth year: {}'.format(df['Birth Year'].max()))
        print('The most common birth year: {}'.format(df['Birth Year'].mode()[0]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data(df):

    print(df.head())
    num = 0
    while True:
        view_raw_data = input('\nWould you like to view five row of raw data? Enter "yes" or "no"\n')
        if view_raw_data.lower() != 'yes':
            return
        num = num + 5
        print(df.iloc[num:num+5])
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