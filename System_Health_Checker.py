import psutil
import time
from datetime import datetime

while True:
    print("\n===== SYSTEM HEALTH CHECK =====")

    # Time
    now = datetime.now()
    current_time = now.strftime("%d-%m-%Y %H:%M:%S")
    print("TIME:", current_time)

    # CPU
    cpu_usage = psutil.cpu_percent(interval=1)
    print("CPU Usage :", cpu_usage, "%")

    # RAM
    ram = psutil.virtual_memory()
    print("RAM Usage :", ram.percent, "%")

    # Disk
    disk = psutil.disk_usage('/')
    print("Disk Usage:", disk.percent, "%")

    # Alerts
    if cpu_usage > 80:
        print("⚠️ WARNING: CPU usage is high!")
    if ram.percent > 80:
        print("⚠️ WARNING: RAM usage is high!")
    if disk.percent > 80:
        print("⚠️ WARNING: Disk space is low!")

    # Log to file
    with open("system_report.txt", "a") as file:
        file.write("TIME: " + current_time + "\n")
        file.write("CPU Usage: " + str(cpu_usage) + "%\n")
        file.write("RAM Usage: " + str(ram.percent) + "%\n")
        file.write("Disk Usage: " + str(disk.percent) + "%\n")
        file.write("---------------------------\n")

    time.sleep(5)
