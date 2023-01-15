import os
import place_in_semester
import create_subject_folder
import add_files_to_subject
import sort


#go to the folder where material is downloaded to
os.chdir(r'C:\Users\risha\Downloads')

all_files = os.listdir()

#store all the downloaded reference materials in an array
reference_materials = []
for file in all_files:
    if 'Reference_Material' in file:
        reference_materials.append(file)

#create folder for each semester, if they do not exist
for i in range(1, 9):
    if not((os.path.exists(f'Semester_{i}'))):
        os.mkdir(f'Semester_{i}')

#use a dictionary to store keys to find correct semester folder
semester_keys = {
            'FALLSEM2021-22': 1, 'WINSEM2021-22': 2, 
            'FALLSEM2022-23': 3, 'WINSEM2022-23': 4,
            'FALLSEM2023-24': 5, 'WINSEM2023-24': 6,
            'FALLSEM2024-25': 7, 'WINSEM2024-25': 8
}

#storing semesters extracted from semester_keys dictionary
semesters = []
for semester_information in semester_keys.keys():
    semesters.append(semester_information)

#place downloaded file in corresponding semester folder
place_in_semester.place_in_semester_folder(reference_materials, semesters, semester_keys)

#create subject folders in each semester folder
create_subject_folder.create_subject_folders(semesters, semester_keys)

#After creating subject folders start adding files to them
add_files_to_subject.add_files_to_subject(semesters, semester_keys)

#implement sorting by date
#also renames files with more readable names
sort.sort_by_date(semesters, semester_keys)