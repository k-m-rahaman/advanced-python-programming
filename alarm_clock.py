import time
import datetime

alarms = []

def add_alarm():
    alarm = input("Enter alarm time (HH:MM:SS): ")
    alarms.append(alarm)
    print("Alarm added!")

def check_alarms():
    current = datetime.datetime.now().strftime("%H:%M:%S")
    if current in alarms:
        print(f"\n⏰ Alarm for {current}!")
        for _ in range(3):
            print("🔔 Wake up!")
            time.sleep(1)
        alarms.remove(current)

while True:
    print("\n1. Add Alarm\n2. Show Alarms\n3. Start Clock\n4. Exit")
    choice = input("Choice: ")

    if choice == "1":
        add_alarm()

    elif choice == "2":
        print("Alarms:", alarms)

    elif choice == "3":
        print("Clock started... Press Ctrl+C to stop")
        try:
            while True:
                print(datetime.datetime.now().strftime("%H:%M:%S"), end="\r")
                check_alarms()
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nStopped.")

    else:
        break