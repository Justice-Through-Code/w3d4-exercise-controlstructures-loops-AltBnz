
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']


def day_of_week():
    # Let's start simple, and build up from there.
    # 1.1 TODO: Write a for loop that prints out each day in the `days` variable above.
    for day in days:
        print(day)

    # 1.2 TODO: Write another for loop that does the same thing, but this time use the range function
    for day in range(len(days)):
        print(days[day])

def favorite_activities():
    # 2.1 TODO: Now, in a for loop, instead of just printing out the day,
    # let's ask the user what their favorite thing to do is on that day of the week.
    # NOTE: Make sure to use an f-string so that the user knows which day they're being asked about.
    
    favorite_user_activities = list()
    
    for day in days:
        prompt = f'What is your favorite thing to do on {day}s? '
        favorite_daily_activity = input(prompt)
    # We should keep track of the user's favorite things to do so that we can print them out all together.
    # 2.2 TODO: ABOVE your for loop, create a new empty list to hold the user's favorite activities.

    # 2.3 TODO: Now, back in your for loop, append each of the user's answers into your new list.
    # AFTER your loop, print out the list to check if it got populated correctly.
        favorite_user_activities.append(favorite_daily_activity)
    # 2.4: After the code you've written so far, let's create a new for loop.
    # As an example, let's say the user's favorite thing to do on Mondays is plan their week.
    #  This time, we want the output to be something like this:
    # f'On Mondays, your favorite activity is to plan your week.'
    # We need information from both lists! Let's use the `range` function to loop through the indexes
    # of the items in the lists (this will work because the lists are the same length).
    # Each time through this new loop, use the index number to index into each of your lists for the data
    # you need to print out.
    print(favorite_user_activities)
    for index in range(len(days)):
        activity = f'On {days[index]}s, your favorite activity is to {favorite_user_activities[index]}.'
        print(activity)


'''
    Take a look back at the code you just wrote. Look at how much it does!

    Often, programmers will be given large tasks, and it's our responsibility to be able to break it down into
    smaller pieces. We did the above piece by piece.  Now think about what the prompt might have been
    to get us there.

    Maybe: Write a program that asks the user about their favorite thing to do each day of the week.
    Afterward, print out for the user each of their favorite daily activities.

    Would this larger task have felt doable without breaking it down into steps?
    Is it clear what needs to be done?

    Try to break down the steps required for this second loop challenge.
'''
# day_of_week()
# favorite_activities()


def temp_by_day():
    # 3 TODO: Write a program that loops through the days in the week. Each day, ask the user what the temperature
    # is. If the temperature is below 50, tell the user to 'Brr, put on a jacket!'. Or, if the temperature is
    # between 50 and 65, tell the user to 'Cozy, grab a sweater'. Finally, if the temperature is above 65,
    # tell the user to 'Put on some sunscreen!'.
    for day in days:
        prompt = f'What is the temperature today, {day}? '
        daily_temp = int(input(prompt))
        if daily_temp < 50:
            print('Brr, put on a jacket!')
        elif daily_temp >= 50 and daily_temp < 65:
            print('Cozy, grab a sweater')
        elif daily_temp > 65:
            print('Put on some sunscreen!')

def temp_by_day_continuous():
    # 4 TODO: Write a program that asks the user what temperature it is outside. While the temperature is below 65,
    # tell the user to wear a sweater. Once the temperature is over 65, stop looping, and tell the user that
    # Spring has sprung!
    prompt = f'What is the temperature outside? '
    outdoor_temp = int(input(prompt))

    while outdoor_temp < 65:
        print('Wear a sweater')
        outdoor_temp = int(input(prompt))
        if outdoor_temp >= 65:
            print('Spring has sprung!')
            break
    # NOTE: If you accidentally create an infinite while loop, it's ok! Go into the command line and
    # hit control + C to stop the program. No harm has been done to your computer.

# temp_by_day()
# temp_by_day_continuous()