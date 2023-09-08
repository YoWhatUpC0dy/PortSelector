# PortSelector
Python script that empowers users to extract specific subsets of Nmap's "top-ports,"

In summary, this Python script simplifies the process of selecting specific subsets of Nmap's "top-ports," making it more convenient and efficient for network assessments.

Here's how it works:

Purpose: The script is designed to facilitate the selection of specific TCP or UDP ports from Nmap's predefined "top-ports" list. This can help streamline network assessments by excluding previously scanned ports.

Convenience: It generates a comma-separated list of selected ports that you can easily copy and use as an argument for tools like Nmap or Masscan.

Protocol Selection: You can choose to work with either TCP or UDP ports, but not both simultaneously. The selection is made based on the /usr/share/nmap/nmap-services file, aligning with Nmap's default "top-ports" functionality.

Environmental Variable Option: The script provides an optional '-setEnvVar' parameter. When used, it creates a new Bash instance with the selected ports assigned to the provided environmental variable name. This allows you to use the ports without manual copying. After running your Nmap scan, you can exit the new Bash instance to return to your original context.

NOTE -  The script is to work with Python 3.
