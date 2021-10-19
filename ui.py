from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, highlightthickness=0)
        self.score_label.grid(row=0, column=1)
        self.question_area = Canvas(width=300, height=250, bg="white")
        self.question_area.grid(row=1, column=0, columnspan=2, pady=50)
        self.question = self.question_area.create_text(150, 125, text="Create question here", width=280, fill=THEME_COLOR, font=("Arial", 20, "italic"))
        true = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true, command=self.true_pressed)
        self.true_btn.grid(row=2, column=0)
        false = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false, command=self.false_pressed)
        self.false_btn.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.question_area.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.question_area.itemconfig(self.question, text=q_text)
        else:
            self.question_area.itemconfig(self.question, text="You've reached the end of the quiz.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.question_area.config(bg="green")
        else:
            self.question_area.config(bg="red")
        self.window.after(1000, self.get_next_question)
