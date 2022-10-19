theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}

board_keys = []

for key in theBoard:
    board_keys.append(key)
print("Клетки распределены таким образом:")
print("1 2 3")
print("4 5 6")
print("7 8 9")

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def game():
    player = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("Твой ход, " + player + ".\nВ какую клетку поставить?")

        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = player
            count += 1
        else:
            print("Эта клетка занята.\nВ какую клетку поставить?")
            continue

        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nИгра окончена.\n")
                print(player + " выиграл!")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                printBoard(theBoard)
                print("\nИгра окончена.\n")
                print(player + " выиграл!")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("\nИгра окончена.\n")
                print(player + " выиграл!")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
                printBoard(theBoard)
                print("\nИгра окончена.\n")
                print(player + " выиграл!")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                printBoard(theBoard)
                print("\nИгра окончена.\n")
                print(player + " выиграл!")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nИгра окончена.\n")
                print(player + " выиграл!")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("\nИгра окончена.\n")
                print(player + " выиграл!")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nИгра окончена.\n")
                print(player + " выиграл!")
                break

        if count == 9:
            print("\nИгра окончена!\n")
            print("Ничья!")
            break

        if player == 'X':
            player = 'O'
        else:
            player = 'X'

    restart = input("Хочешь сыграть снова?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            theBoard[key] = " "

        game()


if __name__ == "__main__":
    game()
