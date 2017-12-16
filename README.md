# pova
Python Offline Voice Assistant

## What is pova?
Pova is a dialog manager which utilises the Julius speech-to-text engine, the eSpeak text-to-speech engine and the VoxForge voice model to create a simple, lightweight and modular voice assistant.

## Dependencies
- [Julius](https://github.com/julius-speech/julius)
- [eSpeak](http://espeak.sourceforge.net/)

## "Installing" the custom Voice
If you want a more natural and less robotic voice, simply execute `espeak --version` in the terminal to find out where the espeak data is located and copy the pova.voice file to the voices subfolder. If you don't want this, you can switch back to the standard espeak voice by specifying `--standard-voice`.

## Terminal options
| Option    | Description   |
| ---       | ---           |
| `-v`      | Be verbose (Display everything) |
| `-q`      | Be quiet (No error messages, just in- and output) |
| `-qq`     | Shut up (Display nothing at all) |
| `--standard-voice` | Use standard eSpeak voice instead of `pova.voice` |

## Using pova
A conversation goes like this:
```
Pova?
Yes, master?
<Call>
<Answer>
```

## Writing an applet
An applet **must** contain a `calls` list, where all the strings with which the applet should be initiated are stored, and a `handle()` function, which is called when one of the `calls` is made.
A call may **not** contain any punctuation or abbreviation, not even a `'` (I hope I can fix this soon)

## Note
I'm currently using a VoxForge model which I adapted to my voice, so you better not use the one I included but rather do this too, like it's explained [here](http://www.voxforge.org/home/dev). You'll have to follow the How-To or the tutorial first. **This is not trivial.** I can provide support doing that but I won't spoonfeed you.
