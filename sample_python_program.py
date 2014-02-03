from boost_xbox_controller import XBoxControllerManager

xbox_controller_manager = XBoxControllerManager()
success = xbox_controller_manager.initialize()


NO_ACTION = 0
LEFT_THUMBSTICK_HORIZONTAL = 1
LEFT_THUMBSTICK_VERTICAL = 2
RIGHT_THUMBSTICK_HORIZONTAL = 3
RIGHT_THUMBSTICK_VERTICAL = 4
BUTTON_PRESSED = 5
BUTTON_RELEASED = 6


def no_action(junk):
    pass


def left_thumbstick_horizontal(value):
    print "left thumbstick horizontal %s" % value


def left_thumbstick_vertical(value):
    print "left thumbstick vertical %s" % value


def right_thumbstick_horizontal(value):
    print "right thumbstick horizontal %s" % value


def right_thumbstick_vertical(value):
    print "right thumbstick vertical %s" % value


def button_pressed(button_value):
    print "button pressed %s" % button_value


def button_released(button_value):
    print "button released %s" % button_value


EVENT_FUNCTIONS = {
    NO_ACTION: no_action,
    LEFT_THUMBSTICK_HORIZONTAL: left_thumbstick_horizontal,
    LEFT_THUMBSTICK_VERTICAL: left_thumbstick_vertical,
    RIGHT_THUMBSTICK_HORIZONTAL: right_thumbstick_horizontal,
    RIGHT_THUMBSTICK_VERTICAL: right_thumbstick_vertical,
    BUTTON_PRESSED: button_pressed,
    BUTTON_RELEASED: button_released
}

if success:
    while True:
        event_id, value = xbox_controller_manager.get_next_event()
        func = EVENT_FUNCTIONS.get(event_id, no_action)
        func(value)
