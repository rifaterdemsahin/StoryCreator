# Antigravity IDE: Script Rewriting System
## For "Secure AI: Interpret and Protect Models" Course Scripts

---

# LOCKED STRUCTURE (Extracted from script_sample.pdf)

```
COURSE SCRIPT STRUCTURE
├── SECTION 1: COURSE INTRO VIDEO (3 min, ~450 words)
│   ├── Hook (Engaging Opening)
│   ├── Self-Introduction
│   ├── Course Title Reveal
│   ├── Course Overview
│   ├── Key Takeaways (bullet points)
│   └── Closing Remarks
│
├── SECTION 2: MODULES' SCRIPTS
│   ├── MODULE 1: THE ATTACKER'S PLAYBOOK (3 videos)
│   │   ├── Video 1: Evasion Attacks (7.5 min)
│   │   ├── Video 2: Data Poisoning (7.5 min)
│   │   └── Video 3: Model Stealing (7.5 min)
│   │
│   ├── MODULE 2: BUILDING THE SHIELD (3 videos)
│   │   ├── Video 1: Adversarial Training (7.5 min)
│   │   ├── Video 2: Input Sanitization (7.5 min)
│   │   └── Video 3: Differential Privacy (7.5 min)
│   │
│   └── MODULE 3: AI SECURITY LIFECYCLE (3 videos)
│       ├── Video 1: Red Team Methodology (7.5 min)
│       ├── Video 2: Security Metrics (7.5 min)
│       └── Video 3: Complete Security Lifecycle (7.5 min)
│
├── SECTION 3: OUTRO VIDEO (3-5 min, ~450 words)
│   ├── Opening & Acknowledgment
│   ├── Recap of Course Content
│   ├── Motivational Message
│   ├── Encouragement for Continued Growth
│   ├── Actionable Next Steps
│   └── Closing Remarks
│
└── SECTION 4: PROMO VIDEO (~3 min, ~300 words)
    ├── Hook - Problem Statement
    ├── Self-Introduction
    ├── Course Announcement
    ├── Key Benefits (bullets)
    ├── Real-Life Impact
    ├── Unique Selling Points (bullets)
    ├── Target Audience Call-Out
    ├── Closing Inspiration
    └── Call to Action

VIDEO SCRIPT STRUCTURE (Per Module Video)
├── Video Type & Duration
├── Hook (scenario-based opening)
├── Video Overview
├── Learning Objectives (bullet list)
├── Transition sentence
├── Content Section
│   ├── Core Concepts (numbered)
│   ├── Technical Walkthrough/Mechanics
│   ├── Code Examples (if applicable)
│   └── Real-World Scenario
├── Pre-Summary Transition
├── Summary
├── Transition to IVQ
├── In-Video Question (IVQ)
│   ├── Question stem
│   ├── 4 answer options (a-d)
│   ├── Correct Answer
│   ├── Explanation
│   └── Explain Incorrect Options
└── Transition to Next Video/Practice
```

---

# PART 1: MASTER ORCHESTRATOR PROMPT

```
PROMPT: SCRIPT REWRITER MASTER

You are rewriting the "Secure AI: Interpret and Protect Models" course script.

ABSOLUTE RULES:
1. PRESERVE exact structure (sections, subsections, components)
2. PRESERVE all technical accuracy (algorithms, code, concepts)
3. PRESERVE learning objectives (same outcomes, different words)
4. PRESERVE timing targets (word counts per section)
5. CHANGE wording, analogies, examples, sentence structures

INPUT: [Paste original script section]

REWRITE PARAMETERS:
- Tone: [Formal/Conversational/Energetic] (default: match original energy)
- Analogy Style: [Technical/Everyday/Pop-culture]
- Example Domain: [Same/Healthcare/Finance/Autonomous/General]

OUTPUT: Complete rewritten section matching exact structure.
```

---

# PART 2: BOTTOM-UP APPROACH
*Build from components to complete script*

## Level 1: HOOK REWRITER

```
PROMPT: HOOK TRANSFORMER

Rewrite this video hook while maintaining its purpose and impact.

ORIGINAL HOOK:
"[Paste hook text]"

HOOK PURPOSE: [Grab attention / Create urgency / Establish relevance]
VIDEO TOPIC: [e.g., "Evasion Attacks"]

REQUIREMENTS:
- Same emotional impact (fear/curiosity/urgency)
- Different scenario or analogy
- Same length (~50-80 words)
- Must connect to video topic
- End with tension or question

ALTERNATIVE SCENARIO OPTIONS:
1. [Healthcare domain]
2. [Financial domain]
3. [Consumer tech domain]
4. [Government/military domain]

OUTPUT:
---
ORIGINAL HOOK: [text]
REWRITTEN HOOK: [new version]
SCENARIO USED: [which domain]
EMOTIONAL DRIVER: [what emotion it triggers]
---
```

