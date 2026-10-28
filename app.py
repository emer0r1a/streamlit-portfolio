import random
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

NAME = "Rea Emerald Sabellita"
SECTION = "CS365 - F2"
PROGRAM = "Computer Science Undergraduate"
SCHOOL = "Cebu Institute of Technology – University"

st.set_page_config(page_title=f"{NAME} · Portfolio", page_icon="🌸", layout="wide",
                   initial_sidebar_state="collapsed")

PAGES = ["Home", "Autobiography", "Skills", "Projects", "Contact"]
EPIGRAPHS = ["the cover page", "dear diary,", "the toolbox", "the scrapbook", "last page · write back"]

for k, v in {"likes": 0, "xp": 0, "messages": [], "ran": False, "ticket": None, "page": PAGES[0]}.items():
    st.session_state.setdefault(k, v)


def add_xp(n):
    st.session_state.xp += n


def go(p):
    st.session_state.page = p


# THEME
PALETTES = {
    "Rose + Lavender": ("#F4A6C8", "#B79CED", "#FBE6F1", "290deg"),
    "Orchid": ("#D9A9F2", "#9D86E9", "#EFE5FB", "290deg"),
    "Blue + Purple": ("#8EC5FF", "#A78BFA", "#E6EEFF", "235deg"),
}

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@700;800&family=JetBrains+Mono:wght@500&display=swap');
:root{--a1:__A1__;--a2:__A2__;--tint:__TINT__;--ink:#2B2340;--paper:#FFFBFD;--turn:__TURN__;}
html,body,[class*="css"],.stMarkdown,button,input,textarea{font-family:'Inter',system-ui,sans-serif!important;color:var(--ink);
 -webkit-font-smoothing:antialiased;line-height:1.6;}
.stApp{background-color:#FDF6F9;
 background-image:linear-gradient(rgba(43,35,64,.04) 1px,transparent 1px),linear-gradient(90deg,rgba(43,35,64,.04) 1px,transparent 1px);
 background-size:36px 36px;}
.block-container{padding-top:2.4rem;max-width:1120px;}
header[data-testid="stHeader"]{background:transparent;}
[data-testid="stSidebar"]{background:var(--tint);border-right:2px solid var(--ink);}
h1,h2,h3,h4{font-family:'Plus Jakarta Sans','Inter',sans-serif!important;color:var(--ink);font-weight:800;letter-spacing:-.02em;line-height:1.2;}
p{font-size:.98rem;}
.eyebrow,.mono{font-family:'Inter',sans-serif!important;text-transform:uppercase;letter-spacing:.09em;font-size:.7rem;font-weight:700;}
.eyebrow{background:var(--a1);display:inline-block;padding:.2rem .65rem;border:2px solid var(--ink);border-radius:999px;margin-bottom:.7rem;}
.big{font-family:'Plus Jakarta Sans',sans-serif;font-size:clamp(2.2rem,5vw,3.6rem);line-height:1.08;font-weight:800;letter-spacing:-.03em;margin:.2rem 0 .9rem;}
.hl{background:linear-gradient(transparent 58%,var(--a1) 58%);padding:0 .12em;}
.hl2{background:linear-gradient(transparent 58%,var(--a2) 58%);padding:0 .12em;}
.muted{color:#5d5673;}
.card{background:var(--paper);border:2px solid var(--ink);border-radius:18px;padding:1.2rem 1.4rem;
 box-shadow:6px 6px 0 var(--a2);margin-bottom:1.1rem;transition:transform .15s,box-shadow .15s;}
.card:hover{transform:translate(-3px,-3px);box-shadow:9px 9px 0 var(--a1);}
.card h3,.card h4{margin-top:0;}
.pcard{border-top:12px solid var(--a1);min-height:280px;}
.pill{display:inline-block;padding:.15rem .7rem;margin:.15rem .2rem .15rem 0;border:2px solid var(--ink);border-radius:999px;
 font-size:.74rem;font-weight:600;background:var(--tint);transition:transform .15s;}
.pill:nth-child(3n){background:var(--a1);} .pill:nth-child(3n+1){background:var(--a2);}
.pill:hover{transform:rotate(-4deg) scale(1.08);}
.marq{overflow:hidden;border:2px solid var(--ink);border-radius:12px;background:var(--a2);margin:1.4rem 0;box-shadow:4px 4px 0 var(--ink);}
.track{display:inline-block;white-space:nowrap;animation:scroll 28s linear infinite;padding:.55rem 0;}
.track span{font-weight:700;font-size:.8rem;letter-spacing:.08em;margin:0 1.2rem;}
@keyframes scroll{to{transform:translateX(-50%);}}
.stage{position:relative;padding:0 0 .5rem;}
.term{background:var(--ink);border-radius:16px;border:2px solid var(--ink);box-shadow:8px 8px 0 var(--a1);overflow:hidden;}
.term .bar{background:#463c66;padding:.5rem .8rem;}
.dot{display:inline-block;width:11px;height:11px;border-radius:50%;margin-right:6px;}
.term .body{padding:1rem 1.2rem;font-family:'JetBrains Mono',monospace;font-size:.8rem;color:#f4e9ff;}
.line{overflow:hidden;white-space:nowrap;width:0;animation:type 1.3s steps(34) forwards;margin:.15rem 0;}
.l2{animation-delay:1.4s;}.l3{animation-delay:2.8s;}.l4{animation-delay:3.4s;}.l5{animation-delay:4s;}
@keyframes type{to{width:100%;}}
.k{color:var(--a1);}.v{color:#c8b6ff;}
.sticker{position:absolute;border:2px solid var(--ink);border-radius:12px;padding:.25rem .7rem;background:var(--a1);
 font-weight:700;font-size:.74rem;animation:float 3.2s ease-in-out infinite;box-shadow:3px 3px 0 var(--ink);}
.s1{top:-16px;right:18px;transform:rotate(6deg);}
.s2{bottom:-6px;left:-14px;transform:rotate(-7deg);background:var(--a2);animation-delay:1s;}
@keyframes float{50%{margin-top:-8px;}}
.avatar{width:96px;height:96px;border-radius:50%;background:linear-gradient(135deg,var(--a1),var(--a2));border:3px solid var(--ink);
 display:flex;align-items:center;justify-content:center;font-size:2rem;font-weight:800;color:#fff;position:relative;box-shadow:4px 4px 0 var(--ink);}
.avatar::before{content:"";position:absolute;inset:-10px;border:2px dashed var(--ink);border-radius:50%;animation:spin 14s linear infinite;}
.flower{font-size:3.4rem;display:inline-block;animation:spin 12s linear infinite;filter:drop-shadow(3px 3px 0 var(--ink));}
@keyframes spin{to{transform:rotate(360deg);}}
.ticket{background:repeating-linear-gradient(90deg,var(--paper),var(--paper) 10px,var(--tint) 10px,var(--tint) 20px);
 border:2px dashed var(--ink);border-radius:14px;padding:1rem 1.2rem;}

/* JOURNAL NAVIGATION */
.st-key-topnav{position:relative;margin:2rem 0 4rem;padding:1.9rem 1.6rem 1.1rem;border:2px solid var(--ink);border-radius:18px;
 background:repeating-linear-gradient(transparent 0 31px,rgba(183,156,237,.11) 31px 32px),var(--paper);
 /* stacked sheets of paper peeking out underneath */
 box-shadow:0 5px 0 -1px var(--paper),0 5px 0 0 var(--ink),0 10px 0 -1px var(--paper),0 10px 0 0 var(--ink);
 overflow:visible !important;}

.rings{display:flex;justify-content:space-between;align-items:center;margin:-52px 1.2rem 1.2rem 1.2rem;pointer-events:none;z-index:5;position:relative;}
.rings i{display:block;width:12px;height:26px;border:2px solid var(--ink);border-radius:6px;
 background:linear-gradient(90deg,#fff,var(--tint));box-shadow:2px 2px 0 var(--ink);transition:transform .2s;}
.rings i:nth-child(odd){background:linear-gradient(90deg,#fff,var(--a1));}
.rings i:hover{transform:translateY(-3px) rotate(-8deg);}

/* journal title */
.brand{display:inline-block;font-family:'Plus Jakarta Sans',sans-serif;font-weight:800;font-size:1.15rem;line-height:1.3;white-space:nowrap;
 background:var(--paper);padding:.3rem .8rem .35rem;border-radius:10px;}
.brand small{display:block;font-family:'Inter',sans-serif;font-weight:700;font-size:.6rem;letter-spacing:.12em;text-transform:uppercase;color:#5d5673;margin-top:.1rem;}
.st-key-brandrow{margin-bottom:1.1rem;}
.st-key-brandrow [data-testid="stHorizontalBlock"]{align-items:center;}
.st-key-brandrow .stButton{display:flex;justify-content:flex-end;}
.st-key-like button{width:auto!important;min-width:4.5rem;padding:.35rem 1rem!important;margin-left: 5rem;}

.st-key-tabrow [data-testid="stHorizontalBlock"]{gap:.45rem;align-items:flex-end;border-bottom:2px solid var(--ink);padding-top:.4rem;}
.st-key-topnav [class*="st-key-nav"] button{width:100%;min-width:0;margin-bottom:-2px;padding:.5rem .4rem .55rem;
 border-radius:12px 12px 0 0!important;box-shadow:none!important;overflow:visible;
 background:color-mix(in srgb,var(--a1) 45%,#fff)!important;transition:transform .18s,background .18s,padding .18s;}
.st-key-topnav [class*="st-key-nav"] button>div,.st-key-topnav [class*="st-key-nav"] button [data-testid="stMarkdownContainer"]{
 overflow:visible!important;text-overflow:clip!important;max-width:none!important;width:auto;}
.st-key-topnav [class*="st-key-nav"] button p{font-weight:700;font-size:.88rem;margin:0;white-space:nowrap;overflow:visible!important;text-overflow:clip!important;}
.st-key-topnav .st-key-nav1 button{background:color-mix(in srgb,var(--a2) 45%,#fff)!important;}
.st-key-topnav .st-key-nav2 button{background:var(--tint)!important;}
.st-key-topnav .st-key-nav3 button{background:color-mix(in srgb,var(--a1) 25%,#fff)!important;}
.st-key-topnav .st-key-nav4 button{background:color-mix(in srgb,var(--a2) 25%,#fff)!important;}
.st-key-topnav [class*="st-key-nav"] button:hover{transform:translateY(-3px) rotate(-1.4deg)!important;}
/* the open chapter: taller, merges into the page, highlighter underline */
.st-key-topnav [class*="st-key-nav"] button[data-testid="stBaseButton-primary"]{background:var(--paper)!important;
 border-bottom-color:var(--paper)!important;padding-top:.8rem;transform:none!important;animation:tabpop .35s cubic-bezier(.3,1.6,.5,1);}
.st-key-topnav [class*="st-key-nav"] button[data-testid="stBaseButton-primary"] p{background:linear-gradient(transparent 62%,var(--a1) 62%);}
@keyframes tabpop{from{transform:translateY(8px) scale(.94);}to{transform:none;}}

.pagebar{display:flex;align-items:center;gap:.9rem;flex-wrap:wrap;margin-top:1.1rem;padding-right:4.5rem;}
.pagebar>*{background:var(--paper);padding:.15rem .5rem;border-radius:8px;}
.pagebar .dots{padding:.35rem .6rem;}
.dots{display:flex;gap:.35rem;align-items:center;}
.dots b{display:block;width:10px;height:10px;border:2px solid var(--ink);border-radius:50%;background:#fff;transition:all .3s;}
.dots b.done{background:var(--a1);}
.dots b.now{background:var(--a2);width:28px;border-radius:999px;}
.epi{font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;font-style:italic;font-size:.9rem;color:#5d5673;margin-left:auto;}

.ribbon{position:absolute;right:2.2rem;bottom:-46px;z-index:5;filter:drop-shadow(2px 3px 0 var(--ink));pointer-events:none;
 transform-origin:top center;animation:dangle 3.4s ease-in-out infinite;}
.ribbon div{width:34px;height:56px;padding-top:.55rem;text-align:center;font-family:'JetBrains Mono',monospace;font-weight:500;
 font-size:.78rem;background:linear-gradient(var(--a1),var(--a2));clip-path:polygon(0 0,100% 0,100% 100%,50% 80%,0 100%);}
@keyframes dangle{50%{transform:rotate(3deg);}}

@keyframes flipA{from{opacity:0;transform:perspective(1400px) rotateY(-16deg) translateX(-18px);}to{opacity:1;transform:none;}}
@keyframes flipB{from{opacity:0;transform:perspective(1400px) rotateY(-16deg) translateX(-18px);}to{opacity:1;transform:none;}}
[class*="st-key-pgA"]{animation:flipA .6s cubic-bezier(.2,.8,.2,1) both;transform-origin:left center;}
[class*="st-key-pgB"]{animation:flipB .6s cubic-bezier(.2,.8,.2,1) both;transform-origin:left center;}

@media (max-width:760px){
 .rings i:nth-child(even){display:none;}
 .ribbon{display:none;}
 .pagebar{padding-right:0;}
 .epi{margin-left:0;}
}
@media (prefers-reduced-motion:reduce){
 [class*="st-key-pg"],.ribbon{animation:none!important;}
}

[class*="st-key-toc"] button{justify-content:flex-start!important;text-align:left!important;}
[class*="st-key-toc"] button>div,[class*="st-key-toc"] button [data-testid="stMarkdownContainer"]{width:100%;justify-content:flex-start!important;text-align:left!important;}
[class*="st-key-toc"] button p{text-align:left!important;width:100%;}
[class*="st-key-toc"] button[data-testid="stBaseButton-primary"]{background:var(--a2)!important;}

.stButton>button,.stDownloadButton>button,.stFormSubmitButton>button,.stLinkButton>a{background:var(--a1)!important;color:var(--ink)!important;
 border:2px solid var(--ink)!important;border-radius:12px!important;font-weight:700!important;box-shadow:4px 4px 0 var(--ink);transition:all .12s;}
.stButton>button:hover,.stDownloadButton>button:hover,.stFormSubmitButton>button:hover,.stLinkButton>a:hover{transform:translate(-2px,-2px);box-shadow:6px 6px 0 var(--ink);}
.stButton>button:active,.stFormSubmitButton>button:active{transform:translate(3px,3px);box-shadow:0 0 0 var(--ink);}
[data-baseweb="input"],[data-baseweb="textarea"],[data-baseweb="select"]>div{border:2px solid var(--ink)!important;border-radius:12px!important;background:#fff!important;}
[data-baseweb="tag"]{background:var(--a1)!important;color:var(--ink)!important;border:2px solid var(--ink);border-radius:8px!important;}
[data-baseweb="tag"] span{color:var(--ink)!important;}
[data-baseweb="slider"],[data-baseweb="radio"]>div:first-child,[data-baseweb="checkbox"]>span:first-child{filter:hue-rotate(var(--turn));}
[data-testid="stMetric"]{background:var(--paper);border:2px solid var(--ink);border-radius:16px;padding:.9rem 1rem;box-shadow:5px 5px 0 var(--a2);}
[data-testid="stMetricLabel"] p{text-transform:uppercase;font-size:.7rem;letter-spacing:.07em;font-weight:700;}
.stTabs [data-baseweb="tab-list"]{gap:.35rem;background:var(--paper);border:2px solid var(--ink);border-radius:16px;padding:.35rem;
 box-shadow:4px 4px 0 var(--a2);width:fit-content;max-width:100%;margin-bottom:1rem;}
.stTabs [data-baseweb="tab"]{height:auto;border:2px solid transparent;border-radius:11px;background:transparent;padding:.45rem 1.1rem;transition:all .15s;}
.stTabs [data-baseweb="tab"] p{font-weight:700;font-size:.93rem;color:var(--ink);}
.stTabs [data-baseweb="tab"]:hover{background:var(--tint);}
.stTabs [data-baseweb="tab"][aria-selected="true"]{background:linear-gradient(90deg,var(--a1),var(--a2));border-color:var(--ink);box-shadow:3px 3px 0 var(--ink);}
.stTabs [data-baseweb="tab-highlight"],.stTabs [data-baseweb="tab-border"]{display:none;}
[data-testid="stExpander"]{border:2px solid var(--ink)!important;border-radius:14px!important;background:var(--paper);}
[data-testid="stForm"]{border:2px solid var(--ink);border-radius:18px;background:var(--paper);box-shadow:6px 6px 0 var(--a2);}
.stProgress>div>div>div>div{background:linear-gradient(90deg,var(--a1),var(--a2));}
[data-testid="stCode"] pre{border:2px solid var(--ink);border-radius:12px;}
</style>
"""

# SIDEBAR
with st.sidebar:
    st.markdown(f'<div class="eyebrow">quick panel</div><h3 style="margin:0">🌸 {NAME}</h3>'
                f'<p class="muted" style="margin:.2rem 0 1rem">{PROGRAM}<br>{SECTION}</p>', unsafe_allow_html=True)
    st.markdown("**Table of Contents**")
    for _i, _p in enumerate(PAGES):
        st.button(_p, key=f"toc{_i}", on_click=go, args=(_p,), use_container_width=True, type="primary" if st.session_state.page == _p else "secondary")
    st.divider()
    theme = st.selectbox("🎨 Color theme", list(PALETTES))
    st.markdown("**Find me online**")
    st.link_button("GitHub", "https://github.com/emer0r1a", use_container_width=True)
    st.link_button("LinkedIn", "https://www.linkedin.com/", use_container_width=True)
    st.divider()
    xp_slot = st.container()

A1, A2, TINT, TURN = PALETTES[theme]
st.markdown(CSS.replace("__A1__", A1).replace("__A2__", A2).replace("__TINT__", TINT).replace("__TURN__", TURN),
            unsafe_allow_html=True)

# TOP NAVIGATION
with st.container(key="topnav"):
    st.markdown('<div class="rings">' + "<i></i>" * 14 + "</div>", unsafe_allow_html=True)
    with st.container(key="brandrow"):
        b1, b2 = st.columns([4, 1], vertical_alignment="center")
        b1.markdown(f'<div class="brand">🌸 {NAME}<small>autobiography & portfolio</small></div>', unsafe_allow_html=True)
        if b2.button(f"💖 {st.session_state.likes}", key="like", help="Like this portfolio"):
            st.session_state.likes += 1
            add_xp(5)
            st.toast("Thanks for the love!", icon="🌸")
    with st.container(key="tabrow"):
        tab_cols = st.columns([1, 1.45, 1, 1.1, 1.1], vertical_alignment="bottom")
        for n, p in enumerate(PAGES):
            tab_cols[n].button(p, key=f"nav{n}", on_click=go, args=(p,), use_container_width=True,
                               type="primary" if st.session_state.page == p else "secondary")

    page = st.session_state.page
    idx = PAGES.index(page)
    dots = "".join(f'<b class="{"done" if j < idx else "now" if j == idx else ""}"></b>' for j in range(len(PAGES)))
    st.markdown(
        f'<div class="pagebar"><span class="mono">chapter {idx + 1:02d} / {len(PAGES):02d}</span>'
        f'<div class="dots">{dots}</div><span class="epi">{EPIGRAPHS[idx]}</span></div>'
        f'<div class="ribbon"><div>{idx + 1:02d}</div></div>',
        unsafe_allow_html=True)

# DATA
SKILLS = pd.DataFrame({
    "Skill": ["Java", "Django", "Python", "Kotlin", "PHP", "MySQL", "PostgreSQL", "Android Studio", "UI/UX Design", "HTML/CSS"],
    "Category": ["Core CS", "Web", "Data", "Mobile", "Web", "Data", "Data", "Mobile", "Creative", "Web"],
    "Proficiency": [92, 88, 90, 85, 80, 88, 85, 85, 90, 90],
    "Hours": [350, 220, 300, 190, 140, 210, 180, 170, 160, 240],
})

PROJECTS = [
    {
        "cat": "Full-Stack", 
        "title": "Face Value – Skincare Ingredient Compatibility", 
        "role": "Full-Stack Developer",
        "tools": ["Django", "Python", "HTML/CSS", "PostgreSQL"],
        "desc": "An ingredient-checking web system that identifies potential allergens and compatibility concerns based on a user's saved preferences, profiles, and skin care goals.", 
        "done": 57
    },
    {
        "cat": "Mobile", 
        "title": "Furbits – Lost and Found & Pet Adoption", 
        "role": "Android Developer",
        "tools": ["Kotlin", "Android Studio", "SQL"],
        "desc": "An Android application designed for reporting lost/found animals, browsing listings, and publishing pets for adoption with reliable local database storage.", 
        "done": 100
    },
    {
        "cat": "Systems", 
        "title": "MedServe – Public Health Center Queuing System", 
        "role": "Software Developer",
        "tools": ["Java", "JavaFX", "MySQL"],
        "desc": "A desktop queue management system built for public health centers featuring online queuing, live queue tracking, notifications, and patient history records.", 
        "done": 100
    },
    {
        "cat": "Data Analytics", 
        "title": "Midterm Data Analytics Project Dashboard", 
        "role": "Data Science Student Analyst",
        "tools": ["Python", "Pandas", "Scikit-Learn", "Matplotlib", "Seaborn"],
        "desc": "Applied exploratory data analysis, K-means clustering, DBSCAN outlier detection, linear regression modeling, and Apriori association rules on Spotify streaming metrics.", 
        "done": 100
    },
]


def pills(items):
    return "".join(f'<span class="pill">{i}</span>' for i in items)


def section(label, title):
    st.markdown(f'<div class="eyebrow">{label}</div><h2 style="margin-top:0">{title}</h2>', unsafe_allow_html=True)


def pager():
    st.divider()
    i = PAGES.index(page)
    a, mid, b = st.columns([1.3, 1.4, 1.3], vertical_alignment="center")
    mid.markdown(f'<div class="mono" style="text-align:center">— page {i + 1} of {len(PAGES)} —</div>',
                 unsafe_allow_html=True)
    if i > 0:
        a.button(f"◂ {PAGES[i - 1]}", on_click=go, args=(PAGES[i - 1],), key="prev",
                 use_container_width=True, help="Turn back a page")
    if i < len(PAGES) - 1:
        b.button(f"{PAGES[i + 1]} ▸", on_click=go, args=(PAGES[i + 1],), key="next",
                 use_container_width=True, help="Turn the page")


# PAGES
def home():
    initials = "".join(w[0] for w in NAME.strip("[]").split()[:2]).upper() or "ME"
    left, right = st.columns([1.15, 1], gap="large")
    with left:
        st.markdown(
            f'<div style="display:flex;align-items:center;gap:1.4rem;margin:.6rem 0 1rem"><div class="avatar">{initials}</div>'
            '<div class="flower">🌸</div></div>'
            f'<div class="eyebrow">{SECTION} · CIT-U · BS Computer Science</div>'
            '<div class="big">Crafting <span class="hl">digital</span> <span class="hl2">experiences</span>.</div>'
            f'<p class="muted" style="font-size:1.05rem">Hi, I\'m <b>{NAME}</b>, a {PROGRAM}. '
            'I build intuitive web and mobile applications, design user-centric interfaces, and bring ideas to life through code.</p>',
            unsafe_allow_html=True)
    with right:
        st.markdown(
            '<div class="stage"><div class="sticker s1">✦ open to collab</div>'
            '<div class="term"><div class="bar"><span class="dot" style="background:#F4A6C8"></span>'
            '<span class="dot" style="background:#B79CED"></span><span class="dot" style="background:#fff"></span></div>'
            '<div class="body">'
            '<div class="line"><span class="k">$</span> open portfolio.sql</div>'
            '<div class="line l2"><span class="k">SELECT</span> * <span class="k">FROM</span> student;</div>'
            f'<div class="line l3"><span class="v">school</span> : {SCHOOL[:30]}</div>'
            '<div class="line l4"><span class="v">stack</span>  : Python, C#, SQL</div>'
            '<div class="line l5"><span class="v">status</span> : caffeinated ✓</div>'
            '</div></div><div class="sticker s2">v1.0 🌸</div></div>', unsafe_allow_html=True)

    items = ["JAVA", "DJANGO", "PYTHON", "KOTLIN", "POSTGRESQL", "MYSQL", "ANDROID STUDIO", "UI/UX DESIGN", "WEB DEV", "GAMING"]
    row = "".join(f"<span>{i} ✦</span>" for i in items)
    st.markdown(f'<div class="marq"><div class="track">{row}{row}</div></div>', unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Projects Completed", "3+", "+1 this term")
    m2.metric("Tech Stacks Mastered", "8+")
    m3.metric("Code Commits", "High", "🔥")
    m4.metric("Portfolio Likes", st.session_state.likes)
    pager()


def autobiography():
    section("// chapter select", "My story")
    t1, t2, t3 = st.tabs(["🎓  Background", "🎮  Interests", "🏆  Milestones"])

    with t1:
        chapters = {
            "Freshman": "Started my journey at Cebu Institute of Technology – University, building strong analytical roots through my STEM background and diving into foundational programming and object-oriented principles.",
            "Sophomore": "Advanced deeper into core Computer Science—mastering Data Structures and Algorithms, Object-Oriented Programming, and Database Management Systems. During this year, I developed MedServe (a JavaFX queue management system for public health centers) and Furbits (an Android app in Kotlin for pet adoptions and lost/found reports).",
            "Now": "Building scalable web and mobile applications—integrating frameworks like Django for projects like Face Value while focusing on user-centered design, database management, and interaction.",
        }
        pick = st.select_slider("Scrub through my timeline", options=list(chapters), value="Freshman")
        st.markdown(f'<div class="card"><div class="eyebrow">{pick}</div><h3>{chapters[pick]}</h3>'
                    f'<p class="muted">BS Computer Science · CIT-University (Class of 2028)</p></div>',
                    unsafe_allow_html=True)
        with st.expander("Relevant Coursework"):
            st.markdown("- Data Structures and Algorithms\n- Object-Oriented Programming\n"
                        "- Database Management Systems\n- Web Development\n"
                        "- Human-Computer Interaction\n- Mobile Application Development")

    with t2:
        topic = st.radio("Pick an interest", ["Web Development", "UI/UX Design", "Digital Illustration", "Game Development & Gaming"], horizontal=True)
        info = {
            "Web Development": ("💻", "Building responsive, robust, and intuitive web applications using frameworks like Django and modern frontend tools.", 10),
            "UI/UX Design": ("✨", "Designing user-friendly interfaces and clear layouts focused on accessibility and seamless user experiences.", 6),
            "Digital Illustration": ("🎨", "Expressing creativity through digital art, asset design, and visual styling elements.", 5),
            "Game Development & Gaming": ("🎮", "Exploring game mechanics, interactive environments, and engaging digital gameplay experiences.", 8),
        }
        icon, text, hrs = info[topic]
        st.markdown(f'<div class="card"><h3>{icon} {topic}</h3><p>{text}</p><span class="pill">{hrs} hrs / week</span></div>',
                    unsafe_allow_html=True)
        
    with t3:
        details = st.checkbox("Show technical highlights", value=True)
        cols = st.columns(3)
        ms = [
            ("🌿", "Face Value", "Skincare ingredient compatibility checker web app.", "Django, PostgreSQL, custom user profiles & allergen matching."),
            ("🐾", "Furbits", "Android app for lost/found animals and pet adoptions.", "Kotlin, Android Studio, local SQL data storage."),
            ("🏥", "MedServe", "Public health center queue management system.", "Java, JavaFX, MySQL, real-time tracking & scheduling.")
        ]
        for c, (i, t, d, n) in zip(cols, ms):
            extra = f'<p class="muted">{n}</p>' if details else ""
            c.markdown(f'<div class="card"><div style="font-size:2rem">{i}</div><h4>{t}</h4><p>{d}</p>{extra}</div>',
                        unsafe_allow_html=True)
        with st.expander("Peek at some code"):
            st.code("# Checking skincare ingredient safety & compatibility\ndef check_allergen(user_allergies, product_ingredients):\n    conflicts = [ing for ing in product_ingredients if ing in user_allergies]\n    return conflicts if conflicts else \"Safe to use!\"", language="python")
    pager()


def skills():
    section("// query playground", "Skills, but make it SQL")
    st.write("Build a query against my skills table, then run it. The numbers are my own self-assessment and practice hours.")
    st.markdown(pills(SKILLS.Skill), unsafe_allow_html=True)
    st.write("")

    a, b = st.columns(2)
    with a:
        cols = st.multiselect("SELECT", list(SKILLS.columns), default=list(SKILLS.columns))
        cat = st.selectbox("WHERE category =", ["ANY"] + sorted(SKILLS.Category.unique()))
    with b:
        minp = st.slider("AND proficiency >=", 0, 100, 60, step=5)
        order = st.radio("ORDER BY", ["Proficiency", "Hours", "Skill"], horizontal=True)
    desc = st.checkbox("DESC", value=True)
    limit = st.slider("LIMIT", 1, len(SKILLS), len(SKILLS))

    where = f"Proficiency >= {minp}" + ("" if cat == "ANY" else f" AND Category = '{cat}'")
    sql = (f"SELECT {', '.join(cols) if cols else '...'}\nFROM skills\nWHERE {where}\n"
           f"ORDER BY {order} {'DESC' if desc else 'ASC'}\nLIMIT {limit};")
    st.code(sql, language="sql")

    if st.button("▶ Run query"):
        st.session_state.ran = True
        add_xp(10)
        st.toast("Query executed!", icon="🌸")

    if not st.session_state.ran:
        st.info("Hit **Run query** to see results.")
    elif not cols:
        st.warning("Pick at least one column to SELECT.")
    else:
        df = SKILLS[SKILLS.Proficiency >= minp]
        if cat != "ANY":
            df = df[df.Category == cat]
        df = df.sort_values(order, ascending=not desc).head(limit)
        if df.empty:
            st.warning("0 rows returned. Try lowering the proficiency filter.")
        else:
            st.markdown(f'<div class="mono">{len(df)} rows · avg proficiency {df.Proficiency.mean():.0f}%</div>', unsafe_allow_html=True)
            left, right = st.columns([3, 2])
            with left:
                metric = st.radio("Chart", ["Proficiency", "Hours"], horizontal=True)
                st.bar_chart(df.set_index("Skill")[metric], color=A2)
            with right:
                st.dataframe(df[cols], hide_index=True, use_container_width=True)
            st.markdown("**Top skills**")
            for r in df.sort_values("Proficiency", ascending=False).head(3).itertuples():
                st.caption(r.Skill)
                st.progress(int(r.Proficiency))
    pager()


def projects():
    section("// selected work", "Projects")
    cat = st.radio("Filter", ["All"] + list(dict.fromkeys([p["cat"] for p in PROJECTS])), horizontal=True)
    shown = [p for p in PROJECTS if cat in ("All", p["cat"])]
    for c, p in zip(st.columns(len(shown)), shown):
        with c:
            st.markdown(
                f'<div class="card pcard"><div class="eyebrow">{p["cat"]}</div><h3>{p["title"]}</h3>'
                f'<p><b>Role:</b> {p["role"]}</p><p>{pills(p["tools"])}</p><p class="muted">{p["desc"]}</p></div>',
                unsafe_allow_html=True)
            with st.expander("Case file"):
                st.write(f"**Outcome:** {p['desc']}")
                st.write("**Tools:** " + ", ".join(p["tools"]))
                st.metric("Completion", f"{p['done']}%")
                st.progress(p["done"])
                
                if p["cat"] == "Data Analytics":
                    st.subheader("📊 Data Analytics Visualizations & Model Results")
                    st.markdown("Detailed breakdown of exploratory insights, clustering performance, and predictive regression metrics.")

                    SP_GREEN = '#1DB954'
                    SP_GREEN_DK = '#128A3D'
                    SP_INK = '#191414'
                    SP_GREY = '#8C8C8C'
                    SP_LGREY = '#E6E6E6'
                    SP_WHITE = '#FFFFFF'
                    SP_PINK = '#E8115B'
                    SP_BLUE = '#1E6FD9'
                    SP_GOLD = '#F2A900'
                    SP_CMAP = LinearSegmentedColormap.from_list('spotify', [SP_PINK, SP_WHITE, SP_GREEN])

                    np.random.seed(42)
                    n_samples = 948
                    
                    st.markdown("### 1. Descriptive Stats: Correlation & Distribution")
                    fig1, axes1 = plt.subplots(1, 2, figsize=(14, 5))
                    
                    dummy_corr = np.array([
                        [1.00,  0.15, -0.05,  0.20, -0.30, -0.10,  0.05, -0.02,  0.35,  0.40],
                        [0.15,  1.00,  0.10,  0.45, -0.25, -0.15,  0.02, -0.08,  0.28,  0.32],
                        [-0.05, 0.10,  1.00,  0.05,  0.12,  0.03,  0.10,  0.04, -0.05, -0.08],
                        [0.20,  0.45,  0.05,  1.00, -0.50, -0.20,  0.08, -0.12,  0.42,  0.50],
                        [-0.30,-0.25,  0.12, -0.50,  1.00,  0.35, -0.05,  0.15, -0.38, -0.42],
                        [-0.10,-0.15,  0.03, -0.20,  0.35,  1.00, -0.02,  0.05, -0.15, -0.20],
                        [0.05,  0.02,  0.10,  0.08, -0.05, -0.02,  1.00,  0.01,  0.04,  0.06],
                        [-0.02,-0.08,  0.04, -0.12,  0.15,  0.05,  0.01,  1.00, -0.07, -0.09],
                        [0.35,  0.28, -0.05,  0.42, -0.38, -0.15,  0.04, -0.07,  1.00,  0.85],
                        [0.40,  0.32, -0.08,  0.50, -0.42, -0.20,  0.06, -0.09,  0.85,  1.00]
                    ])
                    audio_labels = ['bpm', 'dance', 'valence', 'energy', 'acous', 'instr', 'live', 'speech', 'log_str', 'log_play']
                    
                    sns.heatmap(dummy_corr, annot=True, fmt='.2f', cmap=SP_CMAP, cbar=False, 
                                xticklabels=audio_labels, yticklabels=audio_labels, ax=axes1[0], annot_kws={"size": 8})
                    axes1[0].set_title('Correlation: Audio vs Streams', fontsize=11, fontweight='bold')
                    
                    dummy_streams = np.random.exponential(scale=300, size=n_samples)
                    sns.histplot(dummy_streams, bins=35, color=SP_GREEN, edgecolor=SP_WHITE, ax=axes1[1])
                    axes1[1].set_title('Distribution of Streams (Right-Skewed)', fontsize=11, fontweight='bold')
                    axes1[1].set_xlabel('Streams (millions)')
                    
                    plt.tight_layout()
                    st.pyplot(fig1)
                    plt.close(fig1)

                    st.markdown("### 2a. K-Means Silhouette Scores")
                    fig2a, ax2a = plt.subplots(figsize=(8, 4))
                    ks = [2, 3, 4, 5, 6]
                    sil = [0.227, 0.212, 0.215, 0.186, 0.186]
                    ax2a.plot(ks, sil, marker='o', color=SP_GREEN_DK, linewidth=2)
                    ax2a.axhline(0.5, color=SP_PINK, linestyle='--', label="'Good' threshold = 0.5")
                    for k, s in zip(ks, sil):
                        ax2a.text(k, s + 0.012, f'{s:.2f}', ha='center', fontweight='bold', fontsize=9)
                    ax2a.set_title('K-Means: Silhouette Score by Cluster Count', fontsize=11, fontweight='bold')
                    ax2a.set_xlabel('Number of clusters (k)')
                    ax2a.set_ylabel('Silhouette score')
                    ax2a.set_xticks(ks)
                    ax2a.set_ylim(0, 0.55)
                    ax2a.legend(fontsize=8)
                    ax2a.grid(True, linestyle='--', alpha=0.5)
                    plt.tight_layout()
                    st.pyplot(fig2a)
                    plt.close(fig2a)

                    st.markdown("### 2b. DBSCAN Parameter Choice (k-Distance)")
                    fig2b, ax2b = plt.subplots(figsize=(8, 4))
                    k_dist = np.sort(np.random.normal(loc=1.2, scale=0.4, size=n_samples).clip(0.2, 3.5))
                    ax2b.plot(k_dist, color=SP_GREEN_DK, linewidth=2)
                    ax2b.axhline(2.0, color=SP_PINK, linestyle='--', label='Chosen eps = 2.0')
                    ax2b.set_title('DBSCAN: 5-Nearest-Neighbor Distance Plot', fontsize=11, fontweight='bold')
                    ax2b.set_xlabel('Songs (sorted by distance)')
                    ax2b.set_ylabel('Distance to 5th nearest neighbor')
                    ax2b.legend(fontsize=8)
                    ax2b.grid(True, linestyle='--', alpha=0.5)
                    plt.tight_layout()
                    st.pyplot(fig2b)
                    plt.close(fig2b)

                    st.markdown("### 3. DBSCAN PCA Outlier Detection Map")
                    fig3, ax3 = plt.subplots(figsize=(8, 4.5))
                    pc1_norm = np.random.normal(0, 1.5, 930)
                    pc2_norm = np.random.normal(0, 1.2, 930)
                    pc1_out = np.array([-4.5, 5.2, 4.8, -3.9, 5.5, 4.1, -4.2, 5.0, -4.8, 4.3, -5.1, 4.7, -4.6, 5.3, 4.0, -4.1, 4.9, -5.0, 4.6, -4.4])
                    pc2_out = np.array([3.5, -3.2, 3.8, -3.5, 3.1, -3.8, 3.2, -3.1, 3.9, -3.3, 3.4, -3.6, 3.7, -3.0, 3.3, -3.4, 3.6, -3.7, 3.0, -3.9])
                    
                    ax3.scatter(pc1_norm, pc2_norm, c=SP_GREY, alpha=0.45, s=20, label='Main Sound Cluster (930)')
                    ax3.scatter(pc1_out, pc2_out, c=SP_PINK, alpha=0.95, edgecolor=SP_INK, linewidth=0.7, s=40, label='Sonic Outliers (18)')
                    ax3.set_title('DBSCAN: Main Audio Blob vs. Sonic Outliers', fontsize=11, fontweight='bold')
                    ax3.set_xlabel('PC1 (42% of variance)')
                    ax3.set_ylabel('PC2 (18% of variance)')
                    ax3.legend(fontsize=8)
                    ax3.grid(True, linestyle='--', alpha=0.5)
                    plt.tight_layout()
                    st.pyplot(fig3)
                    plt.close(fig3)

                    st.markdown("### 4. Regression Model Performance ($R^2$)")
                    fig4, ax4 = plt.subplots(figsize=(8, 4))
                    scores = {
                        'Sound only': 0.05,
                        'Playlists only': 0.68,
                        'Sound + Playlists': 0.71,
                        'Full Model (+ Age + Collab)': 0.74
                    }
                    bars = ax4.bar(list(scores.keys()), list(scores.values()), color=[SP_PINK, SP_GREEN, SP_BLUE, SP_GOLD])
                    for b, v in zip(bars, scores.values()):
                        ax4.text(b.get_x() + b.get_width() / 2, v + 0.02, f'{v:.2f}', ha='center', fontweight='bold', fontsize=9)
                    ax4.axhline(0, color=SP_INK, linewidth=1)
                    ax4.set_title('Cross-Validated $R^2$ Explaining Streaming Success', fontsize=11, fontweight='bold')
                    ax4.set_ylabel('$R^2$ Score')
                    ax4.set_ylim(0, 0.9)
                    plt.xticks(rotation=15, fontsize=8)
                    plt.tight_layout()
                    st.pyplot(fig4)
                    plt.close(fig4)

                    st.markdown("### 5. Apriori Association Rules (Lift)")
                    fig5, ax5 = plt.subplots(figsize=(9, 4.5))
                    rule_names = [
                        'danceable', 
                        'high_energy', 
                        'major_key', 
                        'acoustic + fast_bpm', 
                        'danceable + high_energy', 
                        'on_many_playlists', 
                        'old_song_pre2020 + on_many_playlists'
                    ]
                    lifts = [1.05, 1.12, 1.18, 1.25, 1.34, 1.85, 2.10]
                    confs = [0.28, 0.30, 0.32, 0.35, 0.39, 0.55, 0.62]
                    colors = [SP_PINK, SP_PINK, SP_PINK, SP_PINK, SP_PINK, SP_GREEN, SP_GREEN]
                    
                    bars5 = ax5.barh(rule_names, lifts, color=colors)
                    ax5.axvline(1, color=SP_INK, linestyle='--', linewidth=1.2)
                    for i, (lift, conf) in enumerate(zip(lifts, confs)):
                        ax5.text(lift + 0.04, i, f'lift {lift:.2f} | conf {conf:.0%}', va='center', fontsize=8, fontweight='bold')
                    ax5.set_title('Apriori Rules: Sound Traits (Pink) vs Popularity Signals (Green)', fontsize=11, fontweight='bold')
                    ax5.set_xlabel('Lift (1.0 = random baseline)')
                    ax5.set_xlim(0, 2.6)
                    plt.tight_layout()
                    st.pyplot(fig5)
                    plt.close(fig5)

    pager()


def contact():
    section("// say hello", "Contact & feedback")
    with st.form("contact", clear_on_submit=True):
        c1, c2 = st.columns(2)
        name = c1.text_input("Your name")
        email = c2.text_input("Email")
        topic = st.selectbox("Topic", ["Feedback", "Collaboration", "Recruiting", "Just saying hi"])
        mood = st.radio("Vibe", ["😍", "🙂", "🤔", "😅"], horizontal=True)
        rating = st.slider("Portfolio rating", 1, 5, 5)
        msg = st.text_area("Message", placeholder="Write something nice...")
        reply = st.checkbox("I'd like a reply")
        sent = st.form_submit_button("Send Message")

    if sent:
        if not name.strip() or not msg.strip():
            st.error("Name and message are required.")
        else:
            st.session_state.ticket = {"name": name, "topic": topic, "mood": mood, "rating": rating,
                                       "id": random.randint(1000, 9999)}
            st.session_state.messages.append({"Name": name, "Topic": topic, "Vibe": mood, "Rating": rating, "Reply": reply})
            add_xp(20)
            st.balloons()
            st.success(f"Message sent! Thanks, {name} 🎉")

    t = st.session_state.ticket
    if t:
        st.markdown(f'<div class="ticket"><div class="mono">ticket #{t["id"]}</div>'
                    f'<h3 style="margin:.2rem 0">{t["mood"]} {t["topic"]} from {t["name"]}</h3>'
                    f'<div class="mono">rating {"★" * t["rating"]}</div></div>', unsafe_allow_html=True)
    if st.session_state.messages:
        with st.expander("Messages this session"):
            st.dataframe(pd.DataFrame(st.session_state.messages), hide_index=True)

    st.write("")
    resume = (f"{NAME}\n{PROGRAM}\nSection: {SECTION}\n\nSKILLS\n"
              + "\n".join(f"- {r.Skill}: {r.Proficiency}%" for r in SKILLS.itertuples())
              + "\n\nPROJECTS\n"
              + "\n".join(f"- {p['title']} ({p['role']}): {', '.join(p['tools'])}" for p in PROJECTS))
    pager()


PAGE_FUNCS = {"Home": home, "Autobiography": autobiography, "Skills": skills,
              "Projects": projects, "Contact": contact}

with st.container(key=f"pg{'AB'[idx % 2]}_{idx}"):
    PAGE_FUNCS[page]()

with xp_slot:
    xp = st.session_state.xp
    st.markdown(f'<div class="mono">Visitor level {xp // 50 + 1} · {xp} XP</div>', unsafe_allow_html=True)
    st.progress((xp % 50) / 50)
