"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics_extention import BreakoutGraphics


FRAME_RATE = 1000 / 20  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    """
    Players need to use the mouse to control the position of the paddle,
    and bounce the falling ball to the upper brick area to destroy all bricks.
    The ball bounces off any object and boundary except the boundary
    at the bottom of the game window.
    """
    global NUM_LIVES
    graphics = BreakoutGraphics(NUM_LIVES)
    x = graphics.get_ball_x()
    y = graphics.get_ball_y()

    # Add the animation loop here!
    cnt = 0  # Another switch that controls ball activation.
    while True:

        if graphics.is_start and cnt == 0:  # Allows the ball to move.
            cnt += 1
            NUM_LIVES -= 1
            if NUM_LIVES == -1:  # Restart three times to end the game.
                break
            graphics.kill_ball(NUM_LIVES)

            x = graphics.get_ball_x()
            y = graphics.get_ball_y()

        graphics.ball.move(x, y)

        y = graphics.brick_clear(y)  # Rules for using ball bounces.
        graphics.ball.move(x, y)

        # When the ball goes beyond the side bounds of the window.
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width > graphics.window.width:
            x = -x

        # When the ball goes beyond the upper bounds of the window.
        if graphics.ball.y < 0 :
            y = -y

        # When the ball exceeds the border at the bottom of the window.
        if graphics.ball.y + graphics.ball.height > graphics.window.height:
            graphics.reset_ball()  # Return the ball to the starting point.
            cnt = 0
            x = 0
            y = 0
            graphics.is_start = False

        if graphics.bricks == 0:  # The player destroys all the bricks in the window and successfully passes the level!
            break

        pause(FRAME_RATE)
    graphics.word()


if __name__ == '__main__':
    main()