**EXAMPLE OUTPUT:**

```
ORIGINAL HOOK:
"Imagine you're a security professional at a leading autonomous vehicle company. Your team deployed a vision system that identifies stop signs with 99.2% accuracy..."

REWRITTEN HOOK:
"Picture this: You're the head of AI at a major hospital. Your diagnostic model detects melanoma with 99.4% accuracy—better than most dermatologists. Celebrated in medical journals. Then a researcher shows you an image. A tiny pattern, invisible to doctors, added to a skin photo. Your model says 'benign.' The patient goes home. The cancer spreads. This isn't science fiction—it's been demonstrated in peer-reviewed research. Today, we're exploring why your accuracy metrics are lying to you."

SCENARIO USED: Healthcare domain
EMOTIONAL DRIVER: Fear + professional responsibility
```

---

## Level 2: LEARNING OBJECTIVES REWRITER

```
PROMPT: LEARNING OBJECTIVES TRANSFORMER

Rewrite these learning objectives using different verbs and phrasing.

ORIGINAL OBJECTIVES:
[Paste bullet points]

VIDEO TOPIC: [e.g., "Adversarial Training"]

REQUIREMENTS:
- Use different action verbs (Bloom's taxonomy equivalents)
- Same cognitive level (knowledge/comprehension/application/analysis)
- Same learning outcomes
- Same number of objectives

VERB SUBSTITUTION GUIDE:
- "Explain" → "Describe" / "Articulate" / "Clarify"
- "Implement" → "Develop" / "Construct" / "Build"
- "Identify" → "Recognize" / "Detect" / "Pinpoint"
- "Analyze" → "Evaluate" / "Assess" / "Examine"
- "Describe" → "Outline" / "Characterize" / "Detail"

OUTPUT:
---
ORIGINAL OBJECTIVES:
• [objective 1]
• [objective 2]

REWRITTEN OBJECTIVES:
• [new objective 1]
• [new objective 2]

VERB CHANGES:
- [old verb] → [new verb] (same cognitive level: [level])
---
```

---

## Level 3: CONTENT SECTION REWRITER

```
PROMPT: CONTENT BLOCK TRANSFORMER

Rewrite this content section while preserving technical accuracy.

ORIGINAL CONTENT:
<>
[Paste content between <> markers]
<>

SECTION TYPE: [Core Concept / Algorithm Walkthrough / Code Example / Real-World Scenario]

REQUIREMENTS:
- Same information, different explanation approach
- Same technical terms (don't rename FGSM, DP-SGD, etc.)
- Different analogies or metaphors
- Same structure (numbered concepts, steps, etc.)
- Preserve all code exactly (only change comments if needed)

REWRITE APPROACH:
- [ ] Use different leading metaphor
- [ ] Restructure explanation order (if logical)
- [ ] Add/change transitional phrases
- [ ] Use different example values (where safe)

OUTPUT:
---
REWRITTEN CONTENT:
<>
[New content]
<>

CHANGES MADE:
- [Change 1]
- [Change 2]

TECHNICAL ACCURACY CHECK:
☐ All algorithms correct
☐ All code preserved
☐ All metrics accurate
☐ All terminology consistent
---
```

---

## Level 4: IVQ REWRITER

```
PROMPT: IN-VIDEO QUESTION TRANSFORMER

Rewrite this IVQ while testing the same knowledge.

ORIGINAL IVQ:
Question: [question text]
• a) [option a]
• b) [option b]
• c) [option c]
• d) [option d]
Correct Answer: [letter]
Explanation: [text]

IVQ TYPE: [Recall / Application / Scenario-based]
CONCEPT TESTED: [e.g., "epsilon parameter in FGSM"]

REQUIREMENTS:
- Same correct answer concept
- Same difficulty level
- Same question type
- Different wording
- Different incorrect option phrasing
- Reordered options (correct answer in different position)

OUTPUT:
---
REWRITTEN IVQ:

Question: [new question text]
• a) [reworded/reordered option]
• b) [reworded/reordered option]
• c) [reworded/reordered option]
• d) [reworded/reordered option]

Correct Answer: [new letter position]

Explanation: [reworded explanation]

Explain Incorrect Options:
• Option [x] is incorrect because [reason]
• Option [y] is incorrect because [reason]
• Option [z] is incorrect because [reason]

VERIFICATION:
☐ Same concept tested
☐ Same difficulty
☐ Correct answer still valid
---
```

---

## Level 5: FULL VIDEO ASSEMBLER

