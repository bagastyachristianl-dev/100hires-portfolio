# 100Hires Portfolio Project — Step 2: Research Project

**Candidate:** Bagastya Christian Santoso
**Topic:** AI-Powered SEO Content Production

---

## Overview

This step builds a research foundation on **AI-powered SEO content production** by identifying 10 genuine practitioners in the space (not just popular commentators), collecting their recent published content via APIs and manual collection, and organizing it into a structured repository that could support a real playbook later.

---

## Tools Used

| Tool | Purpose |
|------|---------|
| [Cursor IDE](https://cursor.com/) | Development environment |
| Claude Code / Codex (Cursor extensions) | Assisted with research, script writing, and content organization |
| `youtube-transcript-api` (Python) | Fetched YouTube video transcripts via API |
| GitHub | Version control and repository hosting |

---

## What Was Collected

- **10 experts** identified and documented in `/research/sources.md`, each with role, platform links, and a brief note explaining why they were selected as genuine practitioners rather than generic SEO commentators.
- **YouTube transcripts** for Kevin Indig, Lily Ray, and Britney Muller, fetched programmatically using a Python script built with `youtube-transcript-api`. One video (Garrett Sussman) could not be fetched because subtitles were disabled on that video.
- **LinkedIn posts** for all 10 experts, organized by author in `/research/linkedin-posts/`.

---

## Why These Experts

Selection was based on four criteria:
1. **Hands-on practitioner status** — do they run agencies, lead SEO teams, or build AI-visibility products, rather than just writing about the field?
2. **Evidence of original research or experiments** — original data, testing, or frameworks, not recycled takes.
3. **Active and consistent publishing in 2025–2026** — relevance to the current state of AI search.
4. **Specific relevance to AI-driven search/content** — not generalist SEO influencers.

Full reasoning for each expert is documented in `/research/sources.md`.

---

## Issues & Solutions

| Issue | How I Solved It |
|-------|------------------|
| `youtube-transcript-api`'s `get_transcript()` method failed with a `ModuleNotFoundError`/`AttributeError` | The installed version of the library (1.2.4) had changed its API from a static method to an instance-based method. I updated the script to use `YouTubeTranscriptApi().fetch(video_id)` instead. |
| Two Python versions were installed on the machine (3.12 and 3.14), causing `pip install` to install packages to the wrong interpreter | Used `python -m pip install` instead of `pip install` to ensure the package installed to the same Python interpreter used to run the script. |
| One video (Garrett Sussman, Episode 11) had subtitles disabled | Not all YouTube videos have available transcripts. Documented the failure rather than silently skipping it, and relied on this expert's LinkedIn content instead. |
| Not all 10 experts are equally active on YouTube | Focused programmatic transcript collection on the experts with genuinely active channels, and relied on LinkedIn content for the rest, to keep material high-signal rather than padded. |

---

## Repository Structure
---

## Reflection

This step was less about volume and more about judgment — identifying which voices in a crowded AI SEO space are actually doing the work versus repackaging other people's ideas. I prioritized people running real experiments, advising real companies, or building real products, since that material is the strongest foundation for a future playbook. I also ran into real technical friction (Python environment conflicts, an outdated API call) and documented how I diagnosed and resolved each one, rather than only showing the final working state.

---

*Submitted as part of the 100Hires portfolio evaluation process.*
