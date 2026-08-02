import json
from pathlib import Path
from quiz import Quiz

class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        project_root = Path(__file__).resolve().parent
        self.file_name = project_root / "state.json"

        self.load_data()

    def add_quiz(self):
        question = input("추가할 퀴즈의 질문을 입력하세요: ")
        answer = input("정답을 입력하세요: ")

        new_quiz = Quiz(question, answer)
        self.quizzes.append(new_quiz)

        self.save_data()

        print("퀴즈가 추가되었습니다.")

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
            self.save_data()
            print("새로운 최고 점수입니다!")

        print(f"최고 점수: {self.best_score}")

    def save_data(self):
        data = {
            "best_score": self.best_score,
            "quizzes": []
        }

        for quiz in self.quizzes:
            quiz_data = {
                "question": quiz.question,
                "answer": quiz.answer
            }

            data["quizzes"].append(quiz_data)

        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load_data(self):
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                data = json.load(file)

            self.best_score = data["best_score"]
            self.quizzes = []

            for quiz_data in data["quizzes"]:
                quiz = Quiz(
                    quiz_data["question"],
                    quiz_data["answer"]
                )
                self.quizzes.append(quiz)

            print("저장된 데이터를 불러왔습니다.")

        except FileNotFoundError:
            print("저장된 파일이 없어 기본 퀴즈를 사용합니다.")
            self.add_default_quizzes()

        except json.JSONDecodeError:
            print("저장된 파일이 없어 기본 퀴즈로 복구합니다.")
            self.quizzes = []
            self.best_score = 0
            self.add_default_quizzes()
            self.save_data()

    def show_best_score(self):
        print(f"\n현재 최고 점수는 {self.best_score}점입니다.\n")