```
PROMPT: VIDEO SCRIPT ASSEMBLER

Assemble rewritten components into complete video script.

VIDEO: [e.g., "Module 1, Video 1: Evasion Attacks"]
DURATION TARGET: [e.g., 7.5 minutes]

COMPONENTS TO ASSEMBLE:
1. HOOK: [rewritten hook]
2. VIDEO OVERVIEW: [rewritten overview]
3. LEARNING OBJECTIVES: [rewritten objectives]
4. CONTENT: [rewritten content blocks]
5. SUMMARY: [rewritten summary]
6. IVQ: [rewritten IVQ]
7. TRANSITION: [rewritten transition]

ASSEMBLY REQUIREMENTS:
- Add smooth transitions between sections
- Ensure consistent tone throughout
- Verify all required elements present
- Check word count approximation

OUTPUT:
---
VIDEO [X]: [TITLE]
Video Type: [type]
Duration: [duration]

Hook: [assembled hook]

Video Overview: [assembled overview]

Learning Objective: "By the end of this video, you will be able to:
• [objective 1]
• [objective 2]
• [objective 3]
• [objective 4]"

[Transition sentence]

Content:
<>
[Assembled content]
<>

[Pre-summary transition]

Summary: [assembled summary]

Transition to IVQ: [transition text]

In-Video Question (IVQ):
[Assembled IVQ]

[Final transition]
---

COMPLETENESS CHECK:
☐ Hook present
☐ Overview present
☐ Objectives present (correct count)
☐ Content sections complete
☐ Summary present
☐ IVQ complete with all parts
☐ Transitions smooth
☐ Tone consistent
```

---

# PART 3: TOP-DOWN APPROACH
*Start with strategy, drill into details*

## Step 1: FULL SCRIPT ANALYZER

```
PROMPT: COURSE SCRIPT ANALYZER

Analyze this complete course script and create a rewriting blueprint.

SCRIPT: [Paste entire script_sample.pdf content]

EXTRACT AND DOCUMENT:

1. STRUCTURE MAP
   - List all sections with hierarchy
   - Word counts per section
   - Component types per video

2. TONE PROFILE
   - Formality (1-10): [score]
   - Energy (1-10): [score]
   - Technical density (1-10): [score]
   - Instructor personality markers

3. RECURRING ELEMENTS
   - Transition phrases used
   - Hook patterns (scenario types)
   - Summary structures
   - IVQ question types

4. TECHNICAL INVENTORY
   - Algorithms mentioned
   - Code examples
   - Metrics and numbers
   - Real-world examples used

5. REWRITE OPPORTUNITIES
   - Sections with similar hooks (need variety)
   - Repeated phrases
   - Analogy refresh candidates

OUTPUT AS: Structured JSON + narrative analysis
```

---

## Step 2: REWRITE STRATEGY GENERATOR

```
PROMPT: REWRITE STRATEGY PLANNER

Based on this analysis, create a rewriting strategy.

ANALYSIS: [Output from Script Analyzer]

TARGET CHANGES:
- Tone shift: [e.g., "slightly more conversational"]
- Analogy refresh: [e.g., "use more everyday examples"]
- Hook variety: [e.g., "vary industry scenarios"]

GENERATE:

1. GLOBAL REWRITE RULES
   - Phrases to replace globally
   - Transition templates to use
   - Tone markers to add/remove

2. SECTION-SPECIFIC INSTRUCTIONS
   For each section:
   - What to preserve exactly
   - What to change
   - Specific new analogies/examples

3. CONSISTENCY REQUIREMENTS
   - Terms that must stay identical
   - Instructor name (keep: Rifat Erdem Sahin)
   - Course title (keep exact)
   - Technical terms (keep exact)

4. QUALITY GATES
   - Minimum hook impact score
   - Required transition smoothness
   - IVQ validity check

OUTPUT: Detailed rewrite plan document
```

---

## Step 3: SECTION-BY-SECTION EXECUTOR

```
PROMPT: SECTION EXECUTOR

Execute rewrite for this specific section following the strategy.

SECTION: [e.g., "SECTION 1: COURSE INTRO VIDEO"]

ORIGINAL:
[Paste section]

REWRITE STRATEGY FOR THIS SECTION:
[From Strategy Planner]

GLOBAL RULES:
[From Strategy Planner]

EXECUTE REWRITE following all guidelines.

OUTPUT:
---
SECTION: [name]

[Complete rewritten section]

---

COMPLIANCE CHECK:
☐ Structure preserved
☐ Word count within 10% of original
☐ All components present
☐ Tone matches target
☐ Technical accuracy maintained
☐ Global rules applied
```

---

## Step 4: FINAL ASSEMBLY & QC

