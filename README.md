# <b> Auto Clicker Typer </b>

<b> Demo: </b> Auto Clicker Typer repeating self-made sequence of clicks and types after 1 shortcut press

https://user-images.githubusercontent.com/33188761/209883268-ad0dbd29-e00a-43ac-bbc3-bcdf738a5069.mp4

## <b> Clicking and typing automation </b>

This is a simple auto repeat robot. This can be used if you need to click or type the same sequence a lot, and can repeat most sequences of mouse and keyboard actions on your full desktop screen.

<b> Control with shortcuts easily: </b>
- ⏺ Start recording: 'Ctrl' + ',' (Comma)
- ⏹ Stop and save recording: 'Ctrl' + '.' (Period)
- ⏯ Start robot to repeat recording: 'Ctrl' + '/' (Forward slash)
- 🚪 Exit application: 'Esc'

## <b> How to quick install </b>
<b>[3 min Youtube setup tutorial & walkthrough video here](https://youtu.be/LvmsKqfO8r4)</b>
1. Ensure that you have [python3](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installation/) installed
2. Download this repository (download and unzip or git clone)
3. Open up terminal or command prompt 
4. Navigate to the 'auto-clicker-typer' folder
5. Run 'pip install -r requirements.txt' OR 'pip install pynput'
6. Run 'python3 robot.py'
7. Start using the shortcuts

Note: on computers like Mac, you may need to go to System Preferences -> Security & Privacy -> Accessibility and check 'Terminal' to enable computer control.

## <b> How to change shortcuts </b> ##
If you'd like to change the shortcuts:
1. Edit the robot.py file and find the comment that says "# Activate the robot"
2. Change the " if key.char == ' ' " line to key.char == 'insert-new-key' for changing Start, Listen, or Done Listening shortcuts
3. Save the file and your new shortcut will be 'Ctrl' + 'insert-new-key'

## <b> Privacy Policy </b>
<b>No data collection.</b> No information, screen display, or data is collected, changed, or saved. Once you exit the application, all data is deleted. 

<b>Zero remote access.</b> In terms of security, this application does not allow other people or devices to control your computer or view your computer's data at any time or in any capacity. 

## <b> Liability </b>
Auto Clicker Typer is not liable for any misuse of this product. By using Auto Clicker Typer, you are agreeing to using this product responsibly.

## <b> Contact us </b>
Questions, comments, concerns? Email 1kevin.huang[at]gmail.com
