class MoodDiary():

    def __init__(self):
        self.date_q = 'What date is it today? '
        self.time_q = 'Time: '
        self.mood_q = 'Mood: '
        self.things_q = 'Do you want a new thing to your todo list for today? '
        self.write_q = 'Do you want to write something for today? '
        self.write_q_cont = 'What is it? '
        self.text = ''
        self.mornings = []
        self.thingsie = []

    def checkout(self):
        f = open('Diary.txt', 'r+')
        s = open('Stats.txt', 'a+')
        if f != '':
            fs = f.readlines()
            for fa in fs:
                s.write(f"\n{fa}")
            f = open('Diary.txt','w+')
            f.truncate()
        f.close()
        s.close()


    def morning(self):
        print('Hello!')
        date = input(self.date_q)
        time = input(self.time_q)
        mood = input(self.mood_q)
        self.mornings.append(date)
        self.mornings.append(time)
        self.mornings.append(mood)

    def write(self):
        while True:
            write = input(self.write_q)
            if write in ['yes', 'Yes']:
                text = input(self.write_q_cont)
                self.text = text
                break
            if write in ['no','No']:
                print('Okay!')
                break
            else:
                print("Sorry, I don't understand. Respond yes or no.")

    def things(self):
        while True:
            things_q = input(self.things_q)
            if things_q in ['No', 'no']:
                print('Have a good day!')
                break
            else:
                things = input(self.write_q_cont)
                self.thingsie.append(things)

    def file_write(self):
        with open('Diary.txt', 'w') as f:
            f.write(f"\nDate: {self.mornings[0]}\n")
            f.write(f"{self.mornings[1]}\n")
            f.write(f"{self.mornings[2]}\n")
            if self.text:
                f.write(f"{self.text}\n")
            for th in self.thingsie:
                f.write(f"Thing to do: {th}\n")




