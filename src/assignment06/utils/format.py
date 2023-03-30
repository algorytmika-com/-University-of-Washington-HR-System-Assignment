SEPARATOR = 50 * '-'
NEW_LINE_PROMPT = "\n>>>"
LOCATION_PROMPT = F"Give the location and name of the database file that is relative to the above path (e.g. /folder/hr.csv):{NEW_LINE_PROMPT}"

def print_message(message):
    print('\n' + SEPARATOR)
    print(message)
    print(SEPARATOR + '\n')