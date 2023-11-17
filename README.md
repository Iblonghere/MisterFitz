# MisterFitz 
The Python code for system monitoring and security analysis.

## Git Clone
git clone https://github.com/Iblonghere/MisterFitz

## Introduction (Windows/Linux)
This README file provides an overview of Mister Fitz the Python code for system monitoring and security analysis. The code utilizes various libraries and tools to gather system information, visualize system usage, track network activity, analyze system logs, detect malware attacks, and identify insider threats.

### Windows Code Overview
The Python code consists of the following main components:
1. System Information Retrieval: The code retrieves CPU, memory, and disk usage information using the `psutil` library.
2. Visualization: It creates visualizations of system usage using `matplotlib` and `seaborn`.
3. Network Activity Tracking: The code uses the `psutil` library to track network connections and log suspicious activity.
4. Log Analysis: It utilizes the Python `logging` module to log suspicious activity in a security log file.
5. Malware Detection: The code scans directories for malware using the Microsoft Defender Antivirus command-line utility.
6. Insider Threat Detection: It uses the `psutil` library to identify suspicious running processes.

### Usage
To use the code, follow these steps:
1. Ensure that the required libraries (`psutil`, `matplotlib`, `seaborn`) are installed.
2. Run the Python script to retrieve system information, visualize system usage, track network activity, analyze system logs, and detect security threats.

## Linux Code Overview
Installation:
1. Ensure Python is installed on the Linux system.
2. Install the required dependencies using pip: 
   $ pip install psutil matplotlib seaborn

## Usage:
1. Run the Python script using the command: 
   $ python FitzLinux.py
2. View the generated pie chart and line chart to analyze system usage.

## Dependencies:
- psutil
- matplotlib
- seaborn

## Visualizations:
The code generates a pie chart to visualize current system usage and a line chart to track system usage over time.

## Security Measures:
The code includes log analysis for detecting unauthorized access attempts and insider threat detection by monitoring running processes.


### Additional Considerations
It is important to note that the code provided is a demonstration and may need to be customized for specific system environments and security requirements. Additionally, it is recommended to adhere to Python security best practices to ensure the code is free of vulnerabilities and bugs
