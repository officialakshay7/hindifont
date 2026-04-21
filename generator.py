import os, datetime

BASE = "/home/claude/site"

# ══════════════════════════════════════════════════
# DESIGN SYSTEM - Deep ink + Turmeric gold aesthetic
# Indian editorial / premium content site
# ══════════════════════════════════════════════════

GF = "https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;0,900;1,600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Noto+Sans+Devanagari:wght@400;500;600;700&display=swap"

CSS = """
:root{
  --ink:#0D0C0A;--ink2:#1A1916;--ink3:#2C2A26;
  --gold:#D97706;--gold2:#F59E0B;--gold3:#FDE68A;
  --cream:#FEFCE8;--warm:#FFFBF0;--white:#FFFFFF;
  --stone:#6B6460;--stone2:#9C948E;--stone3:#C8C2BC;
  --border:#EDE9E4;--border2:#D6D0CA;
  --green:#15803D;--red:#B91C1C;--blue:#1D4ED8;
  --r4:4px;--r8:8px;--r12:12px;--r16:16px;--r24:24px;--r32:32px;
  --s1:0 1px 3px rgba(0,0,0,.06);
  --s2:0 4px 16px rgba(0,0,0,.08);
  --s3:0 12px 40px rgba(0,0,0,.10);
  --s4:0 24px 64px rgba(0,0,0,.12);
  --tr:.2s cubic-bezier(.4,0,.2,1);
  --fd:'Playfair Display',Georgia,serif;
  --fb:'Plus Jakarta Sans',system-ui,sans-serif;
  --fh:'Noto Sans Devanagari',serif;
}
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
html{font-size:16px;scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{font-family:var(--fb);background:var(--warm);color:var(--ink);line-height:1.6;
  -webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:inherit;text-decoration:none}
img{max-width:100%;display:block}
button{font-family:var(--fb);cursor:pointer;border:none;background:none}
ul,ol{list-style:none}
input,textarea{font-family:var(--fb)}

/* ── LAYOUT ── */
.wrap{max-width:1200px;margin:0 auto;padding:0 20px}
.wrap-sm{max-width:860px;margin:0 auto;padding:0 20px}
.wrap-xs{max-width:680px;margin:0 auto;padding:0 20px}

/* ── HEADER ── */
#hdr{
  position:sticky;top:0;z-index:500;
  background:rgba(13,12,10,.97);
  backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);
  border-bottom:1px solid rgba(255,255,255,.06);
}
.hdr-inner{display:flex;align-items:center;justify-content:space-between;height:62px;gap:16px}
.logo{display:flex;align-items:center;gap:10px;flex-shrink:0}
.logo-mark{
  width:36px;height:36px;border-radius:10px;
  background:linear-gradient(135deg,var(--gold),var(--gold2));
  display:flex;align-items:center;justify-content:center;
  font-family:var(--fh);font-size:1.15rem;color:#fff;font-weight:700;
  box-shadow:0 2px 8px rgba(217,119,6,.4);
}
.logo-text{font-family:var(--fd);font-size:1.25rem;font-weight:700;color:#fff;letter-spacing:-.01em}
.logo-text span{color:var(--gold2)}

.nav-desk{display:flex;align-items:center;gap:2px}
.nav-desk a{
  color:rgba(255,255,255,.6);font-size:.85rem;font-weight:500;
  padding:6px 12px;border-radius:20px;transition:var(--tr);
}
.nav-desk a:hover{color:#fff;background:rgba(255,255,255,.08)}
.nav-desk a.active{color:var(--gold2)}
.nav-btn{
  background:var(--gold);color:var(--ink) !important;
  padding:7px 16px !important;border-radius:20px !important;
  font-weight:700 !important;font-size:.82rem !important;
  transition:var(--tr) !important;
}
.nav-btn:hover{background:var(--gold2) !important;transform:translateY(-1px)}

/* hamburger */
.ham{
  display:none;flex-direction:column;gap:5px;
  width:38px;height:38px;align-items:center;justify-content:center;
  border-radius:var(--r8);transition:var(--tr);
}
.ham span{display:block;width:20px;height:2px;background:#fff;border-radius:2px;transition:var(--tr);transform-origin:center}
.ham:hover{background:rgba(255,255,255,.08)}
.ham.on span:nth-child(1){transform:translateY(7px) rotate(45deg)}
.ham.on span:nth-child(2){opacity:0;transform:scaleX(0)}
.ham.on span:nth-child(3){transform:translateY(-7px) rotate(-45deg)}

/* mobile drawer */
.mob-nav{
  display:none;position:fixed;inset:62px 0 0;
  background:rgba(13,12,10,.99);backdrop-filter:blur(24px);
  -webkit-backdrop-filter:blur(24px);z-index:499;
  overflow-y:auto;flex-direction:column;
  padding:24px 20px 40px;
  animation:drawerIn .25s ease both;
}
@keyframes drawerIn{from{opacity:0;transform:translateY(-8px)}to{opacity:1;transform:none}}
.mob-nav.on{display:flex}
.mob-sec{color:rgba(255,255,255,.3);font-size:.68rem;font-weight:700;
  letter-spacing:1.5px;text-transform:uppercase;padding:20px 12px 8px}
.mob-sec:first-child{padding-top:4px}
.mob-nav a{
  color:rgba(255,255,255,.75);font-size:.975rem;font-weight:500;
  padding:13px 12px;border-radius:var(--r12);transition:var(--tr);
  border-bottom:1px solid rgba(255,255,255,.05);
}
.mob-nav a:hover{color:#fff;background:rgba(255,255,255,.06)}
.mob-cta{
  margin-top:20px;background:var(--gold);color:var(--ink) !important;
  text-align:center;padding:15px 12px !important;
  border-radius:var(--r16) !important;font-weight:700 !important;
  font-size:.975rem !important;border:none !important;
}

/* ── BREADCRUMB ── */
.crumb{background:var(--white);border-bottom:1px solid var(--border);padding:10px 0;font-size:.78rem}
.crumb ol{display:flex;align-items:center;flex-wrap:wrap;gap:4px;color:var(--stone2)}
.crumb li::after{content:"›";margin-left:4px;color:var(--stone3)}
.crumb li:last-child::after{display:none}
.crumb a{color:var(--gold);transition:var(--tr)}
.crumb a:hover{color:var(--gold2)}

/* ── HERO ── */
.hero{
  background:var(--ink);position:relative;overflow:hidden;
  padding:88px 0 72px;
}
.hero-bg{
  position:absolute;inset:0;pointer-events:none;
  background:
    radial-gradient(ellipse 60% 70% at 5% 50%,rgba(217,119,6,.14) 0%,transparent 60%),
    radial-gradient(ellipse 40% 50% at 90% 10%,rgba(245,158,11,.08) 0%,transparent 50%),
    radial-gradient(ellipse 30% 40% at 75% 80%,rgba(217,119,6,.06) 0%,transparent 50%);
}
.hero-grid-bg{
  position:absolute;inset:0;pointer-events:none;opacity:.04;
  background-image:linear-gradient(rgba(255,255,255,.3) 1px,transparent 1px),
    linear-gradient(90deg,rgba(255,255,255,.3) 1px,transparent 1px);
  background-size:48px 48px;
}
.hero-deva-bg{
  position:absolute;right:-30px;top:50%;transform:translateY(-50%);
  font-family:var(--fh);font-size:18vw;font-weight:700;color:rgba(255,255,255,.025);
  line-height:1;pointer-events:none;user-select:none;white-space:nowrap;
}
.eyebrow{
  display:inline-flex;align-items:center;gap:8px;
  background:rgba(217,119,6,.15);border:1px solid rgba(217,119,6,.3);
  color:var(--gold2);padding:5px 14px;border-radius:20px;
  font-size:.72rem;font-weight:700;letter-spacing:.8px;text-transform:uppercase;
  margin-bottom:20px;
}
.eyebrow-dot{width:6px;height:6px;border-radius:50%;background:var(--gold);animation:blink 2s infinite}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.3}}
.hero h1{
  font-family:var(--fd);
  font-size:clamp(2.2rem,5.5vw,4rem);
  font-weight:900;color:#fff;line-height:1.07;
  letter-spacing:-.03em;margin-bottom:18px;
}
.hero h1 .hi{font-family:var(--fh);font-size:.9em;display:block;margin-bottom:4px;opacity:.85}
.hero h1 em{color:var(--gold2);font-style:italic}
.hero-sub{color:rgba(255,255,255,.5);font-size:1rem;line-height:1.75;max-width:520px;margin-bottom:32px}

/* search */
.search-box{max-width:540px;position:relative;margin-bottom:44px}
.search-box input{
  width:100%;background:rgba(255,255,255,.07);
  border:1.5px solid rgba(255,255,255,.1);color:#fff;
  font-family:var(--fb);font-size:.93rem;
  padding:14px 56px 14px 18px;border-radius:var(--r12);outline:none;transition:var(--tr);
}
.search-box input::placeholder{color:rgba(255,255,255,.3)}
.search-box input:focus{
  background:rgba(255,255,255,.1);border-color:var(--gold);
  box-shadow:0 0 0 4px rgba(217,119,6,.15);
}
.search-box button{
  position:absolute;right:6px;top:50%;transform:translateY(-50%);
  background:var(--gold);color:var(--ink);width:38px;height:38px;
  border-radius:var(--r8);font-size:.95rem;transition:var(--tr);
  display:flex;align-items:center;justify-content:center;
}
.search-box button:hover{background:var(--gold2);transform:translateY(-50%) scale(1.05)}

.hero-stats{display:flex;flex-wrap:wrap;gap:36px}
.stat-n{font-family:var(--fd);font-size:2rem;font-weight:700;color:#fff;line-height:1}
.stat-l{font-size:.72rem;color:rgba(255,255,255,.4);text-transform:uppercase;letter-spacing:.8px;margin-top:3px}

/* ── SECTIONS ── */
.sec{padding:64px 0}
.sec-tint{background:var(--cream)}
.sec-dark{background:var(--ink2)}
.sec-white{background:var(--white)}

.sec-tag{
  display:inline-block;background:#FEF3C7;color:#92400E;
  font-size:.68rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;
  padding:3px 10px;border-radius:5px;margin-bottom:10px;
}
.sec-tag-dk{background:rgba(217,119,6,.15);color:var(--gold2)}
.sec-title{
  font-family:var(--fd);font-size:clamp(1.5rem,2.8vw,2rem);
  font-weight:700;color:var(--ink);letter-spacing:-.02em;margin-bottom:6px;
}
.sec-title-dk{color:#fff}
.sec-sub{color:var(--stone);font-size:.9rem;max-width:480px}
.sec-hdr{margin-bottom:36px}
.sec-hdr-row{display:flex;align-items:flex-end;justify-content:space-between;gap:16px;flex-wrap:wrap;margin-bottom:36px}
.view-all{
  display:inline-flex;align-items:center;gap:5px;
  color:var(--gold);font-size:.82rem;font-weight:600;transition:var(--tr);white-space:nowrap;
}
.view-all:hover{color:var(--gold2);gap:9px}

/* ── FILTER PILLS ── */
.pills{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:28px}
.pill{
  background:var(--white);border:1.5px solid var(--border2);
  color:var(--ink3);font-size:.8rem;font-weight:600;
  padding:7px 16px;border-radius:40px;transition:var(--tr);cursor:pointer;
}
.pill:hover,.pill.on{background:var(--gold);color:var(--ink);border-color:var(--gold);box-shadow:0 4px 12px rgba(217,119,6,.25)}

/* ── FONT CARDS ── */
.fonts-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:18px}
.font-card{
  background:var(--white);border:1.5px solid var(--border);
  border-radius:var(--r16);overflow:hidden;transition:var(--tr);display:block;color:inherit;
}
.font-card:hover{border-color:var(--gold);box-shadow:var(--s3);transform:translateY(-4px)}
.fc-prev{
  background:linear-gradient(135deg,#FFFBF0,#FEF9EC);
  padding:28px 24px 22px;border-bottom:1.5px solid var(--border);
  min-height:108px;display:flex;flex-direction:column;
  align-items:center;justify-content:center;position:relative;
}
.fc-prev::after{
  content:'';position:absolute;bottom:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,var(--border2),transparent);
}
.fc-deva{font-family:var(--fh);font-size:1.85rem;color:var(--ink3);text-align:center;line-height:1.5}
.fc-lat{font-size:.78rem;color:var(--stone2);margin-top:4px;text-align:center}
.fc-body{padding:15px 18px 17px}
.fc-name{font-weight:700;font-size:.9rem;color:var(--ink);margin-bottom:3px}
.fc-desc{font-size:.77rem;color:var(--stone);line-height:1.5;margin-bottom:12px;
  display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.fc-foot{display:flex;align-items:center;justify-content:space-between;gap:8px}
.tags{display:flex;gap:5px;flex-wrap:wrap}
.tag{font-size:.63rem;font-weight:700;text-transform:uppercase;letter-spacing:.3px;padding:2px 8px;border-radius:4px}
.te{background:#FEF3C7;color:#92400E}
.tu{background:#D1FAE5;color:#065F46}
.tw{background:#EDE9FE;color:#4C1D95}
.ta{background:#FEE2E2;color:#991B1B}
.tc{background:#FDF2F8;color:#831843}
.tf{background:#ECFDF5;color:#065F46}
.dl-btn{
  display:inline-flex;align-items:center;gap:5px;
  background:var(--gold);color:var(--ink);
  font-size:.73rem;font-weight:700;padding:6px 12px;border-radius:var(--r8);
  transition:var(--tr);white-space:nowrap;flex-shrink:0;
}
.dl-btn:hover{background:var(--gold2);transform:translateY(-1px)}

/* ── CATEGORY CARDS ── */
.cat-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:12px}
.cat-card{
  background:var(--white);border:1.5px solid var(--border);
  border-radius:var(--r12);padding:20px 14px;text-align:center;
  transition:var(--tr);display:block;color:inherit;
}
.cat-card:hover{border-color:var(--gold);box-shadow:var(--s2);transform:translateY(-3px)}
.cat-icon{font-family:var(--fh);font-size:2rem;color:var(--gold);margin-bottom:8px;line-height:1}
.cat-name{font-weight:700;font-size:.83rem;color:var(--ink);margin-bottom:2px}
.cat-cnt{font-size:.7rem;color:var(--stone2)}

/* ── BLOG CARDS ── */
.blog-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:18px}
.bc{
  background:var(--white);border:1.5px solid var(--border);
  border-radius:var(--r16);overflow:hidden;display:block;color:inherit;transition:var(--tr);
}
.bc:hover{border-color:var(--gold);box-shadow:var(--s3);transform:translateY(-4px)}
.bc-thumb{
  background:linear-gradient(135deg,var(--ink2),var(--ink3));
  height:140px;display:flex;align-items:center;justify-content:center;
  font-family:var(--fh);font-size:4rem;color:rgba(255,255,255,.1);
  position:relative;overflow:hidden;
}
.bc-thumb::after{content:'';position:absolute;inset:0;background:linear-gradient(135deg,rgba(217,119,6,.18),transparent)}
.bc-body{padding:18px}
.bc-cat{
  display:inline-block;background:#FEF3C7;color:#92400E;
  font-size:.65rem;font-weight:700;text-transform:uppercase;letter-spacing:.5px;
  padding:2px 9px;border-radius:4px;margin-bottom:8px;
}
.bc h3{font-weight:700;font-size:.9rem;color:var(--ink);line-height:1.45;margin-bottom:7px}
.bc p{font-size:.78rem;color:var(--stone);line-height:1.6;
  display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.bc-more{display:inline-flex;align-items:center;gap:4px;margin-top:12px;
  color:var(--gold);font-size:.78rem;font-weight:600;transition:var(--tr)}
.bc:hover .bc-more{gap:8px}

/* ── CTA BANNER ── */
.cta-band{
  background:linear-gradient(135deg,var(--ink),var(--ink3));
  border-radius:var(--r24);padding:44px 48px;
  display:flex;align-items:center;justify-content:space-between;
  gap:28px;flex-wrap:wrap;position:relative;overflow:hidden;
}
.cta-band::before{
  content:'';position:absolute;right:-60px;top:-60px;
  width:280px;height:280px;border-radius:50%;
  background:radial-gradient(circle,rgba(217,119,6,.18),transparent 70%);
}
.cta-band h2{font-family:var(--fd);font-size:1.7rem;color:#fff;margin-bottom:7px;letter-spacing:-.02em}
.cta-band p{color:rgba(255,255,255,.5);font-size:.9rem}
.cta-band-btn{
  background:var(--gold);color:var(--ink);
  padding:13px 28px;border-radius:var(--r12);
  font-weight:700;font-size:.9rem;white-space:nowrap;
  transition:var(--tr);display:inline-block;flex-shrink:0;
}
.cta-band-btn:hover{background:var(--gold2);transform:translateY(-2px);box-shadow:0 8px 24px rgba(217,119,6,.3)}

/* ── FAQ ── */
.faq-item{border-bottom:1px solid var(--border)}
.faq-btn{
  width:100%;display:flex;align-items:center;justify-content:space-between;
  padding:17px 0;background:none;text-align:left;gap:16px;
}
.faq-q{font-weight:600;font-size:.9rem;color:var(--ink);line-height:1.45}
.faq-ico{color:var(--gold);font-size:1.3rem;flex-shrink:0;transition:transform .22s;font-style:normal;line-height:1}
.faq-item.on .faq-ico{transform:rotate(45deg)}
.faq-ans{max-height:0;overflow:hidden;transition:max-height .35s ease}
.faq-item.on .faq-ans{max-height:400px}
.faq-ans-inner{padding-bottom:15px;font-size:.875rem;color:var(--stone);line-height:1.75}
.faq-ans-inner a{color:var(--gold);font-weight:600}

/* ── FONT DETAIL PAGE ── */
.fd-grid{display:grid;grid-template-columns:1fr 320px;gap:40px;align-items:start}
.fd-big-prev{
  background:linear-gradient(135deg,#FFFBF0,#FEF9EC);
  border:2px solid var(--border);border-radius:var(--r16);
  padding:36px;font-family:var(--fh);font-size:2.8rem;color:var(--ink3);
  line-height:1.5;text-align:center;margin-bottom:20px;
}
.fd-alpha{
  font-family:var(--fh);font-size:1rem;color:var(--stone);
  background:var(--cream);border:1px solid var(--border);
  border-radius:var(--r12);padding:18px 22px;line-height:2.2;
  letter-spacing:.02em;margin-bottom:20px;
}
.fd-meta{width:100%;border-collapse:collapse;margin-bottom:24px}
.fd-meta tr{border-bottom:1px solid var(--border)}
.fd-meta td{padding:11px 0;font-size:.85rem;vertical-align:top}
.fd-meta td:first-child{color:var(--stone);font-weight:600;width:130px;padding-right:14px}
.fd-h2{
  font-family:var(--fd);font-size:1.35rem;font-weight:700;
  color:var(--ink);margin:36px 0 14px;
  padding-bottom:10px;border-bottom:2px solid var(--border);letter-spacing:-.015em;
}
.fd-p{color:#3A3530;line-height:1.85;font-size:.92rem;margin-bottom:13px}

/* download sidebar */
.dl-sidebar{
  background:var(--white);border:2px solid var(--border);
  border-radius:var(--r24);padding:24px;
  box-shadow:var(--s2);position:sticky;top:78px;
}
.dl-title{font-weight:700;font-size:1rem;margin-bottom:4px}
.dl-info{color:var(--stone);font-size:.78rem;margin-bottom:18px}
.dl-main{
  display:block;width:100%;background:var(--gold);color:var(--ink);
  text-align:center;padding:14px;border-radius:var(--r12);
  font-weight:700;font-size:.92rem;margin-bottom:10px;
  transition:var(--tr);font-family:var(--fb);
}
.dl-main:hover{background:var(--gold2);transform:translateY(-1px);box-shadow:0 6px 20px rgba(217,119,6,.3)}
.dl-notes{font-size:.73rem;color:var(--stone);line-height:1.9;margin-bottom:18px}
.dl-compat{border-top:1px solid var(--border);padding-top:16px}
.dl-compat h4{font-size:.68rem;color:var(--stone2);text-transform:uppercase;letter-spacing:1px;font-weight:700;margin-bottom:10px}
.dl-ci{font-size:.82rem;color:var(--ink3);padding:3px 0;display:flex;align-items:center;gap:6px}
.dl-ci::before{content:"✓";color:var(--green);font-weight:700}

/* steps */
.steps{margin:16px 0}
.step{display:flex;gap:14px;margin-bottom:18px;align-items:flex-start}
.step-n{
  background:var(--gold);color:var(--ink);width:30px;height:30px;
  border-radius:50%;display:flex;align-items:center;justify-content:center;
  font-weight:700;font-size:.8rem;flex-shrink:0;margin-top:2px;
}
.step-b h4{font-weight:700;font-size:.88rem;color:var(--ink);margin-bottom:3px}
.step-b p{font-size:.83rem;color:var(--stone);line-height:1.6}

/* compare table */
.cmp-tbl{width:100%;border-collapse:collapse;font-size:.83rem}
.cmp-tbl th{background:var(--ink);color:#fff;padding:11px 14px;text-align:left;font-size:.78rem}
.cmp-tbl th:first-child{border-radius:10px 0 0 0}
.cmp-tbl th:last-child{border-radius:0 10px 0 0}
.cmp-tbl td{padding:11px 14px;border-bottom:1px solid var(--border);color:var(--ink3);vertical-align:top}
.cmp-tbl tr:nth-child(even) td{background:var(--cream)}
.yes{color:var(--green);font-weight:700}.no{color:var(--red);font-weight:700}

/* related */
.rel-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:11px}
.rel-card{
  background:var(--white);border:1.5px solid var(--border);
  border-radius:var(--r12);padding:14px;display:block;color:inherit;transition:var(--tr);
}
.rel-card:hover{border-color:var(--gold);transform:translateY(-2px);box-shadow:var(--s1)}
.rel-name{font-weight:700;font-size:.84rem;color:var(--ink);margin-bottom:3px}
.rel-desc{font-size:.72rem;color:var(--stone)}

/* ── BLOG POST ── */
.bh{background:var(--ink);padding:60px 0 52px;position:relative;overflow:hidden}
.bh::after{content:'';position:absolute;bottom:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,rgba(217,119,6,.4),transparent)}
.bh-cat{
  display:inline-block;background:rgba(217,119,6,.15);color:var(--gold2);
  border:1px solid rgba(217,119,6,.3);
  font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;
  padding:4px 13px;border-radius:20px;margin-bottom:16px;
}
.bh h1{
  font-family:var(--fd);font-size:clamp(1.7rem,3.5vw,2.6rem);
  font-weight:900;color:#fff;line-height:1.15;letter-spacing:-.025em;
  margin-bottom:14px;max-width:760px;
}
.bh-meta{color:rgba(255,255,255,.4);font-size:.8rem;display:flex;gap:14px;flex-wrap:wrap}

.bpc{max-width:760px}
.bpc h2{font-family:var(--fd);font-size:1.4rem;font-weight:700;color:var(--ink);
  margin:40px 0 13px;padding-bottom:9px;border-bottom:2px solid var(--border);letter-spacing:-.015em}
.bpc h3{font-size:1.05rem;font-weight:700;color:var(--ink3);margin:26px 0 9px}
.bpc p{color:#3A3530;line-height:1.85;font-size:.93rem;margin-bottom:14px}
.bpc ul,.bpc ol{margin:14px 0 14px 20px}
.bpc li{color:#3A3530;line-height:1.8;font-size:.92rem;margin-bottom:5px}
.bpc ul li{list-style:disc}.bpc ol li{list-style:decimal}
.bpc strong{font-weight:700;color:var(--ink)}
.bpc a{color:var(--gold);font-weight:600}
.bpc code{background:var(--cream);border:1px solid var(--border);
  padding:2px 7px;border-radius:5px;font-size:.83em;color:#92400E}
.tip{background:#FFFBEB;border:1px solid #FDE68A;border-left:4px solid var(--gold);
  padding:14px 18px;border-radius:0 12px 12px 0;margin:20px 0}
.tip p{margin:0;color:var(--ink3);font-size:.87rem;line-height:1.7}
.tip strong{color:#92400E}
.warn{background:#FFF5F5;border:1px solid #FECACA;border-left:4px solid #EF4444;
  padding:14px 18px;border-radius:0 12px 12px 0;margin:20px 0}
.warn p{margin:0;color:var(--ink3);font-size:.87rem}

/* inline CTA */
.i-cta{
  background:linear-gradient(135deg,var(--gold),var(--gold2));
  border-radius:var(--r16);padding:24px 28px;
  display:flex;align-items:center;justify-content:space-between;
  gap:18px;margin:32px 0;flex-wrap:wrap;
}
.i-cta h3{font-family:var(--fd);font-size:1.2rem;color:var(--ink);margin-bottom:4px}
.i-cta p{color:rgba(13,12,10,.7);font-size:.83rem}
.i-cta a{background:var(--ink);color:#fff;padding:10px 22px;border-radius:var(--r8);
  font-weight:700;font-size:.83rem;white-space:nowrap;transition:var(--tr)}
.i-cta a:hover{box-shadow:0 4px 14px rgba(0,0,0,.25);transform:translateY(-1px)}

/* page hero */
.ph{background:var(--ink);padding:52px 0 44px;border-bottom:1px solid rgba(255,255,255,.06)}
.ph h1{font-family:var(--fd);font-size:clamp(1.7rem,3.5vw,2.4rem);font-weight:900;color:#fff;letter-spacing:-.025em;margin-bottom:8px}
.ph p{color:rgba(255,255,255,.45);font-size:.93rem;max-width:540px}

/* ── FOOTER ── */
footer{background:var(--ink);color:rgba(255,255,255,.4);padding:60px 0 0}
.ft-grid{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:44px;margin-bottom:48px}
.ft-logo{margin-bottom:14px;display:inline-flex}
.ft-brand p{font-size:.82rem;line-height:1.75;max-width:270px}
.ft-col h4{color:rgba(255,255,255,.3);font-size:.67rem;text-transform:uppercase;letter-spacing:1.5px;font-weight:700;margin-bottom:14px}
.ft-col a{display:block;color:rgba(255,255,255,.5);font-size:.83rem;margin-bottom:9px;transition:var(--tr)}
.ft-col a:hover{color:#fff;padding-left:3px}
.ft-bottom{border-top:1px solid rgba(255,255,255,.06);padding:18px 0;
  display:flex;justify-content:space-between;align-items:center;
  font-size:.77rem;flex-wrap:wrap;gap:8px}
.ft-bottom a{color:rgba(255,255,255,.35);transition:var(--tr)}
.ft-bottom a:hover{color:rgba(255,255,255,.65)}

/* ── STATIC PAGES ── */
.prose h2{font-family:var(--fd);font-size:1.4rem;font-weight:700;color:var(--ink);margin:36px 0 13px;padding-bottom:9px;border-bottom:2px solid var(--border)}
.prose h3{font-size:1.05rem;font-weight:700;color:var(--ink3);margin:24px 0 9px}
.prose p{color:#3A3530;line-height:1.85;font-size:.93rem;margin-bottom:13px}
.prose ul{margin:12px 0 12px 20px}.prose ul li{list-style:disc;color:#3A3530;line-height:1.8;font-size:.92rem;margin-bottom:5px}
.prose a{color:var(--gold);font-weight:600}
.prose strong{font-weight:700;color:var(--ink)}

/* ── UTILS ── */
pre{background:var(--ink);color:#A5F3A5;padding:18px;border-radius:var(--r12);overflow-x:auto;font-size:.82rem;line-height:1.7;margin:14px 0}

/* ── RESPONSIVE ── */
@media(max-width:1024px){
  .ft-grid{grid-template-columns:1fr 1fr;gap:32px}
  .fd-grid{grid-template-columns:1fr}
  .dl-sidebar{position:static}
}
@media(max-width:768px){
  .nav-desk{display:none}
  .ham{display:flex}
  .wrap{padding:0 16px}
  .hero{padding:60px 0 52px}
  .hero-deva-bg{display:none}
  .sec{padding:48px 0}
  .cta-band{padding:28px 24px}
  .cta-band h2{font-size:1.35rem}
  .fonts-grid,.blog-grid{grid-template-columns:1fr}
  .ft-grid{grid-template-columns:1fr;gap:24px}
  .blog-layout-aside{display:none}
}
@media(max-width:540px){
  .cat-grid{grid-template-columns:repeat(3,1fr)}
  .i-cta{text-align:center;justify-content:center}
  .hero-stats{gap:22px}
  .hero h1{letter-spacing:-.02em}
  .fd-big-prev{font-size:2rem;padding:24px}
}
"""

