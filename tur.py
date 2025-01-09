import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Hit It!")  # Sets the title of the window
wn.setup(width=600, height=600)

# Create the goal (red circle)
goal = turtle.Turtle()
goal.shape("circle")
goal.color("red")
goal.penup()
goal.speed(0)
goal.goto(random.randint(-250, 250), random.randint(-250, 250))

# Create the player (blue turtle)
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()
player.speed(0)

# Player movement functions
def move_up():
    y = player.ycor()
    if y < 280:
        player.sety(y + 20)

def move_down():
    y = player.ycor()
    if y > -280:
        player.sety(y - 20)

def move_left():
    x = player.xcor()
    if x > -280:
        player.setx(x - 20)

def move_right():
    x = player.xcor()
    if x < 280:
        player.setx(x + 20)

# Key bindings
wn.listen()
wn.onkey(move_up, "w")
wn.onkey(move_down, "s")
wn.onkey(move_left, "a")
wn.onkey(move_right, "d")

# Create enemies (black squares)
enemies = []
for i in range(5):
    enemy = turtle.Turtle()
    enemy.shape("square")
    enemy.color("black")
    enemy.penup()
    enemy.speed(0)
    enemy.goto(random.randint(-250, 250), random.randint(-250, 250))
    enemy.dx = random.choice([-3, 3])
    enemy.dy = random.choice([-3, 3])
    enemies.append(enemy)

# Game variables
goal_count = 0
hit_count = 0

# Display counters
counter = turtle.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(0, 260)
counter.write(f"Goals: {goal_count} | Hits: {hit_count}", align="center", font=("Arial", 16, "normal"))

# Update counters
def update_counters():
    counter.clear()
    counter.write(f"Goals: {goal_count} | Hits: {hit_count}", align="center", font=("Arial", 16, "normal"))

# Main game loop
while True:
    wn.update()

    # Move enemies
    for enemy in enemies:
        enemy.setx(enemy.xcor() + enemy.dx)
        enemy.sety(enemy.ycor() + enemy.dy)

        # Reverse direction if hitting screen edge
        if enemy.xcor() > 280 or enemy.xcor() < -280:
            enemy.dx *= -1
        if enemy.ycor() > 280 or enemy.ycor() < -280:
            enemy.dy *= -1

        # Check for collision with player
        if player.distance(enemy) < 20:
            hit_count += 1
            update_counters()
            player.goto(0, 0)  # Reset player position

            # End game if too many hits
            if hit_count >= 6:
                counter.clear()
                counter.write("Game Over!", align="center", font=("Arial", 24, "bold"))
                wn.update()
                wn.mainloop()

    # Check for collision with the goal
    if player.distance(goal) < 20:
        goal_count += 1
        update_counters()
        goal.goto(random.randint(-250, 250), random.randint(-250, 250))

        # End game if player reaches 3 goals
        if goal_count >= 3:
            counter.clear()
            counter.write("You Win!", align="center", font=("Arial", 24, "bold"))
            wn.update()
            wn.mainloop()
