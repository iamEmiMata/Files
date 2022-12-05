from pytube import YouTube
import time
import os

def intro():
    msg = '''
    ++++++++++++++++++++++++++++++++++++

    Y O U T U B E    D O W N L O A D E R 

    ++++++++++++++++++++++++++++++++++++
    '''
    msg2 = '''
    Welcome, Choose an option

    1. Download music 
    2. Download video
    0. Exit
    '''
    print(msg)
    time.sleep(1)
    print(msg2)

def choose():

    op = input('>   ')

    while op != '0':
        if op == '0':
            print('Exit!')
        elif op == '1':
            music()
            break
        elif op == '2':
            video()
            break
        else:
            print('Give a valid option...')

def video():

    link = input("\nEnter your link here\n> ")
    yt = YouTube(link)

    print(f'\nYou are Downloading \n{yt.title} ')
    ys = yt.streams.get_highest_resolution()
    time.sleep(2)
    print('\nWait a second your video is cooking...')
    ys.download()
    print("Your download is completed")

def music():

    link = input("Enter your link here\n> ")
    yt = YouTube(link)
    
    print(f'\nYou are Downloading \n{yt.title} ')
    convert = yt.streams.filter(only_audio=True).first()
    time.sleep(2)
    print('\nWait a second your song is cooking')
    musicFile = convert.download()
    name, ext = os.path.splitext(musicFile)
    newFile = name + '.mp3'
    os.rename(musicFile, newFile)
    print("Your download is completed")

intro()
choose()