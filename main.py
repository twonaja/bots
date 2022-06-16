import echobot
import wikibot


def main():
    token: str = 'you telegram token'
    choice: int = int(input('Choose bot! 1 - echo; 2 - wiki:\n'))
    if choice == 1:
        echobot.echo_bot(token)
    elif choice == 2:
        wikibot.wiki_bot(token)


if __name__ == '__main__':
    main()
