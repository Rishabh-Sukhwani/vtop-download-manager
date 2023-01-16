import os
import sys
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

            dates.sort(key=lambda date: datetime.strptime(date, r"%d-%m-%Y"))

            i=0
            for date in dates:
                for material in materials_in_subject_folder:
                    if (find_date(material)==date):
                        try:
                            #start serializing index
                            i+=1
                            extension = extract_extension(material)
                            
                            #set the new name for the file
                            new_name = f"0{i}- "+extract_name(material) + " - " + date + " " + extract_name(material) + " - " + subject + extension
                            
                            #set source and destination file path to rename
                            source_path = os.path.join(os.getcwd(), material)
                            destination_path = os.path.join(os.getcwd(), new_name)
                            
                            #to make sure the process is not being used
                            materials_in_subject_folder.remove(material)
                            
                            #rename the file
                            os.rename(source_path, destination_path)
                        except FileExistsError:
                            pass
                        except OSError:
                            #fix name for when it gets too long and gives error
                            fixed_name = extract_name(material)[:30]
                            #print(fixed_name)
                            new_name = f"0{i}- "+fixed_name + " - " + date + " " + fixed_name + " - " + subject + extension
                                
                            #set source and destination file path to rename
                            source_path = os.path.join(os.getcwd(), material)
                            destination_path = os.path.join(os.getcwd(), new_name)

                            #rename the file
                            os.rename(source_path, destination_path)
                        except PermissionError:
                            print("Please close all files that are in any of the semester folders")
                            sys.exit()
                        except:
                            print("An exception occured")

                        break

            os.chdir(second_level_dir)
        
        os.chdir(base_dir)