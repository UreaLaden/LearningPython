from math import ceil

def book_timeline():
    words = int(input("Words per Line: "))
    lines = int(input("Lines per Page: "))
    pages =int(input("Total pages: "))
    deadline = int(input('Desired weeks until completion: ')) * 7
    total_words = int((words * lines) * pages)
    reading_speed_per_min = 225
    daily_words = (total_words / reading_speed_per_min) / deadline
    print(f'If you want to read this book in {deadline} days, You will need to schedule {ceil(daily_words)} minutes per day for reading. ')
    redo = input('Try again? ')
    if redo == 'yes':
        book_timeline()
    if redo == 'no':
        return

book_timeline()
    