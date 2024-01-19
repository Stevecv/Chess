import colorama
from colorama import Fore

pieces = ["♔ ", "♕ ", "♖ ", "♗ ", "♘ ", "♙ ", "♚ ", "♛ ", "♜ ", "♝ ", "♞ ", "♟︎ ", "", "• "]

data = [2,  4,  3,  1,  0,  3,  4,  2,
        5,  5,  5,  5,  5,  5,  5,  5,
        12, 12, 12, 12, 12, 12, 12, 12,
        12, 12, 12, 12, 12, 12, 12, 12,
        12, 12, 12, 12, 12, 12, 12, 12,
        12, 12, 12, 12, 12, 12, 12, 12,
        11, 11, 11, 11, 11, 11, 11, 11,
        8,  10, 9,  7,  6,  9,  10, 8]

renderRed = []
renderBlue = []
def clearBoard():
  global renderBlue
  global renderRed
  a = 0
  for t in data:
    if t == 13:
      data[a] = 12
    a = a+1
  renderRed = []
  renderBlue = []
  
def printBoard():
  for i in range(20):
    print("")
  global renderRed
  global renderBlue
  print("  A B C D E F G H")
  whitesqr = "■ "
  blacksqr = "□ "

  square = "w"
  line = ""
  tile = 0
  for y in range(0, 8):
    for x in range(0, 8):
      piece = data[tile]
      if square == "w":
        if piece == 12:
          line = line + whitesqr
        else:
          line = rColour(tile, renderRed, line)
          line = line + pieces[piece] + Fore.WHITE
        square = "b"
      elif square == "b":
        if piece == 12:
          line = line + blacksqr
        else:
          line = rColour(tile, renderRed, line)
          line = line + pieces[piece] + Fore.WHITE
        square = "w"
        

      tile = tile + 1
    print(str(8 - y) + " " + line + " " + str(8 - y))
    if square == "w":
      square = "b"
    elif square == "b":
      square = "w"
    line = ""
  print("  A B C D E F G H")

turn = "white"
def askPiece():
  return input("It is {}'s turn. Enter the piece you wish to move > ".format(turn))

def rColour(tile, renderRed, line):
  global renderBlue
  if tile in renderBlue:
    line = line + Fore.BLUE
  if tile in renderRed:
    line = line + Fore.RED
  return line
    
def askPlace():
  place = input("It is {}'s turn. Enter where you want to move or c to cancel> ".format(turn))
  if place == "c":
    clearBoard()
    printBoard()
  else:
    return place

pieceToMove = 65
place = 65
def getNumFromAlgebraic(a, num):
  global pieceToMove
  global renderBlue
  global place
  if a == None:
    a = askPiece()
  a = a.upper()
  try:
    expression = list(a)
    letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
    i = 0
    for letter in letters:
      if letter == expression[0]:
        number1 = i+1
        break
      i = i+1
    number2 = 9-int(expression[1])

  except:
    print(a + " is not a valid move!")
    if num == 1:
      pieceToMove = getNumFromAlgebraic(askPiece(), 1)
    else:
      place = getNumFromAlgebraic(askPlace(), 1)
      
    return 65
  return ((number2*8)-(8-number1))-1


def isWhite(n):
  p = data[n]
  if (p == 12):
    return False
  if p > 5:
    return True
  else:
    return False

def isBlack(n):
  p = data[n]
  if (p == 12):
    return False
  if p < 6:
    return True
  else:
    return False

def canTakeColour(piece, taker):
  if (isBlack(piece) and isWhite(taker)) or (isWhite(piece) and isBlack(taker)):
    return True
  else:
    return False
    
  
    
  
#Raycasts
def raycastUp(f, c):
  moves = []
  for i in range(1,c+1):
    place = f-8*i
    moves.append(place)
    if data[place] != 12:
      break
  return moves

def raycastDown(f, c):
  moves = []
  for i in range(1,c+1):
    place = f+8*i
    moves.append(place)
    if place > 63:
      break
    if data[place] != 12:
      break
  return moves

def raycastLeft(f, c):
  moves = []
  if (f % 8 == 0):
    return moves
  for i in range(1,c+1):
    place = f-i
    moves.append(place)
    if (place % 8 == 0):
      break
    if data[place] != 12:
      break
      
  return moves

