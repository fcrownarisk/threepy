import det1234
import det5678
import det9101112
import one
import oppoone
import square
import antisquare
import pyramid
import antipyramid
import tri
import antitri
DET = det1234 + det5678 + det9101112
TRI = tri - antitri
ONE = one + oppoone
Square = square * antisquare
Pyramid = pyramid % antipyramid
DETtri = DET * TRI
triDET = TRI % DET
ONESquare = ONE * square
squareONE = square % ONE
oppoPyramid = antipyramid / pyramid
dimPyramid = square - antisquare

def SUM():
    [DET/TRI + TRI/DET =='DETTRI' +'TRIDET']
    ['DETTRI' +ONESquare == 'SquareONE' + 'TRIDET']
    [Pyramid == oppoPyramid + dimPyramid]
    


