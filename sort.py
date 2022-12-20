import os
from datetime import datetime
from utils.extract_extension import extract_extension
from utils.extract_name import extract_name
from utils.find_date import find_date

def sort_by_date(semesters, semester_keys):
    for semester in semesters:

        base_dir = os.getcwd()

        semester_value = semester_keys[semester]
        os.chdir(os.path.join(f'Semester_{semester_value}'))
        second_level_dir = os.getcwd()
        
        subjects_directories = os.listdir()

        for subject in subjects_directories:
            dates = []
            names = []

            os.chdir(os.path.join(subject))
            materials_in_subject_folder = os.listdir()

            for material in materials_in_subject_folder:
                dates.append(find_date(material))
                names.append(extract_name(material))
            
            #print(dates)

            dates.sort(key=lambda date: datetime.strptime(date, r"%d-%m-%Y"))
            #print("Sorted datelist: ", dates)

            #print(names)
            i=0
            for date in dates:
                for material in materials_in_subject_folder:
                    if (find_date(material)==date):
                        try:
                            i+=1
                            extension = extract_extension(material)
                            #print(f"{i}: "+extract_name(material) + "| " + date + " | " + subject)
                            new_name = f"0{i}- "+extract_name(material) + " - " + date + " - " + subject + extension
                            source_path = os.path.join(os.getcwd(), material)
                            #print(source_path)
                            destination_path = os.path.join(os.getcwd(), new_name)
                            materials_in_subject_folder.remove(material)
                            #print(destination_path)
                            #print(source_path + " | " + destination_path)
                            os.rename(source_path, destination_path)
                        except FileExistsError:
                            pass
                        break

            os.chdir(second_level_dir)
        
        os.chdir(base_dir)