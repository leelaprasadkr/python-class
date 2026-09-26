THRESHOLD = 70.0

readings = []

while True:

    print("\n1-add reading 2-report 3-quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        value = float(input("Sensor value: "))
        readings.append(value)

    elif choice == "2":
        if not readings:
            print("No data yet.")
            continue

        alerts = 0

        for r in readings:
            if r > THRESHOLD:
                alerts += 1

        avg = sum(readings) / len(readings)

        print(f"Count={len(readings)} Average: {avg:.1f} Alerts: {alerts}")

    elif choice == "3":
        print("Mission console closed")
        break

    else:
        print("Invalid choice.")