# ══════════════════════════════════════════════════
# SHARED COMPONENTS
# ══════════════════════════════════════════════════
def head(title, desc, kw, canon, depth=0):
    a = "../" * depth
    return f"""<!DOCTYPE html>
<html lang="hi-IN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{kw}">
<meta name="robots" content="index,follow">
<link rel="canonical" href="https://hindifont.co.in{canon}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="https://hindifont.co.in{canon}">
<meta property="og:type" content="website">
<meta property="og:locale" content="hi_IN">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{GF}" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>"""

def hdr():
    return """<header id="hdr">
<div class="wrap">
<div class="hdr-inner">
  <a href="/" class="logo" aria-label="HindiFont Home">
    <div class="logo-mark" aria-hidden="true">अ</div>
    <div class="logo-text">HindiFont<span>.co.in</span></div>
  </a>
  <nav class="nav-desk" aria-label="Main navigation">
    <a href="/">Home</a>
    <a href="/fonts/">All Fonts</a>
    <a href="/category/">Categories</a>
    <a href="/blog/">Blog</a>
    <a href="/about/">About</a>
    <a href="/fonts/" class="nav-btn">⬇ Download</a>
  </nav>
  <button class="ham" id="ham" aria-label="Toggle menu" aria-expanded="false" aria-controls="mob">
    <span></span><span></span><span></span>
  </button>
</div>
</div>
</header>
<nav class="mob-nav" id="mob" aria-label="Mobile navigation">
  <span class="mob-sec">Navigate</span>
  <a href="/">🏠 Home</a>
  <a href="/fonts/">🔤 All Hindi Fonts</a>
  <a href="/category/">📂 Categories</a>
  <a href="/blog/">📖 Blog & Guides</a>
  <a href="/about/">ℹ️ About Us</a>
  <a href="/contact/">✉️ Contact</a>
  <span class="mob-sec">Quick Links</span>
  <a href="/fonts/kruti-dev-010/">Kruti Dev 010</a>
  <a href="/fonts/devlys-010/">Devlys 010</a>
  <a href="/fonts/mangal/">Mangal Font</a>
  <a href="/fonts/noto-sans-devanagari/">Noto Sans Devanagari</a>
  <a href="/category/government-exam/">Govt Exam Fonts</a>
  <a href="/fonts/" class="mob-cta">⬇ Download Free Fonts</a>
</nav>"""

