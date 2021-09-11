@echo off


:start
cls

set python_ver=36
mode 800
color 2
python ./get-pip.py

pip install pyttsx3
pip install pytz
pip install smtplib
pip install requests
pip install tkinter
pip install wikipedia
pip install opencv-python
pip install win32api
pip install datetime
pip install pipwin
pipwin install pyaudio
pip install SpeechRecognition
pip install pyjokes
pip install pywhatkit
pip install countryinfo
pip install freegames
pip install googletrans==3.1.0a0
