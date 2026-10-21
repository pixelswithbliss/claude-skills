# pixel-skills

Marketing skills for Pixel With Bliss — **52 playbooks** that Claude picks automatically when a request matches. You never need to remember their names.

**Version:** synced with [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) v2.13.0 (Oct 19, 2026).

## Install

### Claude app (web, desktop, mobile) — one upload
1. Download [`bundle/pixel-marketing.zip`](bundle/pixel-marketing.zip).
2. In Claude: **Customize → Skills → + → Create skill → Upload a skill**, choose the zip, keep it toggled on.
3. "Code execution and file creation" must be on (Settings → Capabilities).

`pixel-marketing` is one skill that contains all 52 playbooks and routes each request to the right one.

### Claude Code
```
/plugin marketplace add pixelswithbliss/claude-skills
/plugin install pixel-skills@pixel-skills
```
Later updates: `/plugin update pixel-skills`

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

## Repo layout
- `skills/` — the 52 skills (Claude Code plugin)
- `tools/` — tool and integration notes the skills link to (◆ = sponsored partner of the upstream project)
- `bundle/pixel-marketing.zip` — the one-upload version for the Claude app
- `scripts/build_bundle.py` — builds that zip

## Credits

Skills by [Corey Haines](https://github.com/coreyhaines31/marketingskills), used under the MIT License (see `LICENSE`).
