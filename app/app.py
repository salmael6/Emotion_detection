import streamlit as st
import joblib
from pathlib import Path

# =============================
# Configuration de la page
# =============================
st.set_page_config(
    page_title="Détection des Émotions",
    page_icon="🧠",
    layout="centered"
)

# =============================
# Mode sombre uniquement
# =============================
bg_color = "#0E1117"
text_color = "#FAFAFA"
card_color = "#1C1F26"

st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: {bg_color};
            color: {text_color};
        }}

        /* Style des cartes avec animation hover */
        .emotion-card {{
            background-color: {card_color};
            padding: 15px;
            border-radius: 12px;
            text-align: center;
            font-size: 18px;
            box-shadow: 0px 4px 8px rgba(0,0,0,0.2);
            transition: transform 0.3s, box-shadow 0.3s;
        }}
        .emotion-card:hover {{
            transform: translateY(-8px);
            box-shadow: 0px 8px 16px rgba(0,0,0,0.4);
        }}

        /* Style du bouton */
        button[kind="primary"] {{
            color: white !important;
            font-weight: 600;
        }}

        /* Label du text_area */
        label[data-testid="stWidgetLabel"] {{
            color: {text_color} !important;
            font-weight: 600;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# =============================
# Chargement du modèle
# =============================
@st.cache_resource(show_spinner=False)
def load_model():
    BASE_DIR = Path(__file__).resolve().parent
    model_path = BASE_DIR.parent / "model" / "emotion_detector.pkl"
    return joblib.load(model_path)

model = load_model()

# =============================
# Styles des émotions
# =============================
emotion_styles = {
    "joy": ("😄", "Joie", "#F7C948"),
    "sad": ("😢", "Tristesse", "#5DADE2"),
    "anger": ("😡", "Colère", "#E74C3C"),
    "fear": ("😨", "Peur", "#AF7AC5"),
}

# =============================
# Titre et description
# =============================
st.markdown(
    """
    <h1 style="text-align:center;">🧠 Application de Détection des Émotions</h1>
    <p style="text-align:center; font-size:16px;">
    Cette application utilise le <b>Traitement Automatique du Langage Naturel (NLP)</b>
    pour analyser un texte saisi par l’utilisateur et détecter l’émotion dominante exprimée.
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# =============================
# Cartes des émotions avec animation
# =============================
st.markdown("### 🎭 Émotions reconnues")

cols = st.columns(4)
for i, (key, (emoji, label, color)) in enumerate(emotion_styles.items()):
    with cols[i % 4]:
        st.markdown(
            f"""
            <div class="emotion-card" style="background-color:{color};">
                <div style="font-size:30px;">{emoji}</div>
                <b>{label}</b>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("---")

# =============================
# Zone de saisie utilisateur
# =============================
st.markdown("### ✍️ Saisissez un texte en anglais")

user_text = st.text_area(
    "",
    height=120,
    placeholder="Example : I feel so happy today."
)

# =============================
# Bouton de prédiction
# =============================
if st.button("🔍 Détecter l’émotion", use_container_width=True):
    if user_text.strip() == "":
        st.warning("Veuillez entrer un texte.")
    else:
        prediction = model.predict([user_text])[0]
        emoji, label, color = emotion_styles.get(prediction, ("❓", "Inconnue", "#BDC3C7"))

        st.markdown(
            f"""
            <div style="
                background-color:{color};
                padding:25px;
                border-radius:15px;
                text-align:center;
                font-size:26px;
                color:white;
                font-weight:bold;
                margin-top:20px;
                box-shadow: 0px 4px 12px rgba(0,0,0,0.5);
            ">
                {emoji} Émotion détectée : {label}
            </div>
            """,
            unsafe_allow_html=True
        )

# =============================
# Footer
# =============================
st.markdown("---")
st.caption("Projet NLP – Classification des émotions | Streamlit 🧠")
