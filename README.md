# Q-learning을 이용한 틱택토 AI

틱택토하는 ai를 Q-learning으로 만들엇음.

## 작동 방식

1. 랜덤상대랑 좀 하면서 규칙좀 익힘
2. 자기 전 모델이랑 게임 함
   저거 게임 하면서 .pkl파일에 저장됨

## 파일 구조

```
tic-tac-toe/
├── main.py               # 학습 및 플레이를 실행하는 메인 스크립트
├── env.py                # 틱택토 게임 환경
├── agent.py              # QLearningAgent 클래스
├── train.py              # 학습용 함수
├── play.py               # AI와 대결하는 함수
├── q_tables/             # Q-테이블 저장 폴더
│   ├── q_table_random.pkl
│   └── q_table_selfplay.pkl
├── .gitignore            # Git 무시 파일
└── README.md             # 이 파일
```

## 실행 방법

main.py실행

```bash
python main.py
```

이렇게 하고 좀만 기다리면 학습됨.
그리고나서 콘솔에서 직접 게임도 가능.
