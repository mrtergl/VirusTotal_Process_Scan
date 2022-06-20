# ViruTotal_Hash_Scan
Scanning all the running .exe files in VirusTotal with Python.

### Getting .exe files
I used wmi library to get all running files from device. Then saved into a list called "liste".
<br>


|<img src="Images/library.png">|<img src="Images/list.png">|
|---------|---------|
| Library | Getting the files to a list |

<br>

### Scanning hashes of files in VirusTotal
First you have to get the real path of the file. Then with the path, we can get the hash of the file by using this code:
<br>
|<img src="Images/hash.png">|
|---------|
| Get Hash |
<br>
After doing it, we can proceed for scanning the hash of the file using VirusTotal API.

### Saving the results to a file
After the scannning completed for a file. It writes the result to a file called "vt_results_exe". It writes all the scores that comes from VirusTotal. In terminal you can see which process has scanned.

|<img src="Image/terminal.png">|<img src="Image/results.png">|
|---------|---------|
| Terminal | Results |
