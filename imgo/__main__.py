import click
from PIL import ImageGrab
import pyperclip
import pytesseract


@click.command()
@click.argument('lang')
def cli(lang):
    img = ImageGrab.grabclipboard()
    if img is None:
        raise click.UsageError('Clipboard does not contain image')
    else:
        s = pytesseract.image_to_string(img, lang=lang)
        pyperclip.copy(s)
        click.echo(s)


if __name__ == '__main__':
    cli()
