from controllers import facade as f
from utils import format as fmt

def main():
    while True:
        fmt.print_message("MENU")
        response = input(f.prompt)  
        f.clear_console()
        if response == "1":
            f.load_employees()
        elif response == "2":
            f.save_employees()
        elif response == "3":
            f.add_employee()
        elif response == "4":
            f.report_current_employees()
        elif response == "5":
            f.report_former_employees()  
        elif response == "6":        
            f.report_reminders()  
        elif response == "7":
            f.exit_program()
        else:
            print("Not a valid option!")

if __name__ == "__main__":
    main()