import sys
from cx_Freeze import *

# Dependencies are automatically detected, but it might need fine tuning.
#build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

#Include Folders
buildoptions = dict(include_files = ['BMITracker/', 'data/', 'img/'])
#buildOptions = dict(include_files = [(absolute_path_to_your_file,'final_filename')]) #single file, absolute path.

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

	
setup(  name = "BMI Tracker",
		version='1.0',
		description='Track your BMI and weight easily',
		author='Abderraouf Dridi',
		author_email='admin@ard-site.net',
		url='https://www.ard-site.net',
		long_description='This application allows you to calculate and track your BMI. You can also export your BMI calculations including weight as an excel document (csv) or pdf.',
		options=dict(build_exe = buildoptions),
        executables = [Executable("BMITracker\Bmitracker.py", 
		shortcutName="BMI Tracker",
        shortcutDir="BMITracker",
		icon="icon.ico",
		base=base)])