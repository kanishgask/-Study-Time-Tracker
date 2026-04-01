from tracker import get_study_data

def generate_report():
    data = get_study_data()
    
    print("\nStudy Report")
    print("-------------")
    
    for subject, minutes in data.items():
        print(subject, ":", minutes, "minutes")
