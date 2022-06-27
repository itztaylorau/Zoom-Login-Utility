# Semi-Auto Zoom Meeting Attend Utility
This utlilty aims to provide a faster way for you to enter regular zoom meeting rooms. For instance, your lectures or classes.
This utility is 100% run in your pc and do not reuqire any cloud functions or computing.
## Basic Information
|  |  |
|--|--|
| Platform | Windows |
| Prerequisite | Python 3.6 and pyautogui|
|Zoom client | Latest version with valid account
## How to use
1. Press `Win + R` to open Run dialog.
2. Input `cmd` for opening Terminal
3. Head to the directory that saves this utility by `cd`
4. Execute `py run.py`
5. Enter the preset key you saved
6. Wait for the utility to login for you automatically!

## Preset key syntax
```python
ids = [
#Your remarks
["Key you input for login", "Zoom ID", "Zoom Password"],
#For example
#You will enter ABC for key, Zoom ID 123456789, Password 0987
["ABC", "123456789", "0987"],
]
```

## Troubleshoot
P: The utility cannot search the Zoom program correctly.
S: Please switch to English input method so the program can fill the required  search phrase.

## Credit & Acknowledgement
- I don't know but it is some video in YouTube
- Stackoverflow
