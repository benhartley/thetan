"""
Theta Robot MakeCode Python Reference
=====================================

This file documents the Theta robot API as it appears in MakeCode Python.
It is a reference for writing tutorials - NOT executable Python code.

NAMING CONVENTIONS:
- Methods: snake_case (e.g., robot_go_ms, not robotGoms)
- Enum types: PascalCase with Rx prefix (e.g., RxDirection, not RXDirection)
- Enum values: UPPERCASE (e.g., FORWARD, not Forward)

The original TypeScript source is in theta.ts. This file shows the
Python equivalents for use in MakeCode for micro:bit.

NOTE: This code runs on the micro:bit, not on a PC. The theta namespace
and enums are provided by the MakeCode environment.
"""

# ==============================================================================
# ENUMS
# ==============================================================================

class RxDirection:
    """Direction of travel for forward/reverse movement."""
    FORWARD = 0
    REVERSE = 1


class RxRobotDirection:
    """Direction for spinning (left/right)."""
    LEFT = 0
    RIGHT = 1


class RxMotor:
    """Motor selection."""
    LEFT = 0
    RIGHT = 1
    BOTH = 2


class RxStopMode:
    """Stop modes for the robot."""
    COAST = 0  # Slow coast to stop (no brake)
    BRAKE = 1  # Rapid brake stop


class RxPingUnit:
    """Units for sonar/ultrasonic sensor readings."""
    CENTIMETERS = 0
    INCHES = 1
    MICRO_SECONDS = 2


class RxMode:
    """Update mode for LEDs."""
    MANUAL = 0  # Requires show_led_changes() to update
    AUTO = 1    # Updates LEDs automatically on every change


class RxColors:
    """Pre-defined LED colours (hex RGB values)."""
    RED = 0xff0000
    ORANGE = 0xffa500
    YELLOW = 0xffff00
    GREEN = 0x00ff00
    BLUE = 0x0000ff
    INDIGO = 0x4b0082
    VIOLET = 0x8a2be2
    PURPLE = 0xff00ff
    WHITE = 0xffffff
    BLACK = 0x000000


class RxBluetooth:
    """Enable/Disable Bluetooth (affects FireLeds on accessories)."""
    BT_ENABLE = 0
    BT_DISABLE = 1


class RxBuzz:
    """Buzzer state."""
    ON = 0
    OFF = 1


class RxLineSensor:
    """Line sensor selection."""
    LEFT = 0
    RIGHT = 1


class RxLightSensor:
    """Light sensor selection."""
    LEFT = 0
    RIGHT = 1


class RxIOMode:
    """ATMega I/O pin modes."""
    DIGITAL_IN = 0
    INPUT_PULLUP = 1
    DIGITAL_OUT = 2
    PWM_OUT = 3
    SERVO = 4


# Eyeball/Matrix enums (for 5x5 Matrix addon)
class EyePos:
    """Eyeball pupil positions for Matrix display."""
    FORWARD = 0
    DOWN = 1
    UP = 2
    LEFT = 3
    RIGHT = 4
    DOWN_LEFT = 5
    DOWN_RIGHT = 6
    UP_LEFT = 7
    UP_RIGHT = 8


class EyeSize:
    """Eyeball pupil size."""
    SMALL = 0
    LARGE = 1


class BfEyes:
    """BitFace eye selection."""
    LEFT = 0
    RIGHT = 1
    BOTH = 2


