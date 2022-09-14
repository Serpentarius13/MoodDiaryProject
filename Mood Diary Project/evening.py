from checkend import CheckEnd
""" funcs:
    reading_file - reads file
    evening - gets new data for evening
    report - makes a report
    morning_report - prints a morning report
    new - asks for new time/mood data
    counting - checks for completed tasks
    median - produces a median value of completed tasks
    writing_mor - writes report for morning in txt
    writing_ev - writes report for evening in txt
    clear_file - clears temp file
    """
a = CheckEnd()
a.reading_file()
a.morning_report()
a.evening()
a.write()
a.counting()
a.median()
a.nosleep()
a.writing_mor()
a.writing_ev()
a.clear_file()