def ftr(depth=0):
    a = "../" * depth
    return f"""<footer>
<div class="wrap">
<div class="ft-grid">
  <div class="ft-brand">
    <a href="/" class="ft-logo logo">
      <div class="logo-mark">अ</div>
      <div class="logo-text" style="margin-left:10px">HindiFont<span>.co.in</span></div>
    </a>
    <p>India का सबसे बड़ा free Hindi font collection। 500+ fonts — Kruti Dev से Unicode तक। No registration, instant download।</p>
  </div>
  <div class="ft-col">
    <h4>Popular Fonts</h4>
    <a href="/fonts/kruti-dev-010/">Kruti Dev 010</a>
    <a href="/fonts/devlys-010/">Devlys 010</a>
    <a href="/fonts/mangal/">Mangal Font</a>
    <a href="/fonts/chandas/">Chandas</a>
    <a href="/fonts/noto-sans-devanagari/">Noto Sans Devanagari</a>
    <a href="/fonts/hind/">Hind Font</a>
  </div>
  <div class="ft-col">
    <h4>Categories</h4>
    <a href="/category/government-exam/">Govt Exam Fonts</a>
    <a href="/category/unicode/">Unicode Fonts</a>
    <a href="/category/calligraphy/">Calligraphy</a>
    <a href="/category/stylish/">Stylish Fonts</a>
    <a href="/category/web-fonts/">Web Fonts</a>
    <a href="/category/wedding/">Wedding Fonts</a>
  </div>
  <div class="ft-col">
    <h4>Pages</h4>
    <a href="/blog/">Blog</a>
    <a href="/about/">About Us</a>
    <a href="/contact/">Contact</a>
    <a href="/privacy-policy/">Privacy Policy</a>
    <a href="/disclaimer/">Disclaimer</a>
    <a href="/terms/">Terms of Use</a>
    <a href="/sitemap.xml">Sitemap</a>
  </div>
</div>
<div class="ft-bottom">
  <span>© 2025 HindiFont.co.in — All Rights Reserved</span>
  <span>Made with ❤️ for India &nbsp;|&nbsp; <a href="/sitemap.xml">Sitemap</a> &nbsp;|&nbsp; <a href="/privacy-policy/">Privacy</a></span>
</div>
</div>
</footer>
<script>
(function(){{
  // Mobile menu
  var ham=document.getElementById('ham'),mob=document.getElementById('mob');
  if(ham&&mob){{
    ham.addEventListener('click',function(){{
      var o=mob.classList.toggle('on');
      ham.classList.toggle('on',o);
      ham.setAttribute('aria-expanded',o);
      document.body.style.overflow=o?'hidden':'';
    }});
    mob.querySelectorAll('a').forEach(function(a){{
      a.addEventListener('click',function(){{
        mob.classList.remove('on');ham.classList.remove('on');
        document.body.style.overflow='';
      }});
    }});
    document.addEventListener('click',function(e){{
      if(!ham.contains(e.target)&&!mob.contains(e.target)){{
        mob.classList.remove('on');ham.classList.remove('on');
        document.body.style.overflow='';
      }}
    }});
  }}
  // Search
  var si=document.getElementById('si'),sb=document.getElementById('sb');
  function doSearch(){{var q=si?si.value.trim():'';if(q)window.location.href='/fonts/?q='+encodeURIComponent(q);}}
  if(sb)sb.addEventListener('click',doSearch);
  if(si)si.addEventListener('keydown',function(e){{if(e.key==='Enter')doSearch();}});
  // FAQ
  document.querySelectorAll('.faq-btn').forEach(function(b){{
    b.addEventListener('click',function(){{
      var it=b.closest('.faq-item'),op=it.classList.contains('on');
      document.querySelectorAll('.faq-item.on').forEach(function(i){{i.classList.remove('on');}});
      if(!op)it.classList.add('on');
    }});
  }});
  // Filter pills
  document.querySelectorAll('.pill[data-f]').forEach(function(p){{
    p.addEventListener('click',function(){{
      document.querySelectorAll('.pill').forEach(function(x){{x.classList.remove('on');}});
      p.classList.add('on');
      var f=p.dataset.f;
      document.querySelectorAll('.font-card[data-c]').forEach(function(c){{
        c.style.display=(f==='all'||c.dataset.c.split(' ').includes(f))?'':'none';
      }});
    }});
  }});
}})();
</script>
</body></html>"""

def crumb(items, depth=0):
    lis=""
    for lbl,url in items:
        if url: lis+=f'<li><a href="{url}">{lbl}</a></li>'
        else: lis+=f'<li><span aria-current="page">{lbl}</span></li>'
    return f'<nav class="crumb" aria-label="Breadcrumb"><div class="wrap"><ol>{lis}</ol></div></nav>'

def schema_font(f):
    return f"""<script type="application/ld+json">{{"@context":"https://schema.org","@type":"SoftwareApplication","name":"{f["name"]}","applicationCategory":"Font","operatingSystem":"Windows, Mac, Linux","offers":{{"@type":"Offer","price":"0","priceCurrency":"INR"}},"description":"{f["short"]}","downloadUrl":"https://hindifont.co.in/fonts/{f["slug"]}/download/","inLanguage":"hi"}}</script>"""

def schema_article(b):
    return f"""<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"{b["title"]}","author":{{"@type":"Organization","name":"HindiFont.co.in"}},"publisher":{{"@type":"Organization","name":"HindiFont.co.in"}},"datePublished":"2025-01-15","inLanguage":"hi","description":"{b["desc"]}"}}</script>"""

print("✅ Core CSS + templates ready")

# ══════════════════════════════════════════════════
# FONT DATA — 27 specific fonts
# ══════════════════════════════════════════════════
FONTS = [
  dict(slug="kruti-dev-010",name="Kruti Dev 010",prev="कृति देव ०१०",lat="Kruti Dev 010",
    short="SSC, Railway, UP Police exams का official Hindi typing font",
    type="ANSI",tcss="ta",badges=[("te","Govt Exam"),("ta","ANSI")],
    desc1="Kruti Dev 010 भारत का सबसे अधिक use किया जाने वाला Hindi ANSI font है। SSC (Staff Selection Commission), Railway Recruitment Board, और अनेक central government typing exams में यह official standard font है।",
    desc2="Remington keyboard layout पर based यह font traditional Hindi typewriter जैसी feel देता है। Kruti Dev family में 010 सबसे commonly required version है — इसे ज़रूर install करें।",
    kb="Remington / Typewriter",size="~45 KB",cats="government-exam ansi",
    faq=[("SSC typing exam में कौन सा Kruti Dev use होता है?","SSC CHSL और CGL में Kruti Dev 010 standard font है। हमेशा exam notification verify करें।"),
         ("Kruti Dev 010 Unicode है?","नहीं — ANSI font है। Internet use के लिए Mangal बेहतर है।"),
         ("Kruti Dev 010 Windows 11 पर काम करता है?","हाँ, Windows 7, 8, 10 और 11 सभी पर perfectly काम करता है।")],
    install=["Font download करें — .zip या .ttf file मिलेगी।","ZIP हो तो Right-click → Extract Here करें।",".ttf file पर Right-click → <strong>Install</strong> click करें।","MS Word open करें → Font list में 'Kruti Dev 010' select करें।","Remington keyboard layout use करके Hindi typing शुरू करें! 🎉"]),
  dict(slug="kruti-dev-020",name="Kruti Dev 020",prev="कृति देव ०२०",lat="Kruti Dev 020",
    short="Kruti Dev series का widely used variant for offices",
    type="ANSI",tcss="ta",badges=[("te","Govt Exam"),("ta","ANSI")],
    desc1="Kruti Dev 020 Kruti Dev font family का एक important member है। Government offices, printing press और typing centers में widely use होता है।",
    desc2="Remington keyboard layout based — Kruti Dev 010 के बाद यह second most popular Kruti Dev variant है।",
    kb="Remington",size="~47 KB",cats="government-exam ansi",
    faq=[("Kruti Dev 010 और 020 में क्या फर्क है?","Character weight और spacing में minor differences हैं।"),
         ("किस exam में 020 use होता है?","Various state government typing exams में accepted है।")],
    install=["Font download करें।","ZIP extract करें।",".ttf पर Right-click → Install।","Word में font select करें।"]),
  dict(slug="devlys-010",name="Devlys 010",prev="देवलीस ०१०",lat="Devlys 010",
    short="UP Police, UPSSSC, Lekhpal exams का official font",
    type="ANSI",tcss="ta",badges=[("te","Govt Exam"),("ta","ANSI")],
    desc1="Devlys 010 UP state government exams का official Hindi ANSI font है। UP Police, UPSSSC, Lekhpal, Patwari, UP Revenue Department typing tests में यह mandatory है।",
    desc2="Remington keyboard layout based — Kruti Dev का strong alternative। UP exams की preparation कर रहे हैं तो यह font ज़रूरी है।",
    kb="Remington",size="~38 KB",cats="government-exam ansi",
    faq=[("Devlys 010 किन exams में required है?","UP Police, UPSSSC, Lekhpal, Patwari, UP Revenue typing tests।"),
         ("Devlys और Kruti Dev same keyboard है?","दोनों Remington use करते हैं — minor differences के साथ।"),
         ("Devlys 010 free download है?","हाँ, बिल्कुल free। Click करें और download करें।")],
    install=["Font file download करें।","ZIP extract करें।",".ttf Right-click → Install।","Word में Devlys 010 select करें।"]),
  dict(slug="devlys-020",name="Devlys 020",prev="देवलीस ०२०",lat="Devlys 020",
    short="Devlys series का popular alternative variant",
    type="ANSI",tcss="ta",badges=[("te","Govt Exam"),("ta","ANSI")],
    desc1="Devlys 020 UP state exam typing font family का एक popular member है जो various government offices में use होता है।",
    desc2="Devlys 010 के complement के रूप में install करें — दोनों same keyboard layout use करते हैं।",
    kb="Remington",size="~40 KB",cats="government-exam ansi",
    faq=[("Devlys 020 कहाँ use होता है?","UP state government offices और exams में।")],
    install=["Download करें।","Extract करें।","Install करें।","Select करें।"]),
  dict(slug="mangal",name="Mangal Font",prev="मंगल — यूनिकोड",lat="Mangal Unicode",
    short="Windows का default Unicode Hindi font — CPCT और online forms के लिए",
    type="Unicode",tcss="tu",badges=[("tu","Unicode"),("te","CPCT/Govt")],
    desc1="Mangal Microsoft Windows का official Unicode Hindi font है। सभी Windows versions में pre-installed। CPCT typing exam, e-courts, MCA-21, और online government forms में Mangal standard font है।",
    desc2="Unicode होने से Mangal में type किया text internet, email, WhatsApp पर correctly दिखता है — ANSI fonts की यह limitation नहीं है।",
    kb="Inscript",size="~160 KB",cats="government-exam unicode",
    faq=[("CPCT exam में कौन सा font?","CPCT Hindi typing: Mangal font + Inscript keyboard।"),
         ("Mangal और Kruti Dev में कौन बेहतर?","Purpose पर depend: Govt ANSI exams → Kruti Dev। Online/Unicode → Mangal।"),
         ("Mangal Windows में पहले से है?","हाँ Windows Vista+ में built-in है। यहाँ से backup के लिए download करें।")],
    install=["Download करें (अगर install नहीं है)।",".ttf Right-click → Install।","Hindi keyboard Inscript enable करें।","Word में Mangal select → Inscript type करें।"]),
  dict(slug="chandas",name="Chandas Font",prev="चन्दस — संस्कृत",lat="Chandas Sanskrit",
    short="Sanskrit texts, Vedic content और religious documents के लिए",
    type="Unicode",tcss="tu",badges=[("tu","Unicode"),("tf","Open Source")],
    desc1="Chandas एक free, open-source Unicode Devanagari font है जिसे specially Sanskrit और Vedic texts के लिए design किया गया है। Complete Vedic accent marks — udātta, anudātta, svarita — support है।",
    desc2="Religious organizations, Sanskrit scholars, temples, और devotional content creators के लिए Chandas ideal choice है। SIL OFL license — commercial use भी free।",
    kb="Unicode/Inscript",size="~200 KB",cats="unicode calligraphy",
    faq=[("Chandas में Vedic svara marks हैं?","हाँ — complete Vedic accent support।"),
         ("Commercial use free है?","हाँ — SIL OFL license।"),
         ("Sanskrit typing के लिए best font?","Chandas और Sanskrit 2003 दोनों excellent हैं।")],
    install=["Download करें।","Right-click → Install।","Unicode keyboard enable करें।","Word में Chandas select करें।"]),
  dict(slug="noto-sans-devanagari",name="Noto Sans Devanagari",prev="नोटो सैंस",lat="Noto Sans Devanagari",
    short="Google का modern web-optimized Hindi font — websites और apps के लिए",
    type="Unicode",tcss="tu",badges=[("tu","Unicode"),("tw","Web Font")],
    desc1="Noto Sans Devanagari Google का modern, clean Unicode Hindi font है। Websites, mobile apps और digital content के लिए #1 choice। 'No Tofu' project — सभी characters perfectly represented।",
    desc2="100 से 900 तक 9 weights available। Developers के लिए go-to font। Google Fonts CDN से directly use करें — zero cost।",
    kb="Unicode",size="~450 KB",cats="unicode web-fonts",
    faq=[("Website पर कैसे use करें?","fonts.googleapis.com/css2?family=Noto+Sans+Devanagari"),
         ("कितने weights?","100 से 900 तक — Thin से Black।"),
         ("Mobile apps के लिए suitable?","हाँ — Android और iOS दोनों पर excellent।")],
    install=["Download करें।","Right-click → Install।","Websites के लिए Google Fonts CDN use करें।"]),
  dict(slug="noto-serif-devanagari",name="Noto Serif Devanagari",prev="नोटो सेरिफ़",lat="Noto Serif Devanagari",
    short="Elegant serif Hindi font — books, articles और formal documents के लिए",
    type="Unicode",tcss="tu",badges=[("tu","Unicode"),("tw","Web Font")],
    desc1="Noto Serif Devanagari Google का elegant serif Unicode Hindi font है जो long-form reading, books, academic articles और literary content के लिए ideal है।",
    desc2="Traditional serif style के साथ excellent readability। Noto Sans के complement के रूप में use करें।",
    kb="Unicode",size="~480 KB",cats="unicode web-fonts",
    faq=[("Noto Sans vs Serif कौन बेहतर?","Sans: UI/digital। Serif: books/long reading।")],
    install=["Download करें।","Install करें।","Google Fonts CDN use करें।"]),
  dict(slug="hind",name="Hind Font",prev="हिन्द — UI",lat="Hind Devanagari",
    short="UI design और mobile apps के लिए specially optimized Hindi font",
    type="Unicode",tcss="tu",badges=[("tu","Unicode"),("tw","UI Font")],
    desc1="Hind Indian Type Foundry (ITF) द्वारा designed एक modern open-source Devanagari font है। Specially User Interface design और mobile screens के लिए optimized।",
    desc2="5 weights: Light, Regular, Medium, SemiBold, Bold। Latin script का full support। Google Fonts पर free।",
    kb="Unicode",size="~280 KB",cats="unicode web-fonts",
    faq=[("Hind किसने बनाया?","Indian Type Foundry (ITF) — Google Fonts पर free।"),
         ("5 weights available हैं?","हाँ — Light से Bold तक।")],
    install=["Download करें।","Install करें।","Google Fonts CDN: fonts.googleapis.com/css2?family=Hind"]),
  dict(slug="baloo-2",name="Baloo 2",prev="बालू — क्रिएटिव",lat="Baloo 2 Display",
    short="Playful rounded Devanagari — children books, social media और fun designs",
    type="Unicode",tcss="tu",badges=[("tu","Unicode"),("tw","Display")],
    desc1="Baloo 2 ITF द्वारा designed एक playful, rounded Devanagari font है। Children's books, greeting cards, social media posts और creative projects के लिए perfect।",
    desc2="Devanagari और Latin दोनों scripts। 5 weights। Google Fonts पर free।",
    kb="Unicode",size="~350 KB",cats="unicode web-fonts stylish",
    faq=[("Body text के लिए suitable?","Display/heading के लिए best — body text के लिए Hind better है।")],
    install=["Download करें।","Install करें।"]),
  dict(slug="shree-lipi",name="Shree Lipi",prev="श्री लिपि",lat="Shree Lipi Classic",
    short="Dainik Bhaskar, Rajasthan Patrika जैसे newspapers की पसंद",
    type="ANSI",tcss="ta",badges=[("ta","ANSI"),("tc","Publishing")],
    desc1="Shree Lipi India के leading Hindi newspapers और magazines में widely use होने वाली font series है। Professional publishing houses इसे prefer करते हैं।",
    desc2="Excellent readability और elegant letterforms newspapers के लिए ideal बनाते हैं।",
    kb="Custom",size="~120 KB",cats="ansi calligraphy",
    faq=[("कौन से newspapers use करते हैं?","Dainik Bhaskar, Rajasthan Patrika, NavBharat Times।")],
    install=["Download करें।","Right-click → Install।"]),
  dict(slug="lohit-devanagari",name="Lohit Devanagari",prev="लोहित देवनागरी",lat="Lohit Devanagari",
    short="Red Hat का open source Linux Hindi font — FOSS projects के लिए",
    type="Unicode",tcss="tu",badges=[("tu","Unicode"),("tf","Open Source")],
    desc1="Lohit Devanagari Red Hat द्वारा developed free, open-source Unicode Hindi font है। Ubuntu, Fedora, CentOS जैसे Linux distributions में default Hindi font है।",
    desc2="SIL OFL license — commercial use भी free। Terminal, documents, FOSS projects के लिए reliable choice।",
    kb="Unicode",size="~170 KB",cats="unicode web-fonts",
    faq=[("Ubuntu में कैसे install करें?","sudo apt install fonts-lohit-deva"),
         ("Windows पर काम करता है?","हाँ — .ttf Windows, Mac, Linux सभी पर।")],
    install=["Download करें।","Windows: Right-click → Install।","Linux: apt/dnf package use करें।"]),
  dict(slug="kokila",name="Kokila Font",prev="कोकिला — औपचारिक",lat="Kokila Formal",
    short="Windows built-in elegant font — formal letters और government correspondence",
    type="Unicode",tcss="tu",badges=[("tu","Unicode"),("tf","Built-in")],
    desc1="Kokila Microsoft Windows का built-in Unicode Hindi font है। Formal letters, official documents और government correspondence के लिए elegant choice है।",
    desc2="Windows Vista+ में pre-installed। Traditional और refined letterforms।",
    kb="Inscript",size="~195 KB",cats="unicode government-exam",
    faq=[("Kokila Windows में है?","हाँ — Vista, 7, 8, 10, 11 सभी में।")],
    install=["Check करें — अगर already है तो select करें।","नहीं है तो यहाँ से download → Install।"]),
  dict(slug="aparajita",name="Aparajita Font",prev="अपराजिता",lat="Aparajita",
    short="Windows 7+ का built-in elegant Hindi Unicode font",
    type="Unicode",tcss="tu",badges=[("tu","Unicode"),("tf","Built-in")],
    desc1="Aparajita Windows 7 और बाद के versions में built-in Hindi Unicode font है। Literary texts और formal documents के लिए beautiful choice।",
    desc2="Regular और Bold variants। Clean और refined Devanagari letterforms।",
    kb="Inscript",size="~190 KB",cats="unicode",
    faq=[("Aparajita free है?","हाँ — Windows built-in।")],
    install=["Windows 7+ में already available।","Font list में select करें।"]),
  dict(slug="amita",name="Amita Font",prev="अमिता — कैलीग्राफी",lat="Amita Calligraphy",
    short="Wedding invitations और artistic projects के लिए calligraphic Devanagari",
    type="Unicode",tcss="tu",badges=[("tu","Unicode"),("tc","Calligraphy")],
    desc1="Amita एक beautiful calligraphic Devanagari font है जो wedding invitations, greeting cards, और artistic projects के लिए perfect है। Google Fonts पर free।",
    desc2="Unique calligraphic style जो Indian aesthetics को beautifully capture करती है।",
    kb="Unicode",size="~185 KB",cats="unicode calligraphy wedding",
    faq=[("Wedding cards के लिए suitable?","बिल्कुल! Beautiful calligraphic style।"),
         ("Commercial use free?","हाँ — Google Fonts OFL।")],
    install=["Download करें।","Right-click → Install।"]),
  dict(slug="yatra-one",name="Yatra One",prev="यात्रा वन — बोल्ड",lat="Yatra One Bold",
    short="Traditional signage से inspired bold display Devanagari font",
    type="Unicode",tcss="tu",badges=[("tu","Unicode"),("tw","Display")],
    desc1="Yatra One traditional Indian signage और hoardings से inspired एक bold display font है। Posters, banners और impactful headlines के लिए ideal।",
    desc2="EkType द्वारा designed। Google Fonts पर free।",
    kb="Unicode",size="~145 KB",cats="unicode stylish web-fonts",
    faq=[("Body text के लिए suitable?","नहीं — display/heading के लिए designed।")],
    install=["Download करें।","Install करें।"]),
  dict(slug="rozha-one",name="Rozha One",prev="रोझा वन",lat="Rozha One Display",
    short="Bold display serif — editorial headlines और posters के लिए",
    type="Unicode",tcss="tu",badges=[("tu","Unicode"),("tw","Display")],
    desc1="Rozha One एक bold display serif font है जो Hindi headlines, editorial layouts और impactful designs के लिए designed है।",
    desc2="Strong authoritative letterforms। Google Fonts पर free।",
    kb="Unicode",size="~165 KB",cats="unicode stylish web-fonts",
    faq=[("Rozha posters के लिए best है?","हाँ — bold display के लिए excellent।")],
    install=["Download करें।","Install करें।"]),
  dict(slug="tiro-devanagari-hindi",name="Tiro Devanagari Hindi",prev="तिरो देवनागरी",lat="Tiro Devanagari",
    short="Scholarly और refined — academic publications और literary texts के लिए",
    type="Unicode",tcss="tu",badges=[("tu","Unicode"),("tc","Literary")],
    desc1="Tiro Devanagari Hindi एक scholarly, refined font है जो academic publications, literary texts और books के लिए designed है। Tiro Typeworks द्वारा created।",
    desc2="Excellent readability at small sizes। Google Fonts पर free।",
    kb="Unicode",size="~210 KB",cats="unicode calligraphy",
    faq=[("Academic papers के लिए suitable?","हाँ — scholarly use के लिए designed।")],
    install=["Download करें।","Install करें।"]),
  dict(slug="walkman-chanakya",name="Walkman Chanakya",prev="चाणक्य — क्लासिक",lat="Chanakya Classic",
    short="Classic Hindi newspaper font — decades से publishing की पसंद",
    type="ANSI",tcss="ta",badges=[("ta","ANSI"),("tc","Classic")],
    desc1="Walkman Chanakya India के Hindi newspapers और printing industry में decades से use होने वाला classic ANSI font है।",
    desc2="Traditional letterforms जो Hindi typography के heritage का हिस्सा हैं।",
    kb="Chanakya",size="~85 KB",cats="ansi calligraphy",
    faq=[("Newspapers में use होता है?","हाँ — कई traditional Hindi publications में।")],
    install=["Download करें।","Right-click → Install।"]),
  dict(slug="ponnala",name="Ponnala",prev="पोन्नाला — उत्सव",lat="Ponnala Festive",
    short="Festive और decorative Devanagari — Diwali cards और celebrations के लिए",
    type="Unicode",tcss="tu",badges=[("tu","Unicode"),("tc","Festive")],
    desc1="Ponnala एक decorative display font है जो festive occasions, Diwali cards, wedding invitations और celebratory content के लिए perfect है।",
    desc2="Unique decorative letterforms। Google Fonts पर free।",
    kb="Unicode",size="~148 KB",cats="unicode stylish wedding calligraphy",
    faq=[("Diwali cards के लिए suitable?","हाँ — festive style perfect है।")],
    install=["Download करें।","Install करें।"]),
  dict(slug="laila",name="Laila Font",prev="लैला — सुंदर",lat="Laila Calligraphy",
    short="Multi-script calligraphic font — premium wedding और lifestyle content",
    type="Unicode",tcss="tu",badges=[("tu","Unicode"),("tc","Calligraphy")],
    desc1="Laila एक beautiful Unicode font है जो Devanagari, Arabic और Latin scripts में calligraphic style offer करता है। Premium designs के लिए excellent।",
    desc2="Google Fonts पर free। Multicultural और multilingual projects के लिए ideal।",
    kb="Unicode",size="~190 KB",cats="unicode calligraphy wedding",
    faq=[("Wedding cards के लिए best?","हाँ — elegant और premium feel।")],
    install=["Download करें।","Install करें।"]),
  dict(slug="mukta",name="Mukta Font",prev="मुक्त — मॉडर्न",lat="Mukta Modern",
    short="Clean modern Devanagari — branding और contemporary design के लिए",
    type="Unicode",tcss="tu",badges=[("tu","Unicode"),("tw","Branding")],
    desc1="Mukta EkType द्वारा designed एक clean, modern Devanagari font है। Branding, logos और contemporary design projects के लिए excellent।",
    desc2="Hindi, Gujarati और Latin script support। Open source।",
    kb="Unicode",size="~320 KB",cats="unicode web-fonts stylish",
    faq=[("Commercial use free?","हाँ — SIL OFL।")],
    install=["Download करें।","Install करें।"]),
  dict(slug="preeti",name="Preeti Font",prev="प्रीति",lat="Preeti Devanagari",
    short="Nepal और North India में popular ANSI office font",
    type="ANSI",tcss="ta",badges=[("ta","ANSI"),("te","Office")],
    desc1="Preeti एक popular ANSI Devanagari font है जो Nepal और North India में offices और government work के लिए widely used है।",
    desc2="Simple और clear letterforms। Traditional keyboard layout based।",
    kb="Preeti Layout",size="~68 KB",cats="ansi government-exam",
    faq=[("Preeti Nepali typing के लिए है?","Primarily Nepali लेकिन Hindi में भी use होता है।")],
    install=["Download करें।","Right-click → Install।"]),
  dict(slug="agra",name="Agra Font",prev="आगरा — क्रिएटिव",lat="Agra Display",
    short="Creative ANSI Hindi font — display और artistic work के लिए",
    type="ANSI",tcss="ta",badges=[("ta","ANSI"),("tc","Display")],
    desc1="Agra एक creative ANSI Hindi font है। Creative projects, posters और display text के लिए good choice।",
    desc2="Distinctive letterforms जो visual appeal create करते हैं।",
    kb="Custom",size="~70 KB",cats="ansi stylish",
    faq=[("Agra free है?","हाँ — free download।")],
    install=["Download करें।","Right-click → Install।"]),
  dict(slug="richa",name="Richa Font",prev="ऋचा — सुंदर",lat="Richa Magazine",
    short="Hindi magazines और literary publications के लिए elegant font",
    type="ANSI",tcss="ta",badges=[("ta","ANSI"),("tc","Magazine")],
    desc1="Richa एक elegant Hindi ANSI font है जो magazines, literary publications और aesthetic projects के लिए widely used है।",
    desc2="Graceful letterforms जो reading experience को enhance करते हैं।",
    kb="Custom",size="~78 KB",cats="ansi calligraphy",
    faq=[("Magazines में use होता है?","हाँ — several Hindi magazines इसे prefer करते हैं।")],
    install=["Download करें।","Right-click → Install।"]),
  dict(slug="teko",name="Teko Font",prev="टेको — बोल्ड",lat="Teko Bold Condensed",
    short="Modern bold condensed Hindi-Latin font — banners और CTAs के लिए",
    type="Unicode",tcss="tu",badges=[("tu","Unicode"),("tw","Condensed")],
    desc1="Teko एक modern bold condensed font है जो Devanagari और Latin scripts में impactful headlines बनाता है। Urban और contemporary aesthetic।",
    desc2="Google Fonts पर free। 5 weights available।",
    kb="Unicode",size="~185 KB",cats="unicode stylish web-fonts",
    faq=[("Banners के लिए suitable?","हाँ — bold condensed style perfect है।")],
    install=["Download करें।","Install करें।"]),
]

