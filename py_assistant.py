
# import library
import webbrowser
import wikipedia
import smtplib
import os
import random
import pygame
import subprocess


print('''Instruction :
    For Google : write 'google' space Something then prass enter
    For Youtube : write 'youtube' space Something then prass enter
    For Wikipedia : write 'wikipedia' space Somthing then prass enter
    For sending mail : write 'mail' then prass enter
    For playing music : write 'play music' then prass enter
    For exit the program : write 'stop' then prass enter
''')
    
print('Your Program is running.........')


pygame.mixer.init()
AUDIO_FOLDER = 'D:\ZZ_Downloads\Music'
POTPLAYER_PATH = 'C:\Program Files\DAUM\PotPlayer\PotPlayerMini64.exe'
def list_files(folder, extensions):
    return [f for f in os.listdir(folder) if f.endswith(extensions)]

def play_random_file(folder, extensions, background=False):
    files = list_files(folder, extensions)
    if not files:
        print(f"No files found in the folder: {folder}")
    else:
        file = os.path.join(folder, random.choice(files))
        try:
            if background:
                subprocess.Popen([POTPLAYER_PATH, file])
            else:
                subprocess.run([POTPLAYER_PATH, file])
            print(f'Playing file: {file}')
        except Exception as e:
            print(f"Error playing file: {e}")


while True:
    n = input('Choose a mode 1 for speech 2 for text....!\n')
    if n == '1':
        print('Listening...........')
        break
    elif n == '2':
        print('Text mode is running......')
        break
    else:
        print('Invalid input Try again....!')
# for text mode
if n == '2':
    while True:
        command= input('Enter your command: ')
        command = command.lower()
        if command.startswith('google '):
            webbrowser.open('https://www.google.com/search?q='+command[7:])
            print('Search in Google.........')
        elif command.startswith('youtube '):
            webbrowser.open('https://www.youtube.com/results?search_query='+command[8:])
            print('Search in Youtube.........')
        elif command.startswith('wikipedia '):
            query = command[len('wikipedia '):]
            try:
                summary = wikipedia.summary(query, sentences=1)
                print(summary)
            except wikipedia.exceptions.DisambiguationError as e:
                print(f"Disambiguation error: {e.options}")
            except wikipedia.exceptions.PageError:
                print("No Wikipedia page found for the query.")

        elif 'mail' in command:
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            smail = 'author.hasib@gmail.com'

            rmail = input('Enter mail : ')
            subject = input('Enter Subject : ')
            message = input('Enter Message :')

            text = f"Subject: {subject}\n\n{message}"
            server.login(smail,'dqpjbkcokvarvujh')
            server.sendmail(smail,rmail,text)

            print('Mail sent successfully')

        elif command.startswith('play music'):
            play_random_file(AUDIO_FOLDER, ('.mp3', '.wav'), background=True)
        # elif command.startswith('play video'):
        #     play_random_file(VIDEO_FOLDER, ('.mp4', '.avi', '.mkv'))
        
        elif 'stop' in command:
            break
        else:
            print('Invalid input Try again....!')
