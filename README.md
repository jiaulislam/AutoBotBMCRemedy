## AutoBot-BMCRemedy!
<p>A automation project to create/close ticket in BMC Remedy with selenium webdriver. It would require the Custom Data-Driver Excel file to work.
Details requirements has been discussed below.</p>

## Getting Started
<p>To start working with this automation script, Please make sure you have installed described requirments & must have the Custom Excel Data Driver.</p>

>Note: You can use pip from python after python installation done to install all the required modules.

* <a href = "https://www.python.org/"> Python </a>
* <a href = "https://www.selenium.dev/selenium/docs/api/py/"> Selenium </a>
* <a href = "https://openpyxl.readthedocs.io/en/stable/"> Openpyxl </a>

## Procedure 

<p>1. Download the <a href ="https://sites.google.com/a/chromium.org/chromedriver/downloads"> Chromium Web-Driver</a> and place it in C:/Chromedriver32/ .</p>
<p>2. Make Sure your computer $PATH have chromedriver, python, pip in the desktop environement settings.
<p>3. After downloading this script, Run the script with python 
<p>4. Excel Data-Driver file have the instruction what to do next.

## TODO

*   Need a way to parse the NCR Number, NCR Status, NCR date without using Visual Chrome-driver. Hoping to do with Requests Libray. 

*   NCR Group is hard-coded for now for my suitable needs, need to do that dynamic also.


> Caution: This automation script is still in under development, so there's a lot of bugs in the program and may have crush here and there.
