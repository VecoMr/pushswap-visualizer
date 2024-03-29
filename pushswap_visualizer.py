import sys
import os
from subprocess import Popen, PIPE

from matplotlib import pyplot as plt

from src.list_pushswap import *
from src.print_help import *

########## CONFIG ##########
SPEED: int = 10
TIME_BEFORE: int = 3
TIME_AFTER: int = 5
############################

def main():
    argv = sys.argv
    argc = len(argv)
    if "-h" in argv:
        print_help()
        exit(0)
    if not (argc == 2 or argc == 3 or (argc == 4 and "-b" in argv)):
        print_help()
        exit(84)
    if argc < 3:
        if not sys.stdin.isatty():
            inst = sys.stdin.read()[:-1].split(" ")
        list_sort = argv[1].split(" ")
    else:
        if argc == 4:
            argv.remove("-b")
            path_binary = argv[1]
            path_file = argv[2]
            process = Popen(["cat", "./" + path_file], stdout=PIPE)
            (output, err) = process.communicate()
            process.wait()
            try:
                list_sort = output.decode("utf-8").split()
            except:
                print("Bad File, Error = %s", err.decode("utf-8"))
                exit(84)
            args = [path_binary]
            args.extend(list_sort)
            process = Popen(args, stdout=PIPE)
            (output, err) = process.communicate()
            process.wait()
            try:
                inst = output.decode("utf-8")[:-1].split()
            except:
                print("Bad instruction !")
        else:
            inst = argv[1].split(" ")
            list_sort = argv[2].split(" ")
    for i in inst:
        if i not in ("sa", "sb", "sc", "pa", "pb", "ra", "rb", "rr", "rra", "rrb", "rrr"):
            print("Bad instruction for pushswap")
            print(i)
            exit(84)
    try:
        list_sort = list(map(int, list_sort))
    except:
        print("Bad list")
        exit(84)
    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle('Push swap Visualizer')
    ax1.set_xlabel("List A")
    ax2.set_xlabel("List B")
    push_swap = pushswap(inst, list_sort, [], 1)
    fonctions_push_swap: dict = {
        "pa": push_swap.pa,
        "pb": push_swap.pb,
        "sa": push_swap.sa,
        "sb": push_swap.sb,
        "sc": push_swap.sc,
        "ra": push_swap.ra,
        "rb": push_swap.rb,
        "rr": push_swap.pa,
        "rra": push_swap.rra,
        "rrb": push_swap.rrb,
        "pa": push_swap.pa,
    }
    add = 0
    ax1.bar(range(len(push_swap.listA)), push_swap.listA)
    ax2.bar(range(len(push_swap.listB)), push_swap.listB)
    plt.pause(TIME_BEFORE)
    for i in push_swap.sort_list:
        add += 1
        fonctions_push_swap[i]()
        if add % SPEED == 0 or add == 1:
            ax1.cla()
            ax2.cla()
            ax1.bar(range(len(push_swap.listA)), push_swap.listA)
            ax2.bar(range(len(push_swap.listB)), push_swap.listB)
            plt.pause(0.001)
    if push_swap.is_sort():
        print("Is Sort")
    else:
        print("Isn't Sort")
    ax1.cla()
    ax2.cla()
    ax1.bar(range(len(push_swap.listA)), push_swap.listA)
    ax2.bar(range(len(push_swap.listB)), push_swap.listB)
    plt.pause(TIME_AFTER)

if __name__ == "__main__":
    main()
