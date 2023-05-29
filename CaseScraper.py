# --- Import Data Below Copied from Franklin County Code (removing Chrome imports) --- #
# Importing sys, os, and argparse to do command prompt interaction etc
import sys
import os
import argparse
# Importing all needed Selenium stuff
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
# Import Beautiful Soup for parsing the HTML
from bs4 import BeautifulSoup
# Import csv and json for writing to file
import csv
import json
# Import regular expressions for searching final page
import re
# Import time and random to use for spacing out requests
import time
import random
# Import Pretty Printing to make the printing pretty
import pprint

from selenium.webdriver.support.wait import WebDriverWait
# tqdm to make progress bars look nice
from tqdm import tqdm

# Import datetime to setup default "date-to" for today.
from datetime import date
today = date.today().strftime("%m/%d/%Y")


def single_scrape(case_number, date_from='01/01/1900', date_to=today):
    # Initialize webdriver with Firefox, running in headless mode for efficiency.
    options = Options()
    options.add_argument("-headless")
    driver = webdriver.Firefox(options=options)

    # Line below written for seeing window for testing purposes.
    driver = webdriver.Firefox()

    # Testing case data extraction with random Jane Doe case.
    search_page = 'https://portal-dc.tylertech.cloud/Portal/Home/Dashboard/26'
    driver.get(search_page)

    # Initializing wait.
    wait = WebDriverWait(driver, 20)

    # Waiting for window to load page.
    wait.until(EC.number_of_windows_to_be(1))

    # Store the ID of the original window.
    original_window = driver.current_window_handle

    # Establishing salient xpaths of elements to utilize on webpage.
    search_type_dropdown = driver.find_element(By.XPATH, '//select[@id="cboHSSearchBy"]')
    search_button = driver.find_element(By.XPATH, '//input[@id="btnHSSubmit"]')
    search_by_date_from = driver.find_element(By.XPATH, '//input[@id="SearchCriteria_DateFrom"]')
    search_by_date_to = driver.find_element(By.XPATH, '//input[@id="SearchCriteria_DateTo"]')

    # Selects "Case Number" from the "Select Search Types" dropdown menu.
    select_case_number = Select(search_type_dropdown)
    select_case_number.select_by_value("CaseNumber")

    # Locates and inputs case number, date range, and initiates search.
    case_search = driver.find_element(By.XPATH, '//input[@id="SearchCriteria_SearchValue"]')
    case_search.send_keys(case_number)
    search_by_date_from.send_keys(date_from)
    search_by_date_to.send_keys(date_to)
    search_button.click()

    # Establish first URL in list, then clicks to open case.
    case_link = By.XPATH, '//a[@class="caseLink show-only-in-desktop-view"]'
    wait.until(EC.element_to_be_clickable(case_link)).click()

    # Waits for the new window or tab.
    wait.until(EC.number_of_windows_to_be(2))

    # Loop through until we find a new window handle.
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    # Locates case name, prints it, closes tab. Used in testing for now.
    case_name = By.XPATH, '//span[@class="roa-text-bold ng-binding"]'
    wait.until(EC.presence_of_element_located(case_name))
    case_name = driver.find_element(By.XPATH, '//span[@class="roa-text-bold ng-binding"]').text
    print(case_name)
    driver.close()

    # DATA TO GATHER:
    # Parties
    # Attorneys
    # Dispositions
    # Docket
    # Status
    # File-date

single_scrape(case_number="2003-ADM-001639")