def fc(f):
    tags=" ".join([f'<span class="tag {c}">{l}</span>' for c,l in f["badges"][:2]])
    return f"""<a href="/fonts/{f['slug']}/" class="font-card" data-c="{f['cats']}">
  <div class="fc-prev"><div class="fc-deva">{f['prev']}</div><div class="fc-lat">{f['lat']}</div></div>
  <div class="fc-body">
    <div class="fc-name">{f['name']}</div>
    <div class="fc-desc">{f['short']}</div>
    <div class="fc-foot"><div class="tags">{tags}</div><span class="dl-btn">⬇ Download</span></div>
  </div>
</a>"""

print(f"✅ {len(FONTS)} fonts defined")

# ══════════════════════════════════════════════════
# FONT PAGE BUILDER
# ══════════════════════════════════════════════════
def build_font(f):
    tags=" ".join([f'<span class="tag {c}">{l}</span>' for c,l in f["badges"]])
    faqs="".join([f"""<div class="faq-item">
  <button class="faq-btn"><span class="faq-q">{q}</span><i class="faq-ico">+</i></button>
  <div class="faq-ans"><div class="faq-ans-inner">{a}</div></div>
</div>""" for q,a in f["faq"]])
    steps="".join([f'<div class="step"><div class="step-n">{i+1}</div><div class="step-b"><p>{s}</p></div></div>' for i,s in enumerate(f["install"])])
    others=[x for x in FONTS if x["slug"]!=f["slug"]]
    rel="".join([f'<a href="/fonts/{r["slug"]}/" class="rel-card"><div class="rel-name">{r["name"]}</div><div class="rel-desc">{r["short"][:55]}…</div></a>' for r in others[:6]])

    return f"""{head(f'{f["name"]} Font Free Download | HindiFont.co.in',
f'{f["name"]} font free download करें। {f["short"]}। No registration, instant download।',
f'{f["name"].lower()}, hindi font download, {f["type"].lower()} hindi font',
f'/fonts/{f["slug"]}/',2)}
{schema_font(f)}
{hdr()}
{crumb([("Home","/"),("Fonts","/fonts/"),(f["name"],None)],2)}
<div class="ph"><div class="wrap">
  <div style="margin-bottom:10px">{tags}</div>
  <h1 style="font-family:var(--fd);font-size:clamp(1.6rem,3.5vw,2.2rem);font-weight:900;color:#fff;letter-spacing:-.025em;margin-bottom:6px">{f["name"]} — Free Download</h1>
  <p style="color:rgba(255,255,255,.45)">{f["short"]}</p>
</div></div>
<main>
<div class="sec sec-white">
<div class="wrap">
<div class="fd-grid">
<div>
  <div class="fd-big-prev">{f["prev"]}<br><span style="font-size:1.1rem;color:var(--stone2)">अ आ इ ई उ ऊ ए ऐ ओ औ</span></div>
  <div class="fd-alpha">क ख ग घ ङ • च छ ज झ • ट ठ ड ढ ण • त थ द ध न • प फ ब भ म • य र ल व श ष स ह</div>
  <table class="fd-meta">
    <tr><td>Font Name</td><td><strong>{f["name"]}</strong></td></tr>
    <tr><td>Type</td><td>{f["type"]}</td></tr>
    <tr><td>Format</td><td>.TTF (TrueType)</td></tr>
    <tr><td>File Size</td><td>{f["size"]}</td></tr>
    <tr><td>Keyboard</td><td>{f["kb"]}</td></tr>
    <tr><td>License</td><td>Free for personal use</td></tr>
    <tr><td>OS Support</td><td>Windows 7/8/10/11 · Mac · Linux</td></tr>
  </table>

  <h2 class="fd-h2">{f["name"]} Font क्या है?</h2>
  <p class="fd-p">{f["desc1"]}</p>
  <p class="fd-p">{f["desc2"]}</p>

  <h2 class="fd-h2">Install कैसे करें? (Windows)</h2>
  <div class="steps">{steps}</div>
  <div class="tip"><p><strong>💡 Mac पर Install:</strong> .ttf download करें → Font Book app में drag करें → Install Font click करें। Done!</p></div>

  <h2 class="fd-h2">Frequently Asked Questions</h2>
  <div class="faq-list">{faqs}</div>
  <div class="faq-item"><button class="faq-btn"><span class="faq-q">क्या {f["name"]} बिल्कुल free है?</span><i class="faq-ico">+</i></button><div class="faq-ans"><div class="faq-ans-inner">हाँ — HindiFont.co.in पर 100% free। No registration, no payment, direct download।</div></div></div>
  <div class="faq-item"><button class="faq-btn"><span class="faq-q">{f["name"]} Windows 11 पर काम करता है?</span><i class="faq-ico">+</i></button><div class="faq-ans"><div class="faq-ans-inner">हाँ — Windows 7, 8, 10 और 11 सभी पर perfectly काम करता है।</div></div></div>

  <h2 class="fd-h2">Related Hindi Fonts</h2>
  <div class="rel-grid">{rel}</div>
</div>
<aside>
  <div class="dl-sidebar">
    <div class="dl-title">⬇ {f["name"]}</div>
    <div class="dl-info">📁 TTF · {f["size"]} · Free</div>
    <a href="/fonts/{f['slug']}/download/" class="dl-main">⬇ Free Download करें</a>
    <div class="dl-notes">✓ No registration required<br>✓ Direct instant download<br>✓ Virus-free, safe file<br>✓ Works on all OS</div>
    <div class="dl-compat">
      <h4>Compatible With</h4>
      <div class="dl-ci">Windows 10 / 11</div>
      <div class="dl-ci">Windows 7 / 8</div>
      <div class="dl-ci">Mac OS X+</div>
      <div class="dl-ci">MS Word / Excel</div>
      <div class="dl-ci">Photoshop / Illustrator</div>
      <div class="dl-ci">CorelDraw</div>
      <div class="dl-ci">Linux (Ubuntu)</div>
    </div>
  </div>
</aside>
</div>
</div>
</div>
</main>
{ftr(2)}"""

