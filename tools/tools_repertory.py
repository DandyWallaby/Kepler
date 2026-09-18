import tools.time_and_date as date
from tools.error import error

def get_current_day() -> str:
    '''Return current computer day of the month'''
    return date.get_current_day()

def get_current_month() -> str:
    '''Return current computer month of the year'''
    return date.get_current_month()

def get_current_year():
    '''Return current computer year'''
    return date.get_current_year()

def get_current_date(format:str) -> str:
    '''Return current date written in the specified format between:
    "DD-MM-YYYY", "DD MM YYYY", "DD-MM-YY", "DD MM YY",
    "MM-DD-YYYY", "MM DD YYYY", "MM-DD-YY", "MM DD YY",
    "YYYY-MM-DD", "YYYY MM DD", "YY-MM-DD", "YY MM DD",
    "DD-MNAME-YYYY", "DD MNAME YYYY","DD-MNAME-YY","DD MNAME YY",
    "DD-MPRFX-YYYY", "DD MPRFX YYYY", "DD-MPRFX-YY", "DD MPRFX YY"
    
    Note that my prefered option would be "DD-MPRFX-YYYY", but others
    could sometimes be a better fit
    '''

    if not format in ["DD-MM-YYYY", "DD MM YYYY", "DD-MM-YY", "DD MM YY","MM-DD-YYYY", "MM DD YYYY", "MM-DD-YY", "MM DD YY","YYYY-MM-DD", "YYYY MM DD", "YY-MM-DD", "YY MM DD","DD-MNAME-YYYY", "DD MNAME YYYY","DD-MNAME-YY","DD MNAME YY","DD-MPRFX-YYYY", "DD MPRFX YYYY", "DD-MPRFX-YY", "DD MPRFX YY"]:
        return error("get_current_date(format)","Invalid date format", "Looking in <tools_repertory> for valid date formats, or use 'DD_MPRFX_YYYY'")

    return date.get_current_date(format)

def get_current_day_name() -> str:
    return date.get_current_day_name
