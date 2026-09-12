##############################################################################
#TITLE: The Nightmare Before Christmas Movie Poster
#PURPOSE: Recreate the "The Nightmare Before Christmas" movie poster
#AUTHOR: Asha
#DATE: 12/05/26
##############################################################################

#Initialize Tkinter with these
from tkinter import*
from random import*
import math
myInterface = Tk()
screen = Canvas( myInterface, width=900, height=1000, background="black")
screen.pack()


#--------------------------------------------------BACKGROUND----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#MOON GRADIENT

#darkest shade
screen.create_oval(200,50,700,550, fill ="#f5cf2c", outline = "#f5cf2c")
#mid-dark shades
screen.create_oval(240,100,650,490, fill ="#f4d054", outline = "#f5cf2c")
screen.create_oval(260,100,630,480, fill = "#f5da7f", outline = "#f4d054")
#mid-light shades
screen.create_oval(280,120,620,470,fill = "#efdeb1", outline = "#f4d054")
screen.create_oval(300,140,600,450, fill = "#f3e6b9", outline = "#efdeb1")
#lightest shade
screen.create_oval(310,150,590,440, fill ="#ece6d0", outline = "#f4d054")




#-----------------------------------------------------------------------------------------------------------BACK HILL---------------------------------------------------------------------------------------------------------------------------------
#background hill
screen.create_polygon(300,700,325,650,375,625,450,625,500,675,580,710,590,725,650,700,650,900,300,900, fill = "#052a4a", smooth = True)
screen.create_polygon(390,700,450,725,500,750,550,710,555,705,600,710,600,850,450,850,fill = "#031829", smooth = True)


#FENCING
#back hill lower fence beam
screen.create_line(600,725,580,690,520,720,460,725,425,725,350,690,fill ="#313c52",smooth = True, width = 3)

#back hill upper fence beam
screen.create_line(400,670,450,680,500,660,600,640,660,650,fill ="#313c52", smooth = True, width = 3)

#right tilting pickets
right_x = 260
right_x2 = 280
right_y = 665
right_height = 55
for i in range(4):
    screen.create_line(right_x,right_y,right_x2,right_y-right_height, fill = "#313c52", width = 4)
    right_x = right_x+50
    right_x2 = right_x2 +50
    right_y = right_y+20
    right_height = right_height +10

#left tilting pickets again    
left_y = 740
left_x =470
left_x2 = 450
left_height = 100
for i in range(4):
    screen.create_line(left_x,left_y,left_x2,left_y-left_height, fill = "#313c52", width = 4)
    left_x =left_x+50
    left_x2 = left_x2+50
    left_y = left_y-10
    left_height = left_height -5


#BACKGROUND PUMPKINS
for i in range(3):
    
    #create a list of taken spots to prevent overlap
    taken = []

    pumpkin_y = sample(range(680,755,15),1) [0]
    pumpkin_height = randint(20,50)
    pumpkin_x= sample(range(450,600,35),1) [0]
    pumpkin_width = randint(20,50)

    
    spot = (pumpkin_x,pumpkin_y)
    
    #keep trying new spots until you get a new one
    while spot in taken:
        pumpkin_y = sample(range(680,755,15),1) [0]        
        pumpkin_x= sample(range(450,600,35),1) [0]
        spot = (x,y)
    
    #add the chosen spot to the range of already chosen spots 
    taken.append(spot)

    side_offset = pumpkin_width*0.5


    #left oval
    screen.create_oval(pumpkin_x - side_offset, pumpkin_y + 2, 
                       pumpkin_x + pumpkin_width - side_offset, pumpkin_y+pumpkin_height-2,
                       fill = "#bf480b", outline = "#bf480b")
                   
    #right oval
    screen.create_oval(pumpkin_x + side_offset ,pumpkin_y +2 , 
                       pumpkin_x + pumpkin_width + side_offset, pumpkin_y+pumpkin_height-2,
                       fill = "#bf480b", outline = "#bf480b")
    
    #middle oval
    screen.create_oval(pumpkin_x, pumpkin_y, 
                       pumpkin_x + pumpkin_width, pumpkin_y + pumpkin_height, 
                       fill="#bf480b", outline="#bf480b")


    #stem
    stem_width = 10
    screen.create_rectangle(pumpkin_x +(pumpkin_width/2)-(stem_width/2),pumpkin_y - 9,
                            pumpkin_x + (pumpkin_width/2)+(stem_width/2), pumpkin_y, 
                            fill = "#322326", outline = "#322326") 
 



