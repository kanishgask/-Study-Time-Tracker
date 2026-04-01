study_data = {}

def add_study_time(subject, minutes):
    if subject in study_data:
        study_data[subject] += minutes
    else:
        study_data[subject] = minutes

def get_study_data():
    return study_data
