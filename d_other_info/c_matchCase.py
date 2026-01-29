# match case statement is similar to switch case in other languages
# this is an alternative to if-elif-else ladder when we have multiple discrete values to check against

# ============================================================================
print()


# let consider a if elif-else example first
day = 3
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:  
    print("Wednesday")
elif day == 4:
    print("Thursday")       
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day")

# this can be rewritten using match case as shown below

# ============================================================================
print()


# simple match case example
day = 3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")       
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _: # default case, if none of the above matches
        print("Invalid day")


# ============================================================================
print()


# we can put this inside a function as well
def get_day_name(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"       
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day"

print(get_day_name(5))  # Friday
print(get_day_name(10)) # Invalid day