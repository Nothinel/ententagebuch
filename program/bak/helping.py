#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import json
import curses
from curses import wrapper
import os
import hashlib
import random
from simplecrypt import encrypt, decrypt
import glob
from etb import convert_ch

def randomize_stars(file_name):
    with open(file_name, "r") as f:
        string = f.read()
    choices = [" ", "*", "+", "-", "$", "§", "_", "&"]
    ret_val = ""
    for s in string:
        if s == r"*":
            ret_val += (random.choice(choices))
        else: 
            ret_val += s
    return ret_val

#print(randomize_stars("ETB.ltxt"))

#pass_code = "password"
#string = "Hallo, meine Name ist Hase, ich weiß von nichts! äüöÄÜÖ"
#cypher = encrypt(pass_code, string)
#print(cypher)
#print(decrypt(pass_code, cypher).decode("utf8"))

def pwgen(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

def pw_add(pw):
    hash_str = pwgen(pw)
    #os.system(f"echo {hash_str} >> etb.py")

def ans_check_gen(file_name):
    with open(file_name, "r") as f:
        ans_string = f.read()
    ans_check_string = pwgen(ans_string.replace("\n", ""))
    #print(ans_string)
    with open(file_name.replace(".a", ".c"), "w") as f:
        f.write(ans_check_string)
        #f.write(str(ans_string.encode()))

def full_check_gen(directory):
    list_answers = glob.glob(os.path.join(directory, "*.a"))
    print(list_answers)
    for answer in list_answers:
        ans_check_gen(answer)

#full_check_gen("questions/")

def initialize_ETB():
    etb = {}
    etb["einträge"] = []
    etb_eintrag = {}
    etb_eintrag["q"] = "Wo könnte die Ente sich in dieser Gegend versorgen?"
    etb_eintrag["a"] = "Paunsdorf Center"
    etb["einträge"].append(etb_eintrag)
    etb_eintrag = {}
    etb_eintrag["q"] = "Welche Nummer trägt der zentrale Ein/Ausgang Richtung Westen?"
    etb_eintrag["a"] = "1"
    etb["einträge"].append(etb_eintrag)
    with open("ETB.json", "w", encoding="utf-8") as f:
        json.dump(etb, f, indent=4, ensure_ascii=False)

#DANGER WILL KILL PROGRESS initialize_ETB()

def generate_check_ETB(file_name):
    with open(file_name, "r") as f:
        etb = json.load(f)
    for eintrag in etb["einträge"]:
        eintrag["c"] = pwgen(eintrag["a"])
    #print(etb)
    with open(file_name.replace(".json", "_c.json"), "w", encoding="utf-8") as f:
        json.dump(etb, f, indent=4, ensure_ascii=False)
        
generate_check_ETB("ETB.json")

def crop_etb_start(etb_file):
    with open(etb_file, "r") as f:
        line_list = f.readlines()
    ret_val = []
    for line in line_list:
        if not line.startswith("*"):
            line.replace("\n", "")
            ret_val.append(line)
    return ret_val

#print(crop_etb_start("ETB.ltxt"))
def show_ETB(file_name):
    with open(file_name, "r") as f:
        etb = json.load(f)
    print(etb)
#show_ETB("ETB.json")

def make_ETB_entries_list(file_name):
    with open(file_name, "r") as f:
        etb = json.load(f)
    for entry in etb["einträge"]:
        entry["e"] = [entry["e"]]

    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(etb, f, indent=4, ensure_ascii=False)
#make_ETB_entries_list("ETB.json")

def scramble_ascii_art(file_name):
    with open(file_name, "r") as f:
        string =f.read()
    char_list=[]
    for char in string:
        char_list.append(char)
    char_list = set(char_list)
    symbols = [x for x in convert_ch(range(61,1000))]
    #print(symbols)
    for char in char_list:
        if char != "\n":
            string = string.replace(char, random.choice(symbols))
    print(string)
    with open(file_name + ".scrambled", "w") as f:
        f.write(string)
scramble_ascii_art("ascii_art/SKU.txt")
