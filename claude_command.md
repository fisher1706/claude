# Claude Code Quick Reference

## Essential Commands & Shortcuts

### Navigation & Context
- `/context` — View current context
- `/compact` — Compact mode
- `/usage` — Check token usage
- `/models` — View available models
- `/config` — Configure settings
- `/resume` — Resume last session
- `/sandbox` — Manage sandbox

### Session Control
- `/rewind` or **ESC + ESC** — Rewind to previous state
- `/mcp` — Manage MCP servers
- `/init` — Initialize CLAUDE.md

### Mode Switching
- **SHIFT + TAB** — Switch mode (Normal ↔ Plan ↔ Fast)

## CLI Usage

```bash
# Start session normally
claude "explain this project"

# Use plan mode
claude -p "explain this project"

# Continue from last session
claude -c

# Skip all permission prompts
claude --dangerously-skip-permissions

# Debug mode
claude --debug
```

## Debugging & Skills

### Available Skills
```bash
/skills          # List available skills
/code-review     # Review code (low/medium/high/ultra)
/simplify        # Simplify changed code
/design          # Create design canvas
/dataviz         # Create data visualizations
/pr-description  # Generate PR description
/run             # Run/test the project
```

### Error Recovery
- `claude --debug` — Enable debug logging for troubleshooting

## MCP Servers

### Playwright (Web Automation)
```bash
claude mcp add playwright npx @playwright/mcp@latest
```

**Documentation:** https://github.com/microsoft/playwright-mcp

**All MCP Clients:** https://context7.com/docs/resources/all-clients#claude-code

## Learning Resources

- **Skills Introduction:** https://anthropic-partners.skilljar.com/introduction-to-agent-skills/434526
- **Usage Optimization:** https://claudefa.st/blog/guide/development/usage-optimization
- **Usage Dashboard:** https://claude.ai/settings/usage

## Quick Tips

✅ Use **Skills** for structured workflows (PR creation, code review, etc.)  
✅ Use **`/` commands** for navigation and context management  
✅ Use **SHIFT + TAB** to toggle between different modes  
✅ Use **`claude -c`** to continue previous sessions  
✅ Check `/skills` for latest available tools
