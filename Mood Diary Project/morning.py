from main import MoodDiary

""" functions:
    morning - asks for date,time and mood at morning
    write - asks if you want to write something
    things - asks for things to do
    file_write - writes everything"""

a = MoodDiary()
a.checkout()
a.morning()
a.write()
a.things()
a.file_write()
