from datetime import date

def get_current_day():
    return(date.today().day)

def get_current_month():
    return(date.today().month)

def get_current_year():
    return(date.today().year)

def get_current_day_name():
    return(date.today().strftime("%A"))

def format_value_to_x_digits(value: str, digits):
    if len(value) == digits:
        return value
    elif len(value) > digits:
        return value[digits:]
    else:
        return value

def get_current_date(format= "DD-MM-YYYY"):
    stripped = str(date.today()).split("-")
    year = stripped[0]
    month = stripped[1]
    day = stripped[2]

    match format:
        case "DD-MM-YYYY":
            return(day + "-" + month)
    

print(get_current_day())
print(get_current_month())
print(get_current_year())
print(get_current_day_name())
print(get_current_date())