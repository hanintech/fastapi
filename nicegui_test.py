from nicegui import ui

def display_scores():
    korean_score = korean_input.value
    math_score = math_input.value
    english_score = english_input.value
    ui.label(f'국어: {korean_score}')
    ui.label(f'수학: {math_score}')
    ui.label(f'영어: {english_score}')

# 성적 입력을 위한 텍스트박스 생성 (가로 배치)
with ui.row():
    korean_input = ui.number(label="국어", placeholder="점수 입력")
    math_input = ui.number(label="수학", placeholder="점수 입력")
    english_input = ui.number(label="영어", placeholder="점수 입력")

# 버튼 클릭 시 성적을 표시
ui.button("성적 확인", on_click=display_scores)

# 앱 실행
ui.run()
