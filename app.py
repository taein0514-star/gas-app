
import streamlit as st

# 1. 리스트 데이터 구조: [차량명, 1km당 온실가스 배출량(g/km)]
# 실제 차량 기준 반영 (전기차 0g, 경차 레이 약 103g, 대형 세단 제네시스 약 190g)
car_data = [
    ["테슬라", 0],
    ["레이", 103],
    ["제네시스", 190],
    ["롤스로이스", 200]
]

# 2. def 함수: 선택한 차량과 주행 거리를 받아 총 온실가스 배출량(kg) 계산
def calculate_emission(selected_car, distance):
    # 3. 반복문(for): 리스트에서 선택한 차량의 배출량 데이터 찾기
    for name, co2_per_km in car_data:
        if name == selected_car:
            # 총 배출량(kg) 계산 = (1km당 배출량(g) * 주행거리(km)) / 1000
            total_kg = (co2_per_km * distance) / 1000
            return co2_per_km, total_kg
    return 0, 0

# 웹 화면 구성
st.title("🚗 자동차 온실가스 배출량 계산기")
st.write("같은 거리를 주행할 때 차량별 온실가스 배출량을 비교합니다. (점수가 낮을수록 친환경)")

# 드롭다운 목록 생성 (반복문으로 차량 이름만 추출)
car_names = [car[0] for car in car_data]
selected = st.selectbox("비교할 자동차를 선택하세요:", car_names)

# 주행 거리 설정 (기본 100km 기준)
distance = st.slider("주행 거리 (km)", min_value=10, max_value=500, value=100, step=10)

# 함수 호출하여 계산 결과 가져오기
score, total_emission = calculate_emission(selected, distance)

st.subheader(f"📊 분석 결과: {selected}")
st.write(f"- **온실가스 배출량 점수 (1km당 배출량):** `{score}점` ({score} g/km)")
st.write(f"- **{distance}km 주행 시 총 배출량:** `{total_emission:.2f} kg`")

# 4. 조건문 (if / elif / else): 특정 점수(85점) 기준으로 판별
if score == 0:
    st.success(f"친환경 자동차입니다! (주행 중 온실가스를 전혀 배출하지 않습니다. 🌱)")
elif score <= 85:
    st.success(f"친환경 자동차입니다! (배출량 기준 85점 이하 충족 🌿)")
else:
    st.error(f"지구가 아픕니다. (배출량 기준 85점 초과! 온실가스 배출이 많습니다. 🌍😢)")
