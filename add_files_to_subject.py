import os
import shutil
from utils.find_subject import find_subject

def add_files_to_subject(semesters, semester_keys):
    for semester in semesters:

        base_dir = os.getcwd()

        semester_value = semester_keys[semester]
        os.chdir(os.path.join(f'Semester_{semester_value}'))

        files_in_semester = os.listdir()
        
        for material_semester in files_in_semester:
            subject = find_subject(material_semester)

            material_semester_path = os.path.join(material_semester)
            destination_path = os.path.join(subject)
            shutil.move(material_semester_path, destination_path)

        os.chdir(base_dir)