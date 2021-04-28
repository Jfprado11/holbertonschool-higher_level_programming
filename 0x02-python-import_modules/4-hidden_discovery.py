#!/usr/bin/python3
def main():
    import hidden_4
    hid = dir(hidden_4)
    for i in len(hid):
        if hid[i][0] != "_":
            print(hid[i])

if __name__ == "__main__":
    main()
