<div align="center">

# How to Use ISV Intel

A step-by-step guide for researching any company with the SCOUT skill

</div>

---

## What You Need Before Starting

| Requirement | Details |
|-------------|---------|
| **AI Assistant** | Claude Code or GitHub Copilot |
| **Skill Installed** | `company-intel/SKILL.md` in your skills directory |
| **Input** | A company name or website URL |
| **For PPTX output** | Python 3.9+ and `pip install python-pptx` |

---

## Step 1: Install the Skill

**Claude Code:**
```bash
git clone https://github.com/varunk130/isv-intel.git
cp -r isv-intel/skills/company-intel ~/.claude/skills/
```

**GitHub Copilot:**
```bash
git clone https://github.com/varunk130/isv-intel.git
cp -r isv-intel/skills/company-intel .github/skills/
```

Verify the file exists at `company-intel/SKILL.md` in your skills directory.

---

## Step 2: Run the Skill

Open your AI assistant and enter one of these prompts:

### Option A: Provide a URL
```
Run company-intel on https://www.clay.com
```

### Option B: Provide a company name
```
Run company-intel on Tavily
```

### Option C: Ask a question
```
Who are Clay's customers? Use the company-intel skill.
```

If you do not provide a name or URL, the skill will ask you for one before proceeding.

---

## Step 3: What Happens Next

The skill runs the **SCOUT** process automatically:

| Step | What It Does | What You See |
|------|-------------|-------------|
| **S**can | Fetches the company's homepage, /customers, /about, and /pricing pages | "Scanning clay.com..." |
| **C**apture | Extracts customer names, logos, case study quotes, and testimonials | A structured customer table |
| **O**utline | Builds a company profile with tagline, metrics, and capabilities | Company summary |
| **U**ncover | Analyzes patterns: customer segments, industries, company sizes | Segmentation insights |
| **T**abulate | Generates the final deliverables (Markdown report + PPTX deck) | Files saved to outputs/ |

You do not need to run each step manually. The skill handles the entire flow end to end.

---

## Step 4: Review Your Output

The skill produces two deliverables:

### Research Report (Markdown)

A structured document containing:
- Company profile (what they do, tagline, key metrics)
- Full customer list with evidence type (case study, logo, testimonial)
- Quotes with person name and title
- Customer pattern analysis (by industry, size, and segment)

Saved to: `outputs/company-intel-[company]-[date].md`

### Executive Deck (PowerPoint)

A polished 2-slide PPTX:
- **Slide 1**: Company overview, key metrics, positioning, target buyers, best quote, customer segments
- **Slide 2**: Full customer evidence map with all case studies, key results, contacts, and logo features

Saved to: `outputs/company-intel-[company]-[date].pptx`

---

## Where Does the Data Come From?

Every data point comes from the company's **public website**. Nothing is inferred or made up.

| Data Point | Source |
|-----------|--------|
| Customer names | Homepage "Trusted by" logo bars, /customers page |
| Key results (e.g., "3x enrichment") | Metrics shown next to case studies on /customers |
| Quotes | Testimonial text attributed to named individuals |
| Contact names and titles | Attribution lines under testimonial quotes |
| Company metrics (e.g., "300K+ teams") | Homepage hero section, about page |
| Positioning and tagline | Homepage headline and meta description |
| Capabilities | Product description sections on homepage |

The skill only extracts what is explicitly featured. If a customer is not shown on the website, it will not appear in the output.

---

## Example Prompts for Common Scenarios

### Pre-Meeting Research
```
I have a call with Tavily tomorrow. Run company-intel on https://tavily.com 
so I know who their customers are and how they position themselves.
```

### Competitive Intelligence
```
Run company-intel on each of these competitors and build intel slides:
1. https://www.clay.com
2. https://www.apollo.io
3. https://www.zoominfo.com
```

### Partner Evaluation
```
We are considering a partnership with Company X. 
Run company-intel on their website to see their customer base 
and whether there is overlap with ours.
```

### Portfolio Review
```
Run company-intel on each of our top 5 ISV partners 
and build a 2-slide deck for each.
```

### Account Planning
```
Research this prospect's website and tell me what metrics they claim, 
who their customers are, and how they describe their product.
```

---

## Tips for Best Results

| Tip | Why |
|-----|-----|
| **Provide the full URL** | `https://www.clay.com` works better than just "Clay" |
| **Check /customers and /case-studies** | If the homepage has few logos, ask the skill to also scan these pages |
| **Run on multiple companies** | Research 3-5 competitors to build a comparative view |
| **Combine with other skills** | Pair with `battle-scanner` for competitive analysis or `gtm-exec-plan` for a full GTM plan |
| **Ask for specific focus** | "Focus on enterprise customers only" or "Just find their customer list" |

---

## Troubleshooting

**Q: The skill did not find many customers.**
Some companies do not feature customer logos or case studies prominently. Ask the skill to also check `/partners`, `/integrations`, or `/case-studies` pages. Some sites use different URL patterns.

**Q: PowerPoint generation is not working.**
Install python-pptx: `pip install python-pptx`. Ensure Python 3.9+ is in your PATH.

**Q: The output has too little detail.**
Provide more context in your prompt: "Run company-intel on clay.com and include all testimonial quotes with the person's name and title."

**Q: Can I run this on any website?**
Yes. The skill works on any company with a public website. Results vary based on how much customer evidence the company features publicly.

---

<div align="center">

**Need help?** Open an issue on the [ISV Intel repository](https://github.com/varunk130/isv-intel/issues).

**Built by Varun Kulkarni** | Powered by Claude Code & GitHub Copilot

</div>
