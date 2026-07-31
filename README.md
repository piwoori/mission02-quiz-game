# 나만의 퀴즈 게임

## 프로젝트 소개

Python의 기본 문법과 객체지향 프로그래밍(OOP), 파일 입출력(JSON), Git 사용법을 학습하기 위해 제작한 콘솔 기반 퀴즈 게임입니다. :contentReference[oaicite:0]{index=0}

사용자는 퀴즈를 풀고, 새로운 퀴즈를 추가하며, 등록된 퀴즈 목록과 최고 점수를 확인할 수 있습니다. 프로그램을 종료한 후에도 퀴즈와 최고 점수는 파일에 저장되어 유지됩니다. :contentReference[oaicite:1]{index=1}

---

## 개발 환경

- Python 3.11.8
- IntelliJ IDEA
- Git
- SourceTree
- macOS

---

## 실행 방법

프로젝트 폴더에서 아래 명령어를 실행합니다.

```bash
python3 main.py
```

---

## 주요 기능

- [ ] 메인 메뉴
- [ ] 퀴즈 풀기
- [ ] 퀴즈 추가
- [ ] 퀴즈 목록 조회
- [ ] 최고 점수 확인
- [ ] 데이터 저장(JSON)
- [ ] 데이터 불러오기(JSON)
- [ ] 예외 처리

---

## 프로젝트 구조

```text
mission02-quiz-game/
├── main.py
├── quiz.py
├── quiz_game.py
├── state.json
├── README.md
├── .gitignore
└── docs/
    └── screenshots/
```

### 파일 설명

| 파일 | 설명 |
|------|------|
| main.py | 프로그램 시작 파일 |
| quiz.py | Quiz 클래스 |
| quiz_game.py | QuizGame 클래스 |
| state.json | 퀴즈 및 최고 점수 저장 파일 |
| README.md | 프로젝트 설명 |
| docs/screenshots | 실행 화면 스크린샷 |

---

## 데이터 저장

프로그램에서 사용하는 데이터는 `state.json` 파일에 저장됩니다.

저장 내용

- 등록된 퀴즈
- 최고 점수

예상 구조

```json
{
  "quizzes": [],
  "best_score": 0
}
```

---

## 개발 예정

- [ ] Quiz 클래스 구현
- [ ] QuizGame 클래스 구현
- [ ] 메뉴 구현
- [ ] 퀴즈 플레이 기능
- [ ] 퀴즈 추가 기능
- [ ] JSON 저장 및 불러오기
- [ ] 예외 처리
- [ ] README 보완

---

## Git Commit Convention

| 타입 | 설명 |
|------|------|
| Chore | 프로젝트 설정 |
| Feat | 기능 추가 |
| Refactor | 코드 개선 |
| Fix | 버그 수정 |
| Docs | README 수정 |