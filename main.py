import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="MBTI 포켓몬 추천기",
    page_icon="⚡",
    layout="centered"
)

# MBTI별 포켓몬 추천 데이터
pokemon_data = {
    "INTJ": {
        "name": "뮤츠",
        "emoji": "🧠💜",
        "type": "에스퍼 타입",
        "description": "전략적이고 지적인 당신! 뮤츠처럼 강력한 지능과 독립적인 성향을 가졌어요. 혼자만의 시간을 즐기며 깊이 사고하는 모습이 닮았답니다!",
        "skills": "사이코키네시스, 회복, 배리어, 염동력"
    },
    "INTP": {
        "name": "폴리곤",
        "emoji": "🔷🤓",
        "type": "노말 타입",
        "description": "논리적이고 분석적인 당신! 폴리곤처럼 데이터와 이론을 사랑하는 천재형이에요. 끊임없이 진화하며 새로운 지식을 탐구하죠!",
        "skills": "트라이어택, 자기암시, 전자포, 변환"
    },
    "ENTJ": {
        "name": "리자몽",
        "emoji": "🔥👑",
        "type": "불꽃/비행 타입",
        "description": "타고난 리더 당신! 리자몽처럼 카리스마 넘치고 목표를 향해 불타오르는 열정의 소유자예요. 하늘을 지배하는 강력한 존재감!",
        "skills": "화염방사, 용의분노, 날개치기, 폭풍불꽃"
    },
    "ENTP": {
        "name": "갸라도스",
        "emoji": "🌊🐉",
        "type": "물/비행 타입",
        "description": "창의적이고 도전적인 당신! 잉어킹에서 갸라도스로 진화하듯, 무한한 가능성과 반전 매력을 가진 토론왕이에요!",
        "skills": "하이드로펌프, 폭포오르기, 용의춤, 분노"
    },
    "INFJ": {
        "name": "루카리오",
        "emoji": "✨🐺",
        "type": "격투/강철 타입",
        "description": "통찰력 있는 당신! 루카리오처럼 파동(감정)을 읽고 깊은 직감을 가진 신비로운 영혼이에요. 정의롭고 충직한 마음의 소유자!",
        "skills": "파동탄, 검의춤, 마음의눈, 신속"
    },
    "INFP": {
        "name": "이브이",
        "emoji": "🌸🦊",
        "type": "노말 타입",
        "description": "순수하고 이상주의적인 당신! 이브이처럼 무한한 가능성을 품고 있어요. 다양한 모습으로 진화할 수 있는 잠재력의 끝판왕!",
        "skills": "박치기, 매혹의보이스, 애교부리기, 진화"
    },
    "ENFJ": {
        "name": "피카츄",
        "emoji": "⚡💛",
        "type": "전기 타입",
        "description": "따뜻한 카리스마의 당신! 피카츄처럼 모두에게 사랑받는 리더예요. 친구들에게 긍정 에너지를 전파하는 햇살 같은 존재!",
        "skills": "10만볼트, 전광석화, 아이언테일, 볼트태클"
    },
    "ENFP": {
        "name": "토게피",
        "emoji": "🥚🌈",
        "type": "페어리 타입",
        "description": "밝고 호기심 많은 당신! 토게피처럼 세상의 행복을 끌어모으는 매력의 소유자예요. 어디서든 분위기 메이커!",
        "skills": "매혹의보이스, 달의힘, 메탈클로, 행복알"
    },
    "ISTJ": {
        "name": "거북왕",
        "emoji": "🛡️🐢",
        "type": "물 타입",
        "description": "성실하고 책임감 강한 당신! 거북왕처럼 듬직하고 신뢰감 있는 베테랑이에요. 단단한 등껍질처럼 굳건한 원칙의 소유자!",
        "skills": "하이드로캐논, 껍질에숨기, 파도타기, 방어"
    },
    "ISFJ": {
        "name": "꼬부기",
        "emoji": "💧🐢",
        "type": "물 타입",
        "description": "헌신적이고 따뜻한 당신! 꼬부기처럼 친구들을 보호하고 챙기는 다정한 마음의 소유자예요. 조용하지만 강한 수호자!",
        "skills": "물대포, 거품, 방어, 돌진"
    },
    "ESTJ": {
        "name": "이상해꽃",
        "emoji": "🌳🌺",
        "type": "풀/독 타입",
        "description": "체계적이고 실용적인 당신! 이상해꽃처럼 든든하고 조직적인 관리자형이에요. 모두를 이끄는 큰 나무 같은 존재!",
        "skills": "솔라빔, 꽃잎댄스, 지진, 광합성"
    },
    "ESFJ": {
        "name": "푸린",
        "emoji": "🎤💗",
        "type": "노말/페어리 타입",
        "description": "사교적이고 다정한 당신! 푸린처럼 노래로 모두를 행복하게 하는 인기쟁이에요. 사람들과 어울리는 걸 사랑하는 따뜻한 존재!",
        "skills": "노래하다, 매혹의보이스, 굴리기, 도와주기"
    },
    "ISTP": {
        "name": "갸라도스",
        "emoji": "⚙️🦎",
        "type": "전기 타입",
        "description": "실용적이고 모험을 즐기는 당신! 라이츄처럼 빠르고 효율적으로 문제를 해결하는 능력자예요. 조용하지만 강력한 한방!",
        "skills": "10만볼트, 전광석화, 번개, 방전"
    },
    "ISFP": {
        "name": "이브이(님피아)",
        "emoji": "🎀🌟",
        "type": "페어리 타입",
        "description": "예술적이고 감성적인 당신! 님피아처럼 우아하고 섬세한 매력의 소유자예요. 자신만의 아름다운 세계를 만들어가는 아티스트!",
        "skills": "매혹의보이스, 달의힘, 애교부리기, 마지막일격"
    },
    "ESTP": {
        "name": "리자몽",
        "emoji": "🔥⚡",
        "type": "불꽃/비행 타입",
        "description": "에너지 넘치는 행동파 당신! 리자몽처럼 즉흥적이고 모험을 사랑하는 자유로운 영혼이에요. 스릴 넘치는 순간을 즐기죠!",
        "skills": "화염방사, 날개치기, 지진, 폭풍불꽃"
    },
    "ESFP": {
        "name": "마릴",
        "emoji": "💙🎉",
        "type": "물/페어리 타입",
        "description": "활발하고 즐거운 당신! 마릴처럼 귀엽고 통통 튀는 매력으로 분위기를 띄우는 파티의 주인공이에요!",
        "skills": "거품광선, 매혹의보이스, 아쿠아테일, 놀이"
    }
}

