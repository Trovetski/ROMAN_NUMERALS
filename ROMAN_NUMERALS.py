class roman:
    temp = {'I':0,'V':0,'X':0,'L':0,'C':0,'D':0,'M':0}#this is for counting how many of them to use
    values = [1000, 500, 100, 50, 10, 5, 1]           #to store the possible sum values
    keys = ['M', 'D', 'C', 'L', 'X', 'V', 'I']        #to store the possible symbols
    def __init__(self, arg):
        self.arg = arg#the input
        self.cnt = 0  #count tracker
        self.i = 0    #just a temporary counter
        while self.arg > 0: #this loop is a remainder algorithm or keep dividing untill you get a negative number
            while self.arg >= 0:
                self.arg -= roman.values[self.i]
                if self.arg >= 0:
                    self.cnt += 1
                else:
                    self.arg += roman.values[self.i]
                    break
            roman.temp.update({roman.keys[self.i]:self.cnt})
            self.cnt = 0
            self.i += 1
        self.adjust()
        roman.temp = {'I':0,'V':0,'X':0,'L':0,'C':0,'D':0,'M':0}#this is for counting how many of them to use
        roman.values = [1000, 500, 100, 50, 10, 5, 1]           #to store the possible sum values
        roman.keys = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        self.i = 0
    
    def adjust(self):#and this function applies the rules for roman numbers
        self.output = ''
        for i in roman.keys:#just adding the character on the basics of the number of times they appear
            self.output = self.output + i*roman.temp[i]
        for i in range(1,7):
            if i%2 == 0:#the repetaion rule in the roman numerals i.e. VV or LL is not valid
                if roman.temp[roman.keys[i]] > 3:
                    self.output = self.output.replace((roman.keys[i]*roman.temp[roman.keys[i]]),(roman.keys[i] + roman.keys[i-1]))
                    roman.temp.update({roman.keys[i-1]:roman.temp[roman.keys[i-1]]+1})
                    roman.temp.update({roman.keys[i]:roman.temp[roman.keys[i]]-3})
        for i in range(1,7):#this fixes it
            if i%2 == 1:
                if roman.temp[roman.keys[i]] > 1:
                    roman.temp.update({roman.keys[i]:0})
                    roman.temp.update({roman.keys[i-1]:roman.temp[roman.keys[i-1]]+1})
                    self.output = self.output.replace((roman.keys[i] + roman.keys[i+1] + roman.keys[i]),(roman.keys[i+1] + roman.keys[i-1]))
        print(self.output)

while True:
    x = int(input("Enter Integer: "))
    y = roman(x)
