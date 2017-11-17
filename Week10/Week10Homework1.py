def countCh(text, ch):
    cnt = text.count(ch, 0, len(text))
    print(cnt)


def main():
    t = input()
    c = input()
    countCh(t, c)


if __name__ == "__main__":
    main()