import datetime
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from fpdf import FPDF
import ctypes, sys, shutil, os.path
import BMITracker.model.Bmi


class UiMainWindow(object):
    bmicalculationsfile = 0
    # position of new line (row) in the BMI calculations table
    newtablelineposition = 0
    # number of columns for bmi calculations file
    cols = 4

    def setup_ui(self, MainWindow):
        'initialize application and saved data of user'
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(916, 590)
        MainWindow.setWindowIcon(QIcon('img/icon.png'))
        # Load winow components
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.weightLabel = QtWidgets.QLabel(self.centralwidget)
        self.weightLabel.setGeometry(QtCore.QRect(10, 10, 331, 61))
        self.weightLabel.setStyleSheet("img-width:30px;\n"
                                       "")
        self.weightLabel.setObjectName("weightLabel")
        # lcdnumber - shows the calculated bmi
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(60, 380, 311, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber.setObjectName("lcdNumber")
        self.weightField = QtWidgets.QTextEdit(self.centralwidget)
        self.weightField.setGeometry(QtCore.QRect(120, 160, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.weightField.setFont(font)
        self.weightField.setObjectName("weightField")
        self.heightField = QtWidgets.QTextEdit(self.centralwidget)
        self.heightField.setGeometry(QtCore.QRect(120, 210, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.heightField.setFont(font)
        self.heightField.setObjectName("heightField")
        self.weightLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.weightLabel_2.setGeometry(QtCore.QRect(310, 160, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.weightLabel_2.setFont(font)
        self.weightLabel_2.setObjectName("weightLabel_2")
        self.heightLabel = QtWidgets.QLabel(self.centralwidget)
        self.heightLabel.setGeometry(QtCore.QRect(310, 210, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.heightLabel.setFont(font)
        self.heightLabel.setObjectName("heightLabel")
        self.calculateButton = QtWidgets.QPushButton(self.centralwidget)
        self.calculateButton.setGeometry(QtCore.QRect(120, 260, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.calculateButton.setFont(font)
        self.calculateButton.setObjectName("calculateButton")
        self.calculateButton.setStyleSheet("background-color: green; color:white; font-weight: bold")
        self.lastbmicalculationLabel = QtWidgets.QLabel(self.centralwidget)
        self.lastbmicalculationLabel.setGeometry(QtCore.QRect(450, 90, 341, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lastbmicalculationLabel.setFont(font)
        self.lastbmicalculationLabel.setObjectName("lastbmicalculationLabel")
        self.heightLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.heightLabel_2.setGeometry(QtCore.QRect(60, 350, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.heightLabel_2.setFont(font)
        self.heightLabel_2.setObjectName("heightLabel_2")
        self.bmidescriptionLabel = QtWidgets.QLabel(self.centralwidget)
        self.bmidescriptionLabel.setGeometry(QtCore.QRect(60, 440, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.bmidescriptionLabel.setFont(font)
        self.bmidescriptionLabel.setText("")
        self.bmidescriptionLabel.setObjectName("bmidescriptionLabel")
        self.lastbmicalculationstableview = QtWidgets.QTableWidget(self.centralwidget)
        self.lastbmicalculationstableview.setColumnCount(self.cols)
        self.lastbmicalculationstableview.setGeometry(QtCore.QRect(450, 120, 431, 341))
        self.lastbmicalculationstableview.setObjectName("lastbmicalculationstableview")
        self.lastbmicalculationstableview.setRowCount(0)
        tableheader = self.lastbmicalculationstableview.horizontalHeader()
        tableheader.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        tableheader.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        tableheader.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        tableheader.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lastbmicalculationstableview.setFont(font)
        self.saveascsvfile = QtWidgets.QPushButton(self.centralwidget)
        self.saveascsvfile.setGeometry(QtCore.QRect(450, 30, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.saveascsvfile.setFont(font)
        self.saveascsvfile.setObjectName("saveascsvfile")
        self.saveaspdffile = QtWidgets.QPushButton(self.centralwidget)
        self.saveaspdffile.setGeometry(QtCore.QRect(660, 30, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.saveaspdffile.setFont(font)
        self.saveaspdffile.setObjectName("saveaspdffile")
        self.clearallbmicalculations = QtWidgets.QPushButton(self.centralwidget)
        self.clearallbmicalculations.setGeometry(QtCore.QRect(450, 470, 291, 31))
        self.clearallbmicalculations.setFont(font)
        self.clearallbmicalculations.setObjectName("clearallbmicalculations")
        self.copyrightlabel = QtWidgets.QLabel(self.centralwidget)
        self.copyrightlabel.setGeometry(QtCore.QRect(20, 530, 521, 21))
        self.copyrightlabel.setFont(font)
        self.copyrightlabel.setObjectName("copyrightlabel")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 916, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslate_ui(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Load functions
        self.calculateButton.clicked.connect(self.on_click_calculate_metric)
        self.saveascsvfile.clicked.connect(self.on_click_save_as_csv)
        self.saveaspdffile.clicked.connect(self.on_click_save_as_pdf)
        self.clearallbmicalculations.clicked.connect(self.on_click_clear_all_bmi_calculations)
        # Load saved bmi tracker calculations from file. If file does not exist, then it will be created
        try:
            try:
                #Check if programm has permission to use its data storage
                self.bmicalculationsfile = open("data/bmi_tracker.csv", "x")
            except PermissionError:
                self.error_no_admin_rights()
            self.bmicalculationsfile.write("Date;BMI;Description;Weight in kg\n")
        except IOError:
            # file exists
            self.bmicalculationsfile = open("data/bmi_tracker.csv")
            # table with all saved bmi calculations will be loaded, then in the function retranslate_ui.
            # skip header of file
            linesfile = []

            # Number of added rows to BMI calculation table
            rows = 0
            # Number of rows that contain correct data
            numbercorrectrows = 0
            # recreate header if file is empty. Header (first line) will not be used here for bmi table
            line = self.bmicalculationsfile.readline()
            while line:
                line = self.bmicalculationsfile.readline()
                linesfile.append(line)
                rows += 1
            self.newtablelineposition = rows
            # initialize table model and add calculation data from file to the table model
            for row in range(rows):
                # Get values for a line as lists (date, bmi, bmi desc, weight)
                lineList = linesfile[row].split(';')
                # check if line of file has correct data
                if (len(lineList) == self.cols):
                    numbercorrectrows += 1
                    self.lastbmicalculationstableview.insertRow(row)
                    for col in range(self.cols):
                        linecolumndata = str(lineList[col])
                        self.lastbmicalculationstableview.setItem(row, col, QtWidgets.QTableWidgetItem(linecolumndata))
        self.newtablelineposition = numbercorrectrows

        # if an error happened during read procedure, then set newtablelineposition to the first row
        if (len(linesfile) == 0):
            self.newtablelineposition = 0

        self.bmicalculationsfile.close()
        self.bmicalculationsfile = open("data/bmi_tracker.csv", "a+")

    def retranslate_ui(self, MainWindow):
        'Set text of ui components. All text variables'
        _translate = QtCore.QCoreApplication.translate
        self.weightLabel.setText(_translate("MainWindow",
                                            "<html><body><p><img src=\":/logoApp/bmi_tracker_logo_wide_small.png\"/></p></body></html>"))
        logoApp = QtGui.QPixmap("img/bmi_tracker_logo_wide_small.png")
        self.weightLabel.setPixmap(logoApp)
        # START: Text that can be translated
        MainWindow.setWindowTitle(_translate("MainWindow", "BMI Tracker - Track easily your weight and BMI"))
        self.weightLabel_2.setText(_translate("MainWindow", "Weight in kg"))
        self.heightLabel.setText(_translate("MainWindow", "Height in cm"))
        self.calculateButton.setText(_translate("MainWindow", "OK"))
        self.lastbmicalculationLabel.setText(_translate("MainWindow", "All saved BMI results:"))
        self.heightLabel_2.setText(_translate("MainWindow", "Calculated BMI value:"))
        self.saveascsvfile.setText(_translate("MainWindow", "Save as CSV file"))
        self.saveaspdffile.setText(_translate("MainWindow", "Save as PDF file"))
        self.clearallbmicalculations.setText(_translate("MainWindow", "Clear all saved BMI calculations"))
        self.savefileprompttext = "Save file"
        self.pdfheaderText = "BMI calculations"
        self.bmitext = "BMI"
        self.bmidescriptiontext = "Description"
        self.weighttext = "Weight in kg"
        self.datetext = "Date (dd.MM.yyyy)"
        self.pdffootertext = "BMI calculator created by: admin@ard-site.net (a-dridi - Abderraouf Dridi)"
        self.lastbmicalculationstableview.setHorizontalHeaderLabels(["Date", "BMI", "Description", "Weight in kg"])
        self.clearallbmicalculationstext = "Clear all BMI calculations"
        self.questionclearallbmicalculationtext = "Do you want to delete all saved BMI results?"
        self.copyrightlabel.setText(
            _translate("MainWindow", "(c) 2018 Abderraouf Dridi a.dridi - ( Contact: admin@ard-site.net )"))
        self.errorfileopenedtext = "Error: The file that you want to save is currently opened. Please close the open file."
        # END: Text that can be translated

    def on_click_calculate_metric(self):
        'Metric: BMI calculations - If user clicks the ok button the entered values will be checked and then the bmi will be calculated and displayed'
        heightText = self.heightField.toPlainText()
        weightText = self.weightField.toPlainText()

        if (heightText.isdecimal and weightText.isdecimal):
            # save today's date, height and weight for the bmi calculation. will be used for BMI tracking also
            bmientry = BMITracker.model.Bmi.Bmi()
            bmientry.setWeight(float(weightText))
            bmientry.setHeight(float(heightText))
            bmientry.setDate(datetime.datetime.now)
            bmientry.calculateMetric()
            # Display calculated value
            self.lcdNumber.display(bmientry.getBmi())
            self.bmidescriptionLabel.setText(bmientry.getBMIDesc())
            if bmientry.getBmi() < 15:
                self.bmidescriptionLabel.setStyleSheet("font-weight:bold; color:darkred")
            elif (bmientry.getBmi() >= 15) and (bmientry.getBmi() < 16):
                self.bmidescriptionLabel.setStyleSheet("font-weight:bold; color:red")
            elif (bmientry.getBmi() >= 16) and (bmientry.getBmi() < 18.5):
                self.bmidescriptionLabel.setStyleSheet("font-weight:bold; color:Goldenrod")
            elif (bmientry.getBmi() >= 18.5) and (bmientry.getBmi() < 25):
                self.bmidescriptionLabel.setStyleSheet("font-weight:bold; color:green")
            elif (bmientry.getBmi() >= 25) and (bmientry.getBmi() < 30):
                self.bmidescriptionLabel.setStyleSheet("font-weight:bold; color:Goldenrod")
            elif (bmientry.getBmi() >= 30) and (bmientry.getBmi() < 35):
                self.bmidescriptionLabel.setStyleSheet("font-weight:bold; color:red")
            elif (bmientry.getBmi() >= 35) and (bmientry.getBmi() < 40):
                self.bmidescriptionLabel.setStyleSheet("font-weight:bold; color:darkred")
            else:
                self.bmidescriptionLabel.setStyleSheet("font-weight:bold; color:darkred")

            # save bmi calculation in the bmi_tracker file and add to the list
            datenow = datetime.datetime.now().strftime("%d.%m.%Y")
            self.bmicalculationsfile.write(datenow
                                           + ";" + str(
                "%.2f" % bmientry.getBmi()) + ";" + str(bmientry.getBMIDesc()) + ";" + str(
                bmientry.getWeight()) + "\n")
            # add new calculation to bmi table
            self.lastbmicalculationstableview.insertRow(self.newtablelineposition)
            self.lastbmicalculationstableview.setItem(self.newtablelineposition, 0, QtWidgets.QTableWidgetItem(datenow))
            self.lastbmicalculationstableview.setItem(self.newtablelineposition, 1, QtWidgets.QTableWidgetItem(str(
                "%.2f" % bmientry.getBmi())))
            self.lastbmicalculationstableview.setItem(self.newtablelineposition, 2,
                                                      QtWidgets.QTableWidgetItem(str(bmientry.getBMIDesc())))
            self.lastbmicalculationstableview.setItem(self.newtablelineposition, 3, QtWidgets.QTableWidgetItem(str(
                bmientry.getWeight())))
            self.newtablelineposition += 1

    def on_click_save_as_csv(self):
        'Allow user to save BMI calculations table as csv file'
        filepath = QtWidgets.QFileDialog.getSaveFileName(None, self.savefileprompttext, "", "Text file (*.csv)", )
        # copy data from the file that this application uses to save all BMI calculations to the users file
        self.bmicalculationsfile.close()
        try:
            shutil.copyfile("data/bmi_tracker.csv", filepath[0])
        except Exception:
            self.errorfileopenedtext()
        self.bmicalculationsfile = open("data/bmi_tracker.csv")

    def on_click_save_as_pdf(self):
        'Allow user to save BMI calculations table as pdf document'
        filepath = QtWidgets.QFileDialog.getSaveFileName(None, self.savefileprompttext, "", "PDF Document (*.pdf)", )
        # create pdf page
        pdf = FPDF()
        space = 1.3
        pdf.set_font("Arial", size=13)
        pdf.add_page()
        col_width = pdf.w / 4.4
        row_height = pdf.font_size
        # write header of pdf table
        pdf.cell(col_width, row_height * 2, txt=self.pdfheaderText, border=0)
        pdf.ln(row_height * 2)
        pdf.ln(row_height * 2)
        pdf.cell(col_width, row_height * 1.5, txt=self.datetext, border=0)
        pdf.cell(col_width - 6, row_height * 1.5, txt=self.bmitext, border=0)
        pdf.cell(col_width + 12, row_height * 1.5, txt=self.bmidescriptiontext, border=0)
        pdf.cell(col_width, row_height * 1.5, txt=self.weighttext, border=0)
        pdf.ln(row_height * 1.5)
        # write bmi calculations into a table. cell for cell
        rownumber = self.lastbmicalculationstableview.rowCount()
        for row in range(0, rownumber):
            pdf.cell(col_width, row_height * space, txt=(self.lastbmicalculationstableview.item(row, 0)).text(),
                     border=1)
            pdf.cell(col_width - 6, row_height * space, txt=(self.lastbmicalculationstableview.item(row, 1)).text(),
                     border=1)
            pdf.cell(col_width + 12, row_height * space, txt=(self.lastbmicalculationstableview.item(row, 2)).text(),
                     border=1)
            pdf.cell(col_width, row_height * space, txt=(self.lastbmicalculationstableview.item(row, 3)).text(),
                     border=1)
            pdf.ln(row_height * 1.5)
        # write footer of pdf table
        pdf.ln(row_height * 2)
        pdf.cell(col_width, row_height * 2, txt=self.pdffootertext, border=0)
        try:
            pdf.output(filepath[0])
        except Exception:
            self.error_file_opened()

    def on_click_clear_all_bmi_calculations(self):
        'Dialog: Delete all saved BMI calculation in BMI calculations file and reset BMI calculation table.'
        self.clearbmicalculationsdialog = QtWidgets.QMessageBox()
        self.clearbmicalculationsdialog.setIcon(QtWidgets.QMessageBox.Question)
        # Uses the methods on_click_cancel_clear_all_bmi_calculations and on_click_ok_clear_all_bmi_calculations in class UiClearbmicalculationsDialog
        self.clearbmicalculationsdialog.setWindowTitle(self.clearallbmicalculationstext)
        self.clearbmicalculationsdialog.setText(self.questionclearallbmicalculationtext)
        self.clearbmicalculationsdialog.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        selectedvalue = self.clearbmicalculationsdialog.exec_()
        # Check what user did choose. Ok or Cancel.
        if selectedvalue == QtWidgets.QMessageBox.Yes:
            self.on_click_ok_clear_all_bmi_calculations()
        else:
            self.on_click_cancel_clear_all_bmi_calculations()

    def on_click_cancel_clear_all_bmi_calculations(self):
        'Close Dialog: Delete All Saved BMI calculations'
        self.clearbmicalculationsdialog.hide()

    def on_click_ok_clear_all_bmi_calculations(self):
        'Delete all saved BMI calculation in table and file bmi_tracker.csv. Close dialog (clear_all_bmi_calculations)'
        self.bmicalculationsfile.close()
        self.bmicalculationsfile = open("data/bmi_tracker.csv", "w+")
        self.bmicalculationsfile.write("Date;BMI;Description;Weight in kg\n")
        self.newtablelineposition = 0
        self.lastbmicalculationstableview.setRowCount(0)
        self.lastbmicalculationstableview.clearContents()
        self.clearbmicalculationsdialog.hide()

    def error_file_opened(self):
        'Error: File opened. cannot be written'
        errorfileopeneddialog = QtWidgets.QMessageBox()
        errorfileopeneddialog.setIcon(QtWidgets.QMessageBox.Critical)
        errorfileopeneddialog.setWindowTitle("Error")
        errorfileopeneddialog.setText(self.errorfileopenedtext)
        errorfileopeneddialog.setStandardButtons(QtWidgets.QMessageBox.Ok)
        selectedvalue = errorfileopeneddialog.exec_()
        if (selectedvalue == QtWidgets.QMessageBox.Ok):
            errorfileopeneddialog.hide()

    def error_no_admin_rights(self):
        'Error: Application has no admin rights'
        errornoadminrightsdialog = QtWidgets.QMessageBox()
        errornoadminrightsdialog.setIcon(QtWidgets.QMessageBox.Critical)
        errornoadminrightsdialog.setWindowTitle("Error")
        errornoadminrightsdialog.setText("The application needs admin rights to work and store BMI calculation data. In Windows: Right click on this application and select run as administrator. Then click on \"Yes\" in the next message box.")
        errornoadminrightsdialog.setStandardButtons(QtWidgets.QMessageBox.Ok)
        selectedvalue = errornoadminrightsdialog.exec_()
        if (selectedvalue == QtWidgets.QMessageBox.Ok):
            errornoadminrightsdialog.hide()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
