def main():
    time = input("What time is it? ")
    t = convert(time)

    if 7 <= t <= 8:
        print("breakfast time ")
    elif 12 <= t <= 13:
        print("Lunch time")
    elif 18 <= t <= 19:
        print("Dinner time")

def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)

    if hours > 24:
        hours -= 24
    if minutes > 59:
        hours += 1
        minutes -= 60

    ctime = hours + minutes / 60
    return ctime

if __name__ == "__main__":
    main()