ALL_SPACES = list('123456789')  # Klucze słownika planszy KIK.
X, O, BLANK = 'X', 'O', ' '  # Stałe reprezentujące wartości tekstowe.

class Board:
    board = {}
    currentPlayer, nextPlayer = X, O

    def __init__(self):
        for space in ALL_SPACES:
            self.board[space] = BLANK  # Wszystkie pola na początku są puste.
        return self.board
    
    def __str__(self):
        return f'''
            {self.board['1']}|{self.board['2']}|{self.board['3']} 1 2 3 
            -+-+- 
            {self.board['4']}|{self.board['5']}|{self.board['6']} 4 5 6 
            -+-+- 
            {self.board['7']}|{self.board['8']}|{self.board['9']} 7 8 9'''
    
    def start(self):
        print('Witaj w grze kółko i krzyżyk!')
        while True:
            print(self.gameBoard)  # Wyświetl planszę na ekranie.

            # Zadawaj graczowi pytanie, aż wprowadzi prawidłową liczbę od 1 do 9:
            move = None
            while not self.isValidSpace(move):
                print(f'Jaki jest ruch gracza {self.currentPlayer}? (1-9)')
                move = input()
            self.updateBoard(move, self.currentPlayer)  # Wykonanie ruchu.
            # Sprawdzenie, czy gra jest zakończona:
            if self.isWinner(self.currentPlayer):  # Sprawdzenie, kto wygrał.
                print(self.board)
                print(self.currentPlayer + ' wygrał grę!')
                break
            elif self.isBoardFull():  # Sprawdzenie remisu.
                print(self.board)
                print('Gra zakończyła się remisem!')
                break
            currentPlayer, nextPlayer = nextPlayer, currentPlayer  # Zmiana gracza.
        print('Dziękuję za grę!')

    def isWinner(self, player):
        """Zwraca True, jeśli gracz jest zwycięzcą tej planszy KIK."""
        b, p = self.board, player # Krótsze nazwy jako "składniowy cukier".
        # Sprawdzenie, czy trzy takie same znaki występują w wierszach, kolumnach i po przekątnych.
        return ((b['1'] == b['2'] == b['3'] == p) or # poziomo na górze
                (b['4'] == b['5'] == b['6'] == p) or # poziomo w środku
                (b['7'] == b['8'] == b['9'] == p) or # poziomo u dołu
                (b['1'] == b['4'] == b['7'] == p) or # pionowo z lewej
                (b['2'] == b['5'] == b['8'] == p) or # pionowo w środku
                (b['3'] == b['6'] == b['9'] == p) or # pionowo z prawej
                (b['3'] == b['5'] == b['7'] == p) or # przekątna 1
                (b['1'] == b['5'] == b['9'] == p)) # przekątna 2
    
    def updateBoard(self, space, mark):
        """Ustawia pole na planszy na podany znak."""
        self.board[space] = mark

    def isValidSpace(self, space):
        """Zwraca True, jeśli pole na planszy ma prawidłowy numer i pole jest puste."""
        if space is None:
            return False
        return space in ALL_SPACES or self.board[space] == BLANK

    def isBoardFull(self):
        """Zwraca True, jeśli wszystkie pola na planszy są zajęte."""
        for space in ALL_SPACES:
            if self.board[space] == BLANK:
                return False # Jeśli nawet jedno pole jest puste, zwracaj False.
        return True # Nie ma wolnych pól, zatem zwróć True.



board = Board()
board.start()