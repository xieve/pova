#!/usr/bin/python

import os, sys, subprocess, re, tui, povaLib

verbose = povaLib.verbose

tui.editLast("Reading dict... (0/0)")
voxforgeDict = {}
voxforgeDictF = open("juliusdeps/dict", 'r')
r = re.compile(r"(\S+) +\[\1] +((?:\S\S? )*\S\S?)") # Just a regex to 'decode' the voxforge dictionary
lines = voxforgeDictF.read().splitlines()
for i, line in enumerate(lines):
    tui.editLast("Reading dict... (%i/%i)" % (i + 1, len(lines)))
    tmp = r.match(line).groups()
    voxforgeDict[tmp[0]] = tmp[1]

del lines
voxforgeDictF.close()

print("\nReading applets...")
applets = {}
for f in os.listdir("applets"):
    if not f in ["__pycache__", "pova.py", "povaLib.py", "pova.grammar", "pova.voca", "tui.py", "juliusdeps"]:
        try:
            exec("import applets.%s as curApplet" % f[:-3])
            applets[f[:-3]] = curApplet
            del f, curApplet
        except ModuleNotFoundError:
            print("[WARNING]\tThere's something in the applets folder that doesn't belong there. This is fine.")

print("Generating grammar...")
callDict = {}
for applet in applets.values():
    for call in applet.calls:
        callDict[call.lower()] = applet

grammarStr = "S: NS_B POVA NS_E\n"
vocaStr = "% NS_B\n<s>\tsil\n\n% NS_E\n</s>\tsil\n\n% POVA\npova\tp ow v ah\n\n" # Compressed silence and 'pova' grammar
for call in callDict:
    call = call.upper()
    grammarStr += "S: NS_B " + call + " NS_E\n"
    for word in call.split(" "):
        if vocaStr.find(' ' + word + '\n') == -1:
            vocaStr += "% " + word + '\n' + word.lower() + '\t' + voxforgeDict[word] + "\n\n"

del voxforgeDict
grammarFile = open("pova.grammar", 'w')
vocaFile = open("pova.voca", 'w')
grammarFile.write(grammarStr)
vocaFile.write(vocaStr)
grammarFile.close()
vocaFile.close()

povaLib.run(["mkdfa.pl", "pova"])

r = re.compile(r"sentence1: <s> (.+?) </s>")
active = False
julius = subprocess.Popen(
    ["julius",
    "-dfa", "pova.dfa",
    "-v", "pova.dict",
    "-h", "juliusdeps/hmmdefs",
    "-hlist", "juliusdeps/tiedlist",
    "-input", "mic",
    "-smpFreq", "8000"],
    stdout=subprocess.PIPE, universal_newlines=True)

while julius.poll() is None:
    stdout = julius.stdout.readline()
    if verbose > 0: print("[JULIUS]\t" + stdout.strip())
    c = r.match(stdout)
    if not c is None:
        c = c.group(1)
        if verbose > -2: print("[INFO]\tINPUT:  " + c)
        if c == "pova":
            active = True
            povaLib.say("Yes, master?")
        elif active:
            try:
                callDict[c].handle()
                active = False
            except KeyError:
                continue