os.makedirs(f"{BASE}/fonts", exist_ok=True)
for f in FONTS:
    os.makedirs(f"{BASE}/fonts/{f['slug']}", exist_ok=True)
    open(f"{BASE}/fonts/{f['slug']}/index.html","w").write(build_font(f))

print(f"✅ {len(FONTS)} font pages built")

# ══════════════════════════════════════════════════
# BLOG DATA — 12 posts
# ══════════════════════════════════════════════════
BLOGS = [
  dict(slug="hindi-font-install-windows",cat="Tutorial",date="Jan 2025",read="4 min",
    title="Windows 10/11 में Hindi Font Install कैसे करें — Complete 2025 Guide",
    desc="Kruti Dev, Devlys, Mangal कोई भी Hindi font 2 मिनट में install करें। Step-by-step screenshots guide।",
    kw="hindi font install windows 10, windows 11 hindi font kaise install kare, kruti dev install",
    thumb="अ",
    body="""<p>अगर आप पहली बार Hindi font install कर रहे हैं, तो यह guide आपके लिए है। <strong>सिर्फ 2 मिनट में</strong> किसी भी Hindi font को Windows में install करें।</p>
<div class="tip"><p><strong>💡 पहले font download करें:</strong> <a href="/fonts/">HindiFont.co.in</a> से 100% free fonts — कोई registration नहीं।</p></div>
<h2>Method 1: Right-Click Install (सबसे आसान)</h2>
<div class="steps">
<div class="step"><div class="step-n">1</div><div class="step-b"><h4>Font Download करें</h4><p><a href="/fonts/">HindiFont.co.in</a> से font download करें। .zip या .ttf file मिलेगी।</p></div></div>
<div class="step"><div class="step-n">2</div><div class="step-b"><h4>ZIP Extract करें</h4><p>File .zip हो तो Right-click → "Extract Here"। .ttf file मिलेगी।</p></div></div>
<div class="step"><div class="step-n">3</div><div class="step-b"><h4>.TTF पर Right-Click</h4><p>.ttf file पर Right-click करें।</p></div></div>
<div class="step"><div class="step-n">4</div><div class="step-b"><h4>"Install" Click करें</h4><p>Menu में <strong>"Install"</strong> click — Done! ✓</p></div></div>
<div class="step"><div class="step-n">5</div><div class="step-b"><h4>MS Word में Check करें</h4><p>Word open करें → Font list में नाम type करें → Select करें।</p></div></div>
</div>
<h2>Method 2: Control Panel से Install</h2>
<ol><li><strong>Windows + R</strong> → "control" → Enter</li><li><strong>Appearance → Fonts</strong> folder खोलें</li><li>.ttf file <strong>copy-paste</strong> करें — Automatic install!</li></ol>
<h2>Common Problems और Solutions</h2>
<h3>Font MS Word में नहीं दिख रहा?</h3>
<p><strong>Solution:</strong> MS Word close करके reopen करें। Font install के बाद running apps restart करें।</p>
<h3>"You don't have permission" Error?</h3>
<p><strong>Solution:</strong> .ttf पर Right-click → "Run as Administrator" → Install।</p>
<h3>Font install है लेकिन Hindi नहीं टाइप हो रही?</h3>
<p><strong>Solution:</strong> ANSI fonts के लिए Hindi keyboard चाहिए। Settings → Time & Language → Language → Add हिन्दी।</p>
<div class="i-cta"><div><h3>500+ Free Fonts Download करें</h3><p>Kruti Dev, Devlys, Mangal और बहुत कुछ — बिल्कुल free</p></div><a href="/fonts/">Browse Fonts →</a></div>
<h2>Mac पर Hindi Font Install</h2>
<div class="steps">
<div class="step"><div class="step-n">1</div><div class="step-b"><h4>Font Download करें</h4><p>.ttf file download करें।</p></div></div>
<div class="step"><div class="step-n">2</div><div class="step-b"><h4>Font Book खोलें</h4><p>Applications → Font Book। या font file double-click।</p></div></div>
<div class="step"><div class="step-n">3</div><div class="step-b"><h4>"Install Font" Click करें</h4><p>Done! Font available हो जाएगा।</p></div></div>
</div>
<div class="tip"><p><strong>🎯 Exam Tip:</strong> SSC के लिए <a href="/fonts/kruti-dev-010/">Kruti Dev 010</a>, UP exams के लिए <a href="/fonts/devlys-010/">Devlys 010</a>, CPCT के लिए <a href="/fonts/mangal/">Mangal</a> install करें।</p></div>"""),
  dict(slug="kruti-dev-vs-devlys",cat="Comparison",date="Jan 2025",read="5 min",
    title="Kruti Dev vs Devlys — कौन सा Font बेहतर है? (Exam Guide 2025)",
    desc="SSC, Railway, UP Police exams के लिए Kruti Dev और Devlys में क्या अंतर है — complete comparison with table।",
    kw="kruti dev vs devlys, ssc typing font, up police typing font, government exam hindi font",
    thumb="क",
    body="""<p>Government Hindi typing exam की preparation कर रहे हैं और confused हैं — <strong>Kruti Dev use करें या Devlys?</strong> इस article में complete answer है।</p>
<div class="tip"><p><strong>Quick Answer:</strong> SSC/Railway = <a href="/fonts/kruti-dev-010/">Kruti Dev 010</a> | UP Police/UPSSSC = <a href="/fonts/devlys-010/">Devlys 010</a> | CPCT = <a href="/fonts/mangal/">Mangal</a></p></div>
<h2>Comparison Table</h2>
<div style="overflow-x:auto;border-radius:12px;border:1px solid var(--border);margin:20px 0">
<table class="cmp-tbl">
<tr><th>Feature</th><th>Kruti Dev 010</th><th>Devlys 010</th></tr>
<tr><td>Font Type</td><td>ANSI</td><td>ANSI</td></tr>
<tr><td>Keyboard Layout</td><td>Remington</td><td>Remington</td></tr>
<tr><td>SSC CHSL/CGL</td><td class="yes">✓ Official</td><td class="no">✗</td></tr>
<tr><td>Railway NTPC</td><td class="yes">✓ Official</td><td class="no">✗</td></tr>
<tr><td>UP Police</td><td class="no">✗</td><td class="yes">✓ Official</td></tr>
<tr><td>UPSSSC/Lekhpal</td><td class="no">✗</td><td class="yes">✓ Official</td></tr>
<tr><td>CPCT (MP)</td><td class="no">✗</td><td class="no">✗ (Mangal)</td></tr>
<tr><td>File Size</td><td>~45 KB</td><td>~38 KB</td></tr>
<tr><td>Free Download</td><td class="yes">✓ Free</td><td class="yes">✓ Free</td></tr>
</table></div>
<h2>Kruti Dev 010 — Details</h2>
<p>Kruti Dev 010 <strong>India का सबसे popular government typing font</strong> है। SSC और Railway जैसे central government exams में official standard है। Remington keyboard layout use करता है — traditional Hindi typewriter जैसा।</p>
<h2>Devlys 010 — Details</h2>
<p>Devlys 010 <strong>UP state government exams का official font</strong> है। UP Police, UPSSSC, Lekhpal, Patwari — इन सभी में Devlys mandatory है। Keyboard layout similar है — switch करना easy है।</p>
<div class="warn"><p><strong>⚠️ Important:</strong> Font requirement change हो सकती है। हमेशा official exam notification ज़रूर check करें।</p></div>
<h2>Safe Approach</h2>
<p>दोनों install करें! दोनों free हैं — <a href="/fonts/kruti-dev-010/">Kruti Dev 010</a> और <a href="/fonts/devlys-010/">Devlys 010</a> दोनों HindiFont.co.in से download करें।</p>"""),
  dict(slug="unicode-vs-ansi",cat="Guide",date="Feb 2025",read="5 min",
    title="Unicode vs ANSI Hindi Font — क्या अंतर है? (2025 Simple Guide)",
    desc="Unicode और ANSI fonts में fundamental difference — कब कौन सा use करें, internet पर क्यों ANSI नहीं चलता।",
    kw="unicode vs ansi hindi font, unicode hindi font kya hai, mangal vs kruti dev difference",
    thumb="य",
    body="""<p>Hindi fonts की दुनिया में दो main types हैं: <strong>Unicode</strong> और <strong>ANSI</strong>। Confused हैं? यह simple guide सब clear कर देगी।</p>
<div class="tip"><p><strong>One Line Summary:</strong> ANSI (Kruti Dev, Devlys) = office/exam typing। Unicode (Mangal, Noto) = internet, email, social media।</p></div>
<h2>ANSI Fonts क्या हैं?</h2>
<p>ANSI fonts एक old encoding system use करते हैं जिसमें Hindi characters को English keyboard keys से map किया जाता है। जब आप Kruti Dev में type करते हैं, actually English characters type होते हैं जो Hindi की तरह दिखते हैं।</p>
<p><strong>इसीलिए:</strong> Email में paste करने पर Hindi नहीं दिखती। Internet पर garbled text आता है। Font installed न हो तो कुछ नहीं दिखता।</p>
<h2>Unicode Fonts क्या हैं?</h2>
<p>Unicode एक universal standard है जो हर Hindi character को एक unique code देता है। Mangal, Noto Sans, Hind — ये Unicode fonts हैं।</p>
<p><strong>Unicode के फायदे:</strong> Internet पर correctly दिखता है। Email में Hindi जाती है। Mobile पर काम करता है। Font install न हो तो भी text correct रहता है।</p>
<h2>Comparison</h2>
<div style="overflow-x:auto;border-radius:12px;border:1px solid var(--border);margin:20px 0">
<table class="cmp-tbl">
<tr><th>Feature</th><th>ANSI Font</th><th>Unicode Font</th></tr>
<tr><td>Examples</td><td>Kruti Dev, Devlys, Shree Lipi</td><td>Mangal, Noto Sans, Hind</td></tr>
<tr><td>Internet पर</td><td class="no">✗ नहीं दिखता</td><td class="yes">✓ Correctly दिखता</td></tr>
<tr><td>Email में</td><td class="no">✗ Garbled</td><td class="yes">✓ Perfect</td></tr>
<tr><td>SSC/UP Exam</td><td class="yes">✓ Official</td><td class="yes">✓ CPCT/Online</td></tr>
<tr><td>Website बनाना</td><td class="no">✗ Not suitable</td><td class="yes">✓ Best choice</td></tr>
<tr><td>WhatsApp/Social</td><td class="no">✗ Breaks</td><td class="yes">✓ Works perfectly</td></tr>
</table></div>
<h2>कौन सा Choose करें?</h2>
<p><strong>ANSI choose करें अगर:</strong> Government typing exam की preparation है। Traditional Hindi publishing है।</p>
<p><strong>Unicode choose करें अगर:</strong> Internet/email पर Hindi लिखनी है। Website/app बनानी है। Social media content है। CPCT exam है।</p>
<div class="tip"><p><strong>💡 Best Approach:</strong> दोनों install करें! Government exam के लिए Kruti Dev, digital use के लिए Noto Sans/Mangal।</p></div>"""),
  dict(slug="government-exam-hindi-typing-fonts",cat="Exam Guide",date="Feb 2025",read="6 min",
    title="Government Exam Hindi Typing Fonts 2025 — SSC, Railway, UP Police Complete List",
    desc="SSC CHSL/CGL, Railway NTPC, UP Police, CPCT — हर exam का exact font, keyboard layout और speed requirement।",
    kw="ssc hindi typing font, railway hindi typing font, up police typing font, cpct font 2025",
    thumb="स",
    body="""<p>Government typing exam में <strong>wrong font use करना = attempt invalid</strong>। इस guide में हर exam का exact font requirement है।</p>
<div class="warn"><p><strong>⚠️ Disclaimer:</strong> Font requirements change हो सकती हैं। Official exam notification ज़रूर check करें।</p></div>
<h2>Exam-wise Font Requirement Table</h2>
<div style="overflow-x:auto;border-radius:12px;border:1px solid var(--border);margin:20px 0">
<table class="cmp-tbl">
<tr><th>Exam</th><th>Font</th><th>Keyboard</th><th>Speed</th></tr>
<tr><td>SSC CHSL/CGL (Hindi)</td><td><a href="/fonts/kruti-dev-010/">Kruti Dev 010</a></td><td>Remington Gail</td><td>25 WPM</td></tr>
<tr><td>Railway NTPC/Group D</td><td><a href="/fonts/kruti-dev-010/">Kruti Dev 010</a></td><td>Remington</td><td>25 WPM</td></tr>
<tr><td>UP Police / SI</td><td><a href="/fonts/devlys-010/">Devlys 010</a></td><td>Remington</td><td>25 WPM</td></tr>
<tr><td>UPSSSC / Lekhpal</td><td><a href="/fonts/devlys-010/">Devlys 010</a></td><td>Remington</td><td>25 WPM</td></tr>
<tr><td>CPCT (Madhya Pradesh)</td><td><a href="/fonts/mangal/">Mangal</a></td><td>Inscript</td><td>5000 KDPH</td></tr>
<tr><td>High Court Stenographer</td><td><a href="/fonts/kruti-dev-010/">Kruti Dev 010</a></td><td>Remington</td><td>80-100 WPM</td></tr>
<tr><td>UPSC CAPF</td><td><a href="/fonts/mangal/">Mangal</a></td><td>Inscript</td><td>Varies</td></tr>
</table></div>
<h2>Fonts Download करें</h2>
<div class="i-cta"><div><h3>सभी Exam Fonts एक जगह</h3><p>Kruti Dev, Devlys, Mangal — free download</p></div><a href="/category/government-exam/">Download करें →</a></div>
<h2>Typing Speed Tips</h2>
<ul><li>Daily minimum <strong>30 minutes practice</strong> करें</li><li>Accuracy 95%+ रखें — speed बाद में बढ़ेगी</li><li>Touch typing सीखें — keyboard देखे बिना type करें</li><li>Practice और exam में <strong>same font use करें</strong></li></ul>"""),
  dict(slug="best-hindi-fonts-whatsapp",cat="Guide",date="Feb 2025",read="3 min",
    title="WhatsApp और Instagram के लिए Best Hindi Fonts 2025",
    desc="Social media पर stylish Hindi text कैसे type करें — WhatsApp, Instagram, Facebook के लिए best fonts।",
    kw="whatsapp hindi font, instagram hindi font, stylish hindi text, social media hindi typing",
    thumb="व",
    body="""<p>WhatsApp status, Instagram captions में stylish Hindi type करना चाहते हैं? यह guide आपके लिए है।</p>
<div class="tip"><p><strong>Important:</strong> Social media के लिए हमेशा <strong>Unicode fonts</strong> use करें — ANSI fonts social media पर garbled दिखते हैं।</p></div>
<h2>Best Hindi Fonts for Social Media</h2>
<ul>
<li><strong><a href="/fonts/noto-sans-devanagari/">Noto Sans Devanagari</a></strong> — Clean, readable, हर device पर perfect</li>
<li><strong><a href="/fonts/baloo-2/">Baloo 2</a></strong> — Playful और fun — creative posts के लिए</li>
<li><strong><a href="/fonts/hind/">Hind</a></strong> — Modern और professional</li>
<li><strong><a href="/fonts/yatra-one/">Yatra One</a></strong> — Bold impact headlines के लिए</li>
<li><strong><a href="/fonts/amita/">Amita</a></strong> — Calligraphic elegance</li>
</ul>
<h2>WhatsApp पर Hindi Stylish Type करें</h2>
<div class="steps">
<div class="step"><div class="step-n">1</div><div class="step-b"><h4>Phone में Hindi Keyboard Enable करें</h4><p>Settings → Language & Input → Add Hindi keyboard। यह automatically Unicode type करेगा।</p></div></div>
<div class="step"><div class="step-n">2</div><div class="step-b"><h4>Type करें और Share करें</h4><p>Hindi keyboard से type करें — सभी devices पर correctly दिखेगा।</p></div></div>
</div>
<h2>Stylish Text Generator</h2>
<p>PC पर किसी Unicode Hindi font में text type करें → Copy करें → WhatsApp में paste करें। Simple!</p>"""),
  dict(slug="hindi-font-android-install",cat="Tutorial",date="Mar 2025",read="4 min",
    title="Android Mobile में Hindi Font कैसे Install करें? (2025 Guide)",
    desc="Android phone में custom Hindi fonts install करने के methods — non-rooted और rooted दोनों phones के लिए।",
    kw="android hindi font install, mobile hindi font, hindi font android phone, smartphone devanagari font",
    thumb="म",
    body="""<p>Android phone में custom Hindi font install करना PC से अलग है। यहाँ सभी methods हैं।</p>
<h2>Method 1: iFont App (Non-Rooted — सबसे Easy)</h2>
<div class="steps">
<div class="step"><div class="step-n">1</div><div class="step-b"><h4>iFont App Download करें</h4><p>Play Store में "iFont" search → Install (free)।</p></div></div>
<div class="step"><div class="step-n">2</div><div class="step-b"><h4>Font File Load करें</h4><p><a href="/fonts/">HindiFont.co.in</a> से .ttf download → iFont में "My Fonts" → "+" → file select।</p></div></div>
<div class="step"><div class="step-n">3</div><div class="step-b"><h4>Apply करें</h4><p>"Apply" tap → Phone reboot।</p></div></div>
</div>
<div class="warn"><p><strong>Note:</strong> iFont Samsung phones पर best works। दूसरे brands पर limited support हो सकता है।</p></div>
<h2>Method 2: Samsung Built-in (Samsung Users)</h2>
<ul><li>Settings → Display → Font Size and Style → Font Style</li><li>या Good Lock → Theme Park → Fonts</li></ul>
<h2>Method 3: Rooted Phone</h2>
<ul><li>Root Explorer से /system/fonts/ खोलें</li><li>.ttf file paste करें → Permissions 644 set करें → Reboot</li></ul>
<div class="tip"><p><strong>💡 Easiest Solution:</strong> Phone की built-in Hindi keyboard use करें — automatically Noto Sans Devanagari (Unicode) use होगा और सभी devices पर perfect दिखेगा।</p></div>"""),
  dict(slug="free-hindi-calligraphy-fonts",cat="Font List",date="Mar 2025",read="3 min",
    title="Top 10 Free Hindi Calligraphy Fonts Download 2025 — Wedding, Artistic",
    desc="Wedding cards, Diwali greetings और artistic projects के लिए best free Hindi calligraphy fonts की curated list।",
    kw="hindi calligraphy font free, wedding card hindi font, artistic hindi font, devanagari calligraphy",
    thumb="क",
    body="""<p>Wedding invitations, Diwali cards, greeting cards — beautiful Hindi calligraphy fonts चाहिए? यहाँ top 10 free options हैं।</p>
<h2>Top 10 Free Hindi Calligraphy Fonts</h2>
<div class="steps">
<div class="step"><div class="step-n">1</div><div class="step-b"><h4><a href="/fonts/amita/">Amita</a></h4><p>Google Font — elegant calligraphic। Wedding invitations के लिए perfect।</p></div></div>
<div class="step"><div class="step-n">2</div><div class="step-b"><h4><a href="/fonts/laila/">Laila</a></h4><p>Multi-script calligraphic — premium wedding feel।</p></div></div>
<div class="step"><div class="step-n">3</div><div class="step-b"><h4><a href="/fonts/ponnala/">Ponnala</a></h4><p>Festive decorative — Diwali और celebrations के लिए।</p></div></div>
<div class="step"><div class="step-n">4</div><div class="step-b"><h4><a href="/fonts/chandas/">Chandas</a></h4><p>Sanskrit calligraphy — scholarly और traditional।</p></div></div>
<div class="step"><div class="step-n">5</div><div class="step-b"><h4><a href="/fonts/yatra-one/">Yatra One</a></h4><p>Bold signage style — posters और banners।</p></div></div>
<div class="step"><div class="step-n">6</div><div class="step-b"><h4><a href="/fonts/tiro-devanagari-hindi/">Tiro Devanagari</a></h4><p>Scholarly refined — literary और academic।</p></div></div>
<div class="step"><div class="step-n">7</div><div class="step-b"><h4><a href="/fonts/rozha-one/">Rozha One</a></h4><p>Bold serif display — editorial और headlines।</p></div></div>
<div class="step"><div class="step-n">8</div><div class="step-b"><h4><a href="/fonts/richa/">Richa</a></h4><p>Magazine calligraphy — aesthetic और elegant।</p></div></div>
<div class="step"><div class="step-n">9</div><div class="step-b"><h4><a href="/fonts/walkman-chanakya/">Chanakya</a></h4><p>Classic newspaper — traditional Hindi typography।</p></div></div>
<div class="step"><div class="step-n">10</div><div class="step-b"><h4><a href="/fonts/agra/">Agra</a></h4><p>Creative display — artistic projects के लिए।</p></div></div>
</div>
<div class="i-cta"><div><h3>सभी Calligraphy Fonts</h3><p>Wedding, festive और artistic fonts — free download</p></div><a href="/category/calligraphy/">Browse →</a></div>"""),
  dict(slug="hindi-web-fonts-guide",cat="Web Design",date="Mar 2025",read="4 min",
    title="Hindi Website के लिए Best Google Fonts 2025 — Developer Guide",
    desc="Hindi website बनाने के लिए best Google Fonts — implementation code, performance tips और font pairing guide।",
    kw="hindi web font google fonts, website ke liye hindi font, devanagari google font, noto sans devanagari implementation",
    thumb="व",
    body="""<p>Hindi website बना रहे हैं? Correct font choose करना user experience और SEO दोनों के लिए important है।</p>
<h2>क्यों Google Fonts?</h2>
<ul><li>100% free — personal और commercial</li><li>Fast CDN — site slow नहीं होगी</li><li>All browsers compatible</li><li>Easy to implement — 2 lines of code</li></ul>
<h2>Top Hindi Google Fonts</h2>
<div class="steps">
<div class="step"><div class="step-n">1</div><div class="step-b"><h4><a href="/fonts/noto-sans-devanagari/">Noto Sans Devanagari</a> — Best Overall</h4><p>Clean, modern, excellent readability। Body text के लिए #1 choice। 9 weights।</p></div></div>
<div class="step"><div class="step-n">2</div><div class="step-b"><h4><a href="/fonts/hind/">Hind</a> — Best for UI</h4><p>Specially designed for interfaces। 5 weights।</p></div></div>
<div class="step"><div class="step-n">3</div><div class="step-b"><h4><a href="/fonts/baloo-2/">Baloo 2</a> — Best Display</h4><p>Fun और playful। Headings के लिए।</p></div></div>
<div class="step"><div class="step-n">4</div><div class="step-b"><h4><a href="/fonts/teko/">Teko</a> — Best Bold Condensed</h4><p>Modern bold — banners और CTAs।</p></div></div>
</div>
<h2>CSS Implementation</h2>
<pre>&lt;link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@400;600;700&amp;display=swap" rel="stylesheet"&gt;</pre>
<pre>body {
  font-family: 'Noto Sans Devanagari', sans-serif;
}</pre>
<div class="tip"><p><strong>Performance Tip:</strong> <code>display=swap</code> parameter ज़रूर use करें — font loading से page blocking prevent होती है।</p></div>
<h2>Font Pairing Suggestions</h2>
<ul><li><strong>News site:</strong> Tiro Devanagari (headings) + Noto Sans (body)</li><li><strong>App/Startup:</strong> Baloo 2 (brand) + Hind (UI)</li><li><strong>Blog:</strong> Rozha One (headings) + Noto Serif (body)</li></ul>"""),
  dict(slug="hindi-typing-speed-tips",cat="Typing Tips",date="Apr 2025",read="5 min",
    title="Hindi Typing Speed कैसे बढ़ाएं? 10 Proven Tips — Government Exam 2025",
    desc="Hindi typing speed 10 से 30+ WPM बढ़ाने के proven techniques — government exam aspirants के लिए complete guide।",
    kw="hindi typing speed badhane ke tarike, typing speed tips hindi, kruti dev typing practice, hindi typing fast kaise kare",
    thumb="त",
    body="""<p>Government typing exam की preparation है और speed slow है? यह 10 proven tips आपकी speed ज़रूर बढ़ाएंगे।</p>
<div class="steps">
<div class="step"><div class="step-n">1</div><div class="step-b"><h4>Touch Typing सीखें</h4><p>Keyboard देखे बिना type करना सीखें। पहले 2 हफ्ते slow लगेगी — फिर speed automatically बढ़ेगी।</p></div></div>
<div class="step"><div class="step-n">2</div><div class="step-b"><h4>Daily 30-60 Min Practice</h4><p>Consistency key है। Irregular long sessions से better है daily 30 minutes।</p></div></div>
<div class="step"><div class="step-n">3</div><div class="step-b"><h4>Accuracy First, Speed Later</h4><p>95%+ accuracy रखें। Mistakes correct करने में time waste होता है।</p></div></div>
<div class="step"><div class="step-n">4</div><div class="step-b"><h4>Home Row Position</h4><p>Fingers हमेशा ASDF JKL; position पर। हर key के लिए specific finger assign करें।</p></div></div>
<div class="step"><div class="step-n">5</div><div class="step-b"><h4>Common Words First</h4><p>का, की, के, में, है, और, को — सबसे common Hindi words पहले master करें।</p></div></div>
<div class="step"><div class="step-n">6</div><div class="step-b"><h4>Newspaper से Practice</h4><p>Real newspaper text type करें — speed और accuracy दोनों improve होंगे।</p></div></div>
<div class="step"><div class="step-n">7</div><div class="step-b"><h4>Weekly Typing Tests</h4><p>Progress track करें। Improvement देखने से motivation मिलती है।</p></div></div>
<div class="step"><div class="step-n">8</div><div class="step-b"><h4>Rhythm में Type करें</h4><p>Burst typing से better है steady rhythm — consistent speed रखें।</p></div></div>
<div class="step"><div class="step-n">9</div><div class="step-b"><h4>Correct Posture</h4><p>Straight बैठें, wrists neutral रखें। Poor posture से fatigue → slow speed।</p></div></div>
<div class="step"><div class="step-n">10</div><div class="step-b"><h4>Correct Font Use करें</h4><p>Practice और exam में same font! <a href="/fonts/kruti-dev-010/">Kruti Dev 010</a> (SSC) या <a href="/fonts/devlys-010/">Devlys 010</a> (UP)।</p></div></div>
</div>
<div class="tip"><p><strong>🎯 Goal:</strong> 3-4 months की consistent practice से 25-30 WPM achieve किया जा सकता है।</p></div>"""),
  dict(slug="ms-word-hindi-font-guide",cat="Tutorial",date="Apr 2025",read="3 min",
    title="MS Word में Hindi Font Use करने का Complete Guide 2025",
    desc="MS Word में Hindi fonts use करना, Hindi typing enable करना और documents को properly save करना — step by step।",
    kw="ms word hindi font, word mein hindi kaise type kare, microsoft word hindi typing, word hindi document save",
    thumb="व",
    body="""<p>MS Word में Hindi type करना है? यह guide step-by-step बताएगी।</p>
<h2>Step 1: Hindi Font Install करें</h2>
<p>पहले font install करें। <a href="/fonts/">HindiFont.co.in</a> से free download → <a href="/blog/hindi-font-install-windows/">install guide</a> follow करें।</p>
<h2>Step 2: Word में Font Select करें</h2>
<div class="steps">
<div class="step"><div class="step-n">1</div><div class="step-b"><h4>MS Word Open करें</h4><p>New document open करें।</p></div></div>
<div class="step"><div class="step-n">2</div><div class="step-b"><h4>Font Dropdown में Name Type करें</h4><p>Font field में "Kruti Dev 010" type करें।</p></div></div>
<div class="step"><div class="step-n">3</div><div class="step-b"><h4>Select करें और Type करें</h4><p>Font select करें और Hindi typing शुरू करें।</p></div></div>
</div>
<h2>Step 3: Hindi Keyboard Enable करें</h2>
<ul><li>Settings → Time & Language → Language → + हिन्दी add करें</li><li>Taskbar में language switcher आएगा (ENG ↔ HIN)</li><li>या Windows + Space से switch करें</li></ul>
<h2>ANSI vs Unicode in Word</h2>
<ul><li><strong>ANSI (Kruti Dev, Devlys):</strong> Font select करें → Remington keyboard से type करें</li><li><strong>Unicode (Mangal, Noto):</strong> Hindi Inscript keyboard enable करें → type करें</li></ul>
<div class="tip"><p><strong>💾 Save Tip:</strong> Share करना है तो PDF export करें — font automatically embed होगा। Word document share करते समय receiver के PC में font होना ज़रूरी है (ANSI fonts के लिए)।</p></div>"""),
  dict(slug="top-hindi-fonts-design",cat="Design",date="May 2025",read="4 min",
    title="Graphic Design के लिए Best 10 Hindi Fonts 2025 — Logos, Posters, Branding",
    desc="Logos, posters, branding और creative projects के लिए best Hindi fonts — designer's curated guide।",
    kw="hindi font for design, logo hindi font, poster hindi font, graphic design devanagari font, branding hindi",
    thumb="ड",
    body="""<p>Graphic designer हैं और Hindi में stunning designs बनाना चाहते हैं? यहाँ curated list है।</p>
<h2>Top 10 Hindi Fonts for Design</h2>
<div class="steps">
<div class="step"><div class="step-n">1</div><div class="step-b"><h4><a href="/fonts/yatra-one/">Yatra One</a> — Bold Impact</h4><p>Movie posters और powerful headlines के लिए।</p></div></div>
<div class="step"><div class="step-n">2</div><div class="step-b"><h4><a href="/fonts/baloo-2/">Baloo 2</a> — Friendly Brand</h4><p>Food brands, kids products और friendly businesses।</p></div></div>
<div class="step"><div class="step-n">3</div><div class="step-b"><h4><a href="/fonts/tiro-devanagari-hindi/">Tiro Devanagari</a> — Luxury</h4><p>Premium brands और high-end services।</p></div></div>
<div class="step"><div class="step-n">4</div><div class="step-b"><h4><a href="/fonts/rozha-one/">Rozha One</a> — Editorial</h4><p>Magazines और editorial layout।</p></div></div>
<div class="step"><div class="step-n">5</div><div class="step-b"><h4><a href="/fonts/amita/">Amita</a> — Elegant Script</h4><p>Wedding brands और lifestyle।</p></div></div>
<div class="step"><div class="step-n">6</div><div class="step-b"><h4><a href="/fonts/ponnala/">Ponnala</a> — Festive</h4><p>Diwali marketing और celebrations।</p></div></div>
<div class="step"><div class="step-n">7</div><div class="step-b"><h4><a href="/fonts/teko/">Teko</a> — Tech Modern</h4><p>Startups, apps और modern brands।</p></div></div>
<div class="step"><div class="step-n">8</div><div class="step-b"><h4><a href="/fonts/mukta/">Mukta</a> — Clean Brand</h4><p>Clean branding और contemporary identity।</p></div></div>
<div class="step"><div class="step-n">9</div><div class="step-b"><h4><a href="/fonts/laila/">Laila</a> — Multicultural</h4><p>Bilingual और multicultural projects।</p></div></div>
<div class="step"><div class="step-n">10</div><div class="step-b"><h4><a href="/fonts/noto-sans-devanagari/">Noto Sans Devanagari</a> — Versatile</h4><p>All-purpose — logos से UI तक।</p></div></div>
</div>
<div class="tip"><p><strong>Pro Tip:</strong> Design में हमेशा <strong>Unicode fonts</strong> use करें — export पर text correctly render होगा।</p></div>"""),
  dict(slug="photoshop-hindi-font-guide",cat="Tutorial",date="May 2025",read="3 min",
    title="Photoshop में Hindi Font कैसे Use करें? — Complete 2025 Guide",
    desc="Adobe Photoshop में Hindi text add करना — World Ready Composer, font selection और best fonts for Photoshop।",
    kw="photoshop hindi font, hindi text photoshop, adobe photoshop devanagari, photoshop hindi typing",
    thumb="फ",
    body="""<p>Photoshop में Hindi text add करना है? यह guide step-by-step बताएगी।</p>
<h2>Prerequisites</h2>
<ul><li>Hindi font install होना चाहिए (install नहीं है? <a href="/fonts/">यहाँ से download करें</a>)</li><li>Adobe Photoshop CC 2015 या newer</li></ul>
<h2>Photoshop में Hindi Text — Steps</h2>
<div class="steps">
<div class="step"><div class="step-n">1</div><div class="step-b"><h4>World Ready Composer Enable करें</h4><p>Edit → Preferences → Type → "World Ready Composer" select करें → OK → Photoshop Restart।</p></div></div>
<div class="step"><div class="step-n">2</div><div class="step-b"><h4>Text Tool Select करें</h4><p>T (Type tool) press करें।</p></div></div>
<div class="step"><div class="step-n">3</div><div class="step-b"><h4>Hindi Font Select करें</h4><p>Font dropdown में "Noto Sans Devanagari" या अपना font select करें।</p></div></div>
<div class="step"><div class="step-n">4</div><div class="step-b"><h4>Hindi Keyboard Switch करें</h4><p>Windows + Space → Hindi keyboard → Type करें।</p></div></div>
</div>
<div class="warn"><p><strong>Important:</strong> Photoshop में Unicode fonts (Noto Sans, Mangal, Hind) better काम करते हैं। ANSI fonts में rendering issues हो सकती हैं।</p></div>
<h2>Best Hindi Fonts for Photoshop</h2>
<ul>
<li><strong><a href="/fonts/noto-sans-devanagari/">Noto Sans Devanagari</a></strong> — Clean body text</li>
<li><strong><a href="/fonts/baloo-2/">Baloo 2</a></strong> — Fun display</li>
<li><strong><a href="/fonts/yatra-one/">Yatra One</a></strong> — Bold impact posters</li>
<li><strong><a href="/fonts/amita/">Amita</a></strong> — Calligraphic elegance</li>
<li><strong><a href="/fonts/rozha-one/">Rozha One</a></strong> — Editorial headlines</li>
</ul>"""),
]

