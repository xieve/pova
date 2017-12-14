import subprocess, sys

print(sys.argv)

if "-v" in sys.argv: verbose = 1
elif "-q" in sys.argv: verbose = -1
elif "-qq" in sys.argv: verbose = -2
else: verbose = 0

def run(args, verbose = verbose):
    if verbose > 0:
        proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        while proc.poll() is None:
            stdout, stderr = proc.communicate()
            if stdout:
                for line in stdout.splitlines():
                    print('[' + args[0].upper() + "]\t" + line.strip())
            if stderr:
                for line in stderr.splitlines():
                    print('[' + args[0].upper() + "] [ERR]\t" + line.strip())
    elif verbose > -1:
        proc = subprocess.run(args, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, universal_newlines=True)
        if proc.stderr:
            for line in proc.stderr.splitlines():
                print('[' + args[0].upper() + "] [ERR]\t" + line.strip())
    else: subprocess.run(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def say(out):
    if verbose > -2: print("[INFO]\tOUTPUT: " + out)
    run(["espeak", "-s", "150", '"%s"' % out])
