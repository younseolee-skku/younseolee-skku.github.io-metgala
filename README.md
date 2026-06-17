# younseolee-skku.github.io-metgala


# 2026 Met Gala MD Benchmarking Dashboard
### BLACKPINK × Luxury Fashion — Data-Driven Brand Influence Visualizer

> A single-page intelligence dashboard built for fashion MDs to benchmark BLACKPINK members' influence at the 2026 Met Gala through real social data, Google Trends, and EMV rankings.

[Final project [2024312091 Younseo Lee] _compressed.pdf](https://github.com/user-attachments/files/29029092/Final.project.2024312091.Younseo.Lee._compressed.pdf)

*you can access this pdf at main branch also.

---

## 🎯 Project Overview

The luxury fashion industry increasingly depends on global fandoms and digital influence—not just product design—to drive brand equity. BLACKPINK members have each become synonymous with a major luxury house: **Jennie × Chanel**, **Jisoo × Dior**, **Rosé × Saint Laurent**, **Lisa × Louis Vuitton / Robert Wun**.

This project visualizes *why* luxury brands invest in BLACKPINK by turning the 2026 Met Gala into a data case study. It is designed as a practical tool for **fashion MDs and brand strategists** who need to quickly extract insights and benchmark digital performance.

The 2026 Met Gala recorded a total EMV of **$1.49 billion** and **2.23 billion engagements**—the strongest media impact in the event's history. BLACKPINK-affiliated brands occupied **3 of the top 4 spots** in the Wearisma EMV ranking.

Therefore, fashion industry professionals and practical fashion MDs need to understand the relationship between BLACKPINK and the Met Gala in order to quickly derive strategic insights and identify marketing opportunities.

---

## 📌 Key Features

### `00` Introduction
- Context-setting hero section explaining the site's purpose
- Key stats cards: Total EMV, Engagements, MD use case framing

### `01` Influence by Member
- Bar charts comparing each member's Met Gala Instagram post performance
- **Interactive filters**: toggle members (Jisoo / Jennie / Lisa / Rosé) and metrics (Likes / Comments / Shares)
- Data sourced via Instagram scraping from each member's official account

### `02` Look Archive
- Per-member outfit gallery with 3 images each (overall look → dress detail → makeup/accessory)
- Sliding viewer with aspect-ratio-responsive frames
- Detailed styling descriptions for each image
- **MD Planning Memo**: interactive text area with design comparison dropdown (A vs B matrix) and one-click `.txt` report download

### `03` Brand Benefit
Three sub-sections:

1. **Google Trends Time Series** — 30-day global search interest for Chanel, Dior, Saint Laurent, and Louis Vuitton around Met Gala (May 4). Includes a dual-handle range slider and preset buttons (pre / day-of / post / full view).

2. **Brand Official Instagram Comparison** — Likes comparison across all Met Gala posts on each brand's official account, highlighting BLACKPINK members vs. other celebrities. Includes image cards linked to actual Instagram posts.

3. **Wearisma EMV Ranking** — Horizontal bar chart of 2026 Met Gala EMV leaders (Saint Laurent $186.4M → Dior $162.7M → Loewe $150.2M → Chanel $144.5M), with excerpted Wearisma report quotes.

### `04` MD Implications
- Strategic summary for next-season buying/production decisions
- Highlights artist branding storytelling as the highest-ROI marketing lever

---

## 🗂️ Data Sources & Collection Methods

| Data | Method |
|---|---|
| Member Instagram post metrics (likes, comments, shares) | Instagram scraper (member accounts, Met Gala posts only) |
| Google Trends search interest | Google Trends CSV export — 30-day window (Apr 19 – May 18, 2026) |
| Brand official Instagram post data | Manual collection — brand, featured celebrities, likes, URL |
| Wearisma EMV ranking | Published Wearisma Partnership Analysis Report (2026 Met Gala) |

> **Note on Google Trends:** Lisa attended as a Host Committee member (not as a Louis Vuitton representative), but a simultaneous spike in Louis Vuitton search interest around May 4 is treated as partial evidence of her independent influence.

---

## 🛠️ Tech Stack

| Layer | Tools |
|---|---|
| Markup & Layout | HTML5, Tailwind CSS (via CDN `@tailwindcss/browser@4`) |
| Charts | Chart.js |
| Typography | Google Fonts — Cinzel (luxury serif), Noto Sans KR |
| Interactivity | Vanilla JavaScript |
| Export | Blob API → `.txt` download |

No build step required. Single-file HTML — open in any browser.

---

## 📁 File Structure

```
/
├── index.html              # Main dashboard (single-page)
├── jennie1.webp ~ jennie3.webp
├── rose1.png ~ rose3.webp
├── jisoo1.webp ~ jisoo3.webp
├── lisa1.webp ~ lisa3.webp
├── chanel1.jpeg ~ chanel3.jpg
├── dior1.jpg ~ dior6.jpg
├── yls1.jpg ~ yls3.jpg
└── README.md
```

---

## 💡 Design Decisions

- **Color system**: Primary accent `#8A111A` (red carpet burgundy) against a white/neutral-50 base — minimal, editorial, premium
- **Fixed sidebar navigation** for fast section switching (hidden on mobile)
- **Aspect-ratio-responsive image frames** — each outfit image renders at its native ratio rather than cropped
- **Interactive memo + download** positioned alongside the Look Archive so MDs can capture insights in context
- **BLACKPINK vs. Other Celebs** bar coloring in the brand Instagram section makes the influence gap immediately legible

---

## 📊 Key Findings

- **Jisoo** generated the strongest organic Instagram performance among all four members at the 2026 Met Gala — attributable to her first-ever Met Gala appearance and the Dior custom dress crafted by Jonathan Anderson
- **Saint Laurent** topped the Wearisma EMV chart at $186.4M; **Chanel** achieved the highest average engagement rate at **12.66%** with Jennie leading brand conversation
- **All four BLACKPINK-affiliated brands** showed a near-simultaneous Google search index spike toward 100 during Met Gala week
- **Lisa** has evolved beyond brand-dependent ambassador status, joining the 2026 Met Gala Host Committee — her Robert Wun look (featuring a 3D-scanned arm piece referencing traditional Thai dance) was covered globally by Vogue

---

## 🔗 References

- [Vogue: Lisa Looks Angelic in Custom Robert Wun at the 2026 Met Gala](https://www.vogue.com/article/lisa-looks-angelic-in-custom-robert-wun-at-the-2026-met-gala)
- [Sports Donga: Met Gala Host Committee Lisa Behind the 3D Scan](https://sports.donga.com/ent/article/all/20260505/133862324/1)
- Wearisma Partnership Analysis Report — Met Gala 2026 EMV Rankings

---

## 👩‍💻 Author

**Younseo Lee** · 2024312091  
© 2026