def raycastRight(f, c):
  moves = []
  print((f % 8 == 0))
  #if (f % 8 == 0):
  #  return moves
  for i in range(1,c+1):
    place = f+i
    if (place % 8 == 0):
      break
    moves.append(place)
    if data[place] != 12:
      break
      
  return moves


def raycastDownRight(f, c):
  moves = []
  if (f % 8 == 0):
    return moves
  for i in range(1,c+1):
    place = (f+i)+(8*i)
    if place >= 0:
      if place > 63:
        break
      if (place % 8 == 0):
        break
      moves.append(place)
      if data[place] != 12:
        break
      
  return moves

def raycastDownLeft(f, c):
  moves = []
  if (f % 8 == 0):
    return moves
  for i in range(1,c+1):
    place = (f-i)+(8*i)
    if place >= 0:
      moves.append(place)
      if place > 63:
        break
      if (place % 8 == 0):
        break
      if data[place] != 12:
        break
      
  return moves

def raycastUpRight(f, c):
  moves = []
  if (f % 8 == 0):
    return moves
  for i in range(1,c+1):
    place = (f+i)-(8*i)
    if place >= 0:
      if (place % 8 == 0):
        break
      moves.append(place)
      if data[place] != 12:
        break
      
  return moves

def raycastUpLeft(f, c):
  moves = []
  if (f % 8 == 0):
    return moves
  for i in range(1,c+1):
    place = (f-i)-(8*i)
    if place >= 0:
      moves.append(place)
      if (place % 8 == 0):
        break
      if data[place] != 12:
        break
      
  return moves

def queenRaycast(f, show):
  moves = raycastUpLeft(f, 8) + raycastUpRight(f, 8) + raycastDownLeft(f, 8) + raycastDownRight(f, 8) + raycastUp(f, 8) + raycastDown(f, 8) + raycastLeft(f, 8) + raycastRight(f, 8)
  #return moves
  if show == True:
    for move in moves:
      showPossibleMove(f, move)
  return moves

def bishopRaycast(f, show):
  moves = raycastUpLeft(f, 8) + raycastUpRight(f, 8) + raycastDownLeft(f, 8) + raycastDownRight(f, 8)
  #return moves
  if show == True:
    for move in moves:
      showPossibleMove(f, move)
  return moves
    
def rookRaycast(f, show):
  moves = raycastUp(f, 8) + raycastDown(f, 8) + raycastLeft(f, 8) + raycastRight(f, 8)
  #return moves
  if show == True:
    for move in moves:
      showPossibleMove(f, move)
  return moves
    
def kingRaycast(f, show):
  moves = raycastUp(f, 1) + raycastDown(f, 1) + raycastLeft(f, 1) + raycastRight(f, 1) + raycastUpLeft(f, 1) + raycastDownLeft(f, 1) + raycastDownRight(f, 1) + raycastUpRight(f, 1)

  return moves

def knightRaycast(f, show):
  possibleMoves = []
  possibleMoves.append(f+16)
  possibleMoves.append(f+16)
  possibleMoves.append(f+8)
  possibleMoves.append(f+8)

  possibleMoves.append(f-16)
  possibleMoves.append(f-16)
  possibleMoves.append(f-8)
  possibleMoves.append(f-8)
  moves = []

  
  rightNumbers = [7, 15, 23, 39, 47, 55, 63]
  leftNumbers = [0, 8, 16, 24, 40, 48, 56]
    
  count = -1
  operations = [1, -1, 2, -2, 1, -1, 2, -2]
  finalMoves = []
  for move in possibleMoves:
    if (move % 8 == 0):
      continue
    t = move
    l = move
    for j in range(0,9):
      if t not in rightNumbers:
        t = t+1
      elif l not in leftNumbers:
        l = l-1
    
      
    count = count+1
        
    if move + operations[count] <= t and move + operations[count] >= l:
      move = move + operations[count]
      moves.append(move)
      finalMoves.append(move)
      if show == True:
        showPossibleMove(f, move)
  return finalMoves
      
      
        
