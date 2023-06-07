# DC Courts Scraping Project

This scraping code was developed by John Eagle Miles [(@Jem379)] (https://github.com/Jem379/), a law student who partnered with the CJDC as part of Georgetown University Law Center's Computer Programing for Lawyers class.

It is a work-in-progress but may serve as a helpful example on how to scrape DC court websites.

The program is built to automate scraping of the the DC court's website using Selenium. It is currently built to work with Firefox drivers.

**CaseScraper.py** navigates the court website and scrapes specific case numbers.

**CaseNumberGenerator.py** is not fully implemented but generates case numbers based on the DC Court's case numbering system. It is close to full implementation but misses some case numbers and may need altering for specific date ranges (see code comments). 

**SeleniumTesting.py** contains beta code for navigating the site and circumventing the captcha that is re-implemented in CaseScraper.py.