def build_blog(b, all_b):
    others=[x for x in all_b if x["slug"]!=b["slug"]][:3]
    rel="".join([f'<a href="/blog/{o["slug"]}/" class="bc"><div class="bc-thumb">{o["thumb"]}</div><div class="bc-body"><span class="bc-cat">{o["cat"]}</span><h3>{o["title"]}</h3><p>{o["desc"]}</p><span class="bc-more">पढ़ें →</span></div></a>' for o in others])
    return f"""{head(b["title"]+" | HindiFont.co.in",b["desc"],b["kw"],f'/blog/{b["slug"]}/',2)}
{schema_article(b)}
{hdr()}
<div class="bh"><div class="wrap"><span class="bh-cat">{b["cat"]}</span>
<h1>{b["title"]}</h1>
<div class="bh-meta"><span>{b["date"]}</span><span>{b["read"]} read</span><span>HindiFont Team</span></div>
</div></div>
{crumb([("Home","/"),("Blog","/blog/"),(b["title"][:45]+"…",None)],2)}
<main>
<div class="sec sec-white">
<div class="wrap">
<div style="display:grid;grid-template-columns:1fr 260px;gap:44px;align-items:start" class="blog-layout">
<article class="bpc">{b["body"]}
<div class="tip" style="margin-top:32px"><p><strong>📥 Related Fonts:</strong> इस article के fonts <a href="/fonts/">HindiFont.co.in</a> पर free available हैं।</p></div>
</article>
<aside class="blog-layout-aside" style="position:sticky;top:78px">
<div style="background:var(--white);border:2px solid var(--border);border-radius:var(--r16);padding:20px;margin-bottom:16px">
<h3 style="font-family:var(--fd);font-size:1rem;margin-bottom:14px">Popular Fonts</h3>
<a href="/fonts/kruti-dev-010/" style="display:block;color:var(--gold);font-size:.83rem;font-weight:600;margin-bottom:8px">⬇ Kruti Dev 010</a>
<a href="/fonts/devlys-010/" style="display:block;color:var(--gold);font-size:.83rem;font-weight:600;margin-bottom:8px">⬇ Devlys 010</a>
<a href="/fonts/mangal/" style="display:block;color:var(--gold);font-size:.83rem;font-weight:600;margin-bottom:8px">⬇ Mangal Font</a>
<a href="/fonts/noto-sans-devanagari/" style="display:block;color:var(--gold);font-size:.83rem;font-weight:600;margin-bottom:8px">⬇ Noto Sans Devanagari</a>
<a href="/fonts/hind/" style="display:block;color:var(--gold);font-size:.83rem;font-weight:600">⬇ Hind Font</a>
</div>
<div style="background:linear-gradient(135deg,var(--gold),var(--gold2));border-radius:var(--r16);padding:20px;text-align:center">
<p style="font-family:var(--fd);font-size:1rem;font-weight:700;margin-bottom:6px;color:var(--ink)">500+ Free Fonts</p>
<p style="font-size:.78rem;color:rgba(13,12,10,.7);margin-bottom:14px">सभी fonts free download</p>
<a href="/fonts/" style="background:var(--ink);color:#fff;padding:9px 18px;border-radius:var(--r8);font-weight:700;font-size:.82rem;display:block;text-align:center">Browse →</a>
</div>
</aside>
</div>
</div>
</div>
<div class="sec sec-tint">
<div class="wrap"><div class="sec-hdr"><h2 class="sec-title">Related Articles</h2></div>
<div class="blog-grid">{rel}</div></div>
</div>
</main>
{ftr(2)}"""

