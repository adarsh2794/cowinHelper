from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://selfregistration.cowin.gov.in/")
driver.implicitly_wait(10) # seconds

def getOtp(phoneNum):
    numberBox = driver.find_element_by_xpath('//*[@id="mat-input-0"]')
    numberBox.send_keys (phoneNum)
    getOtpButton = driver.find_element_by_xpath('//*[@id="main-content"]/app-login/ion-content/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[1]/ion-grid/form/ion-row/ion-col[2]/div/ion-button')
    getOtpButton.click()


def verifyOtp(otp):
    enterOtp = driver.find_element_by_xpath('//*[@id="mat-input-1"]')
    enterOtp.send_keys(otp)
    verifyOtpButton = driver.find_element_by_xpath('//*[@id="main-content"]/app-login/ion-content/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col/ion-grid/form/ion-row/ion-col[3]/div/ion-button');
    verifyOtpButton.click()



def scheduleRow(rowNo):
    elementPath = '//*[@id="main-content"]/app-beneficiary-dashboard/ion-content/div/div/ion-grid/ion-row/ion-col/ion-grid[1]/ion-row[5]/ion-col/ion-grid/ion-row['+str(rowNo)+']/ion-col[2]/ul/li/a/span'
    scheduleButton = driver.find_element_by_xpath(elementPath)
    scheduleButton.click()

def enterPin(pin):
     pinCodeText = driver.find_element_by_xpath(' //*[@id="mat-input-2"]')
     pinCodeText.send_keys(pin)
     searchButton = driver.find_element_by_xpath('//*[@id="main-content"]/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row[1]/ion-col[4]/ion-button')
     searchButton.click()

def filter18():
    scheduleButton = driver.find_element_by_xpath('//*[@id="main-content"]/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row[2]/ion-col[1]/div/div[1]/label')
    scheduleButton.click()

def findSlot():
    num = "9830235370"#Give your number here
    getOtp(num)
    otp = input("Please enter your otp \n")
    print("OTP is "+otp)
    verifyOtp(otp)
    rowNum = 4
    scheduleRow(rowNum)#You can schedule the desired person row
    pin= "700027"#Enter Pin Here
    enterPin(pin)#Enter your Pin Here
    filter18()#Can be modified for 45+

findSlot()

