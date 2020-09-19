from fbchat import Client
from fbchat.models import *
from PIL import Image
import argparse
import time
import pandas as pd
import random

parser = argparse.ArgumentParser()
parser.add_argument('end', help='What number lunch meme?')
args =  parser.parse_args()

meme_path = f'lunch meme {args.end}.png'
# meme_path = f'lunch meme {args.end}.mp4' 

username = 'thomas.nobes.5'
password = 'Jazziegirl1%'
client = Client(username, password)


friends = ['Eliza Jones',
        #    'Cameron Smith',
        #    'Rory McNab',
           'Shon Kolomoisky',
        #    'Rylan Jardine',
        #    'Stevie Thomas',
           'Ethan Payne',
           'Grace Jones',
           'Maddy Howell',
           'Emily Jones',
           'Maeva Berchon',
           'Hayden McMahon',
           'Daniel Guy',
           'Ashley Nobes',
           'Dongsquad']
# friends = ["Thomas Nobes"]

msg = 'Prepare for the holy transformation: lunch memes ABOUT lunch memes ending...'

users = client.fetchThreadList()
for user in users:
    if user.name in friends:
        if user.type == ThreadType.GROUP:
            sent = client.sendLocalFiles(meme_path, thread_id=user.uid, thread_type=ThreadType.GROUP)
            # sent_msg = client.send(Message(text=msg), thread_id=user.uid, thread_type=ThreadType.GROUP)
        else:
            sent = client.sendLocalFiles(meme_path, thread_id=user.uid)
            # sent_msg = client.send(Message(text=msg), thread_id=user.uid)
        pause = random.randrange(0, 5)
        time.sleep(pause)
        if sent:
            print(f'Message sent to {user.name} successfully!')

client.logout()
