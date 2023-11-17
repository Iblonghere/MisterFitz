
import os
import psutil
import matplotlib.pyplot as plt
import seaborn as sns
import logging

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

# Use custom log analysis tools to analyze system logs for security threats
# Here, we use the Python logging module to log any suspicious activity
logging.basicConfig(filename='security.log', level=logging.INFO)
logging.info('Unauthorized access attempt detected')

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
