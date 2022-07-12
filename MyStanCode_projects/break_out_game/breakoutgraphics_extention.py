"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Height of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, lives, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height, x=(self.window.width - paddle_width) / 2,
                            y=(self.window.height - paddle_offset - paddle_height))
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2, x=(self.window.width - ball_radius * 2) / 2,
                          y=(self.window.height - ball_radius * 2) / 2)
        self.ball.filled = True
        self.window.add(self.ball)

        # Create a instance for ball radius.
        self.b = ball_radius * 2

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        self.is_start = False  # Ｍouse start switch
        onmouseclicked(self.ball_move)
        onmousemoved(self.move_paddle)

        # Count the number of bricks
        self.bricks = brick_rows * brick_cols

        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(width=brick_width, height=brick_height,
                                   x=0 + (brick_spacing + brick_width) * j,
                                   y=brick_offset + (brick_spacing + brick_height) * i)
                self.brick.filled = True
                if i % brick_cols <= 1:
                    self.brick.fill_color = 'red'
                    self.brick.color = 'red'
                elif i % brick_cols <= 3:
                    self.brick.fill_color = 'orange'
                    self.brick.color = 'orange'
                elif i % brick_cols <= 5:
                    self.brick.fill_color = 'yellow'
                    self.brick.color = 'yellow'
                elif i % brick_cols <= 7:
                    self.brick.fill_color = 'green'
                    self.brick.color = 'green'
                elif i % brick_cols <= 9:
                    self.brick.fill_color = 'blue'
                    self.brick.color = 'blue'
                self.window.add(self.brick)

        # Show lives
        for i in range(lives + 1):
            self.ball_lives_x = self.window.width - (self.b * 0.5 + BRICK_SPACING) * i
            self.ball_lives_y = self.window.height - self.b
            self.ball_lives = GOval(self.b * 2 * 0.3, self.b * 2 * 0.3, x=self.ball_lives_x, y=self.ball_lives_y)
            self.ball_lives.filled = True
            self.window.add(self.ball_lives)

        self.score = 0
        self.score_label = GLabel('Score: ' + str(self.score))
        self.score_label.font = 'Helvetica-20-bold-italic'
        self.window.add(self.score_label, x=5, y=self.score_label.height+10)

    def move_paddle(self, event):
        """
        Make the paddle moveable.
        """
        if event.x <= 0 + self.paddle.width:  # left border
            paddle_x = 0
        elif event.x >= self.window.width - self.paddle.width:  # Right border
            paddle_x = self.window.width - self.paddle.width
        else:
            paddle_x = event.x - self.paddle.width / 2
        self.window.add(self.paddle, x=paddle_x, y=self.paddle.y)

    def ball_move(self, event):
        """
        Switches to move the ball and set the initial speed of the ball.
        """
        self.is_start = True
        self.set_ball_velocity()

    def set_ball_velocity(self):
        """
        Initial speed of the ball.
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def get_ball_x(self):
        """
        Get the speed of the X axis.
        """
        return self.__dx

    def get_ball_y(self):
        """
        Get the speed of the Y axis.
        """
        return self.__dy

    def brick_clear(self, y):
        """
        Set the bounce condition of the ball.
        :parm y: speed of the Y axis
        :return y: speed of the Y axis
        """
        for i in [0, self.b]:
            for j in [0, self.b]:  # Check the four vertices of the ball
                obj = self.window.get_object_at(self.ball.x + i, self.ball.y + j)  # Check for objects.
                if obj is not None and obj is not self.score_label:  # If an object is detected.
                    if obj is not self.paddle:  # Judgment is a brick.
                        self.window.remove(obj)
                        y = -y
                        self.bricks -= 1  # Count the number of bricks eliminated.
                        self.score += 1  # Record the score.
                        self.score_label.text = 'Score: ' + str(self.score)
                    # Judging that it is a paddle and hitting it from above.
                    elif obj is self.paddle and (self.ball.y + j) - self.paddle.y < INITIAL_Y_SPEED:
                        y = -y
                    # Judging that it is a board and hitting it from the side.
                    elif obj is self.paddle and (self.ball.y + j) - self.paddle.y >= INITIAL_Y_SPEED:
                        y = y
                    # Judging that it is a ball lives object.
                    elif (self.ball.x + i) >= self.ball_lives_x and (self.ball.y + j) >= self.ball_lives_y:
                        y = y
                    return y
                else:  # No bounce.
                    y = y
        return y

    def reset_ball(self):
        """
        reposition the ball, return the ball to the starting point.
        """
        self.ball.x = (self.window.width - self.b) / 2
        self.ball.y = (self.window.height - self.b) / 2

    def kill_ball(self, blives):
        """
        Count the number of games remaining
        :parm: blives: number of games remaining
        """
        lives_x = (self.window.width - ((self.b * 0.5 + BRICK_SPACING) * (blives + 1))) + (self.b * 0.3)
        lives_y = self.window.height - self.b + (self.b * 0.3)
        ballives = self.window.get_object_at(lives_x, lives_y)
        self.window.remove(ballives)

    def word(self):
        """
        Tell USER the game result.
        """
        if self.bricks == 0:
            label = GLabel('YOU WINNN!!!')
            label.font = 'Helvetica-40-bold-italic'
            label.color = 'orange'
            self.window.add(label, x=1, y=self.window.height / 2)
        else:
            label = GLabel('GameOver LOSER!!!')
            label.font = 'Helvetica-40-bold-italic'
            label.color = 'black'
            self.window.add(label, x=1, y=self.window.height/2)







