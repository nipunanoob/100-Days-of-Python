from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=30, pady=30)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg='white', font=('Arial', 20))
        self.score_label.grid(row=0, column=1)

        self.question_canvas = Canvas(self.window, bg='white', height=250, width=300)
        self.question_text = self.question_canvas.create_text(
            150,
            125,
            width=280,
            text="CHECK UI",
            font=FONT,
            fill=THEME_COLOR
        )

        self.question_canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file='images/true.png')
        false_image = PhotoImage(file='images/false.png')

        self.true_button = Button(image=true_image, highlightthickness=0, command=self.user_selects_true)
        self.true_button.grid(row=2, column=1)

        self.false_button = Button(image=false_image, highlightthickness=0, command=self.user_selects_false)
        self.false_button.grid(row=2, column=0)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.question_canvas.configure(bg='white')
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=q_text)
            self.buttons_enabled()
        else:
            self.question_canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.buttons_disabled()

    def user_selects_true(self):
        self.buttons_disabled()
        self.give_feedback(self.quiz.check_answer("True"))

    def user_selects_false(self):
        self.buttons_disabled()
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.flash_green()
        else:
            self.flash_red()
        self.window.after(1000, self.get_next_question)

    def flash_green(self):
        self.question_canvas.configure(bg='green')

    def flash_red(self):
        self.question_canvas.configure(bg='red')

    def buttons_enabled(self):
        self.true_button.config(state='active')
        self.false_button.config(state='active')

    def buttons_disabled(self):
        self.true_button.config(state='disabled')
        self.false_button.config(state='disabled')