os.makedirs(f"{BASE}/blog",exist_ok=True)
for b in BLOGS:
    os.makedirs(f"{BASE}/blog/{b['slug']}",exist_ok=True)
    open(f"{BASE}/blog/{b['slug']}/index.html","w").write(build_blog(b,BLOGS))

print(f"✅ {len(BLOGS)} blog pages built")

# ══════════════════════════════════════════════════
# HOMEPAGE
# ══════════════════════════════════════════════════
all_fc = "\n".join([fc(f) for f in FONTS])
blog_cards = "\n".join([f'<a href="/blog/{b["slug"]}/" class="bc"><div class="bc-thumb">{b["thumb"]}</div><div class="bc-body"><span class="bc-cat">{b["cat"]}</span><h3>{b["title"]}</h3><p>{b["desc"]}</p><span class="bc-more">पढ़ें →</span></div></a>' for b in BLOGS[:6]])

hp = f"""{head("Hindi Font Download — 500+ Free Hindi Fonts | HindiFont.co.in",
"Download 500+ free Hindi fonts — Kruti Dev, Devlys, Mangal, Unicode fonts। SSC, Railway, UP Police exams। No registration, instant download।",
"hindi font download, kruti dev font, devlys font, mangal font, unicode hindi font, free hindi fonts, ssc typing font","/")}<script type="application/ld+json">{{"@context":"https://schema.org","@type":"WebSite","name":"HindiFont.co.in","url":"https://hindifont.co.in","potentialAction":{{"@type":"SearchAction","target":"https://hindifont.co.in/fonts/?q={{search_term_string}}","query-input":"required name=search_term_string"}}}}</script>
{hdr()}
<!-- HERO -->
<section class="hero">
<div class="hero-bg"></div><div class="hero-grid-bg"></div>
<div class="hero-deva-bg" aria-hidden="true">अ आ इ ई</div>
<div class="wrap">
  <div class="eyebrow"><span class="eyebrow-dot"></span>India का #1 Free Hindi Font Website</div>
  <h1><span class="hi">हिंदी फॉन्ट डाउनलोड करें</span>500+ <em>Free</em> Hindi Fonts</h1>
  <p class="hero-sub">Kruti Dev, Devlys, Mangal, Chandas और 500+ fonts — completely free। Government exam, websites, WhatsApp, design — सबके लिए। No registration।</p>
  <div class="search-box" role="search">
    <input type="text" id="si" placeholder="Font खोजें... (Kruti Dev, Mangal, Hind...)" aria-label="Search fonts">
    <button id="sb" aria-label="Search">🔍</button>
  </div>
  <div class="hero-stats">
    <div><div class="stat-n">{len(FONTS)}+</div><div class="stat-l">Hindi Fonts</div></div>
    <div><div class="stat-n">100%</div><div class="stat-l">Free Download</div></div>
    <div><div class="stat-n">0</div><div class="stat-l">Registration</div></div>
    <div><div class="stat-n">10L+</div><div class="stat-l">Downloads</div></div>
  </div>
</div>
</section>

<!-- CATEGORIES -->
<section class="sec sec-tint">
<div class="wrap">
<div class="sec-hdr-row">
  <div><span class="sec-tag">Browse by Type</span><h2 class="sec-title">Font Categories</h2></div>
  <a href="/category/" class="view-all">सभी Categories →</a>
</div>
<div class="cat-grid">
  <a href="/category/government-exam/" class="cat-card"><div class="cat-icon">स</div><div class="cat-name">Govt Exam</div><div class="cat-cnt">SSC, UP Police, Railway</div></a>
  <a href="/category/unicode/" class="cat-card"><div class="cat-icon">य</div><div class="cat-name">Unicode</div><div class="cat-cnt">Internet, Web, Apps</div></a>
  <a href="/category/ansi/" class="cat-card"><div class="cat-icon">क</div><div class="cat-name">ANSI Fonts</div><div class="cat-cnt">Office, Typing</div></a>
  <a href="/category/web-fonts/" class="cat-card"><div class="cat-icon">व</div><div class="cat-name">Web Fonts</div><div class="cat-cnt">Google Fonts</div></a>
  <a href="/category/calligraphy/" class="cat-card"><div class="cat-icon">ल</div><div class="cat-name">Calligraphy</div><div class="cat-cnt">Wedding, Artistic</div></a>
  <a href="/category/stylish/" class="cat-card"><div class="cat-icon">ब</div><div class="cat-name">Stylish</div><div class="cat-cnt">Social, Design</div></a>
  <a href="/category/wedding/" class="cat-card"><div class="cat-icon">श</div><div class="cat-name">Wedding</div><div class="cat-cnt">Cards, Invitations</div></a>
  <a href="/fonts/" class="cat-card" style="border-style:dashed"><div class="cat-icon" style="color:var(--stone2)">+</div><div class="cat-name">View All</div><div class="cat-cnt">500+ fonts</div></a>
</div>
</div>
</section>

<!-- ALL FONTS -->
<section class="sec">
<div class="wrap">
<div class="sec-hdr-row">
  <div><span class="sec-tag">Most Downloaded</span><h2 class="sec-title">🔥 Top Hindi Fonts</h2><p class="sec-sub">सबसे ज़्यादा download किए जाने वाले fonts</p></div>
  <a href="/fonts/" class="view-all">सभी {len(FONTS)} Fonts →</a>
</div>
<div class="pills">
  <button class="pill on" data-f="all">सभी <span style="background:rgba(0,0,0,.08);padding:1px 8px;border-radius:10px;font-size:.7rem;margin-left:4px">{len(FONTS)}</span></button>
  <button class="pill" data-f="government-exam">Govt Exam</button>
  <button class="pill" data-f="unicode">Unicode</button>
  <button class="pill" data-f="ansi">ANSI</button>
  <button class="pill" data-f="web-fonts">Web Fonts</button>
  <button class="pill" data-f="calligraphy">Calligraphy</button>
  <button class="pill" data-f="wedding">Wedding</button>
  <button class="pill" data-f="stylish">Stylish</button>
</div>
<div class="fonts-grid">{all_fc}</div>
</div>
</section>

<!-- CTA -->
<section style="padding:0 0 64px">
<div class="wrap">
<div class="cta-band">
  <div><h2>Government Exam Font Pack</h2><p>SSC, Railway, UP Police, CPCT — सभी exams के correct fonts। Free download, zero registration।</p></div>
  <a href="/category/government-exam/" class="cta-band-btn">Free Download करें →</a>
</div>
</div>
</section>

<!-- BLOG -->
<section class="sec sec-tint">
<div class="wrap">
<div class="sec-hdr-row">
  <div><span class="sec-tag">Guides & Tutorials</span><h2 class="sec-title">📖 Hindi Font Blog</h2><p class="sec-sub">Fonts के बारे में complete guides और tips</p></div>
  <a href="/blog/" class="view-all">सभी Articles →</a>
</div>
<div class="blog-grid">{blog_cards}</div>
</div>
</section>

<!-- FAQ -->
<section class="sec sec-white">
<div class="wrap-sm">
<div class="sec-hdr"><span class="sec-tag">Common Questions</span><h2 class="sec-title">Frequently Asked Questions</h2></div>
<div class="faq-list">
  <div class="faq-item"><button class="faq-btn"><span class="faq-q">HindiFont.co.in पर सभी fonts बिल्कुल free हैं?</span><i class="faq-ico">+</i></button><div class="faq-ans"><div class="faq-ans-inner">हाँ — 100% free। No registration, no payment, no subscription। Direct download करें।</div></div></div>
  <div class="faq-item"><button class="faq-btn"><span class="faq-q">Government typing exam के लिए कौन सा font best है?</span><i class="faq-ico">+</i></button><div class="faq-ans"><div class="faq-ans-inner">SSC/Railway → <a href="/fonts/kruti-dev-010/">Kruti Dev 010</a>। UP Police/UPSSSC → <a href="/fonts/devlys-010/">Devlys 010</a>। CPCT → <a href="/fonts/mangal/">Mangal</a>। Official notification ज़रूर check करें।</div></div></div>
  <div class="faq-item"><button class="faq-btn"><span class="faq-q">Windows 11 में Hindi font कैसे install करें?</span><i class="faq-ico">+</i></button><div class="faq-ans"><div class="faq-ans-inner">Download → ZIP extract → .ttf Right-click → Install। 2 मिनट का process। <a href="/blog/hindi-font-install-windows/">Complete guide यहाँ।</a></div></div></div>
  <div class="faq-item"><button class="faq-btn"><span class="faq-q">WhatsApp पर best Hindi font कौन सा है?</span><i class="faq-ico">+</i></button><div class="faq-ans"><div class="faq-ans-inner">Social media के लिए <a href="/fonts/noto-sans-devanagari/">Noto Sans Devanagari</a> — Unicode होने से सभी devices पर correctly दिखता है।</div></div></div>
  <div class="faq-item"><button class="faq-btn"><span class="faq-q">Unicode और ANSI font में क्या अंतर है?</span><i class="faq-ico">+</i></button><div class="faq-ans"><div class="faq-ans-inner">ANSI (Kruti Dev, Devlys): Govt exam typing के लिए। Unicode (Mangal, Noto): Internet, email, social media के लिए। <a href="/blog/unicode-vs-ansi/">Detailed guide यहाँ।</a></div></div></div>
  <div class="faq-item"><button class="faq-btn"><span class="faq-q">Android phone में Hindi font कैसे install करें?</span><i class="faq-ico">+</i></button><div class="faq-ans"><div class="faq-ans-inner">iFont app (Play Store — free) use करें। Samsung में Settings → Display → Font Style। <a href="/blog/hindi-font-android-install/">Complete guide।</a></div></div></div>
</div>
</div>
</section>
</main>
{ftr()}"""
open(f"{BASE}/index.html","w").write(hp)
print("✅ Homepage built")

