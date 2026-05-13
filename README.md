# pixel-skills

Custom Claude Code plugin for Pixel With Bliss.

## Skills

| Skill | Trigger |
|-------|---------|
| `content-strategy` | `/content-strategy` or mention content planning, content ideas, what to post |

## Install

In Claude Code terminal:
```
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

## Adding New Skills

1. Create folder: `skills/<skill-name>/`
2. Add `SKILL.md` with frontmatter (`name`, `description`)
3. Commit and push to GitHub
4. Run `/plugin update pixel-skills` in Claude Code to pull latest
