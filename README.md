# VTOP-DOWNLOAD-MANAGER

vtop-download-manager is a python program for dealing with the unreadable names given to reference material on VTOP's course page. The program sorts all the material downloaded from course page into each subject in each semester and sorts it according to the date given on VTOP. It also renames and gives a chronological serial number to each file.

The program sorts and renames a file named like this:
```py
'WINSEM2022-23_BCSE205L_TH_VL2022230502962_Reference_Material_I_15-12-2022_Modified_Harvard_Architecture'
```
in the dowloads folder
to this in its corresponding semester and subject folder:
```py
'03- Modified Harvard Architecture - 15-12-2022 - BCSE205L'
```

## Installation

No external packages used. All packages and libraries used come with python.

## Usage

Enter your PC's username in this line in main.py
```py
os.chdir(r'C:\Users\your-user-name-on-pc\Downloads')
```
The program assumes that all material is downloaded and the previously stored material is in the downloads folder itself.
The program has to be run manually each time a file is downloaded from the course page in VTOP to sort and rename it.

## Contributing

Pull requests are welcome. Feel free to contribute!

## License

[MIT]
(https://choosealicense.com/licenses/mit/)