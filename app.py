# =========================
# frontend: app.py  (FULL FILE)
# =========================
import requests
import streamlit as st
import re

# =============================
# CONFIG
# =============================
API_BASE = "https://movie-recommendation-system-suqs.onrender.com" or "http://127.0.0.1:8000"
TMDB_IMG = "https://image.tmdb.org/t/p/w500"

st.set_page_config(page_title="Movie+", page_icon="🎬", layout="wide")

# =============================
# STYLES (minimal modern)
# =============================
st.markdown(
    """
<style>
/* =========================
AMAZON PRIME+ CLEAN THEME v2
========================= */

/* ---- Theme tokens (easy tweaks) ---- */
:root{
  --bg0:#0b1218;
  --bg1:#0f171e;
  --text:#e8eef7;
  --muted:rgba(232,238,247,.72);
  --muted2:rgba(232,238,247,.60);
  --line:rgba(255,255,255,.08);
  --prime:#00a8e1;
  --prime2:#1f9fff;

  --card:rgba(18, 28, 38, 0.72);
  --card2:rgba(18, 28, 38, 0.55);
  --cardBorder:rgba(0,168,225,.16);

  --shadow:0 12px 28px rgba(0,0,0,.28);
  --shadow2:0 18px 42px rgba(0,168,225,.10);
}

/* App background + default text */
.stApp {
  background:
    radial-gradient(1100px 520px at 15% -10%, rgba(0,168,225,.18), transparent 60%),
    radial-gradient(900px 520px at 85% 10%, rgba(31,159,255,.10), transparent 55%),
    linear-gradient(180deg, var(--bg1) 0%, var(--bg0) 100%);
  color: var(--text);
}

/* Container spacing */
.block-container {
  padding-top: 1rem;
  padding-bottom: 2rem;
  max-width: 1450px;
}

/* Make Streamlit layout containers transparent */
[data-testid="stVerticalBlock"],
[data-testid="column"],
[data-testid="stHorizontalBlock"],
[data-testid="stContainer"] {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
}

/* Divider */
hr { border-color: var(--line) !important; }

/* Text helpers */
.small-muted { color: var(--muted); font-size: 0.92rem; line-height: 1.35rem; }
.tiny-muted { color: var(--muted2); font-size: 0.86rem; }

/* Better 2-line truncation for movie titles */
.movie-title{
  font-size: 0.96rem;
  line-height: 1.22rem;
  color: var(--text);
  font-weight: 650;

  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;

  overflow: hidden;
  min-height: calc(1.22rem * 2);
}

/* =========================
CARD (glass)
========================= */
.card{
  border-radius: 18px;
  padding: 14px;
  background: linear-gradient(180deg, rgba(18,28,38,.80), rgba(18,28,38,.62));
  border: 1px solid var(--cardBorder);
  box-shadow: var(--shadow);
  backdrop-filter: blur(10px);
  transition: transform 160ms ease, border-color 160ms ease, box-shadow 160ms ease;
}

.card:hover{
  transform: translateY(-2px);
  border-color: rgba(0,168,225,.42);
  box-shadow: var(--shadow), var(--shadow2);
}

/* Optional poster-card (won't affect existing UI unless you use it) */
.poster-card{
  border-radius: 18px;
  padding: 10px;
  background: rgba(18,28,38,.62);
  border: 1px solid rgba(255,255,255,.08);
  box-shadow: 0 10px 24px rgba(0,0,0,.22);
}

/* Images */
img { border-radius: 14px; }

/* Posters hover zoom (subtle + smooth) */
.stImage img{
  transition: transform 160ms ease, filter 160ms ease;
}
.stImage img:hover{
  transform: scale(1.02);
  filter: saturate(1.03) contrast(1.02);
}

/* =========================
BUTTONS (Prime)
========================= */
.stButton > button{
  background: linear-gradient(90deg, var(--prime), var(--prime2));
  color: #ffffff;
  border-radius: 12px;
  border: 1px solid rgba(255,255,255,0.08);
  padding: 8px 14px;
  font-weight: 750;
  letter-spacing: .2px;
  transition: transform 120ms ease, box-shadow 120ms ease, background 120ms ease, filter 120ms ease;
}

.stButton > button:hover{
  transform: translateY(-1px);
  filter: brightness(.98);
  box-shadow: 0 12px 24px rgba(0,168,225,.20);
}

.stButton > button:active{
  transform: translateY(0px) scale(.99);
  box-shadow: 0 8px 18px rgba(0,168,225,.14);
}

.stButton > button:disabled{
  opacity: .55;
  cursor: not-allowed;
}

/* =========================
INPUTS (clean)
========================= */
.stTextInput input,
.stSelectbox div[data-baseweb="select"] > div,
.stSlider div[data-baseweb="slider"]{
  background: rgba(18, 28, 38, 0.68) !important;
  color: var(--text) !important;
  border-radius: 12px !important;
  border: 1px solid rgba(255,255,255,0.10) !important;
}

/* Focus ring */
.stTextInput input:focus,
.stSelectbox div[data-baseweb="select"] > div:focus-within{
  box-shadow: 0 0 0 3px rgba(0,168,225,.18) !important;
  border-color: rgba(0,168,225,.35) !important;
}

/* Selectbox text */
.stSelectbox * { color: var(--text) !important; }

/* =========================
SIDEBAR
========================= */
section[data-testid="stSidebar"]{
  background: linear-gradient(180deg, #0b1218, #081016);
  border-right: 1px solid rgba(0, 168, 225, 0.18);
}
section[data-testid="stSidebar"] .block-container{ padding-top: 1rem; }

/* =========================
KIDS SAFE BADGE
========================= */
.kids-pill{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 11px;
  border-radius: 999px;
  font-size: 0.85rem;
  border: 1px solid rgba(0,168,225,.28);
  background: rgba(255,255,255,.04);
}

.kids-on{
  background: rgba(0,168,225,.18);
  color: #6fe6ff;
  font-weight: 750;
}

.kids-off{
  color: rgba(232,238,247,.72);
  font-weight: 650;
}

/* =========================
WARNING BOX
========================= */
.warn{
  padding: 10px 12px;
  border-radius: 14px;
  border: 1px solid rgba(255, 77, 77, 0.35);
  background: rgba(255, 77, 77, 0.12);
  color: #ffb4b4;
}

/* Hide default Streamlit menu/footer */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
</style>
""",
    unsafe_allow_html=True,
)

