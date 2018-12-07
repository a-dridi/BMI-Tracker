# BMI Tracker

This application allows you to track your BMI and weight. You can calculate your BMI and check if you have a healthy BMI. All your calculations can be exported to an PDF or CSV file.
![Screenshot of application BMI Tracker](https://raw.githubusercontent.com/a-dridi/BMI-Tracker/master/img/screenshot1.PNG)

This application is in English only. Please check the chapter Configuration to know more on how to translate the UI to another language. If you want to have a translation of this application or you have any other questions/requests, then feel free to contact me. 


## Configuration

This application is monolingual and in English only. If you want to translate the UI of this application into another language, then change the string values in the method "retranslate_ui" in Bmitracker.py.


## Installation
### Downloading this application as an exectable.
This application is available as an exe file version or with an installer for Windows.
Please check the Release page of this Github project.

### Recompile this application as an executable
You can create an executable yourself for Windows or Mac OS with Pyinstaller or Cx_freeze. 
If you use Pyinstaller then you can use the following command in the root folder of this application.
```
pyinstaller --onefile --windowed --add-data="data/;." --add-data="img/;." --add-data="BMITracker/;." --icon="icon.ico" Bmitracker.py
```


## Authors

* **A. Dridi** - [a-dridi](https://github.com/a-dridi/)


