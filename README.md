# pixel-skills

Custom Claude Code plugin for Pixel With Bliss — **41 marketing skills** that Claude loads on its own when a request matches, or that you can call by name (e.g. `/pixel-skills:cold-email`).

## Skills

⭐ = most useful for Pixel With Bliss (a solo photo/video business). The rest were written for software/SaaS companies but still work.

### Content & social
| Skill | Use it for |
|---|---|
| ⭐ `content-strategy` | Planning what content to make — topics, pillars, calendars |
| ⭐ `social-content` | Instagram, TikTok, Facebook, LinkedIn posts and scheduling |
| ⭐ `video` | Creating video with AI tools or code-based frameworks |
| ⭐ `image` | Marketing images — social graphics, banners, mockups |
| ⭐ `copywriting` | Writing copy for any page (home, about, services) |
| ⭐ `copy-editing` | Improving or refreshing existing copy |
| `community-marketing` | Building an online community around the brand |

### Getting clients
| Skill | Use it for |
|---|---|
| ⭐ `cold-email` | Cold outreach emails and follow-ups that get replies |
| ⭐ `email-sequence` | Automated email flows and drip campaigns |
| ⭐ `lead-magnets` | Freebies (LUTs, guides) that collect emails |
| ⭐ `pricing-strategy` | Setting prices and packages |
| ⭐ `sales-enablement` | Pitch decks, one-pagers, objection handling |
| ⭐ `marketing-ideas` | Brainstorming marketing ideas |
| ⭐ `marketing-psychology` | Using behavioral science in marketing |
| ⭐ `customer-research` | Understanding what clients want |
| ⭐ `co-marketing` | Partnerships and joint campaigns (venues, planners) |
| `referral-program` | Referral and word-of-mouth programs |
| `free-tool-strategy` | Building a free tool as a marketing magnet |
| `launch-strategy` | Planning a launch or announcement |

### Ads
| Skill | Use it for |
|---|---|
| ⭐ `paid-ads` | Google, Meta (Facebook/Instagram), LinkedIn ad campaigns |
| ⭐ `ad-creative` | Ad headlines, text, and variations |
| `ab-test-setup` | Planning A/B tests |

### Website, SEO & conversions
| Skill | Use it for |
|---|---|
| ⭐ `seo-audit` | Finding SEO problems on the site |
| ⭐ `ai-seo` | Getting found in ChatGPT / AI answers |
| ⭐ `schema-markup` | Structured data so Google understands the site |
| ⭐ `page-cro` | Making a page convert more visitors |
| ⭐ `form-cro` | Improving the booking/contact form |
| `site-architecture` | Page structure, navigation, URLs |
| `programmatic-seo` | Many SEO pages from a template |
| `competitor-alternatives` | "X vs Y" comparison pages |
| `directory-submissions` | Listing the business in directories for backlinks |
| `popup-cro` | Popups and banners |
| `analytics-tracking` | Setting up analytics and tracking |

### Research & setup
| Skill | Use it for |
|---|---|
| ⭐ `product-marketing-context` | Creates a business profile doc the other skills read first — **run this one first** |
| ⭐ `competitor-profiling` | Researching competitors from their URLs |
| `revops` | Lead lifecycle and sales handoff |

### SaaS / app-specific (rarely needed)
`signup-flow-cro`, `onboarding-cro`, `paywall-upgrade-cro`, `churn-prevention`, `aso-audit`

## Install

In the Claude Code terminal, add the marketplace once, then install:
```
/plugin marketplace add pixelswithbliss/claude-skills
/plugin install pixel-skills@pixel-skills
```

Or add to `~/.claude/settings.json`:
```json
"extraKnownMarketplaces": {
  "pixel-skills": {
    "source": {
      "source": "github",
      "repo": "pixelswithbliss/claude-skills"
    }
  }
},
"enabledPlugins": {
  "pixel-skills@pixel-skills": true
}
```

## Use in the Claude app (claude.ai / desktop / mobile)

The app can't install this plugin directly, so it uses a single bundled skill, **pixel-marketing**, that contains all 41 playbooks and picks the right one automatically.

Rebuild it after changing skills:
```
python3 scripts/build_bundle.py skills dist
```
Then upload `dist/pixel-marketing.zip` in Claude under Customize → Skills (replace the old one).

## Adding New Skills

1. Create folder: `skills/<skill-name>/`
2. Add `SKILL.md` with frontmatter (`name`, `description`) — `name` must match the folder name
3. Commit and push to GitHub
4. Run `/plugin update pixel-skills` in Claude Code to pull latest

## Credits

The 41 skills come from [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) by Corey Haines, used under the MIT License (see `LICENSE`). Imported May 2026; upstream has since reorganized and added skills.
