import wejscie
from generator import generatorKluczy

from prompt_toolkit.validation import Validator
from prompt_toolkit.application import Application
from prompt_toolkit import prompt
from prompt_toolkit import PromptSession
from prompt_toolkit.document import Document
from prompt_toolkit.application import Application
from prompt_toolkit.application.current import get_app
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.focus import (
    focus_next,
    focus_previous,
)
from prompt_toolkit.layout import HSplit, Layout, VSplit
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import Box, Button, Frame, Label, TextArea


def wejscia():
    session = PromptSession()

    while True:
        try:
            text = session.prompt('> ')
        except KeyboardInterrupt:
            continue
        except EOFError:
            break
        else:
            print('You entered:', text)
    print('GoodBye!')


# Event handlers for all the buttons.
def buttonKluczClicked():
    def _(event):
        event.app.layout.focus(inputArea)

    outputArea.text = 'Wprowadz liczebe pomocniczą,\naby wygenerowac klucz.'
    _()
    inputArea.accept_handler = accept


def buttonTablicaClicked():
    outputArea.text = 'Rozpoczeto generowanie tablicy'


def buttonKodowanieClicked():
    outputArea.text = 'Rozpoczeto kodowanie'


def buttonSzyfrowanieClicked():
    outputArea.text = 'Rozpoczeto szyfrowanie'


def buttonDeszyfrowanieClicked():
    outputArea.text = 'Rozpoczeto deszyfrowanie'


def buttonDekodowanieClicked():
    outputArea.text = 'Rozpoczeto dekodowanie'


def exit_clicked():
    get_app().exit()


def forceInput():
    inputArea = TextArea(focusable=True)
    '''kb.add('down')(None)
    kb.add('up')(None)'''


def accept(buff):
    # Evaluate "calculator" expression.
    output = inputArea.text
    error = wejscie.tui(output)
    if error == '':
        outputArea.text = error
    else:
        outputArea.text = output

global inputArea, outputArea

# All the widgets for the UI.
buttonKlucz = Button('Generuj kluczy', handler=buttonKluczClicked)
buttonTablica = Button('Generuj tablice', handler=buttonTablicaClicked)
buttonKodowanie = Button('Zakoduj', handler=buttonKodowanieClicked)
buttonSzyfrowanie = Button('Zaszyfruj', handler=buttonSzyfrowanieClicked)
buttonDeszyfrowanie = Button('Zdeszyfruj', handler=buttonDeszyfrowanieClicked)
buttonDekodowanie = Button('Zdekoduj', handler=buttonDekodowanieClicked)
buttonExit = Button('Exit', handler=exit_clicked)
outputArea = TextArea(focusable=False, read_only=True)
inputArea = TextArea(focusable=True, height=20, style='class:input-field',
                     multiline=False, wrap_lines=False)

# Combine all the widgets in a UI.
# The `Box` object ensures that padding will be inserted around the containing
# widget. It adapts automatically, unless an explicit `padding` amount is given.
root_container = Box(
    HSplit([
        Label(text='Do nawigacji użyj prycisków kierunkowych'),
        VSplit([
            Box(
                body=HSplit(
                    [buttonKlucz, buttonTablica, buttonKodowanie,
                     buttonSzyfrowanie, buttonDeszyfrowanie,
                     buttonDekodowanie],
                    padding=1, width=20),
                padding=1,
                style='class:left-pane'),
            HSplit([
                Box(
                    body=Frame(outputArea),
                    padding=1,
                    style='class:right-pane'),
                Box(
                    body=Frame(inputArea),
                    padding=1,
                    style='class:right-pane'),
            ])
        ]),
    ])
)

layout = Layout(
    container=root_container,
    focused_element=buttonKlucz)


# Key bindings.
kb = KeyBindings()
kb.add('down')(focus_next)
kb.add('up')(focus_previous)
@kb.add('`')
def _(event):
    outputArea.text = 'Autor: K.R.'


# Styling.
style = Style([
    ('left-pane', 'bg:#ffd700 #000000'),
    ('right-pane',      'bg:#00aa00 #000000'),
    ('button',          '#000000'),
    ('button-arrow',    '#000000'),
    ('button focused', 'bg:#ff0000'),
    ('text-area focused', 'bg:#ff0000'),
])


# Build a main application object.
application = Application(
    layout=layout,
    key_bindings=kb,
    style=style,
    full_screen=True)


def main():
    application.run()


'''def main():
    autor()
    wejscieZKonsoli()
    wejscia()'''

if __name__ == '__main__':
    main()
