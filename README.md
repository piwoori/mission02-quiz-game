# 🫯 나만의 퀴즈 게임

Python 객체지향 프로그래밍(OOP)과 JSON 파일 입출력, Git 브랜치 전략을 학습하기 위해 제작한 콘솔 기반 객관식 퀴즈 게임입니다.

사용자는 등록된 퀴즈를 풀고, 새로운 퀴즈를 추가하며, 퀴즈 목록과 최고 점수를 확인할 수 있습니다.
모든 퀴즈와 최고 점수는 `state.json` 파일에 저장되어 프로그램을 종료한 후에도 유지됩니다.

## 퀴즈 주제 선정 이유

개발을 학습하면서 자주 접하는 Python, Java, Git 등의 내용을 문제로 구성하였습니.

단순히 퀴즈를 푸는 프로그램이 아니라 학습 내용을 복습할 수 있도록 개발 관련 주제를 선택하였다.

---

# 개발 환경

- Python 3.11.8
- IntelliJ IDEA
- Git
- SourceTree
- macOS

---

# 실행 방법

프로젝트 폴더에서 아래 명령어를 실행합니다.

```bash
python3 main.py
```

---

# 주요 기능

## 1. 메인 메뉴

사용자가 원하는 기능을 선택할 수 있는 메인 메뉴를 제공합니다.

- 퀴즈 풀기
- 퀴즈 추가
- 퀴즈 목록
- 점수 확인
- 종료

![메인 메뉴](docs/screenshots/main-menu.png)

---

## 2. 퀴즈 풀기

등록된 모든 퀴즈를 객관식(4지선다)으로 풀이할 수 있습니다.

- 선택지 출력
- 정답/오답 판별
- 최종 점수 계산
- 최고 점수 갱신

![퀴즈 풀기](docs/screenshots/play-quiz.png)

### 결과 화면

![결과](docs/screenshots/quiz-result.png)

---

## 3. 퀴즈 추가

사용자가 직접 새로운 퀴즈를 등록할 수 있습니다.

입력 항목

- 문제
- 선택지 4개
- 정답 번호

추가된 퀴즈는 JSON 파일에 즉시 저장됩니다.

![퀴즈 추가](docs/screenshots/add-quiz.png)

---

## 4. 퀴즈 목록 조회

현재 등록된 모든 퀴즈를 확인할 수 있습니다.

![퀴즈 목록](docs/screenshots/quiz-list.png)

---

## 5. 최고 점수 조회

현재 저장되어 있는 최고 점수를 확인할 수 있습니다.

![최고 점수](docs/screenshots/best-score.png)

---

## 6. 데이터 저장

퀴즈와 최고 점수는 `state.json` 파일에 저장됩니다.

프로그램을 다시 실행해도 기존 데이터가 유지됩니다.

![state.json](docs/screenshots/state-json.png)

---

## 7. 예외 처리

사용자의 잘못된 입력을 처리하도록 구현했습니다.

- 메뉴 범위를 벗어난 입력
- 숫자가 아닌 메뉴 입력
- 빈 입력
- 숫자가 아닌 정답 입력
- 1~4 범위를 벗어난 정답 번호
- JSON 파일이 없는 경우
- JSON 파일이 손상된 경우(`JSONDecodeError`)
- `KeyboardInterrupt(Ctrl+C)`
- `EOFError`

예외 처리 예시

![예외 처리](docs/screenshots/invalid-answer.png)

---

# 프로젝트 구조

```text
mission02-quiz-game
│
├── docs/
│   └── screenshots/
│
├── main.py
├── quiz.py
├── quiz_game.py
├── state.json
├── README.md
└── .gitignore
```

| 파일 | 설명 |
|------|------|
| main.py | 프로그램 시작 및 메뉴 제어 |
| quiz.py | Quiz 클래스 |
| quiz_game.py | 게임 로직 관리 |
| state.json | 퀴즈 및 최고 점수 저장 |
| docs/screenshots | README 이미지 |

---

# 클래스 구조

## Quiz

객관식 문제 하나를 표현하는 클래스입니다.

```text
Quiz
├── question
├── choices
└── answer
```

| 변수 | 설명 |
|------|------|
| question | 문제 |
| choices | 선택지 리스트 |
| answer | 정답 번호 |

---

## QuizGame

게임 전체를 관리하는 클래스입니다.

```text
QuizGame
├── quizzes
├── best_score
├── file_name
│
├── play_quiz()
├── add_quiz()
├── add_default_quizzes()
├── show_quizzes()
├── show_best_score()
├── save_data()
└── load_data()
```

---

# JSON 저장 구조

```json
{
    "best_score": 5,
    "quizzes": [
        {
            "question": "대한민국의 수도는?",
            "choices": [
                "부산",
                "서울",
                "인천",
                "대전"
            ],
            "answer": 2
        }
    ]
}
```

| 항목 | 설명 |
|------|------|
| best_score | 최고 점수 |
| quizzes | 퀴즈 목록 |
| question | 문제 |
| choices | 선택지 |
| answer | 정답 번호 |

---

# Git 브랜치 전략

기능별 브랜치를 생성하여 개발한 후 `main` 브랜치에 병합했습니다.

```text
main
│
└── feature/json
      │
      ├── JSON 저장
      ├── JSON 불러오기
      ├── JSON 예외 처리
      └── 객관식 구조 리팩터링
```

---

# 트러블슈팅

## 1. 서로 다른 환경에서 JSON 파일이 달라지는 문제

두 대의 Mac에서 프로젝트를 작업하면서 각각 다른 JSON 파일이 생성되어
추가한 퀴즈가 서로 다르게 보이는 문제가 발생했습니다.

### 해결

- Git으로 `state.json` 관리
- 작업 전 Pull
- 작업 후 Commit & Push

---

## 2. JSON 파일 위치 문제

상대 경로만 사용할 경우 실행 위치에 따라 JSON 파일이 다른 위치에 생성되는 문제가 있었습니다.

### 해결

`pathlib.Path`를 사용하여 프로젝트 기준 절대 경로를 생성했습니다.

```python
project_root = Path(__file__).resolve().parent
self.file_name = project_root / "state.json"
```

---

## 3. 손상된 JSON 파일

JSON 형식이 잘못되면 프로그램이 종료되는 문제가 있었습니다.

### 해결

`json.JSONDecodeError`를 처리하여

- 기본 퀴즈 복구
- 최고 점수 초기화
- JSON 파일 재생성

하도록 구현했습니다.

---

# 배운 점

이번 프로젝트를 통해 다음 내용을 학습했습니다.

- Python 클래스와 객체지향 프로그래밍
- 생성자(`__init__`)
- 리스트와 반복문
- `enumerate()`
- JSON 저장 및 불러오기
- 파일 입출력
- 예외 처리
- `pathlib`을 이용한 파일 경로 관리
- Git 브랜치 생성 및 병합
- SourceTree를 활용한 Git 관리
