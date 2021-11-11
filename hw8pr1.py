#mandelbrot set
#Norah Pack
#

# keep this import line...
from cs5png3 import *


#
# A test function...
#
def test_fun():
    """Algorithmic image creation, one pixel at a time.
       This is a test function: it should create
       an image named test.png in the current directory.
    """
    WIDTH=300 #the width of the png image
    HEIGHT=200 #the height of the png image
    im = PNGImage(WIDTH, HEIGHT)  # Creates an image of width 300, height 200

    # Nested loops!
    for r in range(HEIGHT):     # loops over the rows with runner variable r
        for c in range(WIDTH): # loops over the columns with c
            if  c == r:   
                im.plotPoint(c, r, (255, 0, 0))
            #else:
            #    im.plotPoint(c, r, (255, 0, 0))
                
    im.saveFile()

#
# start your Lab 8 functions here:
#

def mult(c, n):
    """Mult multiplies c by the positive integer n,
       using only a loop and addition.
    """
    result = 0
    for i in range(n):
        result+=c
    return result

assert mult(3, 5) == 15

def update(c, n):
    """Update starts with z = 0 and runs z = z**2 + c
       for a total of n times. It returns the final z.
    """
    z=0
    for i in range(n):
        z = z**2 + c
    return z

def inMSet(c, n):
    """inMSet accepts
            c for the update step of z = z**2+c
            n, the maximum number of times to run that step.
       Then, it returns
            False as soon as abs(z) gets larger than 2.
            True if abs(z) never gets larger than 2 (for n iterations).
    """
    DIVERGENCE_VALUE=2 # returns False as soon as abs(z) gets larger than the divergence value 
    z=0
    for i in range(n):
        z = z**2 + c
        if(abs(z)>DIVERGENCE_VALUE):
            return False
    return True

assert inMSet(0 + 0j, 25) == True
assert inMSet(3 + 4j, 25) == False
assert inMSet(.3 + -.5j, 25) == True
assert inMSet(-.7 + .3j, 25) == False
assert inMSet(.42 + .2j, 25) == True
assert inMSet(.42 + .2j, 50) == False

from cs5png3 import *   # You might already have this line at the top...

def weWantThisPixel(col, row):
    """This function returns True if we want to show
       the pixel at col, row and False otherwise.
    """
    if col % 10 == 0 or row % 10 == 0:
        return True
    else:
        return False

def test():
    """This function demonstrates how
       to create and save a PNG image.
    """
    width = 300 #the width of the png image
    height = 200 #the height of the png image
    image = PNGImage(width, height)

    # Create a loop that will draw some pixels.

    for col in range(width):
        for row in range(height):
            if weWantThisPixel(col, row):
                image.plotPoint(col, row)

    # We looped through every image pixel; we now write the file.

    image.saveFile()

# if i changed the line if col % 10 == 0 and row % 10 == 0: to the line if col % 10 == 0 or row % 10 == 0:, instead of being a dotted field, the image would be a sort of "plaid" pattern, with black lines vertically and horizontally when the row number or column number is a multiple of 10.

def scale(pix, pixMax, floatMin, floatMax):
    """scale accepts
           pix, the CURRENT pixel column (or row).
           pixMax, the total number of pixel columns.
           floatMin, the minimum floating-point value.
           floatMax, the maximum floating-point value.
       scale returns the floating-point value that
           corresponds to pix.
    """
    return(floatMin+((pix/pixMax)*(floatMax-floatMin)))



def mset():
    """Creates a 300x200 image of the Mandelbrot set.
    """
    NUM_ITERATIONS = 100  # Number of updates; will be assigned to n
    XMIN = -1.2          # The smallest real coordinate value
    XMAX = -.6          # The largest real coordinate value
    YMIN = -.5          # The smallest imaginary coordinate value
    YMAX = -.01          # The largest imaginary coordinate value
    FACTOR = 7           # the scale - factor of the width and the height of the png image
    width = 300*FACTOR        # The width of the png image; We can update the *1 later to enlarge the image...
    height = 200*FACTOR       # The height of the png image
    image = PNGImage(width, height)

    # Create a loop to draw some pixels

    for col in range(width):
        for row in range(height):
            # Use scale twice:
            #   once to create the real part of c (x)
            x = scale(col, width, XMIN, XMAX)
            #   once to create the imaginary part of c (y)
            y = scale(row, height, YMIN, YMAX)
            # THEN, create c, choose n, and test:
            c = x + y*1j
            n = NUM_ITERATIONS
            if inMSet(c, n):
                image.plotPoint(col, row, (255, 212, 243))
            else:
                image.plotPoint(col, row, (168, 255, 194))

    # we looped through every image pixel; we now write the file
    mset=image.saveFile()

