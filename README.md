# Splashed
Adidas bot that creates chrome sessions to wait on the splash page for exclusive releases

# Requirements
- Python 3.5 or later
- Latest version of Chrome
- Libraries: selenium, bs4, zip

# Setup Instructions (follow before running)
- Enter a region locale in config.txt (au, uk, fr, ca, us)
- Enter the splash url in config.txt
- Enter the name of your proxies file in config.txt (Do not include .txt)
- Proxies must be entered one per line (Enter 'localhost' if you do not want to use a proxy)
- Enter a custom css selector (Optional)
- Download all files and run Splashed.py

# Tips
- Stress test your desired amount of tasks you want to run prior to release to see what your computer can handle
- Initialize tasks prior to release (Tasks may take longer to initialize based on the number of tasks and your computer specifications)
- Log in to Gmail when prompted to pass Adidas browser verification and get easier captchas
- If you receive a spinning Add To Cart button on the product page, inject ATC script on the opened cart page
- Region homepages and splash page will take longer to load during a release, be patient (Page reloads are built-in)
- More proxies = more sessions = greater poissibility for success
- Do not minimize any browser sessions, they will be rendered useless (Browser sessions will auto-hide)

Feel free to submit any issues or bugs you encounter, I will do my best to address them!
