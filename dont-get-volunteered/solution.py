import numpy as np

# ! define the calculation to get the distance between two places on the board
# ! define boundaries so paths are found within a 1D array
# *              tbound cell.no > width 
# * lbound cell.no % width = 0   rbound cell.no % width = width -1
# ?           0   1   2   3   4   5   6   7    
# ?           8   9   10  11  12  13  14  15
# ?           16  17  18  19  20  21  22  23
# ?           24  25  26  27  28  29  30  31
# ?           32  33  34  35  36  37  38  39
# ?           40  41  42  43  44  45  46  47
# ?           48  49  50  51  52  53  54  55
# ?           56  57  58  59  60  61  62  63
# *       bbound cell.no > (width ** 2) - width - 1)

def solution(src, wid, dest):
  width = wid
  oneDGrid = [0 for i in range(width*width)]
  oneDGrid[src] = 0

  def check(coord):
    init = coord
    


    topLeft = init - (width * 2 + 1) if init > (width * 2) and not init % width == 0 else None
    topRight = init - (width * 2 - 1) if init > (width * 2) and not init % width == width - 1 else None
    bottomLeft = init + (width * 2 - 1) if init < (width * width - width * 2) and not init % width == 0 else None
    bottomRight = init + (width * 2 + 1) if init < (width * width - width * 2) and not init % width == width - 1 else None
    leftTop = init - (width + 2) if init > width and not init % width == 0 and not init % width == 1 else None
    leftBottom = init + (width - 2) if init < (width * width - width) and not init % width == 0 and not init % width == 1 else None
    rightTop = init - (width - 2) if init > width and not init % width == width - 1 and not init % width == width - 2 else None
    rightBottom = init + (width + 2) if init < (width * width - width) and not init % width == width - 1 and not init % width == width - 2 else None
    
    # for i in range(width):
    #   print(np.array(oneDGrid[i*width:i*width+width]))
    # print("\n")

    if topLeft != None and oneDGrid[topLeft] != None and oneDGrid[coord] < width + 1:
      if oneDGrid[topLeft] == 0 or oneDGrid[topLeft] > oneDGrid[coord] +1:
        oneDGrid[topLeft] = oneDGrid[init] + 1 if oneDGrid[init] != None else 1
        check(topLeft)
    if topRight != None and oneDGrid[topRight] != None and oneDGrid[coord] < width + 1:
      if oneDGrid[topRight] == 0 or oneDGrid[topRight] > oneDGrid[coord]+1:
        oneDGrid[topRight] = oneDGrid[init] + 1 if oneDGrid[init] != None else 1
        check(topRight)
    if bottomLeft != None and oneDGrid[bottomLeft] != None and oneDGrid[coord] < width + 1:
      if oneDGrid[bottomLeft] == 0 or oneDGrid[bottomLeft] > oneDGrid[coord]+1:
        oneDGrid[bottomLeft] = oneDGrid[init] + 1 if oneDGrid[init] != None else 1
        check(bottomLeft)
    if bottomRight != None and oneDGrid[bottomRight] != None and oneDGrid[coord] < width + 1:
      if oneDGrid[bottomRight] == 0 or oneDGrid[bottomRight] > oneDGrid[coord]+1:
        oneDGrid[bottomRight] = oneDGrid[init] + 1 if oneDGrid[init] != None else 1
        check(bottomRight)
    if leftTop != None and oneDGrid[leftTop] != None and oneDGrid[coord] < width + 1:
      if oneDGrid[leftTop] == 0 or oneDGrid[leftTop] > oneDGrid[coord]+1:
        oneDGrid[leftTop] = oneDGrid[init] + 1 if oneDGrid[init] != None else 1
        check(leftTop)
    if leftBottom != None and oneDGrid[leftBottom] != None and oneDGrid[coord] < width + 1:
      if oneDGrid[leftBottom] == 0 or oneDGrid[leftBottom] > oneDGrid[coord]+1:
        oneDGrid[leftBottom] = oneDGrid[init] + 1 if oneDGrid[init] != None else 1
        check(leftBottom)
    if rightTop != None and oneDGrid[rightTop] != None and oneDGrid[coord] < width + 1:
      if oneDGrid[rightTop] == 0 or oneDGrid[rightTop] > oneDGrid[coord]+1:
        oneDGrid[rightTop] = oneDGrid[init] + 1 if oneDGrid[init] != None else 1
        check(rightTop)
    if rightBottom != None and oneDGrid[rightBottom] != None and oneDGrid[coord] < width + 1:
      if oneDGrid[rightBottom] == 0 or oneDGrid[rightBottom] > oneDGrid[coord]+1:
        oneDGrid[rightBottom] = oneDGrid[init] + 1 if oneDGrid[init] != None else 1
        check(rightBottom)
    oneDGrid[src] = 0

  check(src)
  for i in range(width):
    print(np.array(oneDGrid[i*width:i*width+width]))
  print("\n")
  return oneDGrid[dest]
    
print(solution(35, 6, 4)) 
print(solution(4, 12, 65)) 
print(solution(147, 17, 19)) 
print(solution(0, 21, 0))
print(solution(26, 12, 26))
