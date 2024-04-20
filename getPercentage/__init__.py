import subprocess
import psutil


def get_percentage_on_linux():
    try:
        result = subprocess.run(['upower', '-i', '/org/freedesktop/UPower/devices/battery_BAT0'], capture_output=True,
                                text=True)

        output_lines = result.stdout.split('\n')
        print(output_lines, end="/n")
        for line in output_lines:
            if 'percentage' in line:
                percentage = int(line.strip().split()[1][:-1])
                return percentage
    except Exception as e:
        print("Error:", e)
        return None


def get_percentage_on_windows():
    battery = psutil.sensors_battery()
    if battery is not None:
        return battery.percent
    else:
        return None, "Battery is not Present"