```
PROMPT: COURSE SCRIPT FINALIZER

Assemble all rewritten sections into final course script.

REWRITTEN SECTIONS:
[All sections from Section Executor]

PERFORM:

1. ASSEMBLY
   - Combine all sections in order
   - Add section headers
   - Verify formatting

2. CONSISTENCY CHECK
   - Instructor name consistent
   - Course title consistent
   - Technical terms consistent
   - Tone consistent across all videos

3. COMPLETENESS AUDIT
   For each video, verify:
   ☐ Hook
   ☐ Overview
   ☐ Learning Objectives
   ☐ Content sections
   ☐ Summary
   ☐ IVQ (Question + Options + Answer + Explanations)
   ☐ Transitions

4. GENERATE CHANGE LOG
   | Section | Original Element | Changed To | Reason |
   |---------|-----------------|------------|--------|

OUTPUT:
---
# COMPLETE REWRITTEN COURSE SCRIPT

[Full assembled script]

---

# CHANGE SUMMARY

[Table of all changes]

# QUALITY METRICS

- Total word count: [X] (original: [Y])
- Sections rewritten: [count]
- IVQs preserved: [count]
- Technical accuracy: VERIFIED
---
```

---

# PART 4: QUICK-START SINGLE PROMPT

```
PROMPT: COMPLETE SCRIPT REWRITER (SINGLE PASS)

Rewrite this entire course script with different wording while preserving exact structure.

ORIGINAL SCRIPT:
[Paste script_sample.pdf content]

REWRITE PARAMETERS:
- Tone: [Same / More Formal / More Conversational]
- Hook Style: [Same scenarios / Different industries / More dramatic]
- Analogies: [Refresh all / Keep technical ones / Use everyday examples]

ABSOLUTE PRESERVATION (DO NOT CHANGE):
- Instructor name: Rifat Erdem Sahin
- Course title: "Secure AI: Interpret and Protect Models"
- All technical terms (FGSM, DP-SGD, epsilon, etc.)
- All code examples (exact syntax)
- All numerical values and metrics
- Section/video structure and order
- Learning objective outcomes (change wording only)
- IVQ correct answers (change wording only)

REQUIRED CHANGES:
- All hooks: new scenarios, same emotional impact
- All explanations: different sentence structures
- All transitions: fresh phrasing
- All summaries: restructured, same information
- All IVQ questions: reworded, same concept tested

OUTPUT:
1. Complete rewritten script (full document)
2. Change summary (what was modified)
3. Structure verification checklist
```

---

# PART 5: COMPONENT PROMPT LIBRARY

| Prompt | Use Case | Input | Output |
|--------|----------|-------|--------|
| Hook Transformer | Rewrite video hooks | Single hook | New hook + scenario |
| Learning Objectives Transformer | Rewrite objectives | Objective list | New objectives |
| Content Block Transformer | Rewrite content sections | Content block | New content |
| IVQ Transformer | Rewrite questions | Full IVQ | New IVQ |
| Video Script Assembler | Combine components | All video parts | Complete video |
| Course Script Analyzer | Analyze full script | Full script | Structure + analysis |
| Rewrite Strategy Planner | Plan approach | Analysis | Strategy document |
| Section Executor | Rewrite one section | Section + strategy | Rewritten section |
| Course Script Finalizer | Final assembly | All sections | Complete script + QC |
| Complete Script Rewriter | One-shot rewrite | Full script | Full new script |

---

# APPENDIX: STRUCTURE ENFORCEMENT CHECKLIST

```
COURSE INTRO VIDEO CHECKLIST:
☐ Hook (engaging opening)
☐ Self-Introduction (instructor name preserved)
☐ Course Title Reveal (exact title)
☐ Course Overview (three "uncomfortable realities")
☐ Key Takeaways (4 bullet points)
☐ Closing Remarks (transition to Module 1)

MODULE VIDEO CHECKLIST (repeat for each of 9 videos):
☐ Video Type + Duration header
☐ Hook (scenario-based)
☐ Video Overview
☐ Learning Objectives (4 bullets)
☐ Transition to content
☐ Content section with <> markers
☐ Pre-summary transition
☐ Summary paragraph
☐ Transition to IVQ
☐ IVQ with all components
☐ Transition to next video/practice

OUTRO VIDEO CHECKLIST:
☐ Opening & Acknowledgment
☐ Recap (Module 1, 2, 3 summaries)
☐ Motivational Message
☐ Encouragement for Continued Growth
☐ Actionable Next Steps (4 items)
☐ Closing Remarks

PROMO VIDEO CHECKLIST:
☐ Hook - Problem Statement
☐ Self-Introduction
☐ Course Announcement
☐ Key Benefits (4 bullets)
☐ Real-Life Impact
☐ Unique Selling Points (3 bullets)
☐ Target Audience Call-Out
☐ Closing Inspiration
☐ Call to Action
```

---

*System designed for Antigravity IDE | Structure locked to script_sample.pdf*
