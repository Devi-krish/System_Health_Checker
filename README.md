# System_Health_Checker
Python System Monitoring Tool


📌 Project Overview
System Health Checker is a Python-based monitoring tool that checks the real-time health of a computer system.  
It continuously monitors **CPU usage, RAM usage, and Disk usage**, displays warnings when usage is high, and logs system health data into a text file with date and time.

This project is useful for **IT Support, Technical Support, Desktop Support, and System Monitoring roles**.

---

 🎯 Why This Project?
In real-world IT environments, system performance issues like high CPU, low memory, or low disk space can cause:
- System slowness
- Application crashes
- Poor user experience

This tool helps in **proactively identifying system issues** before they become critical.

---

🧠 Why `psutil` is Used?
`psutil` (Process and System Utilities) is a Python library used to retrieve:
- CPU usage
- Memory (RAM) usage
- Disk usage
- System performance metrics

It allows Python programs to interact directly with the operating system and collect real-time system health information, which is essential for monitoring and troubleshooting.

---

 🛠️ Technologies Used
- **Python 3**
- **psutil** – for system resource monitoring
- **datetime** – to add date and time to logs
- **time** – to refresh system checks every 5 seconds

---
 ⚙️ Features
- ✅ Real-time CPU usage monitoring
- ✅ Real-time RAM usage monitoring
- ✅ Disk space usage monitoring
- ⚠️ Warning messages when usage exceeds safe limits
- ⏱️ Auto-refresh every 5 seconds
- 🕒 Logs system health with date & time
- 📄 Saves reports automatically to a text file
- 🧩 Can be converted to a standalone `.exe` file

---


---

 ▶️ How to Run the Project

 1️⃣ Install Python
python --version  
pip install psutil                    Install Required Library
python system_health_checker.py    Run the Program

Use Cases

IT Support system monitoring

Desktop Support troubleshooting

Learning system resource management

Entry-level monitoring automation

Background system health logging


