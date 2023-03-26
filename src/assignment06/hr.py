from controllers import facade as f

def main():
    while True:
        response = input(f.prompt)  
        if response == "1":
            f.load_employees()
        elif response == "2":
            f.save_employees()
        elif response == "3":
            f.add_employee
        elif response == "4":
            f.report_employees()
        elif response == "5":
            f.report_reminders    
        else:
            print("Not a valid option!")

if __name__ == "__main__":
    main()