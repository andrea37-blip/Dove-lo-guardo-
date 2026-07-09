import streamlit as st

# Configurazione della pagina
st.set_page_config(page_title="Dove Lo Guardo AI", page_icon="📺", layout="centered")

# Stile CSS personalizzato per renderlo moderno
st.markdown("""
    <style>
    .main-title { font-size: 42px; font-weight: bold; color: #E50914; text-align: center; margin-bottom: 10px; }
    .subtitle { font-size: 18px; text-align: center; color: #666; margin-bottom: 30px; }
    .platform-card { padding: 15px; border-radius: 10px; background-color: #f0f2f6; margin-bottom: 10px; border-left: 5px solid #007bff; }
    .tv-card { padding: 15px; border-radius: 10px; background-color: #fff3cd; margin-bottom: 10px; border-left: 5px solid #ffc107; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">📺 Dove Lo Guardo? AI</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Scrivi il nome di un film o una serie (o descrivila). L\'AI ti dirà dove vederla in streaming o in TV!</p>', unsafe_allow_html=True)

# Input dell'utente
user_query = st.text_input("Cosa vuoi guardare oggi?", placeholder="Es: Voglio vedere la serie DOC o un film di Nolan...")

# Simulazione Database / Risposte dell'AI accoppiate alle API
MOCK_DATABASE = {
    "doc": {
        "titolo": "Doc - Nelle tue mani",
        "tipo": "Serie TV",
        "streaming": [
            {"piattaforma": "RaiPlay", "tipo": "Gratis / Streaming"},
            {"piattaforma": "Disney+", "tipo": "Incluso nell'abbonamento"}
        ],
        "tv": [
            {"canale": "Rai 1", "orario": "Ogni Lunedì alle 17:00", "nota": "Repliche della Stagione 2"},
            {"canale": "Rai Premium", "orario": "Mercoledì alle 21:20", "nota": "Prima Serata"}
        ]
    },
    "inception": {
        "titolo": "Inception (2010)",
        "tipo": "Film",
        "streaming": [
            {"piattaforma": "Netflix", "tipo": "Incluso nell'abbonamento"},
            {"piattaforma": "Prime Video", "tipo": "Noleggio a 3.99€"}
        ],
        "tv": [
            {"canale": "Canale 5", "orario": "Stasera alle 23:30", "nota": "Seconda serata"}
        ]
    }
}

if user_query:
    query_clean = user_query.lower()
    found = False
    
    with st.spinner("L'AI sta controllando i palinsesti e le piattaforme streaming..."):
        for key, data in MOCK_DATABASE.items():
            if key in query_clean:
                found = True
                st.success(f"Trovato! Ecco i dettagli per: **{data['titolo']}** ({data['tipo']})")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("🌐 Piattaforme Streaming")
                    for stream in data["streaming"]:
                        st.markdown(f"""
                        <div class="platform-card">
                            <strong>{stream['piattaforma']}</strong><br>
                            <small>{stream['tipo']}</small>
                        </div>
                        """, unsafe_allow_html=True)
                        
                with col2:
                    st.subheader("📡 In onda in TV (Digitale/Sat)")
                    for tv in data["tv"]:
                        st.markdown(f"""
                        <div class="tv-card">
                            <strong>{tv['canale']}</strong><br>
                            📅 {tv['orario']}<br>
                            <small>⚠️ {tv['nota']}</small>
                        </div>
                        """, unsafe_allow_html=True)
                break
                
        if not found:
            st.warning("⚠️ Non ho trovato dati in tempo reale per questa specifica ricerca nel database demo. Prova a digitare 'Doc' o 'Inception' per vedere come funziona!")
