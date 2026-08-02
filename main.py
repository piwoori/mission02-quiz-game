from statistics import multimode
from quiz_game import QuizGame

def show_menu():
    print("==============================")
    print("       🫯나만의 퀴즈 게임🫯")
    print("==============================")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("==============================")


def main():
    game = QuizGame()

    while True:
        show_menu()

        menu = input("메뉴를 선택하세요: ").strip()

        if menu == "":
            print("입력값ㅇ; 없습니다. 1부터 5까지의 숫자를 입력해주세요.\n")
        elif menu == "1":
            game.play_quiz()
        elif menu == "2":
            game.add_quiz()
        elif menu == "3":
            game.show_quizzes()
        elif menu == "4":
            game.show_best_score()
        elif menu == "5":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다.")

        print()

if __name__ == "__main__":
    main()