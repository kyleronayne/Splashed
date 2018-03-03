# Splashed 
###### Status: Under Development
Adidas bot that creates chrome sessions to wait on the splash page for exclusive releases

### Requirements
- Python 3.6 or later
- Libraries: selenium, bs4, zip (Install via pip)
- Chrome: https://www.google.com/chrome/

### Setup Instructions (follow before running)
- Satisfy aforementioned requirements
- Enter a region locale in config.txt (au, uk, fr, ca, us)
- Enter the splash url in config.txt
- Enter the name of your proxies file in config.txt (Do not include .txt)
- Proxies must be entered one per line (Enter 'localhost' if you do not want to use a proxy)
- Enter a custom css selector (Optional)
- Download as ZIP

### Tips
- Stress test your desired amount of tasks you want to run prior to release to see what your cpu can handle
- Log in to Gmail when prompted to pass Adidas browser verification and get easier captchas
- If you receive a spinning Add To Cart button on the product page, inject ATC script on the opened cart page
- Region homepages and splash page will take longer to load during a release, be patient (Page reloads are built-in)
- More proxies = more sessions = greater possibility for success
- Do not minimize any browser sessions, they will be rendered useless (Browser sessions will auto-hide)

## To Do
- [ ] Use proxy with checkout browser
- [ ] Get gceeqs cookie
- [ ] Get product page cookies
- [ ] ATC
- [ ] Get cart cookies

Feel free to submit any issues or bugs you encounter, I will do my best to address them!
