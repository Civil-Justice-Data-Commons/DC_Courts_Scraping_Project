# Notes re Grading & Due Date for this Project
* The day before his grades are due for 3L; even after finals, so precise date will be known soon, but it's after finals.
* The write-up can be 3-4, 7-8 pages; lots of writing, with small reflection section at the end. Not too time-consuming.

# Notes re: Website
* Captcha will begin testing for images after I ran about 5 tests. Going to test to see how long it takes for it to reset (an hour? maybe a day?)
  * Appears to be long-lasting, turning off VPN necessary, but it will "time-out" after about 3 searches. May be problematic.
  * Maybe search through something other than case numbers?
* Able to successfully load up one case and print the party names. Given that, it should be easy to extract most everything else. The hard part will be getting the searches done.
* Code is inefficient in the way it's handling elements; can eliminate most uses of time.sleep() with waiting for elements instead. Should be switchable in the near future.
* Code for circumventing captcha came from stackoverflow:
  * https://stackoverflow.com/questions/70945278/how-to-locate-and-click-on-the-recaptcha-checkbox-using-selenium-and-python
  * Found code on another thread to "switch" out of the iframe. Don't understand it entirely yet, but it ran well earlier.
* May be possible to, when loading up results, to load up each case in different tab perhaps and go tab-by-tab for extracting data?
* List of possible 3 letter strings for case number searches can be found on pgs. 10-11 here:
  * https://www.dccourts.gov/sites/default/files/portal/Portal_Case_Search_Guide_2022.pdf

## Update for 3/21/2023:
* Found way to circumvent captcha on website, so all of that lovely code is completely and utterly useless.
* Reading through documentation from Selenium directly was very helpful (as was reviewing James Carey's prior code)
* Case number generator and scope of how to establish a search (i.e., does user input starting year? Do we scrape _every_ case possible? Need to check with James).
* Selenium is a headache, but it's starting to make sense.
* Based on browsing through random cases, it looks as though the case numbers with a 'CA' (like the example case) have a random character at the end; some even had L(RB).
  * While I'm not sure what that letter means, it does mean that the other combinations not using 'CA' don't need an optional letter. Made a note of this in my code.

## Update for 5/22/2023
* Just graduated. Have until the end of this coming weekend to finalize and finish my code.
* Circumstances of graduation and the like are making it difficult to polish this code fully.
* However, I think I can get this code finished, if not very close to a finalized and polished state for James.

## Update for 5/28/2023
* Adapting the code for the new search page has been mostly painless so far.
* Figuring out which data to capture and how to store it is the part I'm most nervous about so far.
* However, I think locating the xpaths and getting the search code generator to work properly are the hard parts for James, as he can likely adapt the code easily to export however he sees best fits.
* Hence, I'm making the 'loop' of the program running through each case number the priority.