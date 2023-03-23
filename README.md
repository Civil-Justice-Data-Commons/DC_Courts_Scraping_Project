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

## Summary as of 3/21/2023:
* Found way to circumvent captcha on website, so all of that lovely code is completely and utterly useless.
* Reading through documentation from Selenium directly was very helpful (as was reviewing James Carey's prior code)
* Case number generator and scope of how to establish a search (i.e., does user input starting year? Do we scrape _every_ case possible? Need to check with James).
* Selenium is a headache, but it's starting to make sense.
* Based on browsing through random cases, it looks as though the case numbers with a 'CA' (like the example case) have a random character at the end; some even had L(RB).
  * While I'm not sure what that letter means, it does mean that the other combinations not using 'CA' don't need an optional letter. Made a note of this in my code.