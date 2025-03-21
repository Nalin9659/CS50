def main():

    dollers= dollers_float(input("How much was a meal? "))
    percentage= percent_float(input("what percentage would you like to tip? "))

    tip= dollers * percentage
    print(f"Leave ${tip:2f}")

def dollers_float(d):
    return float(d.replace("$","##.##"))
    
def percent_float(p):
    return float(p.replace("%",""))/100

main()  
    
