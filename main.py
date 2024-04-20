import checkOS
import getPercentage
from playAlert import alert_on_linux


def main():
    os_name = checkOS.get_os()

    if os_name == "Linux":
        percentage = getPercentage.get_percentage_on_linux()
        alert_on_linux(percentage, 50)
    elif os_name == 'Windows':
        percentage = getPercentage.get_percentage_on_windows()
        # soundAlert.
    elif os_name == 'Darwin':
        pass
    else:
        print("Unknown operating system.")


if __name__ == "__main__":
    main()