# =============================
# STATE + ROUTING (single-file pages)
# =============================
if "view" not in st.session_state:
    st.session_state.view = "home"  # home | details
if "selected_tmdb_id" not in st.session_state:
    st.session_state.selected_tmdb_id = None

qp_view = st.query_params.get("view")
qp_id = st.query_params.get("id")
if qp_view in ("home", "details"):
    st.session_state.view = qp_view
if qp_id:
    try:
        st.session_state.selected_tmdb_id = int(qp_id)
        st.session_state.view = "details"
    except:
        pass


def goto_home():
    st.session_state.view = "home"
    st.query_params["view"] = "home"
    if "id" in st.query_params:
        del st.query_params["id"]
    st.rerun()


def goto_details(tmdb_id: int):
    st.session_state.view = "details"
    st.session_state.selected_tmdb_id = int(tmdb_id)
    st.query_params["view"] = "details"
    st.query_params["id"] = str(int(tmdb_id))
    st.rerun()


# =============================
# API HELPERS
# =============================
@st.cache_data(ttl=30)
def api_get_json(path: str, params: dict | None = None):
    try:
        r = requests.get(f"{API_BASE}{path}", params=params, timeout=25)
        if r.status_code >= 400:
            return None, f"HTTP {r.status_code}: {r.text[:300]}"
        return r.json(), None
    except Exception as e:
        return None, f"Request failed: {e}"


# =============================
# KIDS SAFE MODE (best-effort)
# =============================
DEFAULT_UNSAFE_KEYWORDS = [
    "sex",
    "sexual",
    "xxx",
    "porn",
    "erotic",
    "nude",
    "nudity",
    "strip",
    "brothel",
    "escort",
    "orgy",
    "fetish",
    "rape",
    "molest",
    "adult",
    "18+",
    "nsfw",
]


