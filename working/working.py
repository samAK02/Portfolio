import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(time):
     matches = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) (AM|PM) to (([0-9][0-2]*):*([0-5][0-9])*) (AM|PM)$", time)
     if matches:
         str = matches.groups()
         if int(str[1]) > 12 or int(str[5]) >12:
             raise ValueError
         ftime = update(str[1], str[2], str[3])
         stime = update(str[5],str[6], str[7])
         return ftime + " to " + stime
     else:
         raise ValueError



def update(hours, min, am_pm):
    if am_pm == "PM":
        if int(hours) == 12:
            new_h = 12
        else:
            new_h = int(hours)+12
    else:
        if int(hours) == 12:
            new_h = 0
        else:
            new_h = int(hours)

    if min == None:
        new_min = ":00"
        new_time = f"{new_h:02}" + new_min
    else:
        new_time = f"{new_h:02}" + ":" + min

    return new_time


if __name__ == "__main__":
    main()