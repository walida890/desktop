# TASK 5 — Executive Presentation & Regulatory Submission
## Week 9–10 of the Capstone

---

## Learning Objectives

By the end of this task, the mentee will be able to:
- [ ] Synthesise 4 prior deliverables into a coherent, compelling executive narrative
- [ ] Write an executive summary that a non-technical senior stakeholder can act on
- [ ] Design and deliver a 10-slide stakeholder presentation with a clear recommendation
- [ ] Prepare for and handle a Q&A session with senior stakeholders (including hostile or sceptical questions)
- [ ] Produce a formal regulatory submission document suitable for FCA presentation
- [ ] Use AI to scaffold content, then drive the narrative and final decisions themselves

---

## The Brief: What The Mentee Receives

---

### Meridian Financial — Email from Sarah Chen (Head of Compliance)

**TO:** Business Analysis Team
**FROM:** Sarah Chen, Head of Compliance
**DATE:** [Task 5 Start Date]
**RE: FCA Submission — 6-Week Regulatory Deadline

---

We are now 6 weeks from the FCA deadline. Marcus (CFO) and I need to present a credible remediation plan to the FCA's Supervision team. We have our internal work complete. Your deliverables — the Discovery Report, Requirements Package, Solution Design, and UAT Strategy — form the basis of what we need to present.

I need two things from you:

**1. An Executive Summary** — a 3-page document summarising the problem, the solution, the cost, the timeline, and the risk. Marcus will read this before the meeting. If it doesn't give him what he needs in 3 minutes, we have a problem. He doesn't want BA language. He wants to know: what happened, what we're doing about it, how much it costs, how long it takes, and what happens if we don't do it.

**2. A 10-slide presentation deck** — this is what we'll present to the FCA's Supervision team directly. The FCA reviewers are compliance professionals — they know the regulations. They will be looking for:
  - Evidence that we understand the severity of the gaps
  - A credible plan to fix them
  - Confirmation that we can deliver within the 90-day window (or a realistic extension request)
  - Evidence that we have the right governance in place to prevent recurrence

The presentation must be clear, factual, and honest. Do not oversell what we've done. Do not claim we've solved things we haven't. The FCA can tell.

I've also asked Marcus, James, and Diana to be available for a Q&A rehearsal with you on Friday. Expect challenging questions — they will push on your assumptions.

**Deadline: End of Week 10**

**— Sarah Chen**

---

### Q&A Preparation Pack (Simulated)

The mentee will face the following Q&A challenges in the rehearsal (role-play with mentor):

| Questioner | Likely Challenge | What They're Looking For |
|------------|-----------------|-------------------------|
| Marcus Reid (CFO) | "How much does this cost?" | Concrete numbers, prioritisation logic, ROI or risk mitigation framing |
| Sarah Chen (Compliance) | "Is this actually compliant or just 'more compliant'?" | Honest assessment, known limitations, residual risk |
| James Okafor (Product) | "Why are we recommending a third-party vendor when we said we don't want vendor lock-in?" | A balanced view, clear criteria for the decision |
| Diana Vlasova (Engineering) | "The Salesforce FSC sync gap you identified — have you actually validated that Salesforce can do what you're asking?" | Technical realism, evidence of feasibility validation |
| Priya Sharma (Legal) | "What's our residual AML risk after Sprint 1? What don't we fix?" | An honest gap assessment, risk register, plan for residual risk |

---

## Task 5 Deliverables

### Deliverable 5A: Executive Summary

**Format:** 2–3 pages, plain English

**Audience:** Marcus Reid (CFO), Sarah Chen (Head of Compliance)

**Structure:**

