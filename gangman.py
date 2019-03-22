# define 

def gangman(word):
    wrong=0
    stage=['',
        '|          ',
        '|    \O/   ',
        '|     |    ',
        '|    / \   '
        ]
    rletter=list(word)
    board=['__']*len(word)
    win = False
    print('Welcome to gangman')
    # ここからループ
    while wrong < len(stage)-1:
        print('\n')
        char=input('Guess a letter')
        if char in rletter:
            cind=rletter.index(char)
            board[cind]=char
            rletter[cind]='$'
        else:
            wrong+=1
        print(' '.join(board))
        #gangmanを表示させる
        e=wrong+1
        print('\n'.join(stage[0:e]))
        #終了時
        if '__' not in board:
            print('You win the game')
            print(' '.join(board))
            win= True
            break
    #負けた
    if not win:
        print('\n'.join(stage[:]))
        win=False
        print('You lose.It was {}'.format(word))

