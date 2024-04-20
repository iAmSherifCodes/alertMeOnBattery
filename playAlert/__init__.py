import playsound


def alert_on_linux(percentage, percent):
    if percentage is not None:
        if percentage < percent:
            print("Yo! Battery percentage is below 50%!")
            playsound.playsound("alert_sound.mp3")
        else:
            print("Battery percentage is above 50%.")
    else:
        print("Unable to fetch battery information.")

