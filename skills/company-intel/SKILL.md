---
name: company-intel
description: 'Deep research on any company by scanning their public website to extract customers, partners, case studies, testimonials, key metrics, and competitive positioning. Produces a polished 1-slide PowerPoint summary. Use when: research a company, find customers, who are their customers, company research, company overview, customer list, company intel, customer logos, competitive research on company, scan website for customers.'
---

# Company Intel (SCOUT Framework)

Research any company by scanning their public website and produce a polished 1-slide PowerPoint showing who their customers are, key metrics, positioning, and notable quotes. SCOUT turns a URL into an executive-ready company intelligence slide in minutes.

## When to Use
- Pre-meeting research on a prospect, partner, or competitor
- Building a competitive landscape and need to understand who companies sell to
- Identifying potential co-sell or partner opportunities by mapping customer overlap
- Preparing account intelligence for a sales call
- Creating a quick company overview slide for an internal briefing
- Researching a company before a partnership or investment conversation

## What You'll Need

**Critical inputs (ask if not provided):**
- Company name OR website URL (either one is sufficient)

If only a company name is provided, search the web to find their official website URL before proceeding. If only a URL is provided, extract the company name from the site.

**Always ask the user if they have not provided at least one of these.** Do not proceed without a company name or URL.

**Nice-to-have:**
- Specific focus area (e.g., "just customers", "pricing", "positioning")
- Industry or segment context
- Your company name (for overlap analysis)

## SCOUT Framework

| Step | What It Does | Key Output |
|------|-------------|-----------|
| **S**can | Fetch the company's homepage and key pages (customers, about, pricing) | Raw page content |
| **C**apture | Extract customer logos, names, testimonials, case studies, metrics | Structured customer list |
| **O**utline | Summarize the company's positioning, value prop, and key claims | Company profile |
| **U**ncover | Identify notable patterns: customer segments, industries, company sizes | Customer segmentation |
| **T**abulate | Compile everything into a polished 2-slide deck using ppt-deck-generator | 2-slide PPTX |

## Process

### Step 1: SCAN - Fetch Public Website Data

Use web fetch tools to retrieve content from the company's website. Target these pages in order:

1. **Homepage** - Usually has a "trusted by" logo bar and hero positioning
2. **Customers page** - `/customers`, `/case-studies`, `/stories`, `/clients`
3. **About page** - `/about`, `/about-us`, `/company`
4. **Pricing page** - `/pricing` (optional, for context)

**What to look for on each page:**
- Logo bars (usually near the top or bottom: "Trusted by", "Used by", "Our Customers")
- Case study links (company names in titles, quotes with names and titles)
- Testimonial quotes with person name, role, and company
- Metrics claims ("100M+ users", "10,000+ companies", "$1B+ processed")
- Partner logos or integration badges
- Industry mentions or segment descriptions

### Step 2: CAPTURE - Extract Customer Intelligence

From the scanned pages, build a structured list:

**Customer Extraction Table:**

| # | Customer Name | Source | Evidence Type | Quote or Detail |
|---|--------------|--------|--------------|----------------|
| 1 | [Name] | Homepage logo bar | Logo | - |
| 2 | [Name] | Case study page | Case study + quote | "[Quote]" - [Person], [Title] |
| 3 | [Name] | Testimonial | Quote | "[Quote]" - [Person], [Title] |

**Rules:**
- Only include customers that are explicitly featured (logo, case study, testimonial, or named reference)
- Do not infer or guess customers that are not visibly shown
- Capture the person's name and title if available (from testimonials)
- Note the evidence type: Logo only, Case study, Testimonial quote, Named reference
- Sort by prominence (case studies and quotes first, then logos)

### Step 3: OUTLINE - Build Company Profile

Create a brief company profile from the website content:

| Field | What to Capture |
|-------|----------------|
| Company Name | Official name |
| Tagline | Their main headline or positioning statement |
| What They Do | 1-2 sentence description of their product/service |
| Key Metrics | Any numbers they claim (users, customers, revenue, uptime, etc.) |
| Target Audience | Who they sell to (based on messaging and customer list) |
| Notable Claims | Key differentiators or bold statements from the site |

