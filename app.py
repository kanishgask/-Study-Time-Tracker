from tracker import add_study_time
from report import generate_report
from timer import start_timer
from utils import show_menu

while True:
    
    show_menu()
    choice = input("Enter your choice: ")
    
    if choice == "1":
        subject = input("Enter subject name: ")
        minutes = int(input("Enter study minutes: "))
        add_study_time(subject, minutes)
        
    elif choice == "2":
        generate_report()
        
    elif choice == "3":
        seconds = int(input("Enter timer seconds: "))
        start_timer(seconds)
        
    elif choice == "4":
        print("Goodbye!")
        break
        
    else:
        print("Invalid choice")
