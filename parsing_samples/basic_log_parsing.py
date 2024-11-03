import re
import os

'''
Problem Statement:
    Your task is to parse this log file and extract the following details
    for each entry:
     - IP Address
     - Date and Time
     - HTTP Method
     - Requested URL
     - HTTP status code
     - Bytes Transferred
     - Referrer URL
     - User Agent

After parsing the following details for each entry:
    Provide the following:
        1. Total Number of Requests
        2. Requests Per IP Address
        3. HTTP Methods Usage
        4. Status Code Distribution
        5. Most Requested URLS
        6. Bytes Transferred 
        7. User Agent Analysis
        8. Peak Traffic Time 
     
     
Samples of Logs:
192.168.1.1 - - [25/May/2023:10:15:32 +0000] "GET /index.html HTTP/1.1" 200 54321 "http://example.com/start" "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
192.168.1.2 - - [25/May/2023:10:16:45 +0000] "POST /submit-form HTTP/1.1" 404 0 "http://example.com/form" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
192.168.1.3 - - [25/May/2023:10:17:59 +0000] "GET /about.html HTTP/1.1" 200 12345 "http://example.com/about" "Mozilla/5.0 (X11; Linux x86_64)"
192.168.1.4 - - [25/May/2023:10:18:22 +0000] "GET /contact.html HTTP/1.1" 500 2048 "http://example.com/contact" "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X)"
192.168.1.5 - - [25/May/2023:10:19:30 +0000] "GET /services.html HTTP/1.1" 301 512 "http://example.com/services" "Mozilla/5.0 (Windows NT 6.1; WOW64)"
203.0.113.6 - - [25/May/2023:10:20:45 +0000] "PUT /update-profile HTTP/1.1" 204 0 "http://example.com/profile" "Mozilla/5.0 (Linux; Android 9)"
203.0.113.7 - - [25/May/2023:10:21:50 +0000] "DELETE /remove-item HTTP/1.1" 403 128 "http://example.com/cart" "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X)"
203.0.113.8 - - [25/May/2023:10:22:55 +0000] "HEAD /check-status HTTP/1.1" 200 64 "-" "curl/7.68.0"
198.51.100.9 - - [25/May/2023:10:23:00 +0000] "OPTIONS /options-test HTTP/1.1" 200 256 "-" "PostmanRuntime/7.26"
198.51.100.10 - - [25/May/2023:10:24:05 +0000] "PATCH /modify-entry HTTP/1.1" 500 1024 "http://example.com/edit" "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko"
'''

def main():
    
    try:
        fileName = 'log_samples.txt'
        # Get name of directory that file is stored in 
        workingDir = str(os.path.dirname(os.path.realpath(__file__)))
        # Combine directory and file name for path 
        filePath = os.path.join(workingDir, fileName)
        print(f' Printing Filepath : {filePath}')
        # Open file 
        with open(filePath, 'r') as reader:
            lines = reader.readlines()
            # Iterate through each line of the log file 

            for line in lines:
                # Build out a regular expression that can match
                #   all specified fields into groups,
                 #  extract those groups and store the values 
                 pattern = re.search('(\d+\.\d+\.\d+\.\d+)\s+-\s+-\s+\[(\S+)', line)
                 print(pattern.group(1))
                 date = pattern.group(2).split('/')
                 print(date)
                 print(pattern.group(2))
                 
   

    except FileNotFoundError:
            print(f'{fileName} not found in path: {filePath}')

if __name__ == '__main__':
    main()