#---------------------------------------------------------------------------------------------------------SPIRAL HILL----------------------------------------------------------------------------------------------------------------------------------------------------------------------
screen.create_polygon(900,450,600, 300,450,300,450,300,420,320,420,320,350,380,350,430, 350,480,370,500,400,530,450,540,500,530,520,490,520,450,500,435,475,420,450,430,440,460,440,460,450,440, 475,450, 480,470,450,500, 420,500,400,450,435,415,450,400,500,395,565,450,700,650,500,800, 500, 1100,900,1100, 1200,550,fill = "#28547c", smooth = True)

screen.create_polygon(690,950,850,800,860,650,830,550,700,450,650,400, 550,350,500,325,450,350,400,360,360,450,350,465,375,500,400,515,450,530,500,520,510,500,515,475,508,440,470,425,450,430,440,450,455,440,475,450,480,460,485,480,450,515,425,520,400,500,390,475,405,450,475,380,535,415, 650,520, 700,550, 720,650,700,700,625,750,575,775,525,810,500,850, fill = "#214769", width = 8, smooth = True)


#-------------------------------------------------------------------------------------------------------------------FRONT HILL------------------------------------------------------------------------------------------------------------------------------------------
#front hill
screen.create_polygon(-200,750,150,670,300,630,900,1100,-50,1100,fill = "#061326", smooth = True)
screen.create_polygon(225,650,450,750,550,830,600,865,675,930,705,970,400,930,350,900,330,850,255,760,200,700,225,675,250,650, fill = "#0C2142", outline = "#0C2142", smooth = True)
screen.create_polygon(0,700,100,690,150,680,130,750,140,850,150,900,200,950,230,970,230,999,0,999, fill = "#040C1C", smooth = True)

#FENCING
#front hill lower fence beam
screen.create_line(0,770,150,660,250,630,350,690,fill = "#313c52", smooth = True,width = 6)


#front hill upper fence beam
screen.create_line(0,655,100,620,250,610,330,650,400,670,fill = "#313c52", smooth = True, width =6)

#left tilting pickets
left_y = 750
left_x2 =45
left_x = 70
left_height = 125
for i in range(5):
    screen.create_line(left_x,left_y,left_x2,left_y-left_height, fill = "#313c52", width = 6)
    left_x =left_x+35
    left_x2 = left_x2+35
    left_y = left_y-20
    left_height = left_height - 10
    
#middle pickets
screen.create_line(240,660,245,590, fill = "#313c52", width = 5)
    




#-------------------------------------------------------------------------------------------JACK O LANTERNS------------------------------------------------------------------------

