"""Bundle all skills in claude-skills/skills into ONE auto-routing skill: pixel-marketing."""
import re, shutil, sys, zipfile
from pathlib import Path

SRC = Path(sys.argv[1])          # .../claude-skills/skills
OUT = Path(sys.argv[2])          # output dir
NAME = "pixel-marketing"
DESC = ("Marketing playbooks for content, social posts, video, client outreach, cold email, "
        "pricing, ads, SEO, website copy and conversions. Use for any marketing or getting-clients task.")
assert len(DESC) <= 200, len(DESC)

GROUPS = [
    ("Content & social", [
        ("content-strategy", "Plan what content to make: topics, pillars, calendars"),
        ("social-content", "Instagram, TikTok, Facebook, LinkedIn, YouTube posts and scheduling"),
        ("video", "Create video with AI tools or code-based frameworks"),
        ("image", "Marketing images: social graphics, banners, thumbnails, mockups"),
        ("copywriting", "Write copy for any page: home, about, services, landing"),
        ("copy-editing", "Edit, tighten or refresh existing copy"),
        ("community-marketing", "Build an online community around the brand"),
    ]),
    ("Getting clients", [
        ("cold-email", "Cold outreach emails and follow-ups that get replies"),
        ("email-sequence", "Automated email flows, drips, nurture sequences"),
        ("lead-magnets", "Freebies (LUTs, guides, checklists) that collect emails"),
        ("pricing-strategy", "Prices, packages, tiers, discounts"),
        ("sales-enablement", "Pitch decks, one-pagers, proposals, objection handling"),
        ("marketing-ideas", "Brainstorm marketing ideas and tactics"),
        ("marketing-psychology", "Behavioral science and persuasion principles"),
        ("customer-research", "Understand what clients want; reviews, interviews, surveys"),
        ("co-marketing", "Partnerships and joint campaigns (venues, planners, brands)"),
        ("referral-program", "Referrals, affiliates, word of mouth"),
        ("free-tool-strategy", "A free tool or calculator as a marketing magnet"),
        ("launch-strategy", "Launch or announce a new service or offer"),
    ]),
    ("Ads", [
        ("paid-ads", "Google, Meta (Facebook/Instagram), LinkedIn, TikTok ad campaigns"),
        ("ad-creative", "Ad headlines, primary text, ad variations"),
        ("ab-test-setup", "Plan A/B tests and experiments"),
    ]),
    ("Website, SEO & conversions", [
        ("seo-audit", "Diagnose SEO problems on a site"),
        ("ai-seo", "Get found and cited in ChatGPT / AI answers"),
        ("schema-markup", "Structured data (LocalBusiness, reviews, FAQ)"),
        ("page-cro", "Make a page convert more visitors"),
        ("form-cro", "Improve booking, contact or inquiry forms"),
        ("site-architecture", "Page structure, navigation, URLs, internal links"),
        ("programmatic-seo", "Many SEO pages from a template (e.g. per city/service)"),
        ("competitor-alternatives", "'X vs Y' and alternatives pages"),
        ("directory-submissions", "List the business in directories for backlinks"),
        ("popup-cro", "Popups, banners, slide-ins"),
        ("analytics-tracking", "Set up or audit analytics and tracking"),
    ]),
    ("Research & setup", [
        ("product-marketing-context", "Build the business profile the other playbooks rely on"),
        ("competitor-profiling", "Research and profile competitors from their URLs"),
        ("revops", "Lead lifecycle, CRM stages, follow-up process"),
    ]),
    ("Software/app products (rarely needed for a service business)", [
        ("signup-flow-cro", "Signup and registration flows"),
        ("onboarding-cro", "Post-signup onboarding and activation"),
        ("paywall-upgrade-cro", "In-app paywalls and upgrade screens"),
        ("churn-prevention", "Cancellation flows, retention, failed payments"),
        ("aso-audit", "App Store / Google Play listings"),
    ]),
]

listed = [n for _, items in GROUPS for n, _ in items]
present = sorted(p.name for p in SRC.iterdir() if (p / "SKILL.md").exists())
assert sorted(listed) == present, (set(listed) ^ set(present))

root = OUT / NAME
if root.exists():
    shutil.rmtree(root)
pb = root / "playbooks"
for name in present:
    dst = pb / name
    shutil.copytree(SRC / name, dst, ignore=shutil.ignore_patterns("evals"))
    # Rename nested SKILL.md so the platform sees only ONE skill in the bundle.
    text = (dst / "SKILL.md").read_text()
    text = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.S)  # drop frontmatter
    (dst / "GUIDE.md").write_text(f"<!-- playbook: {name} -->\n" + text.lstrip())
    (dst / "SKILL.md").unlink()

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

1. Match the request to **1 playbook** (2 at most if it clearly spans both, e.g. `cold-email` + `email-sequence`).
2. Read `playbooks/<name>/GUIDE.md` in full before answering. Paths inside a guide such as `references/x.md` are relative to that playbook's folder — open them when the guide says to.
3. When a guide says "see <other-skill>" or "use the <other-skill> skill", that means `playbooks/<other-skill>/GUIDE.md` in this bundle.
4. If nothing in the index fits, answer normally — don't force a playbook.
5. Don't announce which playbook you loaded unless asked; just do the work.

## Business context

Guides ask you to check `.agents/product-marketing-context.md`. That file usually won't exist here. Instead, use what you already know about the user and their business (profile, memory, the conversation). Only ask for details you truly can't infer. If the user wants a reusable profile written, use `product-marketing-context`.

These playbooks were written for software (SaaS) companies. When the user runs a service business (for example photography, videography, events), translate the advice: "signup" → inquiry or booking, "product" → service package, "users" → clients, "trial" → consultation call.

## Index
{chr(10).join(rows)}

---
Playbooks adapted from coreyhaines31/marketingskills (MIT License, © Corey Haines) — see LICENSE.
"""
(root / "SKILL.md").write_text(body)
lic = SRC.parent / "LICENSE"
if lic.exists():
    shutil.copy(lic, root / "LICENSE")

zpath = OUT / f"{NAME}.zip"
with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
    for f in sorted(root.rglob("*")):
        if f.is_file():
            z.write(f, f.relative_to(OUT))
print(zpath, len(present), "playbooks", f"desc={len(DESC)} chars")
