
# set up 2 mode Text or speech
# while loop
# all condition

    # online
    # google somthing_text
    # youtube text
    # wikipedia text 
    # mail
        # Enter mail
        # Enter message
    # codeforces

    # ofline
    # play music
        # What is your mood today (good , sad, romantic)
        # playing music............
print('''Instruction :
    For Google : write 'google' space Something then prass enter
    For Youtube : write 'youtube' space Something then prass enter
    For Wikipedia : write 'wikipedia' space Somthing then prass enter
    For sending mail : mail then entre, write 'mail' and press enter, then write message press enter to send mail.
    For playing music : write 'play music' then prass enter
    For exit the program : write 'stop' then prass enter
''')
    
print('Your Program is running.........')

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
        i = input('Enter your text : ')
        i = i.lower()
        if 'google' in i:
            print('Search in Google.........')
        elif 'youtube' in i:
            print('Search in Youtube.........')
        elif 'wikipedia' in i:
            print('''Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.''')
        elif 'mail' in i:
            mail = input('Enter mail : ')
            message = input('Enter Message :')
            print('mail send...!')
        elif 'codeforces' in i:
            print('your mission is completed...!')
        elif 'play music' in i:
            mood = input('What is your mood today ? (good, sad or romantic)')
            print('Playing music.....')
        elif 'stop' in i:
            break
        else:
            print("Don't understand !! Try again......")