### Step 4: UNCOVER - Analyze Customer Patterns

Look at the customer list and identify patterns:

- **By company size:** Are they selling to startups, mid-market, or enterprise?
- **By industry:** What verticals appear most (tech, finance, healthcare, etc.)?
- **By use case:** What problems do the case studies highlight?
- **Customer count tiers:** How many logos vs. case studies vs. testimonials?
- **Notable names:** Any Fortune 500, well-known brands, or surprising customers?

### Step 5: TABULATE - Generate 2-Slide PPTX

Use the `ppt-deck-generator` skill or `python-pptx` to create a polished 2-slide executive deck.

**Slide 1: Company Overview and Positioning**

```
+------------------------------------------------------------------+
|  [COMPANY NAME]  Company Intelligence Brief          [Date]       |
+------------------------------------------------------------------+
|  [300K+]    [150+]     [140M]     [26]      [16]     [SOC 2]    |
|  GTM Teams  Providers  AI Runs    Customers  Cases   Compliance  |
+------------------------------------------------------------------+
|                            |                                      |
|  WHAT THEY DO              |  POSITIONING                         |
|  [Description paragraph]   |  [Tagline and value prop]            |
|                            |                                      |
|  KEY CAPABILITIES          |  TARGET BUYERS                       |
|  - Capability 1            |  Role 1 - Context                    |
|  - Capability 2            |  Role 2 - Context                    |
|  - Capability 3            |  Role 3 - Context                    |
+------------------------------------------------------------------+
|  "[Best quote]" - Person, Title           [Segment] [Segment]    |
+------------------------------------------------------------------+
```

**Slide 2: Customer Evidence Map**

```
+------------------------------------------------------------------+
|  [COMPANY NAME]  Customer Evidence Map                [Date]      |
|  26 CUSTOMERS  |  16 CASE STUDIES  |  10 LOGO FEATURES           |
+------------------------------------------------------------------+
|  Customer      Key Result           Contact                       |
|  -------       ----------           -------                       |
|  [8 case studies with results       [8 case studies with results  |
|   and contact names per column]      and contact names per column]|
|                                                                   |
+------------------------------------------------------------------+
|  ALSO FEATURED (LOGOS AND PARTNERS)                               |
|  [Logo 1] [Logo 2] [Logo 3] [Logo 4] [Logo 5] ... [Logo 10]    |
+------------------------------------------------------------------+
```

**Slide Design Rules:**
- Use `ppt-deck-generator` color palette (navy dark_bg header, Microsoft blue accent, teal highlights)
- Segoe UI font family throughout, minimum 9pt for any text
- High contrast: dark text on white/light backgrounds, white text on navy only
- No dark text on dark backgrounds
- Slide 1 left column (45%): Company overview and capabilities
- Slide 1 right column (55%): Positioning and target buyers
- Slide 2: Two-column customer grid with colored dots, key results in blue, contact names in gray
- Bottom strips on both slides: navy background with white/teal text only

## Output

Save to:
- `outputs/company-intel-[company-name]-[YYYY-MM-DD].md` (structured research notes)
- `outputs/company-intel-[company-name]-[YYYY-MM-DD].pptx` (2-slide exec deck)

### Deliverables:
1. **Customer Extraction Table**: Full list of identified customers with evidence type and quotes
2. **Company Profile**: Positioning, metrics, target audience, and key claims
3. **Customer Pattern Analysis**: Segmentation by size, industry, and use case
4. **2-Slide PPTX**: Slide 1 = Company overview and positioning, Slide 2 = Full customer evidence map

## Chain Connections
- **Feeds into**: `battle-scanner` (competitive customer overlap analysis), `partner-blueprint` (partner customer mapping), `gtm-exec-plan` (competitive landscape section)
- **Enhanced by**: Run on multiple competitors to build a comparative customer map
- **Pairs with**: `competitive-exec-brief` for full competitive intelligence package