```
EXECUTIVE SUMMARY

THE PROBLEM (1 paragraph)
- What the FCA found and why it matters
- Consequences of inaction (specific, not vague)

WHAT WE FOUND (1 paragraph)
- Key gaps discovered in discovery phase
- Most critical risks — specifically

WHAT WE'RE DOING ABOUT IT (1–2 paragraphs)
- Solution approach (in plain language — no BA jargon, no unexplained acronyms)
- Phased approach: Sprint 1 fixes the critical gaps; what happens in Sprint 2+
- Decision on third-party tooling with rationale

TIMELINE (clear table or timeline graphic)
- Sprint 1 delivery: [Date]
- UAT sign-off: [Date]
- Full remediation complete: [Date]
- FCA 90-day deadline: [Date]
- Are we on track? Yes/No — and if no, what do we need?

COST (clear table)
- Estimated build cost (engineering)
- Third-party tooling costs (vendor subscriptions, API costs)
- Ongoing compliance cost
- Total

RISK AND RESIDUAL RISK (short section)
- What's fixed after Sprint 1
- What's not fixed yet (residual risk)
- What we need to monitor

WHAT HAPPENS IF WE DON'T DO THIS (1 paragraph — be specific)
- Regulatory consequences
- Commercial consequences
- Specific examples (not generic warnings)

RECOMMENDED NEXT STEPS (3–5 bullet points)
- Immediate actions (next 2 weeks)
- Decisions needed (from Marcus/Sarah)
```

---

### Deliverable 5B: Stakeholder Presentation Deck

**Format:** 10–12 slides, suitable for FCA presentation

The deck must tell a coherent story. It is not a data dump — it is an argument for a specific course of action.

**Slide Structure:**

| Slide | Title | Content | Speaker Notes Required? |
|-------|-------|---------|----------------------|
| 1 | Agenda | Clear agenda, set expectations | Yes — tone-setting |
| 2 | Background & Context | What is Meridian, what do we do, why are we here | Yes — establish credibility |
| 3 | What We Found | Summary of discovery findings (AS-IS pain points) | Yes — factual, not emotional |
| 4 | The Gaps | Top 5 regulatory gaps with FCA reference and severity | Yes — be specific, cite real references |
| 5 | Our Proposed Solution | Sprint 1 approach — what we're building | Yes — avoid technical jargon |
| 6 | Solution Architecture | System context diagram (simplified for FCA audience) | Yes — explain what the diagram shows |
| 7 | Vendor Decisions | Third-party tooling rationale (why we chose what we chose) | Yes — anticipate vendor scepticism |
| 8 | Timeline & Milestones | Phased delivery plan with key dates | Yes — be honest about risks |
| 9 | Cost | Summary table — build cost, tooling cost, ongoing cost | Yes — be ready to justify |
| 10 | Risk & Residual Risk | What's fixed, what's not, what we're monitoring | Yes — honesty is the right strategy here |
| 11 | Governance & Prevention | How we'll prevent this happening again | Yes — this is what the FCA wants to see |
| 12 | Recommended Actions | What we need from the FCA and what we're committing to | Yes — clear ask, clear commitments |

**Slide design principles:**
- One key message per slide — if it takes more than 30 seconds to explain, split it
- Data visualisation where possible (gap severity chart, timeline graphic, cost breakdown)
- No BA jargon on slides (acronyms must be defined on first use)
- Regulatory references must be accurate (FCA PS17/14, MLR 2017 — real references)
- FCA reviewers in the room — they know the regulations. Don't explain what a PEP is.

---

### Deliverable 5C: Q&A Preparation Document

**Format:** Structured Q&A brief

The mentee prepares for the Q&A rehearsal by producing a document that anticipates:

**For each likely question:**
- The question (verbatim)
- Who is asking it and why
- What they need to hear
- What the honest answer is (including limitations and uncertainties)
- What to say if we don't know the answer (don't improvise — say "I'll confirm that and come back to you")
- What the dangerous answer is (what NOT to say)

**Difficult question bank:**

| Question | Why It's Difficult | How to Handle |
|----------|-------------------|---------------|
| "How do you know Salesforce FSC can actually do this?" | Diana flagged this as unvalidated | Be honest — say we're validating it in discovery phase of Sprint 1; flag it as a risk |
| "What happens if the third-party vendor fails?" | There is no good answer to this | Acknowledge the risk; explain fallback procedures; note we require vendor SLAs |
| "Why should we trust this timeline?" | 10 weeks is aggressive | Show buffer; show dependencies; show critical path; be honest about what blows the timeline |
| "What residual AML risk remains after Sprint 1?" | You cannot eliminate all risk | Be honest — list what's not fixed; quantify residual risk where possible; explain monitoring plan |
| "What did you not find?" | The FCA will ask this | Be prepared to say "we don't know" where appropriate; show humility |

