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
# claude.ai rejects skill zips with more than 200 files, so every playbook becomes ONE
# file: its guide first, then each extra file (references, assets, scripts) appended as
# a "## File: <path>" section, with a line-number index at the top.
LANG = {".json": "json", ".js": "javascript", ".py": "python", ".html": "html", ".csv": "csv",
        ".yaml": "yaml", ".yml": "yaml", ".sh": "bash", ".ts": "typescript"}


def section(rel, path):
    text = path.read_text(errors="ignore")
    if path.suffix != ".md":
        text = f"```{LANG.get(path.suffix, '')}\n{text.rstrip()}\n```"
    return f"## File: {rel}\n\n{text.strip()}\n"


def merge(title, main_text, extras):
    """extras = [(relpath, Path)]; returns one markdown doc with a line index."""
    parts = [section(rel, p) for rel, p in extras]
    head = f"<!-- {title} -->\n"
    if not parts:
        return head + main_text
    body = main_text.rstrip() + "\n\n---\n# Bundled files\n\n" + "\n".join(parts)

    def assemble(nums):
        index = ["<!-- Bundled files in this playbook (open by line number or search for '## File: <path>'):"]
        index += [f"  - {rel} -> line {n}" for (rel, _), n in zip(extras, nums)]
        index += ["-->", ""]
        return head + "\n".join(index) + "\n" + body

    # The index has a fixed number of lines, so build once with placeholders,
    # read the real line of each header, then fill the numbers in.
    lines = assemble([0] * len(extras)).split("\n")
    marker = lines.index("# Bundled files")
    nums, i = [], marker
    for rel, _ in extras:
        i = lines.index(f"## File: {rel}", i + 1)
        nums.append(i + 1)
    out = assemble(nums)
    check = out.split("\n")
    assert all(check[n - 1] == f"## File: {rel}" for (rel, _), n in zip(extras, nums)), title
    return out


pb = root / "playbooks"
pb.mkdir(parents=True)
for name in present:
    sdir = SRC / name
    main = re.sub(r"^---\n.*?\n---\n", "", (sdir / "SKILL.md").read_text(), count=1, flags=re.S)
    extras = [(str(p.relative_to(sdir)), p) for p in sorted(sdir.rglob("*"))
              if p.is_file() and p.name != "SKILL.md" and "evals" not in p.relative_to(sdir).parts]
    doc = merge(f"playbook: {name}", main.lstrip(), extras)
    # Cross-file links become explicit, relative to the skill root (no new lines added,
    # so the line index stays exact):
    #   ../../X/SKILL.md            -> playbooks/X.md
    #   ../../X/references/y.md     -> playbooks/X.md § references/y.md
    #   ../../tools/integrations/z  -> TOOLS.md § tools/integrations/z
    #   ../SKILL.md (own guide)     -> playbooks/<name>.md
    doc = re.sub(r"\]\((?:\.\./)+tools/([^)\s]+)\)", r"](TOOLS.md § tools/\1)", doc)
    doc = re.sub(r"\]\((?:\.\./)+([a-z0-9-]+)/SKILL\.md", r"](playbooks/\1.md", doc)
    doc = re.sub(r"\]\((?:\.\./){2,}([a-z0-9-]+)/((?:references|assets|scripts)/[^)\s]+)\)",
                 r"](playbooks/\1.md § \2)", doc)
    doc = re.sub(r"\]\((?:\.\./)+SKILL\.md", f"](playbooks/{name}.md", doc)
    # A bare "other-playbook.md" link with no sibling file of that name means the
    # playbook itself (upstream retired ads/references/conversion-tracking.md this way).
    own = {Path(rel).name for rel, _ in extras}
    for other in present:
        if f"{other}.md" not in own:
            doc = doc.replace(f"]({other}.md)", f"](playbooks/{other}.md)")
    (pb / f"{name}.md").write_text(doc)

tools = REPO / "tools"
if tools.is_dir():
    keep = [tools / f for f in ("REGISTRY.md", "SETUP.md", "PARTNERS.md") if (tools / f).exists()]
    keep += sorted((tools / "integrations").glob("*.md"))
    (root / "TOOLS.md").write_text(
        merge("tools: registry and integration notes", "# Tools\n",
              [(str(p.relative_to(REPO)), p) for p in keep]))

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
2. Open `playbooks/<name>.md`. Read the main guide (everything above the "# Bundled files" line) in full before answering.
3. Each playbook file also contains its extra files — `references/...`, `assets/...`, `scripts/...` — as sections headed `## File: <path>`. The comment at the top of the file lists each one with its line number. When the guide mentions such a path (including `../assets/...`), open that section only; don't read every section. Inside a bundled section, a bare link like `other-file.md` means the file next to it in the same folder (e.g. `references/other-file.md`).
4. Paths starting with `tools/` (e.g. `tools/REGISTRY.md`, `tools/integrations/x.md`) are sections of `TOOLS.md` at the root of this skill, indexed the same way.
5. When a guide says "see <other-skill>" or "use the <other-skill> skill", open `playbooks/<other-skill>.md`. Links starting with `playbooks/` or `TOOLS.md` are relative to this skill's root; `X.md § path` means "the `## File: path` section of X.md".
6. If nothing in the index fits, answer normally — don't force a playbook.
7. Don't announce which playbook you loaded unless asked; just do the work.

## Business context

Guides ask you to read files like `.agents/product-marketing.md`. Those usually won't exist here. Instead, use what you already know about the user and their business (profile, memory, the conversation), and only ask for details you truly can't infer. If the user wants a reusable business profile written, use `product-marketing`.

Many playbooks were written for software (SaaS) companies. When the user runs a service business (for example photography, videography, events), translate the advice: "signup" → inquiry or booking, "product" → service package, "users" → clients, "trial" → consultation call. Tools listed in `TOOLS.md` include sponsored partners (marked ◆); prefer free or already-used options unless the user asks.

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
assert sum(1 for f in root.rglob("*") if f.is_file()) < 200, "claude.ai rejects skill zips with 200+ files"
shutil.rmtree(root)  # keep only the zip
print(zpath, len(present), "playbooks", f"desc={len(DESC)} chars")
