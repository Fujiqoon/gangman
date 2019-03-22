import random

def gangman():
    lstword=['Facebook','Amazon','Apple','Google','Netflix']
    wrong=0
    randnum=random.randint(0,4)
    word=lstword[randnum]
    remain_letters=list(word)
    board=['__']*len(word)
    stage=['',
    '|          ',
    '|----------',
    '|    \O/   ',
    '|     |    ',
    '|    / \   '
    ]
    win=False
    print('Welcome to Gangman')
    
    while wrong < len(stage)-1:
        
        char=input('Guess a letter')
        if char in remain_letters:
            cind=remain_letters.index(char)
            board[cind]=char
            remain_letters[cind]='$'
            
        else:
            wrong+=1
            print('\n'.join(stage[0:wrong]))
        print(' '.join(board))
        if '__' not in board:
            print('You win')
            print('The word is {}'.format(word))
            win=True
            break
    if not win:
        print('\n'.join(stage[:]))
        print('You lose.The word is {}'.format(word))
            
gangman()