def draw_pumpkin(x,y):
    #randomly select pumpkin placement and size
    pumpkin_y = y
    pumpkin_height = randint(50,90)
    pumpkin_x= x
    pumpkin_width = randint(40,80)


    side_offset = pumpkin_width*0.5


    #left oval
    screen.create_oval(pumpkin_x - side_offset, pumpkin_y + 5, 
                       pumpkin_x + pumpkin_width - side_offset, pumpkin_y+pumpkin_height-5,
                       fill = "#e26505", outline = "#e26505")
                   
    #right oval
    screen.create_oval(pumpkin_x + side_offset ,pumpkin_y +5 , 
                       pumpkin_x + pumpkin_width + side_offset, pumpkin_y+pumpkin_height-5,
                       fill = "#e26505", outline = "#e26505")

    #middle oval
    screen.create_oval(pumpkin_x, pumpkin_y, 
                       pumpkin_x + pumpkin_width, pumpkin_y + pumpkin_height, 
                       fill="#e26505", outline="#e26505")


    #stem
    stem_width = 10
    screen.create_rectangle(pumpkin_x +(pumpkin_width/2)-(stem_width/2),pumpkin_y - 15,
                            pumpkin_x + (pumpkin_width/2)+(stem_width/2), pumpkin_y, 
                            fill = "#322326", outline = "#322326")




    #jack o lantern face

    #Eyes
    pumpkin_center_x = pumpkin_x + (pumpkin_width/2)
    eye_y = pumpkin_y+(pumpkin_height/3)
    sizing = 13
    spacing = pumpkin_width*0.2

    #Left Eye
    screen.create_polygon(pumpkin_center_x - spacing, eye_y,
                          pumpkin_center_x - spacing - sizing, eye_y,          
                          pumpkin_center_x - spacing - (sizing / 2), eye_y - sizing,
                          fill="yellow")
                      
    #Right Eye                      
    screen.create_polygon(pumpkin_center_x + spacing, eye_y,
                          pumpkin_center_x + spacing + sizing, eye_y,
                          pumpkin_center_x +spacing + (sizing/2), eye_y-sizing,
                          fill = "yellow")                      

    #MOUTH

    mouth = randint(1,2)

    #option 1

    if mouth == 1:
        screen.create_arc(pumpkin_center_x-(2.5*spacing),pumpkin_y+(pumpkin_height/4),
                          pumpkin_center_x + (2.5*spacing), pumpkin_y+(3*(pumpkin_height/4)),
                          fill = "yellow", start=180, extent = 180, outline = "yellow")

        for i in range(round(pumpkin_width/sizing)):                  
            screen.create_polygon(pumpkin_center_x-(2*spacing),pumpkin_y+(pumpkin_height/2.3),
                                  pumpkin_center_x-(2*spacing)+sizing, pumpkin_y+(pumpkin_height/2.3),
                                  pumpkin_center_x-(2*spacing)+(sizing/2), pumpkin_y+(pumpkin_height/2.3)+sizing,
                                  fill = "#e26505", outline = "#e26505")
                          
            pumpkin_center_x = pumpkin_center_x + sizing




    #option 2

    else:   
    
        screen.create_arc(pumpkin_center_x-(2.5*spacing),pumpkin_y+(pumpkin_height/4),
                          pumpkin_center_x + (2.5*spacing), pumpkin_y+(3*(pumpkin_height/4)),
                          fill = "yellow", start=180, extent = 180, outline = "yellow")

        for i in range(2):                  
            screen.create_polygon(pumpkin_center_x-(2*spacing),pumpkin_y+(pumpkin_height/2.3),
                                  pumpkin_center_x-(2*spacing)+sizing, pumpkin_y+(pumpkin_height/2.3),
                                  pumpkin_center_x-(2*spacing)+(sizing/2), pumpkin_y+(pumpkin_height/2.3)+sizing,
                                  fill = "#e26505", outline = "#e26505")
                          
            screen.create_polygon(pumpkin_center_x-(spacing/2.5), pumpkin_y+(3*(pumpkin_height/4)),
                                  pumpkin_center_x-(spacing/2.5)-sizing, pumpkin_y+(3*(pumpkin_height/4)),
                                  pumpkin_center_x-(spacing/2.5) - (sizing/2), pumpkin_y+(3*(pumpkin_height/4))-sizing,
                                  fill ="#e26505", outline = "#e26505")
                          
            pumpkin_center_x = pumpkin_center_x + 2.5*spacing
    
    
    

#create a list of taken spots to prevent overlap
placed_spots = []

#randomly choose pumpkin coordinates
for i in range(5):
    y = sample(range(700,950,75),1) [0]
    x = sample(range(10,400,78),1) [0]
    
    spot = (x,y)
    
    #keep trying new spots until you get a new one
    while spot in placed_spots:
        y = sample(range(700,900,40),1) [0]
        x = sample(range(10,400,78),1) [0]
        spot = (x,y)
    
    #add the chosen spot to the range of already chosen spots 
    placed_spots.append(spot)
    
    #call function to draw 4 randomly sized pumpkins 
    draw_pumpkin(x,y)
    
    


