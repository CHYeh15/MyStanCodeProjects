"""
File: my_drawing.py
Name: Kevin
----------------------
This file uses the campy module to
draw on a GWindow object.
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GPolygon, GLine
from campy.graphics.gwindow import GWindow

# Global variables
window = GWindow(width=800, height=400, title='MyFace')
face_width = 180
face_height = 110
face_x = 360
face_y = 50


def main():
    """
    Title: One of my daughter's favorite characters in Toy Story.

    The Alien is my daughter's favorite character,
    so my family has a lot of related products, so I picked
    one out to imitate.
    """
    skyline()
    body()
    neck()
    face()
    ear()
    eye()
    mouth()
    belt()
    foot()
    hand()
    bedge()
    word()


def face():
    face = GOval(face_width, face_height, x=face_x, y=face_y)
    face.filled = 'True'
    face.fill_color = 'yellowgreen'
    face.color = 'yellowgreen'
    window.add(face)


def neck():
    neck = GOval(face_width * 0.9, face_height * 0.9, x=face_x + 10, y=face_y + 25)
    neck.filled = 'True'
    neck.fill_color = 'purple'
    neck.color = 'purple'
    window.add(neck)


def body():
    body = GOval(face_height * 1.7, face_width * 1.2, x=face_x, y=face_y + face_height - 70)
    body.filled = 'True'
    body.fill_color = 'steelblue'
    body.color = 'steelblue'
    body1 = GRect(face_height * 1.7, face_width * 1.2, x=face_x, y=face_y + face_width*1.2)
    body1.filled = 'True'
    body1.fill_color = 'white'
    body1.color = 'white'
    window.add(body)
    window.add(body1)


def skyline():
    skyline = GRect(5, 30, x=face_x + 90, y=face_y - 20)
    skyline.filled = 'True'
    skyline.fill_color = 'yellowgreen'
    skyline.color = 'yellowgreen'
    skyline1 = GOval(10, 10, x=face_x + 87.5, y=face_y - 30)
    skyline1.filled = 'True'
    skyline1.fill_color = 'yellowgreen'
    skyline1.color = 'yellowgreen'
    window.add(skyline)
    window.add(skyline1)


def belt():
    belt = GPolygon()
    belt.add_vertex((face_width * 2, 220))
    belt.add_vertex((face_width * 2 + 5, 220 + 20))
    belt.add_vertex((face_width * 2 + face_height * 1.7-5, 220 + 20))
    belt.add_vertex((face_width * 2 + face_height * 1.7, 220))
    belt.filled = 'True'
    belt.fill_color = 'black'
    belt.color = 'black'
    belthead = GRect(50, 30, x=(face_width * 2) + (face_height * 1.7-5)/2 - 25, y=215)
    belthead.filled = True
    belthead.fill_color = 'blue'
    belthead.color = 'blue'
    window.add(belt)
    window.add(belthead)


def ear():
    # right ear
    r_ear = GPolygon()
    r_ear.add_vertex((500, 100))
    r_ear.add_vertex((540, 120))
    r_ear.add_vertex((550, 50))
    r_ear.filled = 'True'
    r_ear.fill_color = 'yellowgreen'
    r_ear.color = 'yellowgreen'
    window.add(r_ear)
    # left ear
    l_ear = GPolygon()
    l_ear.add_vertex((400, 100))
    l_ear.add_vertex((360, 120))
    l_ear.add_vertex((350, 50))
    l_ear.filled = 'True'
    l_ear.fill_color = 'yellowgreen'
    l_ear.color = 'yellowgreen'
    window.add(l_ear)


def eye():
    # because this character has three eyes
    eye_size = 25
    eyebal_size = 10
    # the middle eye
    eye_middle = GOval(eye_size, eye_size, x=face_x + ((face_width - eye_size) / 2), y=face_y + 10)
    eye_middle.filled = 'True'
    eye_middle.fill_color = 'white'
    eye_middle.color = 'white'
    eyebal_middle = GOval(eyebal_size, eyebal_size, x=eye_middle.x + ((eye_size - eyebal_size)/2), y=eye_middle.y + ((eye_size - eyebal_size) / 2))
    eyebal_middle.filled = 'True'
    eyebal_middle.fill_color = 'black'
    eyebal_middle.color = 'black'
    window.add(eye_middle)
    window.add(eyebal_middle)
    # the left eye
    eye_left = GOval(eye_size, eye_size, x=eye_middle.x+50, y=eye_middle.y+10)
    eye_left.filled = 'True'
    eye_left.fill_color = 'white'
    eye_left.color = 'white'
    eyebal_left = GOval(eyebal_size, eyebal_size, x=eye_left.x+((eye_size-eyebal_size)/2), y=eye_left.y+((eye_size-eyebal_size)/2))
    eyebal_left.filled = 'True'
    eyebal_left.fill_color = 'black'
    eyebal_left.color = 'black'
    window.add(eye_left)
    window.add(eyebal_left)
    # the right eye
    eye_right = GOval(eye_size, eye_size, x=eye_middle.x-50, y=eye_middle.y+10)
    eye_right.filled = 'True'
    eye_right.fill_color = 'white'
    eye_right.color = 'white'
    eyebal_right = GOval(eyebal_size, eyebal_size, x=eye_right.x+((eye_size-eyebal_size)/2), y=eye_right.y+((eye_size-eyebal_size)/2))
    eyebal_right.filled = 'True'
    eyebal_right.fill_color = 'black'
    eyebal_right.color = 'black'
    window.add(eye_right)
    window.add(eyebal_right)


def mouth():
    eye_size = 25
    mouth1_width = 130
    mouth1_height = 40
    mouth1 = GOval(mouth1_width, mouth1_height, x=face_x+((face_width-mouth1_width)/2), y=face_y+(face_height/2.2))
    mouth1.filled = 'True'
    mouth1.fill_color = 'black'
    mouth1.color = 'black'
    window.add(mouth1)
    mouth2 = GOval(mouth1_width, mouth1_height, x=face_x+((face_width-mouth1_width)/2), y=face_y+(face_height/2.2)-2)
    mouth2.filled = 'True'
    mouth2.fill_color = 'yellowgreen'
    mouth2.color = 'yellowgreen'
    window.add(mouth2)
    mouth_middle = GOval(eye_size*0.8, eye_size*0.8, x=mouth1.x+((mouth1_width-eye_size*0.8)/2), y=mouth1.y+mouth1_height-eye_size*0.8/2)
    mouth_middle.filled = 'True'
    mouth_middle.fill_color = 'black'
    mouth_middle.color = 'black'
    window.add(mouth_middle)
    mouth_left = GOval(eye_size*0.1, eye_size*0.1, x=mouth1.x-mouth1.x*0.005, y=mouth1.y+mouth1.y*0.2)
    mouth_left.filled = 'True'
    mouth_left.fill_color = 'black'
    mouth_left.color = 'black'
    window.add(mouth_left)
    mouth_right = GOval(eye_size*0.1, eye_size*0.1, x=mouth1.x-mouth1.x*0.005+mouth1_width, y=mouth1.y+mouth1.y*0.2)
    mouth_right.filled = 'True'
    mouth_right.fill_color = 'black'
    mouth_right.color = 'black'
    window.add(mouth_right)


def foot():
    # left foot
    left_foot = GOval(face_width * 0.45, face_height * 0.2, x=face_x + 15, y=face_y + face_width * 1.15)
    left_foot.filled = 'True'
    left_foot.fill_color = 'blue'
    left_foot.color = 'blue'
    window.add(left_foot)
    # right foot
    right_foot = GOval(face_width * 0.45, face_height * 0.2, x=face_x + face_width * 0.4 + 20, y=face_y + face_width * 1.15)
    right_foot.filled = 'True'
    right_foot.fill_color = 'blue'
    right_foot.color = 'blue'
    window.add(right_foot)


def hand():
    h_start_x = face_x + 90
    h_start_y = face_y + 125
    # left hand with three fingers
    l_hand = GPolygon()
    l_hand.add_vertex((h_start_x, h_start_y))
    l_hand.add_vertex((h_start_x - 120, h_start_y - 30))
    l_hand.add_vertex((h_start_x - 130, h_start_y))
    l_hand.filled = 'True'
    l_hand.fill_color = 'steelblue'
    l_hand.color = 'steelblue'
    # three fingers
    l_hand_finger = GPolygon()
    l_hand_finger.add_vertex((h_start_x - 120, h_start_y - 30))
    l_hand_finger.add_vertex((h_start_x - 120 - 20, h_start_y - 30 - 15))
    l_hand_finger.add_vertex((h_start_x - 120 - 20, h_start_y - 30 - 15 + 5))
    l_hand_finger.add_vertex((h_start_x - 120 - 20 + 5, h_start_y - 30 - 15 + 15))
    l_hand_finger.add_vertex((h_start_x - 120 - 20 + 5 - 30, h_start_y - 30 - 15 + 15))
    l_hand_finger.add_vertex((h_start_x - 120 - 20 + 5 - 30 - 2, h_start_y - 30 - 15 + 15 + 5))
    l_hand_finger.add_vertex((h_start_x - 120 - 20 + 5 - 20 + 10, h_start_y - 30 - 15 + 15 + 5 + 5))
    l_hand_finger.add_vertex((h_start_x - 120 - 20 + 5 - 20 + 10 - 20, h_start_y - 30 - 15 + 15 + 5 + 10))
    l_hand_finger.add_vertex((h_start_x - 120 - 20 + 5 - 20 + 10 - 20, h_start_y - 30 - 15 + 15 + 5 + 10 + 5))
    l_hand_finger.add_vertex((h_start_x - 130, h_start_y))
    l_hand_finger.filled = 'True'
    l_hand_finger.fill_color = 'blue'
    l_hand_finger.color = 'blue'
    window.add(l_hand)
    window.add(l_hand_finger)
    # right hand with walkie-talkie
    r_hand = GPolygon()
    h_start_x1 = face_x + 100
    h_start_y1 = face_y + 125
    r_hand.add_vertex((h_start_x1, h_start_y1))
    r_hand.add_vertex((h_start_x1+120, h_start_y1 - 30))
    r_hand.add_vertex((h_start_x1+130, h_start_y1))
    r_hand.filled = 'True'
    r_hand.fill_color = 'steelblue'
    r_hand.color = 'steelblue'
    window.add(r_hand)
    # walkie-talkie
    r_hand_finger = GRect(40, 50, x=h_start_x1 + 120, y=h_start_y1 - 40)
    r_hand_finger.filled = True
    r_hand_finger.fill_color = 'black'
    r_hand_finger.color = 'black'
    rect1 = GRect(10, 5, x=h_start_x1+120 + 5 + 5, y=h_start_y1 - 45)
    rect1.filled = True
    rect1.fill_color = 'black'
    rect1.color = 'black'
    rect2 = GRect(5, 50, x=h_start_x1 + 120 + 5 + 7, y=h_start_y1 - 60)
    rect2.filled = True
    rect2.fill_color = 'black'
    rect2.color = 'black'
    rect3 = GRect(30, 15, x=h_start_x1 + 120 + 5, y=h_start_y1-40 + 5)
    rect3.filled = True
    rect3.fill_color = 'grey'
    rect3.color = 'grey'
    circle1 = GOval(5, 5, x=h_start_x1 + 120 + 5, y=h_start_y1 - 40 + 5 + 20)
    circle1.filled = True
    circle1.fill_color = 'yellow'
    circle1.color = 'yellow'
    circle2 = GOval(5, 5, x=h_start_x1 + 120 + 5 + 25, y=h_start_y1 - 40 + 5 + 20)
    circle2.filled = True
    circle2.fill_color = 'yellow'
    circle2.color = 'yellow'
    circle3 = GOval(20, 20, x=h_start_x1 + 120 + 5 + 5, y=h_start_y1 - 40 + 5 + 23)
    circle3.filled = True
    circle3.fill_color = 'yellow'
    circle3.color = 'yellow'
    line1 = GLine(h_start_x1 + 120 + 5 + 5, h_start_y1-40 + 5 + 33, h_start_x1 + 120 + 5 + 25, h_start_y1 - 40 + 5 + 33)
    line2 = GLine(h_start_x1 + 120 + 5 + 7, h_start_y1-40 + 5 + 28, h_start_x1 + 120 + 7 + 21, h_start_y1 - 40 + 5 + 28)
    line3 = GLine(h_start_x1 + 120 + 5 + 7, h_start_y1-40 + 5 + 38, h_start_x1 + 120 + 7 + 21, h_start_y1 - 40 + 5 + 38)
    window.add(r_hand_finger)
    window.add(rect1)
    window.add(rect2)
    window.add(rect3)
    window.add(circle1)
    window.add(circle2)
    window.add(circle3)
    window.add(line1)
    window.add(line2)
    window.add(line3)


def bedge():
    bedge = GOval(25, 25, x=face_x + 140, y=face_y + 120)
    bedge.filled = 'True'
    bedge.fill_color = 'orange'
    bedge.color = 'orange'
    bedge1 = GOval(25, 5, x=face_x + 140, y=face_y + 129)
    bedge1.filled = 'True'
    bedge1.fill_color = 'orange'
    bedge1.color = 'orange'
    bedge2 = GOval(40, 8, x=face_x + 140-7.5, y=face_y + 130)
    bedge2.filled = 'True'
    bedge2.fill_color = 'yellow'
    bedge2.color = 'yellow'
    window.add(bedge)
    window.add(bedge2)
    window.add(bedge1)


def word():
    label = GLabel('Beeeeeeppppp!!!')
    label.font = 'Helvetica-60-bold-italic'
    label.color = 'orange'
    window.add(label, x=200, y=350)


if __name__ == '__main__':
    main()
