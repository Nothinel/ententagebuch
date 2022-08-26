#!/usr/bin/python3

import time
import curses
from curses import wrapper
import os
import hashlib
import json
import random



def convert_ch(chars):
    """
    Converts the output of curses.getch() to basic text
    accept either single char or list of chars
    """
    ret_val = ""
    if not hasattr(chars, "__iter__"):
        chars = [chars]
    for ch in chars:
        ret_val += chr(ch)
    return ret_val


#pw_add("password")

def password(stdscr):
    #curses.noecho()
    stdscr.clear()
    stdscr.refresh()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    GREEN_BLACK = curses.color_pair(1)
    stdscr.nodelay(True)
    y_max, x_max = stdscr.getmaxyx()
    y_init = y_max//2
    x_init = (x_max//2)-6
    stdscr.addstr(y_init-4, x_init, "Passwort eingeben!", GREEN_BLACK | curses.A_BOLD)
    stdscr.move(y_init,x_init)
#    key = stdscr.getkey()
#    stdscr.addstr(10, 10, "hi")
#    stdscr.refresh()
#    stdscr.getch()
    i=0
    entry = []
    while True:
        try:
            #key = stdscr.getkey()
            key = stdscr.getch()
            #os.system(f"echo '{type(key)}' >> keys")
        except:
            key = None
        if key != -1:
            if key == 10: #F10 ends the loop
                break
            if key == 274: #ENTER ends the loop
                break
            elif (key != "^C"):
                i +=1
                stdscr.addstr(y_init, x_init+i, "*", GREEN_BLACK | curses.A_BOLD)
                entry.append(key)
            #os.system(f"echo '{key}' >> keys")
            stdscr.refresh()
    entry = convert_ch(entry)
    PASSWORD = entry
    os.system(f"echo '{entry}' >> keys")
    hashed_entry = hashlib.sha256(entry.encode())
    hash_dig = hashed_entry.hexdigest()
    os.system(f"echo '{hash_dig}' >> keys")
    stdscr.clear()
    #"5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"):
    if (hash_dig ==
    "54986d595e3e8c4b0258170055aab128b4e51ef86abadf53270221c7d41c19b5"):
        return True, PASSWORD
    else:
        return False, PASSWORD

def display_ascii_art(stdscr, file_name, duration=5):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()
    with open(file_name, "r") as f:
        string =f.read()
    with open(file_name, "r") as f:
        count = f.readlines()
    #print(string)
    y, x = len(count), len(count[0])
    y += 1
    x *= 1
    y_max, x_max = stdscr.getmaxyx()
    os.system(f"echo 'y={y}, x={x}, y_max={y_max}, x_max={x_max}' >> dim.txt")
    string_win = curses.newwin(y,x,(y_max-y)//2,(x_max-x)//2)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    GREEN_BLACK = curses.color_pair(1)
    string_win.addstr(0, 0, string, GREEN_BLACK | curses.A_BOLD)
    #string_win.addstr(0, 0, "string", GREEN_BLACK | curses.A_BOLD)
    string_win.refresh()
    if duration: 
        time.sleep(duration)
    else:
        while True:
            key = stdscr.getch()
            if (key == 274) or (key==10):
                break
    del string_win
    curses.curs_set(2)

def display_text_file(stdscr, file_name, duration=10):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()
    with open(file_name, "r") as f:
        string =f.read()
    with open(file_name, "r") as f:
        count = f.readlines()
    #print(string)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    GREEN_BLACK = curses.color_pair(1)
    stdscr.addstr(0, 0, string, GREEN_BLACK | curses.A_BOLD)
    stdscr.refresh()
    if duration: 
        time.sleep(duration)
    else:
        while True:
            key = stdscr.getch()
            if (key == 274) or (key==10):
                break
    curses.curs_set(2)

def progress_bar(stdscr, string, duration=20, clear=True):
    curses.curs_set(0)
    step_duration = duration/50
    if clear:
        stdscr.clear()
        stdscr.refresh()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
    BLACK_GREEN = curses.color_pair(1)
    y_max, x_max = stdscr.getmaxyx()
    for i in range(0,50):
        stdscr.addstr(y_max//2, x_max//2-25+i, string, BLACK_GREEN | curses.A_BOLD)
        stdscr.refresh()
        time.sleep(step_duration)
    curses.curs_set(1)

def input_dialog_free_text(stdscr, file_name, answer_check):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()
    with open(file_name, "r") as f:
        string =f.read()
    with open(file_name, "r") as f:
        count = f.readlines()
    with open(answer_check, "r") as f:
        ans_check = f.read()
    y, x = len(count), len(count[0])
    y += 1
    x *= 1
    y_max, x_max = stdscr.getmaxyx()
    string_win = curses.newwin(y,x,(y_max-y)//2,(x_max-x)//2)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    GREEN_BLACK = curses.color_pair(1)
    string_win.addstr(0, 0, string, GREEN_BLACK | curses.A_BOLD)
    string_win.refresh()
    x_ans_win = 30
    y_ans_win = 1
    ans_win = curses.newwin(y_ans_win,x_ans_win,(y_max-y)//2+2+y,(x_max-x_ans_win)//2)
    solved = False
    while not solved:
        ans_win.clear()
        ans_win.refresh()
        entry=[]
        i = 0
        running=True
        while running:
            key = ans_win.getch()
            os.system(f"echo '{key}' >> keys")
            if (key == 274) or (key==10):
                running = False
            try:
                ans_win.addstr(0, i, convert_ch(key), GREEN_BLACK | curses.A_BOLD)
                entry.append(key)
            except:
                pass
            i += 1
        os.system(f"echo '{entry}' >> keys")
        entry = convert_ch(entry)
        os.system(f"echo '{entry}' >> keys")
        os.system(f"echo '{str(entry.encode())}' >> keys")
        hashed_entry = hashlib.sha256(entry.encode())
        hash_dig = hashed_entry.hexdigest()
        os.system(f"echo '{hash_dig}' >> keys")
        if (hash_dig == ans_check):
            solved=True
    stdscr.clear()
    stdscr.refresh()

def show_partial_etb(stdscr, line_list, start_line=0):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    GREEN_BLACK = curses.color_pair(1)
    for cnt, line in enumerate(line_list):
        #os.system(f"echo '{line}' >> lines")
        stdscr.addstr(start_line + cnt, 0, line, GREEN_BLACK | curses.A_BOLD)
    stdscr.refresh()
    

def guess_line(stdscr, etb_entry):
    progress_bar(stdscr, " ", duration=0.5, clear=False)
    curses.curs_set(0)
    y = 1
    x = len(etb_entry["q"]) + 1
    y_max, x_max = stdscr.getmaxyx()
    #etb_part.append(etb_entry["e"]) 
    string_win = curses.newwin(y,x,(y_max-y)//2,(x_max-x)//2)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    GREEN_BLACK = curses.color_pair(1)
    string_win.addstr(0, 0, etb_entry["q"], GREEN_BLACK | curses.A_BOLD)
    string_win.refresh()
    x_ans_win = 30
    y_ans_win = 1
    ans_win = curses.newwin(y_ans_win,x_ans_win,(y_max-y)//2+2+y,(x_max-x_ans_win)//2)
    solved = False
    while not solved:
        ans_win.clear()
        ans_win.refresh()
        entry=[]
        i = 0
        running=True
        while running:
            key = ans_win.getch()
            os.system(f"echo '{key}' >> keys")
            if (key == 274) or (key==10): #press ENTER to evaluate input
                running = False
            elif (key == 8) or (key==127):
                i = i-1
                if i > 0: entry.pop(-1)
            else:
                try:
                    ans_win.addstr(0, i, convert_ch(key), GREEN_BLACK | curses.A_BOLD)
                    entry.append(key)
                except:
                    pass
                i += 1
        entry = convert_ch(entry)
        hashed_entry = hashlib.sha256(entry.encode())
        hash_dig = hashed_entry.hexdigest()
        if (hash_dig == etb_entry["c"]):
            solved=True
    stdscr.clear()
    stdscr.refresh()


#display_ascii_art(stdscr=1, file_name="falsch.txt")
#display_ascii_art(stdscr=1, file_name="correct.txt")
#display_ascii_art(stdscr=1, file_name="richtig.txt")

def crop_etb_start(etb_file):
    with open(etb_file, "r") as f:
        line_list = f.readlines()
    ret_val = []
    for line in line_list:
        if not line.startswith("*"):
            line.replace("\n", "")
            ret_val.append(line)
    return ret_val

def scramble_ascii_art(file_name, ambiguity=60):
    with open(file_name, "r") as f:
        string =f.read()
    char_list=[]
    for char in string:
        char_list.append(char)
    char_list = set(char_list)
    #symbols = [x for x in convert_ch(range(61,1000))]
    symbols = [",", ".", ":"] + ambiguity * [" "]
    #print(symbols)
    for char in char_list:
        if char != "\n":
            string = string.replace(char, random.choice(symbols))
    print(string)
    with open(file_name + ".scrambled", "w") as f:
        f.write(string)



def main(stdscr):
    done = False
    while not done:
        done, PASSWORD = password(stdscr)
        if not done: display_ascii_art(stdscr, "ascii_art/falsch.txt",
                duration=10)
    display_ascii_art(stdscr, "richtig.txt", duration=5)
    display_text_file(stdscr, "ETB2.ltxt", duration=20)
    display_ascii_art(stdscr, "error_explain.txt", duration=False)
    progress_bar(stdscr, " ", duration=45)
    stdscr.clear()
    with open("ETB2_c.json", "r") as f:
        etb_json = json.load(f)
    line_list = crop_etb_start("ETB2.ltxt")
    for etb_entry in etb_json["einträge"]:
        for line in etb_entry["e"]:
            os.system(f"echo '{line}' >> lines")
            line_list.append(line)
        while len(line_list) > 12:
            line_list.pop(1)
        show_partial_etb(stdscr, line_list, start_line=0)
        #time.sleep(0.2)
        guess_line(stdscr, etb_entry)
    display_ascii_art(stdscr, "end.txt", duration=False)
    for i in range(0,59):
        scramble_ascii_art("ascii_art/Florian.txt")
        display_ascii_art(stdscr, "ascii_art/Florian.txt.scrambled", duration=0.1)
        stdscr.refresh()
        stdscr.clear()
    display_ascii_art(stdscr, "ascii_art/Florian.txt", duration=False)




if __name__ == "__main__":
    wrapper(main)
    os.system("cat ascii_art/Florian.txt")



