from quiz_game import QuizGame

game.show_menu()

def main():
    game = QuizGame()

    try:
        while True:
            show_menu()

            menu = input("메뉴를 선택하세요: ").strip()

            if menu == "":
                print("입력값이 없습니다. 1부터 5까지의 숫자를 입력해주세요.\n")
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
                print("잘못된 입력입니다. 1부터 5까지의 숫자를 입력해주세요.\n")

    except (KeyboardInterrupt, EOFError):
        game.save_data()
        print("\n입력이 중단되었습니다. 데이터를 저장하고 프로그램을 종료합니다.")

if __name__ == "__main__":
    main()