def looks_unsafe_by_title(title: str, extra_keywords: list[str] | None = None) -> bool:
    if not title:
        return False
    title_l = title.strip().lower()
    keywords = DEFAULT_UNSAFE_KEYWORDS + (extra_keywords or [])
    for kw in keywords:
        kw_l = kw.strip().lower()
        if not kw_l:
            continue
        if re.search(rf"(^|[^a-z0-9]){re.escape(kw_l)}([^a-z0-9]|$)", title_l):
            return True
    return False


def kids_safe_filter_cards(cards: list[dict], enable: bool, extra_keywords: list[str] | None = None):
    if not enable:
        return cards

    safe = []
    for m in cards or []:
        title = (m.get("title") or "").strip()
        adult_flag = m.get("adult")  # True/False/None
        if adult_flag is True:
            continue
        if looks_unsafe_by_title(title, extra_keywords=extra_keywords):
            continue
        safe.append(m)
    return safe


def poster_grid(cards, cols=6, key_prefix="grid"):
    if not cards:
        st.info("No movies to show.")
        return

    rows = (len(cards) + cols - 1) // cols
    idx = 0
    for r in range(rows):
        colset = st.columns(cols)
        for c in range(cols):
            if idx >= len(cards):
                break
            m = cards[idx]
            idx += 1

            tmdb_id = m.get("tmdb_id")
            title = m.get("title", "Untitled")
            poster = m.get("poster_url")

            with colset[c]:
                if poster:
                    st.image(poster, use_column_width=True)
                else:
                    st.write("🖼️ No poster")

                if st.button("Open", key=f"{key_prefix}_{r}_{c}_{idx}_{tmdb_id}"):
                    if tmdb_id:
                        goto_details(tmdb_id)

                st.markdown(f"<div class='movie-title'>{title}</div>", unsafe_allow_html=True)


def to_cards_from_tfidf_items(tfidf_items):
    cards = []
    for x in tfidf_items or []:
        tmdb = x.get("tmdb") or {}
        if tmdb.get("tmdb_id"):
            cards.append(
                {
                    "tmdb_id": tmdb["tmdb_id"],
                    "title": tmdb.get("title") or x.get("title") or "Untitled",
                    "poster_url": tmdb.get("poster_url"),
                    "adult": tmdb.get("adult", None) if isinstance(tmdb, dict) else None,
                }
            )
    return cards


def parse_tmdb_search_to_cards(data, keyword: str, limit: int = 24):
    keyword_l = keyword.strip().lower()

    if isinstance(data, dict) and "results" in data:
        raw = data.get("results") or []
        raw_items = []
        for m in raw:
            title = (m.get("title") or "").strip()
            tmdb_id = m.get("id")
            poster_path = m.get("poster_path")
            if not title or not tmdb_id:
                continue
            raw_items.append(
                {
                    "tmdb_id": int(tmdb_id),
                    "title": title,
                    "poster_url": f"{TMDB_IMG}{poster_path}" if poster_path else None,
                    "release_date": m.get("release_date", ""),
                    "adult": bool(m.get("adult", False)),
                }
            )
    elif isinstance(data, list):
        raw_items = []
        for m in data:
            tmdb_id = m.get("tmdb_id") or m.get("id")
            title = (m.get("title") or "").strip()
            poster_url = m.get("poster_url")
            if not title or not tmdb_id:
                continue
            raw_items.append(
                {
                    "tmdb_id": int(tmdb_id),
                    "title": title,
                    "poster_url": poster_url,
                    "release_date": m.get("release_date", ""),
                    "adult": bool(m.get("adult", False)) if "adult" in m else None,
                }
            )
    else:
        return [], []

    matched = [x for x in raw_items if keyword_l in x["title"].lower()]
    final_list = matched if matched else raw_items

    suggestions = []
    for x in final_list[:10]:
        year = (x.get("release_date") or "")[:4]
        label = f"{x['title']} ({year})" if year else x["title"]
        suggestions.append((label, x["tmdb_id"]))

    cards = [
        {"tmdb_id": x["tmdb_id"], "title": x["title"], "poster_url": x["poster_url"], "adult": x.get("adult")}
        for x in final_list[:limit]
    ]
    return suggestions, cards


