from pynput import mouse
from pynput.keyboard import Key, Listener, GlobalHotKeys, Controller
import time

# CODE FOR LISTENING TO KEYBOARD AND MOUSE STROKES
class ComputerTracker:
    def __init__(self):
        self.actions = []
        self.all_actions = []
        self.listening = False
        self.exit = False

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
            self.exit = True
            print("ON PRESS ESC WAS PRESSED")
            # click back in
            mouse_obj = mouse.Controller()
            keyboard = Controller()
            mouse_obj.press(mouse.Button.left)
            keyboard.press(Key.esc)

            self.start_robot_bool = False
            self.actions = []
            self.all_actions = []
            return False

        # Activate the robot
        if len(self.all_actions) >= 3 and self.all_actions[-3][0] == 'press' and self.all_actions[-3][1] == Key.ctrl and self.all_actions[-2][0] == 'press' and self.all_actions[-2][1] == Key.shift:
            try:
                if key.char == 's': # Start
                    print("START ROBOT MODE ACTIVATED")
                    self.start_robot()
                    self.listening = False
                elif key.char == 'l': # Listen
                    print("LISTENING MODE ACTIVATED")
                    self.listening = True
                    self.actions = []
                elif key.char == 'd': # Done listening
                    print("LOADED MODE ACTIVATED. PRESS CTRL+SHIFT+S TO START ROBOT")
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
        print("STARTING ROBOT EXECUTION")
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

        print("COMPLETED ROBOT EXECUTION")


print("...starting...")
CT = ComputerTracker()
CT.handle_keyboard_events()
print("...ending...")