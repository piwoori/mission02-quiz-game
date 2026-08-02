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
        question = input("추가할 퀴즈의 질문을 입력하세요: ").strip()

        choices = []

        for index in range(1, 5):
            choice = input(f"{index}번 선택지를 입력하세요: ").strip()
            choices.append(choice)

        while True:
            answer_input = input("정답 번호를 입력하세요 (1-4): ").strip()

            try:
                answer = int(answer_input)
            except ValueError:
                print("숫자를 입력해주세요.")
                continue

            if answer < 1 or answer > 4:
                print("1부터 4까지의 숫자를 입력해주세요.")
                continue

            break

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)

        self.save_data()

        print("퀴즈가 추가되었습니다.")

    def add_default_quizzes(self):
        quiz1 = Quiz(
            "대한민국의 수도는?",
            ["부산", "서울", "인천", "대전"],
            2
        )
        quiz2 = Quiz(
            "2 + 3의 결과는?",
            ["4", "5", "6", "7"],
            2
        )

        quiz3 = Quiz(
            "파이썬 파일의 확장자는?",
            [".java", ".html", ".py", ".css"],
            3
        )

        quiz4 = Quiz(
            "Java에서 클래스를 선언할 때 사용하는 키워드는?",
            ["class", "new", "import", "static"],
            1
        )

        quiz5 = Quiz(
            "Git에서 로컬 커밋을 원격 저장소로 업로드하는 명령어는?",
            ["pull", "clone", "push", "status"],
            3
        )

        self.quizzes.append(quiz1)
        self.quizzes.append(quiz2)
        self.quizzes.append(quiz3)
        self.quizzes.append(quiz4)
        self.quizzes.append(quiz5)

    def show_quizzes(self):
        print("\n===== 퀴즈 목록 =====")

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"{index}. {quiz.question}")

        print("====================\n")

    def play_quiz(self):

        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다.")
            return

        score = 0

        for quiz in self.quizzes:
            print(f"\n{quiz.question}")

            for index, choice in enumerate(quiz.choices, start=1):
                print(f"{index}. {choice}")

            while True:
                user_input = input("정답 번호를 입력하세요 (1-4): ").strip()

                if user_input == "":
                    print("입력값이 없습니다.")
                    continue

                try:
                    user_answer = int(user_input)
                except ValueError:
                    print("숫자를 입력해주세요.")
                    continue

                if user_answer < 1 or user_answer > 4:
                    print("1부터 4까지의 숫자를 입력해주세요.")
                    continue

                break

            if user_answer == quiz.answer:
                score += 1
                print("정답입니다!")
            else:
                correct_choice = quiz.choices[quiz.answer - 1]
                print(
                    f"오답입니다. 정답은 "
                    f"{quiz.answer}번 {correct_choice}입니다."
                )
        print(f"\n총 {len(self.quizzes)}문제 중 {score}문제를 맞혔습니다.")

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
                "choices": quiz.choices,
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
                    quiz_data["choices"],
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