class BfMouth:
    """BitFace mouth styles."""
    SMILE = 0
    GRIN = 1
    SAD = 2
    FROWN = 3
    STRAIGHT = 4
    OOOH = 5
    EEEH = 6


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
    def robot_go(direction: RxDirection, speed: int) -> None:
        """
        Move robot forward or backward continuously.
        
        Args:
            direction: RxDirection.FORWARD or RxDirection.REVERSE
            speed: Speed of motor (0 to 100)
        
        Example:
            theta.robot_go(RxDirection.FORWARD, 60)
        """
        pass
    
    @staticmethod
    def robot_go_ms(direction: RxDirection, speed: int, milliseconds: int) -> None:
        """
        Move robot forward or backward for a specified duration, then stop.
        
        Args:
            direction: RxDirection.FORWARD or RxDirection.REVERSE
            speed: Speed of motor (0 to 100)
            milliseconds: Duration to move in milliseconds
        
        Example:
            theta.robot_go_ms(RxDirection.FORWARD, 50, 2000)  # Forward at 50% for 2 seconds
        """
        pass
    
    @staticmethod
    def robot_rotate(direction: RxRobotDirection, speed: int) -> None:
        """
        Spin robot in place continuously.
        
        Args:
            direction: RxRobotDirection.LEFT or RxRobotDirection.RIGHT
            speed: Speed of motors (0 to 100)
        
        Example:
            theta.robot_rotate(RxRobotDirection.LEFT, 70)
        """
        pass
    
    @staticmethod
    def robot_rotate_ms(direction: RxRobotDirection, speed: int, milliseconds: int) -> None:
        """
        Spin robot in place for a specified duration, then stop.
        
        Args:
            direction: RxRobotDirection.LEFT or RxRobotDirection.RIGHT
            speed: Speed of motors (0 to 100)
            milliseconds: Duration to spin in milliseconds
        
        Example:
            theta.robot_rotate_ms(RxRobotDirection.RIGHT, 50, 400)  # Spin right for 400ms
        """
        pass
    
    @staticmethod
    def robot_stop(mode: RxStopMode) -> None:
        """
        Stop the robot.
        
        Args:
            mode: RxStopMode.COAST (slow stop) or RxStopMode.BRAKE (rapid stop)
        
        Example:
            theta.robot_stop(RxStopMode.BRAKE)
        """
        pass
    
    @staticmethod
    def motor_move(motor: RxMotor, direction: RxDirection, speed: int) -> None:
        """
        Move individual motor(s) forward or reverse.
        
        Args:
            motor: RxMotor.LEFT, RxMotor.RIGHT, or RxMotor.BOTH
            direction: RxDirection.FORWARD or RxDirection.REVERSE
            speed: Speed of motor (0 to 100)
        
        Example:
            theta.motor_move(RxMotor.LEFT, RxDirection.FORWARD, 40)
        """
        pass
    
    @staticmethod
    def motor_move_ms(motor: RxMotor, direction: RxDirection, speed: int, duration: int) -> None:
        """
        Move individual motor(s) for a specified duration.
        
        Args:
            motor: RxMotor.LEFT, RxMotor.RIGHT, or RxMotor.BOTH
            direction: RxDirection.FORWARD or RxDirection.REVERSE
            speed: Speed of motor (0 to 100)
            duration: Duration in milliseconds
        
        Example:
            theta.motor_move_ms(RxMotor.BOTH, RxDirection.FORWARD, 60, 1000)
        """
        pass
    
    @staticmethod
    def motor_bias(direction: RxRobotDirection, bias: int) -> None:
        """
        Set motor bias to correct veering.
        
        If robot veers right, set bias to LEFT. If robot veers left, set bias to RIGHT.
        
        Args:
            direction: RxRobotDirection.LEFT or RxRobotDirection.RIGHT
            bias: Percentage to bias (0 to 80)
        
        Example:
            theta.motor_bias(RxRobotDirection.LEFT, 5)  # Bias left by 5%
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
            rgb: RGB color as hex value (e.g., 0xff0000 for red) or RxColors enum
        
        Example:
            theta.leds_color(0x00ff00)       # Green (hex)
            theta.leds_color(RxColors.RED)  # Red (enum)
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
            rgb: RGB color as hex value or RxColors enum
        
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
    def set_update_mode(update_mode: RxMode) -> None:
        """
        Set LED update mode.
        
        Args:
            update_mode: RxMode.AUTO (update on every change) or RxMode.MANUAL (requires led_show())
        
        Example:
            theta.set_update_mode(RxMode.MANUAL)
        """
        pass
    
    @staticmethod
    def led_show() -> None:
        """
        Show LED changes (only needed in MANUAL update mode).
        
        Example:
            theta.set_update_mode(RxMode.MANUAL)
            theta.set_pixel(0, RxColors.RED)
            theta.set_pixel(1, RxColors.GREEN)
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
    def read_sonar(unit: RxPingUnit) -> int:
        """
        Read distance from ultrasonic sonar sensor.
        
        Args:
            unit: RxPingUnit.CENTIMETERS, RxPingUnit.INCHES, or RxPingUnit.MICRO_SECONDS
        
        Returns:
            Distance in the specified unit
        
        Example:
            distance = theta.read_sonar(RxPingUnit.CENTIMETERS)
        """
        pass
    
    @staticmethod
    def read_line(sensor: RxLineSensor) -> int:
        """
        Read line sensor value.
        
        Args:
            sensor: RxLineSensor.LEFT or RxLineSensor.RIGHT
        
        Returns:
            Sensor reading (analog value)
        
        Example:
            left_line = theta.read_line(RxLineSensor.LEFT)
        """
        pass
    
    @staticmethod
    def read_light(sensor: RxLightSensor) -> int:
        """
        Read light sensor value.
        
        Args:
            sensor: RxLightSensor.LEFT or RxLightSensor.RIGHT
        
        Returns:
            Light level (analog value)
        
        Example:
            light = theta.read_light(RxLightSensor.LEFT)
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
    def enable_bluetooth(enable: RxBluetooth) -> None:
        """
        Enable or disable Bluetooth (affects FireLeds on accessories).
        
        Args:
            enable: RxBluetooth.BT_ENABLE or RxBluetooth.BT_DISABLE
        
        Example:
            theta.enable_bluetooth(RxBluetooth.BT_ENABLE)
        """
        pass
    
    # --------------------------------------------------------------------------
    # I/O PINS (ATMega328)
    # --------------------------------------------------------------------------
    
    @staticmethod
    def set_io_mode(pin: int, mode: RxIOMode) -> None:
        """
        Set mode of ATMega I/O pins.
        
        Args:
            pin: Pin number (0 to 3)
            mode: RxIOMode.DIGITAL_IN, DIGITAL_OUT, PWM_OUT, SERVO, or INPUT_PULLUP
        
        Example:
            theta.set_io_mode(0, RxIOMode.DIGITAL_OUT)
        """
        pass
    
    @staticmethod
    def read_io_pin(pin: int) -> int:
        """
        Read ATMega I/O pin value.
        
        Args:
            pin: Pin number (0 to 3)
        
        Returns:
            Pin value
        
        Example:
            value = theta.read_io_pin(0)
        """
        pass
    
    @staticmethod
    def write_io_pin(value: int, pin: int) -> None:
        """
        Write to ATMega I/O pin.
        
        Args:
            value: Value to write
            pin: Pin number (0 to 3)
        
        Example:
            theta.write_io_pin(1, 0)  # Set pin 0 high
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
    def mat_show_eyeball(pos: EyePos, rgb: int, size: EyeSize) -> None:
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
    def set_bit_eye(eye: BfEyes, rgb: int) -> None:
        """Set BitFace eye(s) to a color."""
        pass
    
    @staticmethod
    def set_bit_nose(rgb: int) -> None:
        """Set BitFace nose to a color."""
        pass
    
    @staticmethod
    def set_bit_mouth(mouth: BfMouth, rgb: int) -> None:
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
    def oled_line(x1: int, y1: int, x2: int, y2: int, do_set: bool, update: bool) -> None:
        """Draw line on OLED."""
        pass
    
    @staticmethod
    def oled_rectangle(x1: int, y1: int, x2: int, y2: int, do_set: bool, update: bool) -> None:
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
    theta.robot_go(RxDirection.FORWARD, 60)
    theta.robot_go_ms(RxDirection.FORWARD, 50, 2000)
    theta.robot_rotate(RxRobotDirection.LEFT, 70)
    theta.robot_rotate_ms(RxRobotDirection.RIGHT, 50, 400)
    theta.robot_stop(RxStopMode.BRAKE)
    theta.motor_move(RxMotor.LEFT, RxDirection.FORWARD, 40)
    theta.motor_bias(RxRobotDirection.LEFT, 5)

LEDs:
    theta.leds_color(RxColors.GREEN)
    theta.led_clear()
    theta.set_pixel(3, 0xff0000)
    theta.led_rainbow(True)
    theta.led_brightness(100)

Sensors:
    distance = theta.read_sonar(RxPingUnit.CENTIMETERS)
    line = theta.read_line(RxLineSensor.LEFT)
    light = theta.read_light(RxLightSensor.LEFT)
    dial = theta.read_dial()
    battery = theta.read_battery()

Other:
    theta.buzz(True)
"""
