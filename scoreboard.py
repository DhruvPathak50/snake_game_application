from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.pu()
        self.hideturtle()
        self.sety(250)
        self.show_score()



    def show_score(self):
        self.clear()
        self.write(f"Score = {self.current_score} High Score : {self.high_score}", align= ALIGNMENT, font= FONT)

    # def game_over(self):
    #     self.sety(0)
    #     self.write("GAME OVER.", align=ALIGNMENT, font=FONT)
    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("high_score.txt", mode = "w") as file:
                file.write(f"{self.high_score}")
        self.current_score = 0
        self.show_score()


    def update_score(self):
        self.current_score += 1
        self.show_score()