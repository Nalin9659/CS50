def main():
    
    time= input ("What is the time? ")
    time_float = convert(time)


    if 7.0 <= time_float <= 8.0:
        print("Breakfast Time")

    elif 12.0 <= time_float <= 13.0:
        print("Lunch Time ")

    elif 18.0 <= time_float <= 19.0:
        print("Dinner Time")

    else:
        print("Timezon not define")

    # define the convert function
def convert(time):
    hours, minutes = map(int, time.split(":"))
    return hours + (minutes/60)

   # here map(int, time.split(":")) is coverting the time minutes to hours
   # returns hours + (minutes/60) is converting minute into fraction of an hour
if __name__== "__main__":
    main() 
