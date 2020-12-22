# Autobot

Autobot is web automation framework for BMC Remedy, LDMA & ROC to complete boring everyday task with just  excel data.

  - Create Change Request in BMC Remedy System
  - Close Change Request in BMC Remedy System
  - Cancel Change Request in BMC Remedy System
  - Parse the Link Budget from LDMA Robi Axiata website 
  - Parse the ROC info from ROC Robi Axiata website

  ### You can also:
  - Export documents as DOCX, HTML and PDF

# Up Coming Features!

  - ROC is in the pipeline for automating the ROC Milestone clearence.
  - GUI Interface 


### Tech

Autobot uses a number of open source projects to work properly:

* [Selenium](https://www.selenium.dev/) - Web-browser Controller framework!
* [OpenpyXL](https://pypi.org/project/openpyxl/) - Excel File handling framework! 
* [pywin32](https://pypi.org/project/pywin32/) - Win32 api Controllers !
* [pdfkit](https://pypi.org/project/pdfkit/) - To Export the data as PDF !
* [alive_progress](https://pypi.org/project/alive-progress/) - For beautiful termial Progress Bar !

### Installation

Autobot required latest version of [Selenium](https://www.selenium.dev/) to run.

Install the dependencies and devDependencies and start the app.

```sh
$ cd AutoBotBMCRemedy
$ pip3 install -r requirements.txt
$ python3 driver.py
```


### Development

Want to contribute? Great!

Autobot uses Pure python + Selenium framework for fast developing.

Open your favorite Terminal and run these commands.

First Tab:
```sh
$ git clone git@github.com:jiaulislam/AutoBotBMCRemedy.git
```

Second Tab:
```sh
$ cd AutoBotBMCRemedy
```

(optional) Third:
```sh
$ code .
```

### Todos

 - Write MORE Tests
 - Make the code more DRY & Stable

License
----

MIT


**Automation, Hell Yeah!**