# ══════════════════════════════════════════════════
# LISTING PAGES — Fonts, Blog
# ══════════════════════════════════════════════════
all_fc2 = "\n".join([fc(f) for f in FONTS])
fonts_page = f"""{head(f"सभी Hindi Fonts Download — {len(FONTS)}+ Free Fonts | HindiFont.co.in",
"500+ free Hindi fonts — Kruti Dev, Devlys, Mangal, Unicode, Calligraphy। No registration। Instant download।",
"all hindi fonts download, hindi font list, free hindi fonts","/fonts/",1)}
{hdr()}
{crumb([("Home","/"),("All Fonts",None)],1)}
<div class="ph"><div class="wrap"><h1>सभी Hindi Fonts ({len(FONTS)}+)</h1><p>Kruti Dev से Unicode तक — सभी fonts free। No registration, instant download।</p></div></div>
<main><div class="sec"><div class="wrap">
<div class="pills">
  <button class="pill on" data-f="all">सभी ({len(FONTS)})</button>
  <button class="pill" data-f="government-exam">Govt Exam</button>
  <button class="pill" data-f="unicode">Unicode</button>
  <button class="pill" data-f="ansi">ANSI</button>
  <button class="pill" data-f="web-fonts">Web Fonts</button>
  <button class="pill" data-f="calligraphy">Calligraphy</button>
  <button class="pill" data-f="wedding">Wedding</button>
  <button class="pill" data-f="stylish">Stylish</button>
</div>
<div class="fonts-grid">{all_fc2}</div>
</div></div></main>
{ftr(1)}"""
open(f"{BASE}/fonts/index.html","w").write(fonts_page)

all_bc = "\n".join([f'<a href="/blog/{b["slug"]}/" class="bc"><div class="bc-thumb">{b["thumb"]}</div><div class="bc-body"><span class="bc-cat">{b["cat"]}</span><h3>{b["title"]}</h3><p>{b["desc"]}</p><span class="bc-more">पढ़ें →</span></div></a>' for b in BLOGS])
blog_idx = f"""{head("Hindi Font Blog — Guides, Tutorials & Tips | HindiFont.co.in",
"Hindi fonts के बारे में complete guides — install guide, exam tips, typing speed, web fonts।",
"hindi font guide, hindi typing tutorial, govt exam font guide","/blog/",1)}
{hdr()}
{crumb([("Home","/"),("Blog",None)],1)}
<div class="ph"><div class="wrap"><h1>Hindi Font Blog</h1><p>Guides, tutorials और expert tips — Hindi fonts और typing के बारे में।</p></div></div>
<main><div class="sec"><div class="wrap"><div class="blog-grid">{all_bc}</div></div></div></main>
{ftr(1)}"""
open(f"{BASE}/blog/index.html","w").write(blog_idx)
print("✅ Fonts listing + Blog index done")

# ══════════════════════════════════════════════════
# CATEGORY PAGES
# ══════════════════════════════════════════════════
CATS = [
  ("government-exam","Government Exam Fonts","सरकारी","SSC, Railway, UP Police, CPCT typing exams के official Hindi fonts।","government-exam"),
  ("unicode","Unicode Hindi Fonts","यूनिकोड","Internet, websites, email और digital content के लिए Unicode Devanagari।","unicode"),
  ("ansi","ANSI Hindi Fonts","ANSI","Traditional ANSI fonts for government offices और typing exams।","ansi"),
  ("web-fonts","Hindi Web Fonts","वेब","Websites और apps के लिए Google Fonts — fast और free।","web-fonts"),
  ("calligraphy","Calligraphy Hindi Fonts","कैलीग्राफी","Wedding invitations, artistic projects के लिए calligraphy fonts।","calligraphy"),
  ("stylish","Stylish Hindi Fonts","स्टाइलिश","Social media, branding और creative projects के लिए।","stylish"),
  ("wedding","Wedding Hindi Fonts","शादी","Wedding cards, invitations और special occasions के लिए।","wedding"),
]
os.makedirs(f"{BASE}/category",exist_ok=True)
for slug,name,deva,desc,fc_filter in CATS:
    cat_fonts=[f for f in FONTS if fc_filter in f["cats"]] or FONTS[:6]
    cards="\n".join([fc(f) for f in cat_fonts])
    pg=f"""{head(f"{name} Free Download | HindiFont.co.in",f"{desc} Free download, no registration.",f"{name.lower()}, hindi font, free download",f"/category/{slug}/",2)}
{hdr()}
{crumb([("Home","/"),("Categories","/category/"),(name,None)],2)}
<div class="ph"><div class="wrap"><h1>{name}</h1><p>{desc}</p></div></div>
<main><div class="sec"><div class="wrap"><div class="fonts-grid">{cards}</div></div></div></main>
{ftr(2)}"""
    os.makedirs(f"{BASE}/category/{slug}",exist_ok=True)
    open(f"{BASE}/category/{slug}/index.html","w").write(pg)

# Category index
ci_items="\n".join([f'<a href="/category/{s}/" class="cat-card"><div class="cat-icon">{d}</div><div class="cat-name">{n}</div><div class="cat-cnt">{de[:40]}</div></a>' for s,n,d,de,_ in CATS])
ci=f"""{head("Hindi Font Categories | HindiFont.co.in","Hindi fonts को category के हिसाब से browse करें।","hindi font categories, government exam font, unicode font","/category/",1)}
{hdr()}
{crumb([("Home","/"),("Categories",None)],1)}
<div class="ph"><div class="wrap"><h1>Font Categories</h1><p>अपनी ज़रूरत के हिसाब से category choose करें।</p></div></div>
<main><div class="sec"><div class="wrap">
<div class="cat-grid" style="grid-template-columns:repeat(auto-fill,minmax(200px,1fr))">{ci_items}</div>
</div></div></main>
{ftr(1)}"""
open(f"{BASE}/category/index.html","w").write(ci)
print(f"✅ {len(CATS)} category pages + index built")

# ══════════════════════════════════════════════════
# STATIC PAGES — About, Contact, Privacy, Disclaimer, Terms
# ══════════════════════════════════════════════════
def static(slug,title,subtitle,body,depth=1):
    pg=f"""{head(f"{title} | HindiFont.co.in",subtitle,title.lower()+", hindifont.co.in",f"/{slug}/",depth)}
{hdr()}
{crumb([("Home","/"),("…",None)],depth) if depth>1 else crumb([("Home","/"),("…",None)],depth)}
<div class="ph"><div class="wrap"><h1>{title}</h1><p>{subtitle}</p></div></div>
<main><div class="sec sec-white"><div class="wrap-xs"><div class="prose">{body}</div></div></div></main>
{ftr(depth)}"""
    os.makedirs(f"{BASE}/{slug}",exist_ok=True)
    open(f"{BASE}/{slug}/index.html","w").write(pg)

static("about","About Us","HindiFont.co.in — India का #1 free Hindi font download platform","""
<p>HindiFont.co.in India का leading free Hindi font download platform है। हमारा mission है — हर Hindi user को बिना किसी cost के quality fonts provide करना।</p>
<h2>हमारे बारे में</h2>
<p>चाहे आप government typing exam की preparation कर रहे हों, website बना रहे हों, wedding card design कर रहे हों, या social media posts बना रहे हों — HindiFont.co.in पर आपके लिए सही font available है।</p>
<h2>हम क्या Offer करते हैं</h2>
<ul><li>500+ free Hindi fonts — ANSI और Unicode दोनों</li><li>No registration required — direct download</li><li>Government exam fonts (Kruti Dev, Devlys, Mangal)</li><li>Web fonts, calligraphy fonts, stylish fonts</li><li>Step-by-step installation guides</li><li>Hindi typing tips और tutorials</li></ul>
<h2>Copyright Notice</h2>
<p>HindiFont.co.in fonts create नहीं करता — हम existing free/open-source fonts को organize करके provide करते हैं। सभी fonts के copyright उनके respective creators के पास हैं। हम केवल free fonts list करते हैं।</p>
<h2>Contact</h2>
<p>हमसे contact करें: <strong>contact@hindifont.co.in</strong></p>
""")

static("contact","Contact Us","हमसे contact करें — font requests, feedback, support","""
<h2>Contact Information</h2>
<p><strong>Email:</strong> contact@hindifont.co.in</p>
<p>हम आमतौर पर 24-48 hours में reply करते हैं।</p>
<h2>Font Request</h2>
<p>कोई specific Hindi font चाहिए जो यहाँ नहीं है? Email करें। हम add करने की कोशिश करेंगे।</p>
<h2>Bug Report</h2>
<p>Website पर कोई issue मिला? Download link broken है? Email पर बताएं — हम fix करेंगे।</p>
<h2>Copyright Complaint</h2>
<p>अगर आपको लगता है कि हमने आपके copyrighted content को बिना permission के use किया है — हमें तुरंत email करें। हम immediately remove करेंगे।</p>
<h2>Advertise with Us</h2>
<p>HindiFont.co.in पर advertise करना चाहते हैं? Email करें।</p>
""")

static("privacy-policy","Privacy Policy","HindiFont.co.in की privacy policy — आपकी data कैसे use होती है","""
<p><strong>Last Updated:</strong> January 2025</p>
<h2>Data Collection</h2>
<p>HindiFont.co.in minimal data collect करता है। हम registration require नहीं करते। Google Analytics के through anonymous usage data (page views, popular fonts, geography) collect होता है।</p>
<h2>Cookies</h2>
<p>हम basic session cookies और Google Analytics cookies use करते हैं। ये cookies personally identifiable information collect नहीं करतीं।</p>
<h2>Font Downloads</h2>
<p>Font download करते समय कोई personal data collect नहीं होता। Downloads completely anonymous हैं।</p>
<h2>Third-Party Links</h2>
<p>हमारी website में third-party links हो सकते हैं। उन sites की privacy policies हमारी responsibility नहीं है।</p>
<h2>Data Security</h2>
<p>हम industry-standard security measures use करते हैं। चूँकि हम personal data collect नहीं करते, data breach का risk minimal है।</p>
<h2>Children's Privacy</h2>
<p>हम knowingly 13 वर्ष से कम उम्र के बच्चों का data collect नहीं करते।</p>
<h2>Changes to Policy</h2>
<p>Policy changes इस page पर update की जाएंगी। Regular check करते रहें।</p>
<h2>Contact</h2>
<p>Privacy related questions: <strong>privacy@hindifont.co.in</strong></p>
""")

static("disclaimer","Disclaimer","HindiFont.co.in का legal disclaimer","""
<p><strong>Last Updated:</strong> January 2025</p>
<h2>Font Ownership</h2>
<p>HindiFont.co.in किसी भी font का creator या owner नहीं है। सभी fonts के copyright उनके respective designers और foundries के पास हैं।</p>
<h2>Free Fonts Only</h2>
<p>हम केवल वही fonts list करते हैं जो free for personal use के रूप में publicly available हैं। Download करने से पहले individual font की license ज़रूर पढ़ें।</p>
<h2>Commercial Use</h2>
<p>Personal use के लिए free होने का मतलब यह नहीं कि commercial use भी free है। Commercial projects के लिए font की specific license check करें।</p>
<h2>Accuracy</h2>
<p>हम font information को accurate रखने की कोशिश करते हैं लेकिन errors हो सकते हैं। Important decisions लेने से पहले original source verify करें।</p>
<h2>No Warranty</h2>
<p>सभी fonts "as is" basis पर provide किए जाते हैं। HindiFont.co.in किसी भी font के use से होने वाले damage के लिए liable नहीं है।</p>
<h2>DMCA</h2>
<p>अगर आपका copyrighted font यहाँ listed है: <strong>dmca@hindifont.co.in</strong> पर email करें। हम 48 hours में remove करेंगे।</p>
""")

static("terms","Terms of Use","HindiFont.co.in — Terms and Conditions of Use","""
<p><strong>Last Updated:</strong> January 2025</p>
<p>HindiFont.co.in (the "Site") use करके आप इन terms को accept करते हैं।</p>
<h2>Permitted Use</h2>
<ul><li>Font pages browse करना</li><li>Personal use के लिए free fonts download करना</li><li>Installation guides read करना</li></ul>
<h2>Prohibited Use</h2>
<ul><li>Site content को बिना permission के copy करना या resell करना</li><li>Automated scraping tools use करना</li><li>Copyrighted fonts को redistribute करना</li><li>Site को harm करने की कोशिश करना</li></ul>
<h2>Font Licenses</h2>
<p>प्रत्येक font की अपनी license होती है। Download करने से पहले license ज़रूर read करें। HindiFont.co.in font licensing के लिए responsible नहीं है।</p>
<h2>Intellectual Property</h2>
<p>Site content (articles, guides, design) HindiFont.co.in का intellectual property है। Fonts के copyright उनके creators के पास हैं।</p>
<h2>Limitation of Liability</h2>
<p>HindiFont.co.in किसी भी direct, indirect, incidental या consequential damage के लिए liable नहीं है।</p>
<h2>Governing Law</h2>
<p>ये terms Indian law के तहत governed होते हैं।</p>
<h2>Contact</h2>
<p>Terms related queries: <strong>legal@hindifont.co.in</strong></p>
""")

# 404 page
pg404=f"""{head("Page Not Found | HindiFont.co.in","This page does not exist.","404","/")}
{hdr()}
<main style="text-align:center;padding:96px 24px;min-height:60vh;display:flex;align-items:center;justify-content:center;flex-direction:column">
<div style="font-family:var(--fh);font-size:7rem;color:var(--gold);opacity:.2;line-height:1;margin-bottom:16px">४०४</div>
<h1 style="font-family:var(--fd);font-size:2.2rem;font-weight:900;margin-bottom:12px;color:var(--ink)">Page Not Found</h1>
<p style="color:var(--stone);margin-bottom:32px;max-width:400px">यह page exist नहीं करता। नीचे से fonts browse करें।</p>
<div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap">
<a href="/" style="background:var(--gold);color:var(--ink);padding:13px 28px;border-radius:var(--r12);font-weight:700">🏠 Home</a>
<a href="/fonts/" style="background:var(--ink);color:#fff;padding:13px 28px;border-radius:var(--r12);font-weight:700">🔤 All Fonts</a>
</div>
</main>
{ftr()}"""
open(f"{BASE}/404.html","w").write(pg404)
print("✅ All static pages + 404 built")

# ══════════════════════════════════════════════════
# SEO FILES
# ══════════════════════════════════════════════════
today = datetime.date.today().isoformat()
urls = [("https://hindifont.co.in/","1.0","daily")]
urls += [(f"https://hindifont.co.in/fonts/{f['slug']}/","0.9","monthly") for f in FONTS]
urls += [(f"https://hindifont.co.in/blog/{b['slug']}/","0.8","monthly") for b in BLOGS]
urls += [(f"https://hindifont.co.in/category/{s}/","0.7","weekly") for s,*_ in CATS]
urls += [
  ("https://hindifont.co.in/fonts/","0.9","weekly"),
  ("https://hindifont.co.in/blog/","0.8","weekly"),
  ("https://hindifont.co.in/category/","0.7","weekly"),
  ("https://hindifont.co.in/about/","0.4","monthly"),
  ("https://hindifont.co.in/contact/","0.4","monthly"),
  ("https://hindifont.co.in/privacy-policy/","0.3","monthly"),
  ("https://hindifont.co.in/disclaimer/","0.3","monthly"),
  ("https://hindifont.co.in/terms/","0.3","monthly"),
]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for u,p,c in urls: sm += f"  <url><loc>{u}</loc><lastmod>{today}</lastmod><changefreq>{c}</changefreq><priority>{p}</priority></url>\n"
sm += "</urlset>"
open(f"{BASE}/sitemap.xml","w").write(sm)
open(f"{BASE}/robots.txt","w").write(f"User-agent: *\nAllow: /\nDisallow: /fonts/*/download/\n\nSitemap: https://hindifont.co.in/sitemap.xml\n")
open(f"{BASE}/_redirects","w").write("https://www.hindifont.co.in/* https://hindifont.co.in/:splat 301!\n/404 /404.html 404\n")
open(f"{BASE}/_headers","w").write("""/*
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin

/*.css
  Cache-Control: public, max-age=31536000, immutable
/*.js
  Cache-Control: public, max-age=31536000, immutable
""")

total = sum(1 for r,d,files in os.walk(BASE) for f in files if f.endswith('.html'))
print(f"\n{'='*52}")
print(f"  🎉 COMPLETE BUILD")
print(f"  HTML pages total : {total}")
print(f"  Font pages       : {len(FONTS)}")
print(f"  Blog posts       : {len(BLOGS)}")
print(f"  Category pages   : {len(CATS)}")
print(f"  Static pages     : 5 (about/contact/privacy/disclaimer/terms)")
print(f"  Sitemap URLs     : {len(urls)}")
print(f"{'='*52}")