# =============================
# SIDEBAR
# =============================
with st.sidebar:
    st.markdown("## 🎬 Menu")
    if st.button("🏠 Home"):
        goto_home()

    st.markdown("---")
    st.markdown("### 🏠 Home Feed (only home)")
    home_category = st.selectbox(
        "Category",
        ["trending", "popular", "top_rated", "now_playing", "upcoming"],
        index=0,
    )
    GRID_COLS = 6   # change anytime (5,6,7 etc)
    st.markdown("---")
    st.markdown("### 🧒 Kids Safe Mode")
    kids_safe = st.toggle("Enable Kids Safe filter", value=False)

# no extra keywords now
extra_keywords = None


# =============================
# HEADER
# =============================
st.title("🎬 MOVIE+")

pill_class = "kids-pill kids-on" if kids_safe else "kids-pill kids-off"
pill_text = "Kids Safe: ON ✅" if kids_safe else "Kids Safe: OFF"
st.markdown(f"<div class='{pill_class}'>{pill_text}</div>", unsafe_allow_html=True)

st.markdown(
    "<div class='small-muted'>Type keyword → dropdown suggestions + matching results → open → details + recommendations</div>",
    unsafe_allow_html=True,
)
st.divider()


# ==========================================================
# VIEW: HOME
# ==========================================================
if st.session_state.view == "home":
    typed = st.text_input("Search by movie title (keyword)", placeholder="Type: avenger, batman, love...")
    st.divider()

    if typed.strip():
        if len(typed.strip()) < 2:
            st.caption("Type at least 2 characters for suggestions.")
        else:
            data, err = api_get_json("/tmdb/search", params={"query": typed.strip()})
            if err or data is None:
                st.error(f"Search failed: {err}")
            else:
                suggestions, cards = parse_tmdb_search_to_cards(data, typed.strip(), limit=24)

                cards = kids_safe_filter_cards(cards, kids_safe, extra_keywords=extra_keywords)

                if kids_safe and suggestions:
                    filtered = []
                    for label, tid in suggestions:
                        pure_title = label.rsplit(" (", 1)[0]
                        if looks_unsafe_by_title(pure_title, extra_keywords=extra_keywords):
                            continue
                        filtered.append((label, tid))
                    suggestions = filtered

                if suggestions:
                    labels = ["-- Select a movie --"] + [s[0] for s in suggestions]
                    selected = st.selectbox("Suggestions", labels, index=0)
                    if selected != "-- Select a movie --":
                        label_to_id = {s[0]: s[1] for s in suggestions}
                        goto_details(label_to_id[selected])
                else:
                    st.info("No suggestions found (or filtered by Kids Safe Mode). Try another keyword.")

                st.markdown("### Results")
                poster_grid(cards, cols=GRID_COLS, key_prefix="search_results")

                if kids_safe:
                    st.caption("Kids Safe Mode is ON: adult/unsafe titles are filtered out (best-effort).")

        st.stop()

    st.markdown(f"### 🏠 Home — {home_category.replace('_',' ').title()}")
    home_cards, err = api_get_json("/home", params={"category": home_category, "limit": 24})
    if err or not home_cards:
        st.error(f"Home feed failed: {err or 'Unknown error'}")
        st.stop()

    safe_home_cards = kids_safe_filter_cards(home_cards, kids_safe, extra_keywords=extra_keywords)

    if kids_safe:
        st.markdown("#### 🧒 Kids Safe Picks (filtered)")
        poster_grid(safe_home_cards, cols=GRID_COLS, key_prefix="home_feed_kids")
        if len(safe_home_cards) < len(home_cards):
            st.caption(f"Filtered out {len(home_cards) - len(safe_home_cards)} item(s) (best-effort).")
    else:
        poster_grid(home_cards, cols=GRID_COLS, key_prefix="home_feed")