def inMSetColor(c, n):
    """inMSetColor accepts
            c for the update step of z = z**2+c
            n, the maximum number of times to run that step.
       Then, it returns
            False as soon as abs(z) gets larger than 2.
            True if abs(z) never gets larger than 2 (for n iterations).
    """
    DIVERGENCE_VALUE=2.5 # returns False as soon as abs(z) gets larger than the divergence value 
    z=0
    for i in range(n):
        z = z**2 + c
        if(abs(z)>DIVERGENCE_VALUE):
            return (i*1.0/(n*1.0))
    return 1000


def msetColor():
    """Creates a 300x200 image of the Mandelbrot set.
    """
    NUM_ITERATIONS = 200  # Number of updates; will be assigned to n
    XMIN = -2          # The smallest real coordinate value
    XMAX = 1          # The largest real coordinate value
    YMIN = -1          # The smallest imaginary coordinate value
    YMAX = 1          # The largest imaginary coordinate value
    FACTOR = 20           # the scale - factor of the width and the height of the png image
    width = 300*FACTOR        # The width of the png image; We can update the *1 later to enlarge the image...
    height = 200*FACTOR       # The height of the png image
    image = PNGImage(width, height)

    # Create a loop to draw some pixels

    for col in range(width):
        for row in range(height):
            # Use scale twice:
            #   once to create the real part of c (x)
            x = scale(col, width, XMIN, XMAX)
            #   once to create the imaginary part of c (y)
            y = scale(row, height, YMIN, YMAX)
            # THEN, create c, choose n, and test:
            c = x + y*1j
            n = NUM_ITERATIONS
            if inMSetColor(c, n)==1000:
                image.plotPoint(col, row, (0, 0, 0))
            else:
                darkvalue=int(25*(inMSetColor(c,n)**.2))
                rainbow_set=[[255,0,0], [255,127,0], [255,255,0], [0,255,0], [0,0,255],[255,0,0], [255,127,0], [255,255,0], [0,255,0], [0,0,255],[255,0,0], [255,127,0], [255,255,0], [0,255,0], [0,0,255],[255,0,0], [255,127,0], [255,255,0], [0,255,0], [0,0,255],[255,0,0], [255,127,0], [255,255,0], [0,255,0], [0,0,255]]
                number_set=[]
                for i in range(25):
                    number_set.append(rainbow_set[i])

                image.plotPoint(col, row, (number_set[darkvalue][0], number_set[darkvalue][1], number_set[darkvalue][2]))

    # we looped through every image pixel; we now write the file
    mset=image.saveFile()

def example():
    """Shows how to access the pixels of an image.
       inputPixels is a list of rows, each of which is a list of columns,
           each of which is a list [r,g,b].
    """
    inputPixels = getRGB("./pngs/cat.png")
    inputPixels = inputPixels[::-1]       # The rows are reversed

    height1 = len(inputPixels)
    width1 = len(inputPixels[0])

    NUM_ITERATIONS = 200  # Number of updates; will be assigned to n
    XMIN = -2          # The smallest real coordinate value
    XMAX = 1          # The largest real coordinate value

    #x-range is set. y-range should be the centered at 0 and the x-ratio: y-ratio = width-height ratio. 

    y_range=((XMAX-XMIN)*height1/width1)




    YMIN = -1*(y_range/2)          # The smallest imaginary coordinate value
    YMAX = y_range/2          # The largest imaginary coordinate value
    FACTOR = 7           # the scale - factor of the width and the height of the png image
    width = width1*FACTOR        # The width of the png image; We can update the *1 later to enlarge the image...
    height = height1*FACTOR       # The height of the png image

    
    image = PNGImage(width, height)




    # Create a loop to draw some pixels

    for col in range(width):
        for row in range(height):
            # Use scale twice:
            #   once to create the real part of c (x)
            x = scale(col, width, XMIN, XMAX)
            #   once to create the imaginary part of c (y)
            y = scale(row, height, YMIN, YMAX)
            # THEN, create c, choose n, and test:
            c = x + y*1j
            n = NUM_ITERATIONS
            if inMSetColor(c, n)==1000:
                image.plotPoint(col, row, inputPixels[int(row/FACTOR)][int(col/FACTOR)])
            else:
                darkvalue=int(25*(inMSetColor(c,n)**.2))
                rainbow_set=[[255,0,0], [255,127,0], [255,255,0], [0,255,0], [0,0,255],[255,0,0], [255,127,0], [255,255,0], [0,255,0], [0,0,255],[255,0,0], [255,127,0], [255,255,0], [0,255,0], [0,0,255],[255,0,0], [255,127,0], [255,255,0], [0,255,0], [0,0,255],[255,0,0], [255,127,0], [255,255,0], [0,255,0], [0,0,255]]
                number_set=[]
                for i in range(25):
                    number_set.append(rainbow_set[i])

                image.plotPoint(col, row, (number_set[darkvalue][0], number_set[darkvalue][1], number_set[darkvalue][2]))

    # we looped through every image pixel; we now write the file
   

    


    image.saveFile()



