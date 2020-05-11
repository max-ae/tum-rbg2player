import re
from os import system

import click
import requests
import validators


@click.command()
@click.argument('url')
@click.option('--player', '-p', default='vlc', help="command that is executed to invoke the player, defaults to VLC")
@click.option('--view', '-v', type=click.Choice(['combined', 'camera', 'presentation']), default='combined',
              help="view to open")
def main(url, player, view):
    if not validators.url(url) or "live.rbg.tum.de" not in url:
        print("The entered URL is not valid. Please check URL.")
        exit(-1)

    # get and decode HTTP response
    res = requests.get(url)
    text = res.content.decode("utf-8")
    # extract all urls from response
    playlists = re.findall(
        '(https://.*\.m3u8)', text)

    # extract specific video URLs for different perspectives and drop wowza parameters at end of URL
    if view == 'combined':
        comb = [url for url in playlists if 'COMB' in url]
        if len(comb) == 0:
            print("No combined view found. Try to select a different view.")
            exit(-1)
        system(f"{player} {comb[0]}\n")
        return

    if view == 'camera':
        cam = [url for url in playlists if 'CAM' in url]
        if len(cam) == 0:
            print("No camera view found. Try to select a different view.")
            exit(-1)
        system(f"{player} {cam[0]}\n")
        return

    if view == 'presentation':
        pres = [url for url in playlists if 'PRES' in url]
        if len(pres) == 0:
            print("No presentation view found. Try to select a different view.")
            exit(-1)
        system(f"{player} {pres[0]}\n")
        return
