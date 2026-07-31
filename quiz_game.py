from quiz import Quiz

class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0

        self.add_default_quizzes()

    def add_default_quizzes(self):
        quiz1 = Quiz("대한민국의 수도는?", "서울")
        quiz2 = Quiz("2 + 3은?", "5")
        quiz3 = Quiz("파이썬 파일의 확장자는?", "py")

        self.quizzes.append(quiz1)
        self.quizzes.append(quiz2)
        self.quizzes.append(quiz3)

    def show_quizzes(self):
        print("\n===== 퀴즈 목록 =====")

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"{index}. {quiz.question}")

        print("====================\n")