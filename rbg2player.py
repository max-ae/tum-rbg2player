import re
from os import system

import click
import requests
import validators


@click.command()
@click.argument('url')
@click.option('--player', '-p', default='vlc', help="command that is executed to invoke the player, defaults to VLC")
@click.option('--view', '-v', type=click.Choice(['combined', 'camera', 'presentation']), default='combined', help="view to open")
def main(url, player, view):
    if not validators.url(url):
        print("The entered URL is not valid. Please check URL.")
        exit(-1)

    # get and decode HTTP response
    res = requests.get(url)
    text = res.content.decode("utf-8")
    # extract all urls from response
    urls = re.findall(
        '(https://)([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])?', text)

    # extract specific video URLs for different perspectives and drop wowza parameters at end of URL
    playlists = ["".join(url) for url in urls]
    comb = ["".join(url) for url in playlists if 'COMB' in url and 'm3u8' in url][0].split('?')[0]
    pres = ["".join(url) for url in playlists if 'PRES' in url and 'm3u8' in url][0].split('?')[0]
    cam = ["".join(url) for url in playlists if 'CAM' in url and 'm3u8' in url][0].split('?')[0]

    if view == 'combined':
        system(f"{player} {comb}\n")
    if view == 'camera':
        system(f"{player} {cam}\n")
    if view == 'presentation':
        system(f"{player} {pres}\n")
