import textwrap
import locale

import click
import requests

from . import __version__


loc = locale.getlocale()[0].split('_')[0]
API_URL = "https://{lang}.wikipedia.org/api/rest_v1/page/random/summary"


@click.command()
@click.version_option(version=__version__)
@click.option("--lang", help="Language of the Wikipedia")
def main(lang):
    """The hypermodern Python project."""
    if lang:
        url = API_URL.format(lang=lang)
    else:
        url = API_URL.format(lang=loc)
    
    try:
        with requests.get(url) as response:
            response.raise_for_status()
            data = response.json()
    except Exception as e:
        click.secho(f'Error fetching {url}', fg='red')
        quit()
        
    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))

