from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.write(f"Score: {self.score}   HighScore: {self.high_score}", align="center", font=("Arial", 20, "normal"))
        self.hideturtle()

    def reset_score(self):
        self.clear()
        self.write(f"Score: {self.score}   HighScore: {self.high_score}", align="center", font=("Arial", 20, "normal"))
        if self.score > self.high_score:
            self.high_score = self.score
            self.goto(0, 0)
            self.clear()
            self.write(f"  GAME OVER!\nNew HighScore: {self.high_score}", align="center",
                       font=("Arial", 20, "normal"))
            with open("highscore.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        else:
            self.clear()
            self.goto(0, 0)
            self.write(f"GAME OVER!", align="center", font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}   HighScore: {self.high_score}", align="center", font=("Arial", 20, "normal"))
