# news-image-nov-21

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/wenjinqin/news-image-nov-21/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/wenjinqin/news-image-nov-21/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

One page that sums up the world news of **Saturday 21 November 2026**,
drawn entirely with code — no photographs, no stock art. The front page
leads with Iran's missile-and-drone strike on US bases in Bahrain and
carries five more of the day's stories as illustrated panels:

- **Iran strikes US bases in Bahrain** — Tehran says missiles and
  drones hit two US Patriot radars at al-Riffa and Awali; Bahrain says
  a civilian industrial site was hit and set ablaze, with no injuries.
- **Mexico captures "El Chapo Isidro"** — FBI Top 10 fugitive Fausto
  Isidro Meza Flores seized in Guasave, Sinaloa, with US intelligence
  help; 11 people killed in the backlash.
- **Russian missile hits Kryvyi Rih** — a ballistic missile strikes
  President Zelenskyy's hometown; 2 killed, a boy of 7 among them,
  and about 60 wounded.
- **COP31 runs into overtime** — the Antalya talks pass their Friday
  deadline with no deal; the draft drops fossil fuels.
- **Wall Street slides into correction** — the S&P 500 falls 3.7% as
  AI shares slide; the Nasdaq wipes out its 2026 gains.
- **BepiColombo reaches Mercury** — the ESA–JAXA probe enters orbit
  after 8 years and 10 billion km, only the second mission ever to
  orbit the planet.

A ticker along the bottom adds Trump's "not good" on the FBI
crime-database hack, drones setting a Russian cargo ship ablaze in
the Gulf of Finland, and Wolbachia mosquitoes cutting dengue 69%
in a Brazil trial.

Every story was verified against at least two published sources dated
21 November 2026 (Al Jazeera, TRT World, The Jerusalem Post, The Times
of Israel, AP via NPR, Reuters, CNN, The Wall Street Journal, BBC,
France 24, UPI, Dawn, The Straits Times / AP, Nature, ESA). Stories
first reported on an earlier day were deliberately left out: the ICJ's
Myanmar genocide ruling (19 November), the Anthropic IPO (19 November),
the Riemann-hypothesis claim (20 November), the UK–EU reset deal
(20 November), and the FBI database breach first reported by CNN on
20 November.

`draw21.py` renders `entry.png` (1024 × 1024) with Pillow; `main.ts` is
the contest program — it validates the image against the gate's limits
and copies it to `/output/entry.png` in the grading sandbox.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts   # writes out/entry.png
python3 draw21.py                                     # regenerates entry.png
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=d5a50dzy&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>
