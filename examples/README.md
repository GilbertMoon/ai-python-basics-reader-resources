# Examples

본문에서 설명하는 파이썬 예제 코드를 Chapter별로 관리합니다.

현재 구조는 `chapterXX` 형식을 사용합니다.

```text
examples/
├── chapter04/
├── chapter05/
├── chapter06/
├── ...
└── chapter24/
```

예:

```text
examples/chapter05/variable_basics.py
examples/chapter10/range_examples.py
examples/chapter23/expense_manager.py
examples/chapter24/final_report.py
```

운영 원칙:

- 본문의 핵심 코드와 예제 파일의 동작을 일치시킵니다.
- 예제는 해당 Chapter까지 배운 문법을 우선 사용합니다.
- 일부러 오류를 포함한 디버깅 예제는 파일 주석에서 의도적인 오류임을 표시합니다.
- CSV나 텍스트 데이터가 필요한 예제는 `data/chapterXX/`의 파일을 사용합니다.
- AI가 제안한 코드를 그대로 저장하지 않고 직접 실행·검증한 예제만 교재에 사용합니다.