# ==========================================================
# VIEW: DETAILS
# ==========================================================
elif st.session_state.view == "details":
    tmdb_id = st.session_state.selected_tmdb_id
    if not tmdb_id:
        st.warning("No movie selected.")
        if st.button("← Back to Home"):
            goto_home()
        st.stop()

    a, b = st.columns([3, 1])
    with a:
        st.markdown("### 📄 Movie Details")
    with b:
        if st.button("← Back to Home"):
            goto_home()

    data, err = api_get_json(f"/movie/id/{tmdb_id}")
    if err or not data:
        st.error(f"Could not load details: {err or 'Unknown error'}")
        st.stop()

    title_for_checks = (data.get("title") or "").strip()
    adult_flag = data.get("adult", None)
    flagged_by_title = looks_unsafe_by_title(title_for_checks, extra_keywords=extra_keywords)

    if kids_safe and (adult_flag is True or flagged_by_title):
        st.markdown(
            "<div class='warn'>⚠️ Kids Safe Mode: This title looks adult/unsafe (best-effort check). You can go back and pick another movie.</div>",
            unsafe_allow_html=True,
        )

    left, right = st.columns([1, 2.4], gap="large")

    with left:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        if data.get("poster_url"):
            st.image(data["poster_url"], use_column_width=True)
        else:
            st.write("🖼️ No poster")
        st.markdown("</div>", unsafe_allow_html=True)

    with right:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown(f"## {data.get('title','')}")
        release = data.get("release_date") or "-"
        genres = ", ".join([g["name"] for g in data.get("genres", [])]) or "-"
        st.markdown(f"<div class='small-muted'>Release: {release}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='small-muted'>Genres: {genres}</div>", unsafe_allow_html=True)

        if adult_flag is not None:
            st.markdown(
                f"<div class='small-muted'>Adult flag: {'Yes' if adult_flag else 'No'}</div>",
                unsafe_allow_html=True,
            )

        st.markdown("---")
        st.markdown("### Overview")
        st.write(data.get("overview") or "No overview available.")
        st.markdown("</div>", unsafe_allow_html=True)

    if data.get("backdrop_url"):
        st.markdown("#### Backdrop")
        st.image(data["backdrop_url"], use_column_width=True)

    st.divider()

    # =============================
    # ✅ TRAILER SECTION (YouTube)
    # =============================
    st.markdown("### ▶ Trailer")
    trailer, terr = api_get_json(f"/movie/trailer/{tmdb_id}")

    if terr or not trailer:
        st.info("Trailer not available right now.")
    else:
        youtube_key = trailer.get("youtube_key")
        if youtube_key:
            st.video(f"https://www.youtube.com/watch?v={youtube_key}")
        else:
            st.info("No trailer found for this movie.")

    st.divider()
    st.markdown("### ✅ Recommendations")

    if kids_safe and (adult_flag is True or flagged_by_title):
        st.info("Kids Safe Mode: Recommendations hidden for this title.")
        st.stop()

    title = (data.get("title") or "").strip()
    if title:
        bundle, err2 = api_get_json("/movie/search", params={"query": title, "tfidf_top_n": 12, "genre_limit": 12})

        if not err2 and bundle:
            st.markdown("#### 🔎 Similar Movies (TF-IDF)")
            tfidf_cards = to_cards_from_tfidf_items(bundle.get("tfidf_recommendations"))
            tfidf_cards = kids_safe_filter_cards(tfidf_cards, kids_safe, extra_keywords=extra_keywords)
            poster_grid(tfidf_cards, cols=GRID_COLS, key_prefix="details_tfidf")

            st.markdown("#### 🎭 More Like This (Genre)")
            genre_cards = bundle.get("genre_recommendations", [])
            genre_cards = kids_safe_filter_cards(genre_cards, kids_safe, extra_keywords=extra_keywords)
            poster_grid(genre_cards, cols=GRID_COLS, key_prefix="details_genre")
        else:
            st.info("Showing Genre recommendations (fallback).")
            genre_only, err3 = api_get_json("/recommend/genre", params={"tmdb_id": tmdb_id, "limit": 18})
            if not err3 and genre_only:
                genre_only = kids_safe_filter_cards(genre_only, kids_safe, extra_keywords=extra_keywords)
                poster_grid(genre_only, cols=GRID_COLS, key_prefix="details_genre_fallback")
            else:
                st.warning("No recommendations available right now.")
    else:
        st.warning("No title available to compute recommendations.")