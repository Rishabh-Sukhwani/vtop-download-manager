import os
from utils.find_subject import find_subject

def create_subject_folders(semesters, semester_keys):
    for semester in semesters:
        
        base_dir = os.getcwd()

        semester_value = semester_keys[semester]
        os.chdir(os.path.join(f'Semester_{semester_value}'))
        
        files_in_semester = os.listdir()
        
        for material_semester in files_in_semester:
            subject = find_subject(material_semester)
            
            if (not(os.path.exists(subject))):
                os.mkdir(subject)
        
        #go back to previous directory to move to other semesters
        os.chdir(base_dir)