#------------------------------------------------JACK SKELLINGTON------------------------------------------------------------------------------------------------------------------------

#FACE
screen.create_line(510,110,505,130,fill = "black", width = 4)
screen.create_oval(495,85,525,115, fill = "#d5d9d2", outline = "#d5d9d2")
#eye
screen.create_polygon(502,92,515,90,515,102, fill = "#1b1b1c", smooth = True)
#mouth
screen.create_line(495,100,500,100,505,108,width =2, smooth = True)


#BODY
screen.create_polygon(495,130,485,140,490,200,520,225,503,170,520,130, fill = "black")
screen.create_polygon(495,135,492,155,510,135, fill = "#e3e6df")
#RS shoulder
screen.create_line(520,130,535,130, fill = "black", width = 2)
screen.create_line(520,130,535,145, fill = "black", width = 2)
#LS shoulder
screen.create_line(495,130,475,120, width = 2)
screen.create_line(495,130,475,130, width =2)


#LEGS
screen.create_line(490,200,498,300, fill = "black", width = 6)
screen.create_line(501,200,503,240,535,300,fill = "black", width =6)


#ARMS 
screen.create_line(485,140,450,160,480,165, fill ="black", width =4)
screen.create_line(520,130,535,185, 555,215, fill = "black", width = 4)




#------------------------------------------------------------------------------LIGHTBULBS WITH RANDOMIZED COLOURS HANGING OFF "CHRISTMAS"----------------------------------------------------------------------------------
#Set initial (x,y) coordinates for the arcs
x=620
y = 798

while x<820:
    #Draw the arc
    diam = randint(40,90)
    height = randint(40,70)
    screen.create_arc(x,y,x+diam,y+height, start = 180, extent = 180, style = ARC, outline = "black", width = 2)
        
    #Calculate radius sizing horizontally and vertically
    rx = diam / 2
    ry = height / 2
     #Calculate the center of each arc
    centerX = x + rx
    centerY = y + ry

    #Possible light colours
    colours = ["red","blue","yellow","green"]
    
    #Draw the 5 lightbulbs for each arc
    angles = [180, 225, 270, 315, 360]
    
    for i in angles:
        #Convert the angle measurmenet from degree to radian so that the computer can understand it
        #Divide each arc into individual rotations (3.14/semi circle length)
        rad = i*(3.14/180)
        
        #Use cosine to calculate where the dot needs to be placed vertically
        #Use sine to calculate where the dot needs to be placed vertically
        cx = centerX+rx*math.cos(rad)
        cy = centerY -ry*math.sin(rad)
        
        #Randomly choose a colour
        colour = choice(colours)
        
        #Draw each bulb based on the parameters calculated above
        screen.create_oval(cx-3, cy-3, cx+3, cy+3, fill=colour, outline=colour)

    #Adjust the x value to move the stating point across
    x += diam 




#---------------------------------------------------------------------------TEXT------------------------------------------------------------------------------------

#Tim Burton's
screen.create_text(745, 600, text="TIM BURTON'S", font=("times", 18), fill="#f5c622")


#The 
screen.create_text(745, 650, text="THE", font=("times", 25), fill="#f5c622")

#Nightmare
screen.create_text(740,700, text = "NIGHTMARE", font=("times",31), fill="#f5c622")

#Before
screen.create_text(750, 750, text="BEFORE", font=("times", 27), fill="#f5c622")

#Christmas
screen.create_text(740, 805, text="CHRISTMAS", font=("times", 28), fill="#f5c622")




# #------------------------------------------------------Grid lines------------------------------------------------------------------------------------------------------
# #REMOVE THESE BEFORE SUBMITTING ANY ASSIGNMENTS
# spacing = 50

# for x in range(0, 900, spacing): 
#     screen.create_line(x, 25, x, 1000, fill="white")
#     screen.create_text(x, 5, text=str(x), font="Times 9", anchor = N, fill = "white")

# for y in range(0, 1000, spacing):
#     screen.create_line(25, y, 900, y, fill="white")
#     screen.create_text(5, y, text=str(y), font="Times 9", anchor = W, fill = "white")





screen.mainloop()
