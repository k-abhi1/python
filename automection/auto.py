
print("Started main.py...")

import time
import pyautogui as pi

guviLink = "https://www.guvi.in/referral/l/iswca"
name = "Meghna Kumari"

mail = "trialmail@gmai.com"
phoneNo = "9193929458"

def start():
    try:
        # Move to the hamburger icon and click
        pi.moveTo(x=1419, y=59)
        pi.click()
        time.sleep(1)
        
        # Move to the incognito option and click
        pi.moveTo(x=1306, y=147)
        pi.click()
        time.sleep(1)
        
        # Move to omnibox
        pi.moveTo(x=290, y=55)
        pi.click()
        time.sleep(1)
        
        # Paste the link and press enter
        pi.write(guviLink)
        time.sleep(0.5)
        pi.press("enter")
        
        # Wait for website to load
        time.sleep(5)
    except Exception as e:
        print(f"An error occurred in the start function: {e}")

def formFill():
    try:
        # Click on the register button
        pi.moveTo(x=250, y=600)
        pi.click()
        time.sleep(1)
        
        # Enter name
        pi.moveTo(x=912, y=345)
        pi.click()
        time.sleep(0.5)
        pi.write(name)
        
        # Move to email field and enter email
        pi.press('tab')
        time.sleep(0.5)
        pi.write(mail)
        
        # Move to phone number field and enter phone number
        pi.press('tab')
        time.sleep(0.5)
        pi.write(phoneNo)
        
        # Move to Preferred language section and select language
        pi.press('tab')
        time.sleep(0.5)
        for _ in range(6):  # Adjust number of `down` presses as needed
            pi.press('down')
            time.sleep(0.1)
        pi.press('enter')
        
        # Select student option
        pi.moveTo(x=883, y=724)
        pi.click()
        time.sleep(1)
        
        # Additional steps can be added here to select education stream and college name
        # Click on register now
        # pi.moveTo(x=<X_COORD>, y=<Y_COORD>)
        # pi.click()
    except Exception as e:
        print(f"An error occurred in the formFill function: {e}")

# Run the automation script
start()
formFill()

# Display mouse position for debugging purposes
# Uncomment this line for testing to see coordinates
# pi.displayMousePosition()


