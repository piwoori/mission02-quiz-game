from statistics import multimode


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
    while True:
        show_menu()
        menu = input("메뉴를 선택하세요: ")

        if menu == "1":
            print("퀴즈 풀기를 선택했습니다.")
        elif menu == "2":
            print("퀴즈 추가를 선택했습니다.")
        elif menu == "3":
            print("퀴즈 목록을 추가했습니다.")
        elif menu == "4":
            print("점수 확인을 선택했습니다.")
        elif menu == "5":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다.")

        print()

if __name__ == "__main__":
    main()