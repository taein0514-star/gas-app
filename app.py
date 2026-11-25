import tkinter as tk
from tkinter import ttk

# 1. 리스트 활용: [차량 이름, 온실가스 배출량 점수] 묶음
cars = [["테슬라", 10], ["레이", 95], ["제네시스", 180]]

# 2. def 함수 정의
def check(e):
    selected = combo.get()
    # 3. 반복문: 리스트에서 선택한 차량 찾기
    for name, score in cars:
        if name == selected:
            # 4. 조건문: 85점 이하 판별
            if score <= 85:
                label.config(text=f"{score}점 - 친환경 차량입니다.")
            else:
                label.config(text=f"{score}점 - 지구가 아픕니다.")

root = tk.Tk()
root.geometry("300x150")

# 반복문(리스트 컴프리헨션)으로 차량 이름만 뽑아 드롭다운에 넣기
combo = ttk.Combobox(root, values=[c[0] for c in cars], state="readonly")
combo.pack(pady=20)
combo.bind("<<ComboboxSelected>>", check)

label = tk.Label(root, text="차량을 선택하세요")
label.pack(pady=10)

root.mainloop()
