"""Bundle every skill in <repo>/skills into ONE auto-routing skill: pixel-marketing.

Usage:  python3 scripts/build_bundle.py <repo-root> <output-dir>
Output: <output-dir>/pixel-marketing.zip  (upload in Claude: Customize -> Skills)
"""
import re, shutil, sys, zipfile
from pathlib import Path

REPO = Path(sys.argv[1]).resolve()
OUT = Path(sys.argv[2]).resolve()
SRC = REPO / "skills"
NAME = "pixel-marketing"
DESC = ("Marketing playbooks for content, social posts, video, finding clients, cold email, offers, "
        "pricing, ads, SEO, website copy and conversions. Use for any marketing task.")
assert len(DESC) <= 200 and ":" not in DESC, len(DESC)

GROUPS = [
    ("Content & social", [
        ("content-strategy", "Plan what content to make: topics, pillars, calendars"),
        ("social", "Instagram, TikTok, Facebook, LinkedIn, YouTube posts and scheduling"),
        ("video", "Create video with AI tools or code-based frameworks"),
        ("image", "Marketing images: social graphics, banners, thumbnails, mockups"),
        ("copywriting", "Write copy for any page: home, about, services, landing"),
        ("copy-editing", "Edit, tighten or refresh existing copy"),
        ("community-marketing", "Build an online community around the brand"),
    ]),
    ("Finding & winning clients", [
        ("prospecting", "Find and qualify potential clients and build outreach lists (incl. local businesses)"),
        ("cold-email", "Cold outreach emails, DMs, follow-ups that get replies"),
        ("emails", "Email sequences, drips, nurture and follow-up flows"),
        ("sms", "SMS and WhatsApp marketing flows"),
        ("offers", "Design the offer: packages, bonuses, guarantees, urgency"),
        ("pricing", "Prices, packages, tiers, discounts"),
        ("lead-magnets", "Freebies (LUTs, guides, checklists) that collect emails"),
        ("sales-enablement", "Pitch decks, one-pagers, proposals, objection handling"),
        ("events", "Events, meetups, workshops, webinars, trade shows"),
        ("influencer-marketing", "Creator, influencer and ambassador partnerships"),
        ("co-marketing", "Partnerships and joint campaigns (venues, planners, brands)"),
        ("referrals", "Referrals, affiliates, word of mouth"),
        ("public-relations", "Press coverage, journalist outreach, earned media"),
        ("customer-research", "Understand what clients want; reviews, interviews, surveys"),
    ]),
    ("Strategy & ideas", [
        ("marketing-plan", "A full marketing plan"),
        ("marketing-ideas", "Brainstorm marketing ideas and tactics"),
        ("marketing-psychology", "Behavioral science and persuasion principles"),
        ("marketing-council", "Get several expert marketer perspectives on a decision"),
        ("marketing-loops", "Recurring marketing workflows an AI runs on a schedule"),
        ("launch", "Launch or announce a new service or offer"),
        ("free-tools", "A free tool or calculator as a marketing magnet"),
        ("product-marketing", "Build the business profile the other playbooks rely on"),
        ("competitor-profiling", "Research and profile competitors from their URLs"),
    ]),
    ("Ads", [
        ("ads", "Google, Meta (Facebook/Instagram), TikTok, LinkedIn ad campaigns"),
        ("ad-creative", "Ad headlines, primary text, ad variations"),
        ("ab-testing", "Plan A/B tests and experiments"),
    ]),
    ("Website, SEO & tracking", [
        ("seo-audit", "Diagnose SEO problems on a site"),
        ("ai-seo", "Get found and cited in ChatGPT / AI answers"),
        ("schema", "Structured data (LocalBusiness, reviews, FAQ)"),
        ("link-building", "Earn backlinks and third-party mentions"),
        ("cro", "Make a page or form (booking, contact) convert more"),
        ("site-architecture", "Page structure, navigation, URLs, internal links"),
        ("programmatic-seo", "Many SEO pages from a template (e.g. per city/service)"),
        ("competitors", "'X vs Y' and alternatives pages"),
        ("directory-submissions", "List the business in directories for backlinks"),
        ("popups", "Popups, banners, slide-ins"),
        ("analytics", "Set up or audit analytics"),
        ("conversion-tracking", "Track form submissions/bookings into Google Ads, Meta, GA4"),
        ("attribution", "Which marketing actually brings clients"),
        ("revops", "Lead lifecycle, CRM stages, follow-up process"),
    ]),
    ("Software/app products (rarely needed for a service business)", [
        ("signup", "Signup and registration flows"),
        ("onboarding", "Post-signup onboarding and activation"),
        ("paywalls", "In-app paywalls and upgrade screens"),
        ("churn-prevention", "Cancellation flows, retention, failed payments"),
        ("aso", "App Store / Google Play listings"),
    ]),
]