---

### Deliverable 5D: Regulatory Submission Document (Draft)

**Format:** Formal document suitable for FCA presentation

This is a draft regulatory submission. The final version will be reviewed by Priya Sharma (Legal) and Sarah Chen before submission.

The document must:
1. Be written in a formal, factual tone
2. Cite real FCA regulatory references throughout
3. Present findings, solution, and timeline clearly
4. Acknowledge limitations and residual risk honestly
5. Propose a credible and specific remediation plan
6. Include a governance section: how Meridian will ensure this doesn't happen again

**FCA-specific considerations to address:**
- FCA Supervision's likely concerns (based on the case reference and regulatory context)
- How the submission demonstrates Meridian takes the matter seriously
- What Meridian is asking of the FCA (time, flexibility, clarification?)
- What Meridian is committing to unconditionally

---

## AI Prompt Library: Task 5

---

### Prompt 5.1: Executive Summary Generation

```
You are a Senior Business Analyst and Communications Specialist. Write an executive summary for a UK fintech CFO.

Context:
- Meridian Financial is a UK FCA-regulated fintech (open banking payments for SMEs)
- The FCA has identified KYC/AML gaps in Meridian's client onboarding process
- The FCA has given Meridian 90 days to demonstrate a credible remediation plan
- Meridian has completed discovery (AS-IS process, gap analysis), requirements, solution design, and UAT planning
- Sprint 1 (10 weeks) will fix the most critical gaps; Sprint 2 addresses remaining items
- Marcus Reid (CFO) will read this document before a meeting with the FCA

Write a 2-page executive summary that:
1. States the problem clearly (without jargon or acronyms)
2. Summarises what was found (discovery findings)
3. Presents the solution (plain English — what we're building, why)
4. Shows the timeline (Sprint 1 milestones, total completion, FCA deadline)
5. Shows the cost (engineering estimate + third-party tooling + ongoing)
6. States the risk honestly (what's fixed, what isn't, what's monitoring)
7. States consequences of inaction (specific — regulatory fines, commercial impact, specific client risk)
8. Lists 3-5 recommended immediate actions

Marcus Reid is numerate, risk-aware, and impatient with vague language. Do not use BA jargon. Do not use unexplained acronyms. If you use a technical term, define it immediately.

Length: 2–3 pages.
```

**Critique checklist:**
- Could Marcus Reid understand this in 3 minutes without asking a BA what it means?
- Are the consequences of inaction specific and credible, or vague?
- Is the cost realistic for a Series B fintech, or is this an enterprise budget?
- Does the summary make a clear recommendation, or does it just describe what was done?
- Are there any statements that would embarrass Meridian in front of the FCA?

---

### Prompt 5.2: Stakeholder Presentation Scaffolding

```
You are a Senior Business Analyst preparing a stakeholder presentation for a UK fintech regulatory submission.

You are presenting to the FCA's Supervision team. The audience is:
- FCA Compliance supervisors (know the regulations — don't explain basics)
- Meridian CFO and Head of Compliance (know the business)
- Legal Counsel (aware of legal exposure)

Slide deck brief:
[paste brief above]

For each of the following slides, provide:
1. Key message (one sentence — what is this slide arguing?)
2. Content outline (bullet points — what goes on the slide)
3. Data visualisation recommendation (chart, table, diagram — or "no visual needed")
4. Speaker notes (what to say in 60 seconds max per slide)
5. What to anticipate from the audience (what questions will this slide invite?)

Slides:
1. Agenda
2. Background & Context
3. What We Found (Discovery)
4. The Gaps
5. Our Proposed Solution
6. Solution Architecture
7. Vendor Decisions
8. Timeline & Milestones
9. Cost
10. Risk & Residual Risk
11. Governance & Prevention
12. Recommended Actions

Write for a senior audience. No jargon, no unexplained acronyms. Every slide must support the overall narrative: "We understand the problem, we have a credible plan, we are committed to fixing it."
```

**Critique checklist:**
- Is the AI maintaining one key message per slide, or is it trying to put everything on one slide?
- Is the AI being honest about limitations, or is it smoothing over them?
- Are the speaker notes actually what you'd say, or are they a transcript of what the slide says?
- Does the deck tell a coherent story, or is it a collection of unrelated facts?

