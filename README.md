# Splashed 
###### Status: Under Development
Adidas bot that waits on splash headlessly

### Requirements
- Python 3.6 or later
- Libraries: selenium, bs4, zip (Install via pip)
- Chrome: https://www.google.com/chrome/

### Setup Instructions (follow before running)
- Satisfy aforementioned requirements
- Enter a region locale in config.txt (au, uk, fr, ca, us)
- Enter the splash url in config.txt
- Enter the name of your proxies text file in config.txt (Do not include .txt)
- Proxies must be entered one per line (Enter 'localhost' if you do not want to use a proxy)
- Enter a custom css selector (Optional)
- Download as ZIP

### Tips
- Stress test your desired amount of tasks you want to run prior to release to see what your cpu can handle (Tested to handle 200+ tasks on an AWS m5.4xlarge server)
- Log in to Gmail when prompted to pass Adidas browser verification and get easier captchas
- If you receive a spinning Add To Cart button on the product page, inject ATC script on the opened cart page
- Splash page will take longer to load during a release, be patient
- More tasks = greater possibility for success
- If you close a checkout browser you will NOT be able to reopen it, be careful

## To Do
- [ ] Use proxy with checkout browser
- [ ] Slack Notifications
- [ ] Discord Notifications
- [ ] Get gceeqs cookie
- [ ] Get product page cookies
- [ ] ATC
- [ ] Get cart cookies

Feel free to submit any issues or bugs you encounter, I will do my best to address them!
