from quiz import Quiz

class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0

        self.add_default_quizzes()

        self.best_score = 0

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

    def play_quiz(self):
        score = 0

        for quiz in self.quizzes:
            user_answer = input(f"{quiz.question} ")

            if user_answer == quiz.answer:
                score += 1
                print("정답입니다!")
            else:
                print(f"오답입니다. 정답은 {quiz.answer}입니다.")

            print()

        print(f"총 {score}문제를 맞혔습니다.")

        if score > self.best_score:
            self.best_score = score
            print("새로운 최고 점수입니다!")

        print(f"최고 점수: {self.best_score}")