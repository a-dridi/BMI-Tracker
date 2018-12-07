class Bmi:
    'Model class for BMI result entry'

    def calculateMetric(self):
        ' Metric ver: Calculate BMI of saved values (weight,height) and set BMI categorie (underweight, obese, etc.)'
        self.bmi = self.weight / ((self.height / 100) * (self.height / 100))

        if self.bmi < 15:
            self.bmiDesc = "Very severely underweight"
        elif (self.bmi >= 15) and (self.bmi < 16):
            self.bmiDesc = "Very severely underweight"
        elif (self.bmi >= 16) and (self.bmi < 18.5):
            self.bmiDesc = "Underweight"
        elif (self.bmi >= 18.5) and (self.bmi < 25):
            self.bmiDesc = "Normal (healthy)"
        elif (self.bmi >= 25) and (self.bmi < 30):
            self.bmiDesc = "Overweight"
        elif (self.bmi >= 30) and (self.bmi < 35):
            self.bmiDesc = "Moderately obese"
        elif (self.bmi >= 35) and (self.bmi < 40):
            self.bmiDesc = "Severely obese"
        else:
            self.bmiDesc = "Very severely obese"

    def getWeight(self):
        return self.weight

    def getHeight(self):
        return self.height

    def getBmi(self):
        return self.bmi

    def getTrackDate(self):
        return self.trackDate

    def getBMIDesc(self):
        return self.bmiDesc

    def setWeight(self, weight):
        self.weight = weight

    def setHeight(self, height):
        self.height = height

    def setDate(self, date):
        self.date = date
