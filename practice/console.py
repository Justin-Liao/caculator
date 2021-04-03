import os
import sys


def quit():
    sys.exit(0)


def help():
    print("Command list")
    print("_'help' & '?': open help list")
    print("_'quit'      : quit the program")


def main():
    print("- please input command\n- use 'help' to check commands\n")
    while True:
        try:
            cmd = input('> ').strip()
            if cmd == '':
                pass
            elif cmd == 'help' or cmd == '?':
                help()
            elif cmd == 'quit':
                quit()
            else:
                print("- command "+cmd +
                      " not found; please input 'help' to check commands")
        except KeyboardInterrupt:
            print("Ctrl+C detected; Quit program")
            quit()


if __name__ == "__main__":
    main()
