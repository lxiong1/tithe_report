## Tithe Report

The Python script was made to distribute the tithe report to all relevant Good News staff via `Gmail` using an SMTP server.

### Requirement
- Tithe report needs to be the following: 
    - In the same working directory as this script
    - Formatted as `tithe_report_<CURRENT_YEAR>.xlsx`
- Python 2.7+

### Running the Script
1. Make sure you are in the working directory of the script and type the following command in the terminal: `python ./send_report.py`
2. You will be prompt by the terminal to enter the password for `goodnewsusher@gmail.com`
   - Note: Text will be invisible due to the sensitive nature of passwords
3. Once you have entered the correct password, you should get message saying:
>       -------------------------------------------------------------
>      | Tithe report has been sent to the relevant Good News staff! |
>       -------------------------------------------------------------
