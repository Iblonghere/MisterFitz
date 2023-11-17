import psutil
import matplotlib.pyplot as plt
import seaborn as sns
import logging
import os
import subprocess



# Get system information
cpu_percent = psutil.cpu_percent()
memory_percent = psutil.virtual_memory().percent
disk_percent = psutil.disk_usage('/').percent



# Create a pie chart to visualize system usage
labels = ['CPU', 'Memory', 'Disk']
sizes = [cpu_percent, memory_percent, disk_percent]
colors = ['red', 'green', 'blue']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('System Usage')



# Create a line chart to visualize system usage over time
cpu_history = psutil.cpu_percent(percpu=True, interval=1)
memory_history = []
disk_history = []
for i in range(10):
    memory_history.append(psutil.virtual_memory().percent)
    disk_history.append(psutil.disk_usage('/').percent)

plt.figure()
plt.plot(cpu_history)
plt.plot(memory_history)
plt.plot(disk_history)
plt.legend(['CPU', 'Memory', 'Disk'])
plt.title('System Usage Over Time')



# Use system monitoring software to track network activity
# Here, we use the psutil library to get network connections and log any suspicious activity
connections = psutil.net_connections(kind='inet')
for conn in connections:
    if conn.status == 'ESTABLISHED' and conn.raddr:

        print(f"Established connection to {conn.raddr[0]}:{conn.raddr[1]}")



# Use custom log analysis tools to analyze system logs for security threats
# Here, we use the Python logging module to log any suspicious activity
logging.basicConfig(filename='security.log', level=logging.INFO)
logging.info('Unauthorized access attempt detected')



# Detect malware attacks
# Here, we use the Microsoft Defender Antivirus command-line utility to scan for malware

malware_files = []

def scan_directory(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            result = subprocess.run(['MpCmdRun.exe', '-Scan', '-ScanType', '3', '-File', full_path], capture_output=True, text=True)
            if 'found' in result.stdout.lower():
                malware_files.append(full_path)

for path in ['/home', '/var/www']:
    scan_directory(path)

if malware_files:
    print(f"Malware detected in files: {malware_files}")



# Detect insider threats
# Here, we use the psutil library to get a list of running processes and check for any suspicious activity
for proc in psutil.process_iter(['pid', 'name', 'username']):
    try:
        if proc.username() != 'root' and proc.name() not in ['python', 'bash']:
            print(f"Suspicious process detected: {proc.name()} (PID: {proc.pid}, User: {proc.username()})")
    except psutil.AccessDenied:
        pass


# Show the visualizations
plt.show()

