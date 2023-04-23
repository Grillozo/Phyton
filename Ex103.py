def playerstats(p='unown',g=0):
    """
    :param p: Player name (if not informed, return "Unown")
    :param g: Goals (if not informed or informed with a string value, return "0")
    :return:
    """
    if p == '':
        print(f'The player "Unown" scored {g} goals.')
    else:
        print(f'The player {p} scored {g} goals.')

# Program
g = 0
p = str(input("Player Name: ")).strip()
g = str(input("Goals Scored: ")).strip()
if g.isnumeric():
    g = int(g)
else:
    g = 0
playerstats(p,g)