def pawnRaycast(f, show, taking):
  possibleMoves = []
  if isWhite(f):
    if taking == False:
      if f >= 48 and f <= 55:
        possibleMoves = possibleMoves + raycastUp(f, 2)
      else:
        possibleMoves = possibleMoves + raycastUp(f, 1)
      
    if data[f-8+1] != 12 or taking == True:
      possibleMoves.append(f-8+1)
    if data[f-8-1] != 12 or taking == True:
      possibleMoves.append(f-8-1)

  if isBlack(f):
    if taking == False:
      if f >= 8 and f <= 15:
        possibleMoves = possibleMoves + raycastDown(f, 2)
      else:
        possibleMoves = possibleMoves + raycastDown(f, 1)
      
    if data[f+8+1] != 12 or taking == True:
      possibleMoves.append(f+8+1)
    if data[f+8-1] != 12 or taking == True:
      possibleMoves.append(f+8-1)

  if show == True:
    for move in possibleMoves:
      showPossibleMove(f, move)
  return possibleMoves

    
  moves = []
  for move in possibleMoves:
    if (move % 8 == 0):
      continue

    moves.append(move)
    if show == True:
      showPossibleMove(f, move)

def showPossibleMove(original, place):
  if place <= 63 and place >= 0:
    p = data[place]

    if p == 12:
      data[place] = 13
    else:
      if canTakeColour(place, original):
        renderRed.append(place)

def raycastPieceNum(pieceToMove, show, taking):
  m = data[pieceToMove]
  possibleMoves = []
  if m == 1 or m == 7:
    possibleMoves = possibleMoves + queenRaycast(pieceToMove, show)
  if m == 2 or m == 8:
    possibleMoves = possibleMoves + rookRaycast(pieceToMove, show)
  if m == 3 or m == 9:
    possibleMoves = possibleMoves + bishopRaycast(pieceToMove, show)
  if m == 4 or m == 10:
    possibleMoves = possibleMoves + knightRaycast(pieceToMove, show)
  if m == 5 or m == 11:
    possibleMoves = possibleMoves + pawnRaycast(pieceToMove, show, taking)
  if m == 0 or m == 6:
    possibleMoves = possibleMoves + kingRaycast(pieceToMove, show)

    #Check not check
    num = 0
    for piece in data:
      if piece != 0 and piece != 6:
        for kingMove in possibleMoves:
          if kingMove in raycastPieceNum(num, False, True):
            if canTakeColour(pieceToMove, num):
              possibleMoves.remove(kingMove)
      if len(possibleMoves) == 0:
        print("Checkmate.")
        break
          
      num = num+1

    for mo in possibleMoves:
      showPossibleMove(pieceToMove, mo)
  return possibleMoves
    

def checkCheck():
  num = 0

  for piece in data:
    if piece != 0 and piece != 6:
      for kingMove in possibleMoves:
        if kingMove in raycastPieceNum(num, False, True):
          if canTakeColour(pieceToMove, num):
            possibleMoves.remove(kingMove)

        
printBoard()
while True:
  aPiece = askPiece()
  print(aPiece)
  if aPiece == None:
    askPiece()
  pieceToMove = getNumFromAlgebraic(aPiece, 1)
  renderBlue.append(pieceToMove)
  if isWhite(pieceToMove) and turn != "white":
    print("It is " + turn + "'s turn! " + aPiece.upper() + " is black!")
    clearBoard()
    continue
  if isBlack(pieceToMove) and turn != "black":
    print("It is " + turn + "'s turn! " + aPiece.upper() + " is black!")
    clearBoard()
    continue

  m = data[pieceToMove]
  possibleMoves = raycastPieceNum(pieceToMove, True, False)
  

  printBoard()
  place = getNumFromAlgebraic(askPlace(), 1)
  
  if place not in possibleMoves:
    print("That is an illegal move!")
    clearBoard()
    continue

  clearBoard()

  #Remove piece from place
  if(data[pieceToMove] == 12):
    print("There is no piece on {}!".format(aPiece))
    continue
  data[place] = data[pieceToMove]
  data[pieceToMove] = 12
  
  if turn == "white":
    turn = "black"
  else:
    turn = "white"
  
  printBoard()
