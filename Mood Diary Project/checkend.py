from main import MoodDiary
import math
""" funcs:
    reading_file - reads file
    report - makes a report
    morning_report - prints a morning report
    new - asks for new time/mood data
    counting - checks for completed tasks
    median - produces a median value of completed tasks
    writing_mor - writes report for morning in txt
    writing_ev - writes report for evening in txt
    """


class CheckEnd(MoodDiary):

    def __init__(self): # 11
        super().__init__()

        self.new_feelings = []

        self.thingsie = []
        self.things_done = []

        self.read_text = ''
        self.text = ''

        self.res = 0

        self.date = ''
        self.time = ''
        self.mood = ''

        self.nosleep_time = 0

    def reading_file(self):
        with open('Diary.txt', 'r') as f:
            listie = f.readlines()
            while '' in listie:
                listie.remove('')
            self.date = listie[0]
            self.time = listie[1]
            self.mood = listie[2]
            if 'thing to do' not in listie[3]:
                self.read_text = listie[3]
                for a in listie[4:]:
                    self.thingsie.append(a)
            else:
                for a in listie[3:]:
                    self.thingsie.append(a)

    def evening(self):
        time = input(self.time_q)
        mood = input(self.mood_q)
        self.new_feelings.append(time)
        self.new_feelings.append(mood)

    def morning_report(self):
        print(f"Reporting for:")
        print(self.date)
        print(self.time)
        print(self.mood)
        if self.read_text not in ['']:
            print(f"At morning you wrote:")
            print(self.read_text)

    # def new(self):
    #     while True:
    #         write = input(self.write_q)
    #         if write in ['yes','Yes']:
    #             writing = input(self.write_q_cont)
    #             self.text = writing
    #             break
    #         if write in ['no','No']:
    #             print('Okay!')
    #             break
    #         else:
    #             print("Sorry, I don't understand. Respond yes or no.")
    #             continue

    def counting(self):
        for thing in self.thingsie:
            thing.replace('Thing to do', ' ')
            while True:
                complete = input(f"Have you completed: {thing}?")
                if complete in ['Yes','yes']:
                    self.things_done.append(thing)
                    break
                if complete in ['no','No']:
                    break

    def median(self):
        leng1 = len(self.thingsie)
        leng2 = len(self.things_done)
        self.res = leng2 / leng1 * 100
        print(f"You have completed {math.ceil(self.res)}% of your tasks!")
        if self.res > 60:
            print('Good job!')
        elif 25 < self.res <= 60:
            print('You could have done better!')
        elif self.res <= 25:
            print('What were you doing, fucker?')
        print('Have a good night!')

    def writing_mor(self):
        with open('Stats.txt','a') as f:
            f.write(f"\nThe date is:\n")
            f.write(f"\n{self.date}")
            f.write('\nMorning report:\n')
            f.write(f"Time: {self.time}\n")
            f.write(f"Mood: {self.mood}\n")
            if self.read_text:
                f.write(f"At morning you wrote this:\n")
                f.write(f"\t{self.read_text} \n")
            f.write('You have assigned yourself such tasks: \n')
            for thing in self.thingsie:
                f.write(f"\t{thing}")
            f.write('')

    def nosleep(self):
        a = self.time
        a = float(a)
        self.time = self.new_feelings[0]
        self.time = float(self.time)
        self.mood = self.new_feelings[1]
        if a > self.time:
            self.time += 24
            final = self.time - a
            self.nosleep_time = round(final, 2)
            self.time -= 24
        else:
            final = self.time - a
            self.nosleep_time = round(final, 2)

    def writing_ev(self):
        with open('Stats.txt','a') as f:
            f.write('\nEvening report:\n')
            f.write(f"\nTime: {self.time}\n")
            f.write(f"Mood: {self.mood}\n")
            if self.text:
                f.write(f"At night you wrote this:\n")
                f.write(f"\t{self.text}\n")
            f.write('You have completed such tasks: \n')
            for thing in self.things_done:
                f.write(f"\t{thing}\n")
            f.write(f"The amount of completed tasks is {self.res}%!\n")
            f.write(f"You haven't slept for {self.nosleep_time} hours!")


    def clear_file(self):
        with open('Diary.txt', 'r+') as f:
            f.seek(0)
            f.truncate()





