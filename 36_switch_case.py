# Match-case statement (switch): An alternative to using many 'elif' statements
# Execute some code if a value matches a 'case'
# Benefits: cleaner and syntax is more readable

def day_of_week(day):
    match day:
        case 1:
            return "Its a Sunday"
        case 2:
            return "Its a Monday"
        case 3:
            return "Its a Tuesday"
        case 4:
            return "Its a Wednesday"
        case 5:
            return "Its a Thursday"
        case 6:
            return "Its a Friday"
        case 7:
            return "Its a Saturday"
        case _:
            return "Not a valid day"


print(day_of_week(4))


def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False


print(is_weekend("Friday"))
