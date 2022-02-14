import os
import sys

def search_dir(dir, ext, isw, isl, isc, ism, n_file=0, wc=0, lc=0, cc=0, mc=0):
    """
    wc:wordcount
    lc:linecount
    cc:charcount
    """
    path = dir
    in_dirs = os.listdir(dir)
    for dir in in_dirs:
        dir = path + "/" + dir
        if os.path.isdir(dir):
            n_file, wc, lc, cc, mc = search_dir(dir, ext, isw, isl, isc, ism, n_file, wc, lc, cc, mc)
        else:
            fileext = '.'+(dir.split('/')[-1]).split('.')[-1]
            if fileext == ext:
                #print(dir+":This is "+ext+" file")
                n_file += 1
                if ism:
                    byte = os.path.getsize(dir)
                    mc += byte
                line, word, chara = wordcount(dir, isw, isl, isc)
                lc += line
                wc += word
                cc += chara
                if isl:
                    print(line, end=" ")
                if isw:
                    print(word, end=" ")
                if isc:
                    print(chara, end=" ")
                if ism:
                    print(byte, end=" ")
                print(dir)
    return n_file, wc, lc, cc, mc
    
def wordcount(file, isw, isl, isc):
    """
    wc command counts '\n' to count lines.
    And count brank to count words.
    Count charactors to count bytesize.
    Incompatible with multibyte charactors.

    python3 Findlect.py {-option} Directry ext 
    """
    wc = 0
    lc = 0
    cc = 0
    with open(file, "r", encoding="UTF-8") as f:
        lines = f.readlines()
        for line in lines:
            if isl and "\n" in line:
                lc += 1
            if isc:
                cc += len(line)
            if isw:
                words = line.split()
                wc += len(words)
                    
    return lc, wc, cc
    
if __name__ == "__main__":
    shift = 0
    #w:word, c:char, l:line, m:memory
    option_dict = {"w":True, "l":True, "c":True, "m":False}
    if sys.argv[1][0] == "-":
        op = sys.argv[1]
        shift = 1
        if not "w" in op:
            option_dict["w"] = False
        if not "l" in op:
            option_dict["l"] = False
        if not "c" in op:
            option_dict["c"] = False
        if "m" in op:
            option_dict["m"] = True
        
    dir = sys.argv[1+shift]
    ext = sys.argv[2+shift]
    print(dir, ext)
    print(option_dict)
    n_file, wc, lc, cc, mc = search_dir(dir, ext, option_dict["w"],option_dict["l"],
                                        option_dict["c"], option_dict["m"])
    if option_dict["l"]:
        print(lc, end=" ")
    if option_dict["w"]:
        print(wc, end=" ")
    if option_dict["c"]:
        print(cc, end=" ")
    if option_dict["m"]:
        print(mc, "total")
    else:
        print("total")

