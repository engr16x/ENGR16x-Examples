# Button.py

# Created by Aayush Iyengar on behalf on the ENGR 16X Teaching Team

### DO NOT MODIFY CODE IN THIS FILE ###

from gpiozero import DigitalInputDevice
from gpiozero import HoldMixIn

class Button(HoldMixin, DigitalInputDevice):
    """
    Extends :class:`DigitalInputDevice` and represents a simple push button
    or switch.

    Connect one side of the button to a ground pin, and the other to any GPIO
    pin. Alternatively, connect one side of the button to the 3V3 pin, and the
    other to any GPIO pin, then set *pull_up* to :data:`False` in the
    :class:`Button` constructor.

    The following example will print a line of text when the button is pushed::

        from gpiozero import Button

        button = Button(4)
        button.wait_for_press()
        print("The button was pressed!")

    :type pin: int or str
    :param pin:
        The GPIO pin which the button is connected to. See :ref:`pin-numbering`
        for valid pin numbers. If this is :data:`None` a :exc:`GPIODeviceError`
        will be raised.

    :type pull_up: bool or None
    :param pull_up:
        If :data:`True` (the default), the GPIO pin will be pulled high by
        default.  In this case, connect the other side of the button to ground.
        If :data:`False`, the GPIO pin will be pulled low by default. In this
        case, connect the other side of the button to 3V3. If :data:`None`, the
        pin will be floating, so it must be externally pulled up or down and
        the ``active_state`` parameter must be set accordingly.

    :type active_state: bool or None
    :param active_state:
        See description under :class:`InputDevice` for more information.

    :type bounce_time: float or None
    :param bounce_time:
        If :data:`None` (the default), no software bounce compensation will be
        performed. Otherwise, this is the length of time (in seconds) that the
        component will ignore changes in state after an initial change.

    :param float hold_time:
        The length of time (in seconds) to wait after the button is pushed,
        until executing the :attr:`when_held` handler. Defaults to ``1``.

    :param bool hold_repeat:
        If :data:`True`, the :attr:`when_held` handler will be repeatedly
        executed as long as the device remains active, every *hold_time*
        seconds. If :data:`False` (the default) the :attr:`when_held` handler
        will be only be executed once per hold.

    :type pin_factory: Factory or None
    :param pin_factory:
        See :doc:`api_pins` for more information (this is an advanced feature
        which most users can ignore).
    """
    def __init__(self, pin=None, *, pull_up=True, active_state=None,
                 bounce_time=None, hold_time=1, hold_repeat=False,
                 pin_factory=None):
        super().__init__(
            pin, pull_up=pull_up, active_state=active_state,
            bounce_time=bounce_time, pin_factory=pin_factory)
        self.hold_time = hold_time
        self.hold_repeat = hold_repeat

    @property
    def value(self):
        """
        Returns 1 if the button is currently pressed, and 0 if it is not.
        """
        return super().value



Button.is_pressed = Button.is_active
Button.pressed_time = Button.active_time
Button.when_pressed = Button.when_activated
Button.when_released = Button.when_deactivated
Button.wait_for_press = Button.wait_for_active
Button.wait_for_release = Button.wait_for_inactive