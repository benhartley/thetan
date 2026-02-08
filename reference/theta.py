"""
Theta Robot MakeCode Python Reference
=====================================

This file documents the Theta robot API as it appears in MakeCode Python.
It is a reference for writing tutorials - NOT executable Python code.

NAMING CONVENTIONS:
- Methods: snake_case (e.g., robot_goms, not robotGoms)
- Enum types: RX prefix with PascalCase (e.g., RXDirection, not RxDirection)
- Enum values: PascalCase (e.g., Forward, not FORWARD)

The original TypeScript source is in theta.ts. This file shows the
Python equivalents for use in MakeCode for micro:bit.

NOTE: This code runs on the micro:bit, not on a PC. The theta namespace
and enums are provided by the MakeCode environment.
"""

# ==============================================================================
# ENUMS
# ==============================================================================


class RXDirection:
    """Direction of travel for forward/reverse movement."""

    Forward = 0
    Reverse = 1


class RXRobotDirection:
    """Direction for spinning (left/right)."""

    Left = 0
    Right = 1


class RXMotor:
    """Motor selection."""

    Left = 0
    Right = 1
    Both = 2


class RXStopMode:
    """Stop modes for the robot."""

    Coast = 0  # Slow coast to stop (no brake)
    Brake = 1  # Rapid brake stop


class RXPingUnit:
    """Units for sonar/ultrasonic sensor readings."""

    Centimeters = 0
    Inches = 1
    MicroSeconds = 2


class RXMode:
    """Update mode for LEDs."""

    Manual = 0  # Requires led_show() to update
    Auto = 1  # Updates LEDs automatically on every change


class RXColors:
    """Pre-defined LED colours (hex RGB values)."""

    Red = 0xFF0000
    Orange = 0xFFA500
    Yellow = 0xFFFF00
    Green = 0x00FF00
    Blue = 0x0000FF
    Indigo = 0x4B0082
    Violet = 0x8A2BE2
    Purple = 0xFF00FF
    White = 0xFFFFFF
    Black = 0x000000


class RXBluetooth:
    """Enable/Disable Bluetooth (affects FireLeds on accessories)."""

    btEnable = 0
    btDisable = 1


class RXBuzz:
    """Buzzer state."""

    On = 0
    Off = 1


class RXLineSensor:
    """Line sensor selection."""

    Left = 0
    Right = 1


class RXLightSensor:
    """Light sensor selection."""

    Left = 0
    Right = 1


class RXIOMode:
    """ATMega I/O pin modes."""

    DigitalIn = 0
    InputPullup = 1
    DigitalOut = 2
    PWMOUT = 3
    Servo = 4


# Eyeball/Matrix enums (for 5x5 Matrix addon)
class eyePos:
    """Eyeball pupil positions for Matrix display."""

    Forward = 0
    Down = 1
    Up = 2
    Left = 3
    Right = 4
    DownLeft = 5
    DownRight = 6
    UpLeft = 7
    UpRight = 8


class eyeSize:
    """Eyeball pupil size."""

    Small = 0
    Large = 1


class bfEyes:
    """BitFace eye selection."""

    Left = 0
    Right = 1
    Both = 2


class bfMouth:
    """BitFace mouth styles."""

    Smile = 0
    Grin = 1
    Sad = 2
    Frown = 3
    Straight = 4
    Oooh = 5
    Eeeh = 6


# ==============================================================================
# THETA NAMESPACE - Motor Functions
# ==============================================================================