listed = [n for _, items in GROUPS for n, _ in items]
present = sorted(p.name for p in SRC.iterdir() if (p / "SKILL.md").exists())
if sorted(listed) != present:
    sys.exit(f"Index out of sync with skills/: {sorted(set(listed) ^ set(present))} "
             "-- add/remove them in GROUPS in this script.")

root = OUT / NAME
if root.exists():
    shutil.rmtree(root)
pb = root / "playbooks"
for name in present:
    dst = pb / name
    shutil.copytree(SRC / name, dst, ignore=shutil.ignore_patterns("evals"))
    # Only ONE SKILL.md in the bundle: playbooks become GUIDE.md without frontmatter.
    text = (dst / "SKILL.md").read_text()
    text = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.S)
    (dst / "GUIDE.md").write_text(f"<!-- playbook: {name} -->\n" + text.lstrip())
    (dst / "SKILL.md").unlink()
    # Links to other skills' SKILL.md must follow the rename.
    for md in dst.rglob("*.md"):
        s = md.read_text(errors="ignore")
        fixed = re.sub(r"(\]\([^)\s]*?)SKILL\.md(?=[)#])", r"\1GUIDE.md", s)
        if fixed != s:
            md.write_text(fixed)
if (REPO / "tools").is_dir():
    shutil.copytree(REPO / "tools", root / "tools")

rows = []
for title, items in GROUPS:
    rows.append(f"\n### {title}\n\n| Playbook | Use when the request is about |\n|---|---|")
    rows += [f"| `{n}` | {w} |" for n, w in items]

body = f"""---
name: {NAME}
description: {DESC}
---

# Pixel Marketing — playbook router

This skill bundles {len(present)} expert marketing playbooks. The user should never have to name one: pick the right playbook(s) yourself from the index below, read them, and follow them.

## How to use

1. Match the request to **1 playbook** (2 at most if it clearly spans both, e.g. `prospecting` + `cold-email`).
2. Read `playbooks/<name>/GUIDE.md` in full before answering. Paths inside a guide such as `references/x.md` or `../assets/...` are relative to that guide's own folder — open them when the guide says to.
3. Paths that start with `tools/` (e.g. `tools/REGISTRY.md`, `tools/integrations/x.md`) are at the root of this skill, next to this file.
4. When a guide says "see <other-skill>" or "use the <other-skill> skill", open `playbooks/<other-skill>/GUIDE.md`.
5. If nothing in the index fits, answer normally — don't force a playbook.
6. Don't announce which playbook you loaded unless asked; just do the work.

## Business context

Guides ask you to read files like `.agents/product-marketing.md`. Those usually won't exist here. Instead, use what you already know about the user and their business (profile, memory, the conversation), and only ask for details you truly can't infer. If the user wants a reusable business profile written, use `product-marketing`.

Many playbooks were written for software (SaaS) companies. When the user runs a service business (for example photography, videography, events), translate the advice: "signup" → inquiry or booking, "product" → service package, "users" → clients, "trial" → consultation call. Tools listed in `tools/` include sponsored partners (marked ◆); prefer free or already-used options unless the user asks.

## Index
{chr(10).join(rows)}

---
Playbooks from coreyhaines31/marketingskills (MIT License, © Corey Haines) — see LICENSE.
"""
(root / "SKILL.md").write_text(body)
if (REPO / "LICENSE").exists():
    shutil.copy(REPO / "LICENSE", root / "LICENSE")

zpath = OUT / f"{NAME}.zip"
with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
    for f in sorted(root.rglob("*")):
        if f.is_file():
            z.write(f, f.relative_to(OUT))
shutil.rmtree(root)  # keep only the zip
print(zpath, len(present), "playbooks", f"desc={len(DESC)} chars")