---

### Prompt 5.3: Difficult Question Preparation

```
You are a Senior Business Analyst preparing for a hostile Q&A session with a CFO, a Compliance Lead, a Product Manager, a Lead Engineer, and a Legal Counsel.

The subject is a UK fintech's FCA regulatory remediation project. The following difficult questions are anticipated:

Questions:
1. "How do you know Salesforce FSC can actually do this — have you validated it?"
2. "What happens to our compliance obligations if the third-party vendor fails or goes bust?"
3. "Why should we accept a 10-week timeline when the FCA gave us 90 days?"
4. "What residual AML risk remains after Sprint 1 is complete?"
5. "We didn't ask you to recommend a vendor — why is that in the solution?"
6. "What did your discovery NOT find? What don't you know?"
7. "The gap you identified between Salesforce and the microservice — that's a 3-month engineering problem. How does that fit in 10 weeks?"
8. "What's the fallback if the FCA doesn't accept our timeline?"

For each question:
1. Why is this question difficult (what makes it uncomfortable to answer?)
2. What does the questioner actually need to hear?
3. What is the honest answer (including limitations and uncertainties)?
4. What is the dangerous answer (the answer that sounds good but creates a problem?)
5. What is the prepared answer (the answer you would give in the session?)
6. If you don't know the answer — what do you say instead?

Be honest. Do not generate answers that smooth over genuine uncertainty. The goal is to walk into this Q&A session genuinely prepared, not to sound prepared.
```

**Critique checklist:**
- Is the AI giving honest answers or plausible-sounding answers that paper over real gaps?
- Are the "dangerous answers" actually dangerous, or just cautious ones?
- Is the AI's "prepared answer" actually deliverable in under 60 seconds?
- Is the AI flagging questions where the honest answer is "I don't know, I'll find out"?

---

## Task 5 Completion Checklist

- [ ] Executive Summary written for Marcus Reid — could a numerate senior executive understand it in 3 minutes?
- [ ] All 10–12 presentation slides are drafted with speaker notes
- [ ] Presentation tells a coherent narrative (not a collection of facts)
- [ ] Q&A Preparation document covers all 5 likely questioners
- [ ] Regulatory submission draft is complete and suitable for Priya/Sarah review
- [ ] All regulatory references in all documents are verified (not hallucinated)
- [ ] No unexplained BA jargon or acronyms on slides or in executive summary
- [ ] AI-generated content reviewed — all citations verified against FCA Handbook
- [ ] Mentee has rehearsed presentation delivery (not just written the slides)
- [ ] Mentee has completed Q&A rehearsal (role-play with mentor or peers)

---

## Capstone Completion

Upon completing all 5 tasks, the mentee has produced a professional BA portfolio package:

| Deliverable | Task | Format |
|-------------|------|--------|
| Stakeholder Register & Analysis | Task 1 | Table + Power/Interest Grid |
| AS-IS Process Map | Task 1 | BPMN-style process map |
| Gap Analysis Report | Task 1 | Structured table + narrative |
| Discovery Summary Report | Task 1 | 3–4 page document |
| Requirements Package | Task 2 | Structured FR/NFR documents |
| Requirements Backlog | Task 2 | Prioritised backlog table |
| Requirements Review Notes | Task 2 | Annotated self-review |
| Requirements-to-Systems Mapping | Task 3 | Traceability matrix |
| Integration Gap Analysis | Task 3 | Gap table + data flow diagram |
| Solution Options Assessment | Task 3 | Comparison table + recommendation |
| Data Model Gap Analysis | Task 3 | Entity list + gap descriptions |
| UAT Test Strategy | Task 4 | Strategy document |
| Test Scenario Register | Task 4 | Structured scenario outlines |
| Traceability Matrix | Task 4 | Requirements-to-scenarios matrix |
| Executive Summary | Task 5 | 2–3 page document |
| Stakeholder Presentation Deck | Task 5 | 10–12 slides |
| Q&A Preparation Brief | Task 5 | Structured Q&A document |
| Regulatory Submission (Draft) | Task 5 | Formal FCA document |

---
