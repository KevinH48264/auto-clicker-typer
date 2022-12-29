from pynput import mouse
from pynput.keyboard import Key, Listener, GlobalHotKeys, Controller
import time
import sys

# CODE FOR LISTENING TO AND CONTROLLING KEYBOARD AND MOUSE STROKES
class ComputerTracker:
    def __init__(self, repeat_times):
        self.actions = []
        self.all_actions = []
        self.listening = False
        self.exit = False
        self.repeat_times = repeat_times

    def on_move(self, x, y):
        if self.listening:
            self.actions += [('move', (x, y))]

    def on_click(self, x, y, button, pressed):
        if self.listening:
            self.actions += [('click', [x, y, pressed])]

    def on_scroll(self, x, y, dx, dy):
        if self.listening:
            self.actions += [('scroll', [x, y, dx, dy])]

    def on_press(self, key):
        self.all_actions += [('press', key)]
        if self.listening:
            self.actions += [('press', key)]

        if key == Key.esc:
            mouse_obj = mouse.Controller()
            keyboard = Controller()
            mouse_obj.release(mouse.Button.left)
            keyboard.press(Key.esc)

            self.start_robot_bool = False
            self.actions = []
            self.all_actions = []
            return False

        # Activate the robot
        if len(self.all_actions) >= 2 and self.all_actions[-2][0] == 'press' and self.all_actions[-2][1] == Key.ctrl:
            try:
                if key.char == '/': # Start
                    print("\n⏯ Starting robot to repeat recording. \n    To stop the application, press 'Esc' after the recording is over.")
                    self.listening = False
                    self.start_robot()
                elif key.char == ',': # Listen
                    print("\n⏺ Starting to record your mouse and keyboard actions. \n    To stop and save your recording, press 'Ctrl' + '.'\n    To restart your recording, press 'Ctrl' + ','")
                    self.listening = True
                    self.actions = []
                elif key.char == '.': # Done listening
                    print("\n⏹ Stopping and saving recording. \n    To have the robot repeat your saved recording, press 'Ctrl' + '/'. Caution: you can only exit the application after the robot is complete, use with care!\n    To re-record, press 'Ctrl' + ','")
                    self.listening = False
            except AttributeError:
                pass

    def on_release(self, key):
        self.all_actions += [('press', key)]
        if self.listening:
            self.actions += [('release', key)]

    # Collect events until released
    def handle_keyboard_events(self):
        with mouse.Listener(
            on_scroll=self.on_scroll,
            on_move=self.on_move,
            on_click=self.on_click) as listener:
            with Listener(
                on_press=self.on_press,
                on_release=self.on_release
                ) as listener:
                    listener.join()

    def start_robot(self):
        mouse_obj = mouse.Controller()
        keyboard = Controller()

        actions = self.actions[3:-3] # trim the beginning and end commands

        time.sleep(1)
        print("\n🛫 Robot is starting your recording " + str(self.repeat_times) + " time(s)")
        for _ in range(self.repeat_times):
            for a in actions:
                instruction = a[0]
                value = a[1]

                if instruction == "move":
                    mouse_obj.move(value[0] - mouse_obj.position[0], value[1] - mouse_obj.position[1])
                elif instruction == "click" and value[2]:
                    mouse_obj.move(value[0] - mouse_obj.position[0], value[1] - mouse_obj.position[1])
                    mouse_obj.press(mouse.Button.left)
                elif instruction == "scroll":
                    mouse_obj.scroll(value[2], value[3])
                elif instruction == "click" and not value[2]:
                    mouse_obj.move(value[0] - mouse_obj.position[0], value[1] - mouse_obj.position[1])
                    mouse_obj.release(mouse.Button.left)
                elif instruction == "press":
                    if value == Key.enter:
                        time.sleep(0.05)

                    keyboard.press(value)
                elif instruction == "release":
                    keyboard.release(value)

                time.sleep(0.01)

        print("\n🛬 Robot has completed your recording.")
        time.sleep(1)
        print("\n⏺ To start recording again, press 'Ctrl' + ','\n⏯ To have the robot repeat your recording again, press 'Ctrl' + '/'\n🚪To exit, press 'Esc'")

# main code here
overview = "This is a simple auto repeat robot. \n\
This can be used if you need to click or type a lot, and can repeat most keyboard and mouse actions you make."

instructions = "\nControl with shortcuts easily:\n\
    ⏺ Start recording: 'Ctrl' + ',' (Comma) \n\
    ⏹ Stop and save recording: 'Ctrl' + '.' (Period) \n\
    ⏯ Start robot to repeat recording: 'Ctrl' + '/' (Forward slash) \n\
    🚪Exit application: 'Esc'" 

# number of times for robot to repeat
repeat_times = 1
if len(sys.argv) > 1:
    repeat_times = int(sys.argv[1])

CT = ComputerTracker(repeat_times)
time.sleep(1)
print("✅ Application has started successfully. ✅\n")
time.sleep(1)
print("📝 Here are the instructions:")
time.sleep(1)
print(overview)
time.sleep(1)
print(instructions)
CT.handle_keyboard_events()

time.sleep(1)
print("\n✅ Application has ended successfully. ✅")