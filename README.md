# pixel-skills

Marketing skills for Pixel With Bliss — **52 playbooks** that Claude picks automatically when a request matches. You never need to remember their names.

Plus **`humanizer`** — strips AI tells from captions, emails and posts so they sound like you.

**Version:** synced with [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) v2.13.0 (Oct 19, 2026).

## Install

### Claude app (web, desktop, mobile) — one upload
1. Download [`bundle/pixel-marketing.zip`](bundle/pixel-marketing.zip).
2. In Claude: **Customize → Skills → + → Create skill → Upload a skill**, choose the zip, keep it toggled on.
3. "Code execution and file creation" must be on (Settings → Capabilities).

`pixel-marketing` is one skill that contains all 52 playbooks and routes each request to the right one.

For the humanizer, upload [`bundle/humanizer.zip`](bundle/humanizer.zip) the same way (it's a separate skill).

### Claude Code
```
/plugin marketplace add pixelswithbliss/claude-skills
/plugin install pixel-skills@pixel-skills
```
Later updates: `/plugin update pixel-skills`

This installs the 52 marketing skills **and** `humanizer`.

## Humanizer

| Skill | Use it for |
|---|---|
| ⭐ `humanizer` | Rewriting AI-sounding text so it reads like a person wrote it — without changing what it says. Catches "not X but Y" contrasts, forced lists of three, dash overuse, sales language, stock AI words, filler |

Try: *"humanize this caption"* or *"review this email for AI tells."*

**Version:** [blader/humanizer](https://github.com/blader/humanizer) v3.1.0 (Oct 16, 2026). Copied as-is; only the app zip uses a shorter description (claude.ai's 200-character limit).

## Skills

⭐ = most useful for a solo photo/video business. The rest were written for software companies but still work.

### Content & social
| Skill | Use it for |
|---|---|
| ⭐ `content-strategy` | Planning what content to make — topics, pillars, calendars |
| ⭐ `social` | Instagram, TikTok, Facebook, LinkedIn, YouTube posts |
| ⭐ `video` | Creating video with AI tools or code |
| ⭐ `image` | Social graphics, banners, thumbnails, mockups |
| ⭐ `copywriting` | Writing copy for any page |
| ⭐ `copy-editing` | Improving or refreshing existing copy |
| `community-marketing` | Building a community around the brand |

### Finding & winning clients
| Skill | Use it for |
|---|---|
| ⭐ `prospecting` | Finding potential clients and building outreach lists (incl. local businesses) |
| ⭐ `cold-email` | Cold outreach emails, DMs and follow-ups |
| ⭐ `emails` | Email sequences and follow-up flows |
| ⭐ `sms` | SMS and WhatsApp marketing |
| ⭐ `offers` | Packages, bonuses, guarantees, urgency |
| ⭐ `pricing` | Prices, packages, tiers |
| ⭐ `lead-magnets` | Freebies (LUTs, guides) that collect emails |
| ⭐ `sales-enablement` | Pitch decks, one-pagers, proposals |
| ⭐ `events` | Getting clients from events, meetups, workshops |
| ⭐ `influencer-marketing` | Creator and ambassador partnerships |
| ⭐ `co-marketing` | Joint campaigns with venues, planners, brands |
| ⭐ `referrals` | Referrals and word of mouth |
| ⭐ `public-relations` | Press and media coverage |
| ⭐ `customer-research` | Understanding what clients want |

### Strategy & ideas
| Skill | Use it for |
|---|---|
| ⭐ `marketing-plan` | A full marketing plan |
| ⭐ `marketing-ideas` | Brainstorming ideas |
| ⭐ `marketing-psychology` | Behavioral science in marketing |
| ⭐ `product-marketing` | Business profile the other skills read first |
| ⭐ `competitor-profiling` | Researching competitors |
| `marketing-council` | Several expert perspectives on one decision |
| `marketing-loops` | Recurring marketing workflows on a schedule |
| `launch` | Launching a new service or offer |
| `free-tools` | A free tool as a marketing magnet |

### Ads
| Skill | Use it for |
|---|---|
| ⭐ `ads` | Google, Meta, TikTok, LinkedIn ad campaigns |
| ⭐ `ad-creative` | Ad headlines, text, variations |
| `ab-testing` | A/B tests |

### Website, SEO & tracking
| Skill | Use it for |
|---|---|
| ⭐ `seo-audit` | Finding SEO problems |
| ⭐ `ai-seo` | Getting found in ChatGPT / AI answers |
| ⭐ `schema` | Structured data (LocalBusiness, reviews, FAQ) |
| ⭐ `cro` | Making a page or booking form convert more |
| `link-building` | Earning backlinks |
| `site-architecture` | Page structure, navigation, URLs |
| `programmatic-seo` | Many SEO pages from a template |
| `competitors` | "X vs Y" comparison pages |
| `directory-submissions` | Directory listings for backlinks |
| `popups` | Popups and banners |
| `analytics` | Analytics setup |
| `conversion-tracking` | Tracking bookings into Google Ads, Meta, GA4 |
| `attribution` | Which marketing brings clients |
| `revops` | Lead lifecycle and CRM stages |

### Software/app products (rarely needed)
`signup`, `onboarding`, `paywalls`, `churn-prevention`, `aso`

## Updating from upstream

1. Copy the latest `skills/`, `tools/` and `LICENSE` from coreyhaines31/marketingskills.
2. Run `python3 scripts/build_bundle.py . bundle` — it stops and names any new or removed skill so you can add it to the index in the script.
3. Commit, push, and re-upload `bundle/pixel-marketing.zip` in Claude.

**Humanizer:** copy `SKILL.md` and `LICENSE` from blader/humanizer into `skills/humanizer/`, run the same build command, then re-upload `bundle/humanizer.zip`. Check the upstream version in `SKILL.md` → `metadata.version`.

## Repo layout
- `skills/` — the 52 marketing skills + `humanizer` (Claude Code plugin)
- `tools/` — tool and integration notes the skills link to (◆ = sponsored partner of the upstream project)
- `bundle/pixel-marketing.zip` — the one-upload version for the Claude app (55 files; the app rejects zips with 200+ files, so each playbook is merged into one file)
- `bundle/humanizer.zip` — the humanizer for the Claude app
- `scripts/build_bundle.py` — builds both zips (skills listed in `STANDALONE` get their own zip instead of joining the router)

## Credits

Marketing skills by [Corey Haines](https://github.com/coreyhaines31/marketingskills), used under the MIT License (see `LICENSE`).
Humanizer by [Siqi Chen](https://github.com/blader/humanizer), used under the MIT License (see `skills/humanizer/LICENSE`).