class theta:
    """
    Theta robot control functions.

    In MakeCode Python, these are called as theta.function_name().
    This class documents the available API.
    """

    # --------------------------------------------------------------------------
    # MOTOR CONTROL
    # --------------------------------------------------------------------------

    @staticmethod
    def robot_go(direction: RXDirection, speed: int) -> None:
        """
        Move robot forward or backward continuously.

        Args:
            direction: RXDirection.Forward or RXDirection.Reverse
            speed: Speed of motor (0 to 100)

        Example:
            theta.robot_go(RXDirection.Forward, 60)
        """
        pass

    @staticmethod
    def robot_goms(direction: RXDirection, speed: int, milliseconds: int) -> None:
        """
        Move robot forward or backward for a specified duration, then stop.

        Args:
            direction: RXDirection.Forward or RXDirection.Reverse
            speed: Speed of motor (0 to 100)
            milliseconds: Duration to move in milliseconds

        Example:
            theta.robot_goms(RXDirection.Forward, 50, 2000)  # Forward at 50% for 2 seconds
        """
        pass

    @staticmethod
    def robot_rotate(direction: RXRobotDirection, speed: int) -> None:
        """
        Spin robot in place continuously.

        Args:
            direction: RXRobotDirection.Left or RXRobotDirection.Right
            speed: Speed of motors (0 to 100)

        Example:
            theta.robot_rotate(RXRobotDirection.Left, 70)
        """
        pass

    @staticmethod
    def robot_rotatems(
        direction: RXRobotDirection, speed: int, milliseconds: int
    ) -> None:
        """
        Spin robot in place for a specified duration, then stop.

        Args:
            direction: RXRobotDirection.Left or RXRobotDirection.Right
            speed: Speed of motors (0 to 100)
            milliseconds: Duration to spin in milliseconds

        Example:
            theta.robot_rotatems(RXRobotDirection.Right, 50, 400)  # Spin right for 400ms
        """
        pass

    @staticmethod
    def robot_stop(mode: RXStopMode) -> None:
        """
        Stop the robot.

        Args:
            mode: RXStopMode.Coast (slow stop) or RXStopMode.Brake (rapid stop)

        Example:
            theta.robot_stop(RXStopMode.Brake)
        """
        pass

    @staticmethod
    def motor_move(motor: RXMotor, direction: RXDirection, speed: int) -> None:
        """
        Move individual motor(s) forward or reverse.

        Args:
            motor: RXMotor.Left, RXMotor.Right, or RXMotor.Both
            direction: RXDirection.Forward or RXDirection.Reverse
            speed: Speed of motor (0 to 100)

        Example:
            theta.motor_move(RXMotor.Left, RXDirection.Forward, 40)
        """
        pass

    @staticmethod
    def motor_movems(
        motor: RXMotor, direction: RXDirection, speed: int, duration: int
    ) -> None:
        """
        Move individual motor(s) for a specified duration.

        Args:
            motor: RXMotor.Left, RXMotor.Right, or RXMotor.Both
            direction: RXDirection.Forward or RXDirection.Reverse
            speed: Speed of motor (0 to 100)
            duration: Duration in milliseconds

        Example:
            theta.motor_movems(RXMotor.Both, RXDirection.Forward, 60, 1000)
        """
        pass

    @staticmethod
    def motor_bias(direction: RXRobotDirection, bias: int) -> None:
        """
        Set motor bias to correct veering.

        If robot veers right, set bias to Left. If robot veers left, set bias to Right.

        Args:
            direction: RXRobotDirection.Left or RXRobotDirection.Right
            bias: Percentage to bias (0 to 80)

        Example:
            theta.motor_bias(RXRobotDirection.Left, 5)  # Bias left by 5%
        """
        pass

    # --------------------------------------------------------------------------
    # FIRELED CONTROL (Built-in 14 RGB LEDs)
    # --------------------------------------------------------------------------

    @staticmethod
    def leds_color(rgb: int) -> None:
        """
        Set all LEDs to a given color.

        Args:
            rgb: RGB color as hex value (e.g., 0xff0000 for red) or RXColors enum

        Example:
            theta.leds_color(0x00ff00)       # Green (hex)
            theta.leds_color(RXColors.Red)   # Red (enum)
        """
        pass

    @staticmethod
    def led_clear() -> None:
        """
        Clear all LEDs (turn them off).

        Example:
            theta.led_clear()
        """
        pass

    @staticmethod
    def set_pixel(led_id: int, rgb: int) -> None:
        """
        Set a single LED to a given color.

        Args:
            led_id: Position of the LED (0 to 13)
            rgb: RGB color as hex value or RXColors enum

        Example:
            theta.set_pixel(3, 0xff0000)  # Set LED 3 to red
        """
        pass

    @staticmethod
    def led_rainbow(direction: bool) -> None:
        """
        Show a rainbow pattern on all LEDs.

        Args:
            direction: True for up (red at 0), False for down

        Example:
            theta.led_rainbow(True)
        """
        pass

    @staticmethod
    def led_shift(direction: bool) -> None:
        """
        Shift LEDs and clear with zeros.

        Args:
            direction: True for up (0 to 1), False for down

        Example:
            theta.led_shift(False)
        """
        pass

    @staticmethod
    def led_rotate(direction: bool) -> None:
        """
        Rotate LEDs (wraps around).

        Args:
            direction: True for up (0 to 1), False for down

        Example:
            theta.led_rotate(True)
        """
        pass

    @staticmethod
    def led_brightness(brightness: int) -> None:
        """
        Set the brightness of all LEDs.

        Args:
            brightness: Brightness value (0 to 255, default is 40)

        Example:
            theta.led_brightness(100)
        """
        pass

    @staticmethod
    def set_update_mode(update_mode: RXMode) -> None:
        """
        Set LED update mode.

        Args:
            update_mode: RXMode.Auto (update on every change) or RXMode.Manual (requires led_show())

        Example:
            theta.set_update_mode(RXMode.Manual)
        """
        pass

    @staticmethod
    def led_show() -> None:
        """
        Show LED changes (only needed in Manual update mode).

        Example:
            theta.set_update_mode(RXMode.Manual)
            theta.set_pixel(0, RXColors.Red)
            theta.set_pixel(1, RXColors.Green)
            theta.led_show()  # Now both changes appear
        """
        pass

    @staticmethod
    def convert_rgb(red: int, green: int, blue: int) -> int:
        """
        Convert RGB values to a color number.

        Args:
            red: Red value (0 to 255)
            green: Green value (0 to 255)
            blue: Blue value (0 to 255)

        Returns:
            RGB color as integer

        Example:
            color = theta.convert_rgb(50, 100, 200)
            theta.leds_color(color)
        """
        pass

    @staticmethod
    def get_palette_entry(index: int) -> int:
        """
        Get color number from the palette at given index.

        Args:
            index: Index in color palette (0 to 24)

        Returns:
            RGB color as integer

        Example:
            color = theta.get_palette_entry(5)
        """
        pass

    # --------------------------------------------------------------------------
    # SENSORS
    # --------------------------------------------------------------------------

    @staticmethod
    def read_sonar(unit: RXPingUnit) -> int:
        """
        Read distance from ultrasonic sonar sensor.

        Args:
            unit: RXPingUnit.Centimeters, RXPingUnit.Inches, or RXPingUnit.MicroSeconds

        Returns:
            Distance in the specified unit

        Example:
            distance = theta.read_sonar(RXPingUnit.Centimeters)
        """
        pass

    @staticmethod
    def read_line(sensor: RXLineSensor) -> int:
        """
        Read line sensor value.

        Args:
            sensor: RXLineSensor.Left or RXLineSensor.Right

        Returns:
            Sensor reading (analog value)

        Example:
            left_line = theta.read_line(RXLineSensor.Left)
        """
        pass

    @staticmethod
    def read_light(sensor: RXLightSensor) -> int:
        """
        Read light sensor value.

        Args:
            sensor: RXLightSensor.Left or RXLightSensor.Right

        Returns:
            Light level (analog value)

        Example:
            light = theta.read_light(RXLightSensor.Left)
        """
        pass

    @staticmethod
    def read_dial() -> int:
        """
        Read the dial (potentiometer) value.

        Returns:
            Dial position (analog value)

        Example:
            dial_value = theta.read_dial()
        """
        pass

    @staticmethod
    def read_battery() -> int:
        """
        Read battery voltage.

        Returns:
            Battery voltage in millivolts (mV)

        Example:
            voltage = theta.read_battery()
        """
        pass

    # --------------------------------------------------------------------------
    # BUZZER
    # --------------------------------------------------------------------------

    @staticmethod
    def buzz(flag: bool) -> None:
        """
        Turn buzzer on or off.

        Args:
            flag: True for on, False for off

        Example:
            theta.buzz(True)   # Buzzer on
            theta.buzz(False)  # Buzzer off
        """
        pass

    # --------------------------------------------------------------------------
    # BLUETOOTH
    # --------------------------------------------------------------------------

    @staticmethod
    def enable_bluetooth(enable: RXBluetooth) -> None:
        """
        Enable or disable Bluetooth (affects FireLeds on accessories).

        Args:
            enable: RXBluetooth.btEnable or RXBluetooth.btDisable

        Example:
            theta.enable_bluetooth(RXBluetooth.btEnable)
        """
        pass

    # --------------------------------------------------------------------------
    # I/O PINS (ATMega328)
    # --------------------------------------------------------------------------

    @staticmethod
    def set_iomode(pin: int, mode: RXIOMode) -> None:
        """
        Set mode of ATMega I/O pins.

        Args:
            pin: Pin number (0 to 3)
            mode: RXIOMode.DigitalIn, DigitalOut, PWMOUT, Servo, or InputPullup

        Example:
            theta.set_iomode(0, RXIOMode.DigitalOut)
        """
        pass

    @staticmethod
    def read_iopin(pin: int) -> int:
        """
        Read ATMega I/O pin value.

        Args:
            pin: Pin number (0 to 3)

        Returns:
            Pin value

        Example:
            value = theta.read_iopin(0)
        """
        pass

    @staticmethod
    def write_iopin(value: int, pin: int) -> None:
        """
        Write to ATMega I/O pin.

        Args:
            value: Value to write
            pin: Pin number (0 to 3)

        Example:
            theta.write_iopin(1, 0)  # Set pin 0 high
        """
        pass

    # --------------------------------------------------------------------------
    # EEROM (Non-volatile storage)
    # --------------------------------------------------------------------------

    @staticmethod
    def read_eerom(location: int) -> int:
        """
        Read from EEROM.

        Args:
            location: Address to read from

        Returns:
            Value at location (0 to 255)

        Example:
            value = theta.read_eerom(0)
        """
        pass

    @staticmethod
    def write_eerom(value: int, location: int) -> None:
        """
        Write to EEROM.

        Args:
            value: Value to write (0 to 255)
            location: Address to write to

        Example:
            theta.write_eerom(42, 0)
        """
        pass

    # --------------------------------------------------------------------------
    # 5x5 MATRIX ADDON
    # --------------------------------------------------------------------------

    @staticmethod
    def mat_clear() -> None:
        """Clear all Matrix LEDs."""
        pass

    @staticmethod
    def set_matrix(rgb: int) -> None:
        """Set all Matrix LEDs to a color."""
        pass

    @staticmethod
    def set_mat_pixel(led_id: int, rgb: int) -> None:
        """Set single Matrix LED by linear position (0 to 24)."""
        pass

    @staticmethod
    def set_array_pixel(x: int, y: int, rgb: int) -> None:
        """Set Matrix LED by x,y position (0-4 each)."""
        pass

    @staticmethod
    def mat_rainbow() -> None:
        """Show rainbow pattern on Matrix."""
        pass

    @staticmethod
    def mat_rectangle(x1: int, y1: int, x2: int, y2: int, rgb: int, fill: bool) -> None:
        """Draw rectangle on Matrix."""
        pass

    @staticmethod
    def mat_show_eyeball(pos: eyePos, rgb: int, size: eyeSize) -> None:
        """Show eyeball on Matrix."""
        pass

    @staticmethod
    def mat_show_image(image, rgb: int) -> None:
        """Show image on Matrix."""
        pass

    @staticmethod
    def mat_show() -> None:
        """Show Matrix changes (in manual mode)."""
        pass

    @staticmethod
    def mat_brightness(brightness: int) -> None:
        """Set Matrix brightness (0 to 255)."""
        pass

    # --------------------------------------------------------------------------
    # BITFACE ADDON
    # --------------------------------------------------------------------------

    @staticmethod
    def set_bitface(rgb: int) -> None:
        """Set all BitFace LEDs to a color."""
        pass

    @staticmethod
    def set_bit_eye(eye: bfEyes, rgb: int) -> None:
        """Set BitFace eye(s) to a color."""
        pass

    @staticmethod
    def set_bit_nose(rgb: int) -> None:
        """Set BitFace nose to a color."""
        pass

    @staticmethod
    def set_bit_mouth(mouth: bfMouth, rgb: int) -> None:
        """Set BitFace mouth style and color."""
        pass

    @staticmethod
    def bit_brightness(brightness: int) -> None:
        """Set BitFace brightness (0 to 255)."""
        pass

    # --------------------------------------------------------------------------
    # OLED 128x64 ADDON
    # --------------------------------------------------------------------------

    @staticmethod
    def oled_text(text: str, x: int, y: int, inv: bool) -> None:
        """Show text on OLED."""
        pass

    @staticmethod
    def oled_number(num: int, x: int, y: int, inv: bool) -> None:
        """Show number on OLED."""
        pass

    @staticmethod
    def oled_update() -> None:
        """Update OLED from buffer."""
        pass

    @staticmethod
    def oled_set(on: bool) -> None:
        """Set all OLED pixels on or off."""
        pass

    @staticmethod
    def oled_invert(inv: bool) -> None:
        """Invert OLED display colors."""
        pass

    @staticmethod
    def oled_zoom(zoom: bool) -> None:
        """Zoom OLED display."""
        pass

    @staticmethod
    def oled_plot_pixel(x: int, y: int, do_set: bool, update: bool) -> None:
        """Plot pixel on OLED."""
        pass

    @staticmethod
    def oled_line(
        x1: int, y1: int, x2: int, y2: int, do_set: bool, update: bool
    ) -> None:
        """Draw line on OLED."""
        pass

    @staticmethod
    def oled_rectangle(
        x1: int, y1: int, x2: int, y2: int, do_set: bool, update: bool
    ) -> None:
        """Draw rectangle on OLED."""
        pass

    @staticmethod
    def oled_circle(x: int, y: int, r: int, do_set: bool, update: bool) -> None:
        """Draw circle on OLED."""
        pass


# ==============================================================================
# QUICK REFERENCE
# ==============================================================================
"""
COMMON FUNCTIONS FOR TUTORIALS:

Movement:
    theta.robot_go(RXDirection.Forward, 60)
    theta.robot_goms(RXDirection.Forward, 50, 2000)
    theta.robot_rotate(RXRobotDirection.Left, 70)
    theta.robot_rotatems(RXRobotDirection.Right, 50, 400)
    theta.robot_stop(RXStopMode.Brake)
    theta.motor_move(RXMotor.Left, RXDirection.Forward, 40)
    theta.motor_bias(RXRobotDirection.Left, 5)

LEDs:
    theta.leds_color(RXColors.Green)
    theta.led_clear()
    theta.set_pixel(3, 0xff0000)
    theta.led_rainbow(True)
    theta.led_brightness(100)

Sensors:
    distance = theta.read_sonar(RXPingUnit.Centimeters)
    line = theta.read_line(RXLineSensor.Left)
    light = theta.read_light(RXLightSensor.Left)
    dial = theta.read_dial()
    battery = theta.read_battery()

Other:
    theta.buzz(True)
"""
