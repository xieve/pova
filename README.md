# pova
Python Offline Voice Assistant

## What is pova?
Pova is a dialog manager which utilises the Julius speech-to-text engine, the eSpeak text-to-speech engine and the VoxForge voice model to create a simple, lightweight and modular voice assistant.

## Dependencies
- [Julius](https://github.com/julius-speech/julius)
- [eSpeak](http://espeak.sourceforge.net/)

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
