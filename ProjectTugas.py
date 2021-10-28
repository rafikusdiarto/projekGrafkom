from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h= 500,500

# player
gerak_x = 0
gerak_y = 0

# obstacles
posisiX = 0
posisiY = 0

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-500.0, 500.0, -500.0, 500.0)

def obstacles():
    glPushMatrix()
    glBegin(GL_POLYGON)
    glColor3f(1.5, 0.5, 0.5)
    glVertex2f(100, 100)
    glVertex2f(130, 100)
    glVertex2f(130, 130)
    glVertex2f(100, 130)
    glEnd()
    glPopMatrix()

def player():
    glPushMatrix()
    global gerak_x, gerak_y
    glBegin(GL_POLYGON)
    glColor3f(1.5, 0.5, 0.5)
    glVertex2f(-30 + gerak_x, -30 + gerak_y)
    # Kanan Atas
    glVertex2f(30 + gerak_x, -30 + gerak_y)
    # Kanan Bawah
    glVertex2f(30 + gerak_x, 30 + gerak_y)
    # Kiri Bawah
    glVertex2f(-30 + gerak_x, 30 + gerak_y)

    # batas pinggir
    if gerak_x <= -470:
        gerak_x = -470
    elif gerak_x >= 470:
        gerak_x = 470
    elif gerak_y <= -470:
        gerak_y = -470
    elif gerak_y >= 470:
        gerak_y = 470

    # batas pojok
    if gerak_x == -470 and gerak_y >= 470:
        gerak_x = -470
        gerak_y = 470
    elif gerak_x == 470 and gerak_y >= 470:
        gerak_x = 470
        gerak_y = 470
    elif gerak_x == 470 and gerak_y <= -470:
        gerak_x = 470
        gerak_y = -470
    elif gerak_x == -470 and gerak_y <= -470:
        gerak_x = -470
        gerak_y = -470
    glEnd()
    glPopMatrix()

def input_keyboard(key,x,y):
    global gerak_x, gerak_y

    # Untuk mengubah posisi kotak
    if key == GLUT_KEY_UP:
        gerak_y += 20
        print("Tombol Atas ditekan ", "x : ", gerak_x, " y : ", gerak_y)
    elif key == GLUT_KEY_DOWN:
        gerak_y -= 20
        print("Tombol Bawah ditekan ", "x : ", gerak_x, " y : ", gerak_y)
    elif key == GLUT_KEY_RIGHT:
        gerak_x += 20
        print("Tombol Kanan ditekan ", "x : ", gerak_x, " y : ", gerak_y)
    elif key == GLUT_KEY_LEFT:
        gerak_x -= 20
        print("Tombol Kiri ditekan ", "x : ", gerak_x, " y : ", gerak_y)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    player()
    glPopMatrix()
    obstacles()
    glFlush()

def update(value):
    glutPostRedisplay()
    glutTimerFunc(10,update,10)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Eveng Handling Keyboard & Mouse")
    glutDisplayFunc(display)
    glutSpecialFunc(input_keyboard)
    glutTimerFunc(10, update, 0)
    init()
    glutMainLoop()

main()