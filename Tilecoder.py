import math

numTilings = 4
tiles = 26
numTiles = numTilings*tiles*tiles
    
def tilecode(in1,in2,tileIndices):  
    
    in2 = in2 + 380
    step_x = (300.0/(tiles-1))
    step_y = (760.96/(tiles-1))
    
    
    shift_x = (step_x/numTilings)
    shift_y = (step_y/numTilings)
    
    
    x_cord = math.floor(in1/step_x)
    y_cord = math.floor(in2/step_y)
    
    
    tileIndices[0] = (tiles*y_cord + x_cord)
    
    for i in range(numTilings-1):
        in1 = in1 + (shift_x)
        in2 = in2 + (shift_y)
        x_cord = math.floor(in1/step_x)
        y_cord = math.floor(in2/step_y)
        
        tileIndices[i+1] = (tiles*y_cord + x_cord + (tiles*tiles)*(i+1))
        
    
def printTileCoderIndices(in1,in2):
    tileIndices = [-1]*numTilings
    tilecode(in1,in2,tileIndices)
    print 'Tile indices for input (',in1,',',in2, ') are : ', tileIndices

#printTileCoderIndices(300,250)
#printTileCoderIndices(4.0,2.0)
#printTileCoderIndices(5.99,5.99)
#printTileCoderIndices(4.0,2.1)