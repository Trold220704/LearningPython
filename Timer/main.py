from time import sleep

def main():
    user_input()


def user_input():
    try:
        user_time = input('How long will the timer run (hours:minuts:seconds)').split(':')
        hours, mins, sec = user_time
        total_time = (int(hours)*3600)+(int(mins)*60)+int(sec)
        timer(total_time)
    except ValueError:
        print('Needs to be the right format')
        user_input()


def timer(total_time):
    while total_time > 0:
        # Divmod is used to divide a number and returns the remainder to a new variable 
        # divmod(time_input, division)
        hours, remainder = divmod(total_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        # The {:02d} formatting inside format() ensures that the numbers are displayed as two-digit integers, even if they are single-digit.
        # .format takes variables and formats them into the format set before it
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
        print(timer)
        sleep(1)
        total_time -= 1

        if total_time == 0:
            #winsound.Beep(frequency, duration)
            print('Time is done')

if __name__ == '__main__':
    main()
