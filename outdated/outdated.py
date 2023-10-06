def main():

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    date = input("Date: ")

    while True:
        try:
            m,d,y = date.split("/")
            if (int(m) >= 1 and int(m)<= 12) and (int(d)>= 1 and int(d)<=31):
                break
        except:
            try:
                month, day, y = date.split(" ")

                for i in range(len(months)):
                    if month == months[i]:
                        m = i + 1
                d = day.replace(",","")
                if (int(m) >= 1 and int(m)<= 12) and (int(d)>= 1 and int(d)<=31):
                    break
            except:
                pass

    #print the date with the good formmat:
    print(f"{y}-{int(m):02}-{int(d):02}")

main()



