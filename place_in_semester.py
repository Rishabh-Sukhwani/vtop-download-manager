import os
import shutil

def place_in_semester_folder(reference_materials, semesters, semester_keys):
    for reference_material in reference_materials:
        for semester in semesters:
            if semester in reference_material:
                reference_material_path = os.path.join(reference_material)
                semester_value = semester_keys[semester]
                destination_path = os.path.join(f'Semester_{semester_value}')
                shutil.move(reference_material_path, destination_path)