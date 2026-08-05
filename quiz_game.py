import json
from pathlib import Path
from quiz import Quiz


class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.has_played = False
        project_root = Path(__file__).resolve().parent
        self.file_name = project_root / "state.json"

        self.load_data()

    def show_menu(self):
        print("==============================")
        print("       🫯나만의 퀴즈 게임🫯")
        print("==============================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("==============================")

    def add_quiz(self):
        question = self.input_not_empty(
            "추가할 퀴즈의 질문을 입력하세요: "
        )

        choices = []

        for index in range(1, 5):
            choice = self.input_not_empty(
                f"{index}번 선택지를 입력하세요: "
            )
            choices.append(choice)

        while True:
            answer_input = input(
                "정답 번호를 입력하세요 (1-4): "
            ).strip()

            if answer_input == "":
                print("입력값이 없습니다.")
                continue

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

    def input_not_empty(self, message):
        while True:
            value = input(message).strip()

            if value:
                return value

            print("빈 값은 입력할 수 없습니다.")

    def add_default_quizzes(self):
        quiz1 = Quiz(
            "Python에서 여러 값을 순서대로 저장하는 자료형은?",
            ["int", "list", "bool", "str"],
            2
        )

        quiz2 = Quiz(
            "Git에서 현재 변경 상태를 확인하는 명령어는?",
            ["git status", "git push", "git clone", "git merge"],
            1
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
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다.")
            return

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
            quiz.display()

            while True:
                user_input = input(
                    "정답 번호를 입력하세요 (1-4): "
                ).strip()

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

            if quiz.check_answer(user_answer):
                score += 1
                print("정답입니다!")

            else:
                correct_choice = quiz.choices[quiz.answer - 1]

                print(
                    f"오답입니다. 정답은 "
                    f"{quiz.answer}번 {correct_choice}입니다."
                )

        print(
            f"\n총 {len(self.quizzes)}문제 중 "
            f"{score}문제를 맞혔습니다."
        )

        self.has_played = True

        if score > self.best_score:
            self.best_score = score
            print("새로운 최고 점수입니다!")

        self.save_data()

        print(f"최고 점수: {self.best_score}")

    def save_data(self):
        data = {
            "best_score": self.best_score,
            "has_played": self.has_played,
            "quizzes": []
        }

        for quiz in self.quizzes:
            quiz_data = {
                "question": quiz.question,
                "choices": quiz.choices,
                "answer": quiz.answer
            }

            data["quizzes"].append(quiz_data)

        try:
            with open(self.file_name, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

        except OSError as error:
            print(f"데이터를 저장하지 못했습니다: {error}")

    def load_data(self):
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                data = json.load(file)

            self.best_score = data["best_score"]
            self.has_played = data.get("has_played", False)
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
            self.save_data()

        except (json.JSONDecodeError, KeyError, TypeError, OSError):
            print("저장된 파일을 읽을 수 없어 "
                  "기본 퀴즈로 복구합니다.")
            self.quizzes = []
            self.best_score = 0
            self.has_played = False
            self.add_default_quizzes()
            self.save_data()

    def show_best_score(self):
        if not self.has_played:
            print("\n아직 퀴즈를 풀지 않았습니다.\n")
            return

        print(f"\n현재 최고 점수는 {self.best_score}점입니다.\n")