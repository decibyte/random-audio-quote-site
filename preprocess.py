#!/usr/bin/env python

import os, sys, json
import eyed3


def process_audio():
    library = []
    for root, dirs, files in os.walk('./audio'):
        for mp3 in [f for f in files if f.endswith('.mp3')]:
            audio = eyed3.load('audio/%s' % mp3)
            library.append({
                'file': mp3,
                'person': audio.tag.artist,
                'program': audio.tag.title,
                'channel': audio.tag.album,
                'url': audio.tag.comments[0].text,
            })

    with open('./library.json', 'w') as data:
        data.write(json.dumps(library))
        print('Libary updated and saved to library.json')

def process_template(site_name):
    with open('index.template.html', 'r') as f:
        template = f.read()
    with open('index.html', 'w') as f:
        f.write(template.replace('{{ site_name }}', site_name))
    print 'index.html updated and saved with site name: %s' % site_name

if __name__ == '__main__':
    if len(sys.argv) < 2:
        site_name = raw_input('What is the site name? ')
    else:
        site_name = sys.argv[1]

    print 'Generating files for your sound quote site: %s' % site_name
    print 'Processing audio library...'
    process_audio()
    print 'Generating HTML file...'
    process_template(site_name)