# 메인 UI
st.title("⚡ MBTI 포켓몬 추천기 🎮")
st.markdown("### ✨ 당신의 MBTI에 어울리는 포켓몬을 찾아드려요! ✨")
st.markdown("---")

st.markdown("#### 🔍 당신의 MBTI를 선택해주세요!")

# MBTI 선택
mbti_list = ["선택해주세요 👇", "INTJ", "INTP", "ENTJ", "ENTP", 
             "INFJ", "INFP", "ENFJ", "ENFP",
             "ISTJ", "ISFJ", "ESTJ", "ESFJ",
             "ISTP", "ISFP", "ESTP", "ESFP"]

selected_mbti = st.selectbox("MBTI 선택 🎯", mbti_list)

st.markdown("---")

# 결과 표시
if selected_mbti != "선택해주세요 👇":
    pokemon = pokemon_data[selected_mbti]
    
    st.balloons()
    
    st.markdown(f"## 🎉 {selected_mbti}에게 어울리는 포켓몬은...")
    st.markdown(f"# {pokemon['emoji']} {pokemon['name']}!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info(f"**🏷️ 타입**\n\n{pokemon['type']}")
    
    with col2:
        st.success(f"**⚔️ 주요 기술**\n\n{pokemon['skills']}")
    
    st.markdown("### 💌 포켓몬 소개")
    st.warning(pokemon['description'])
    
    st.markdown("---")
    st.markdown("#### 🌟 함께 모험을 떠나볼까요? 🌟")
    
else:
    st.info("👆 위에서 MBTI를 선택하면 어울리는 포켓몬을 알려드려요! 🎁")
    
    st.markdown("### 🎲 MBTI가 뭔지 모르겠다면?")
    st.markdown("""
    - 🧠 **N(직관) vs S(감각)**: 상상력 vs 현실감각
    - ❤️ **F(감정) vs T(사고)**: 공감 vs 논리
    - 🎯 **J(판단) vs P(인식)**: 계획적 vs 자유로운
    - 🗣️ **E(외향) vs I(내향)**: 활발한 vs 차분한
    """)

# 푸터
st.markdown("---")
st.markdown("🎨 Made with ❤️ for 당곡고 학생들 | Powered by Streamlit ⚡")
