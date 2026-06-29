# AI BA Practice Guide
## How to Use AI as a Working BA Tool — Not a Crutch

---

## The Core Principle

AI is a **research assistant, drafter, and challenger** — not an authority. The mentee is the BA. AI generates; the mentee judges.

Every AI output the mentee submits must have been:
1. **Generated** — using a prompt from the prompt library
2. **Reviewed** — against the critique checklist for that prompt
3. **Refined** — the mentee has edited, challenged, or replaced parts of the AI output
4. **Verified** — regulatory references, vendor names, and factual claims have been checked

If the mentee cannot explain why an AI output is correct, it is not correct.

---

## The Three Modes of AI Use in This Programme

---

### Mode 1: Research & Context (Low Stakes)
AI is used to quickly build context — understanding FCA regulations, researching vendors, finding industry patterns.

**When to use:** Early in discovery, when the mentee doesn't yet know enough to evaluate AI output.
**Risk:** AI may hallucinate facts or cite non-existent regulations.
**Mentee's job:** Verify everything. Use FCA Handbook (handbook.fca.org.uk) directly.

**Example:** Using Prompt 1.3 (Regulatory Gap Identification) to understand what PS17/14 actually says.

---

### Mode 2: Drafting & Structuring (Medium Stakes)
AI is used to generate a first draft — requirements, interview questions, test scenarios.

**When to use:** When the mentee knows enough to evaluate the output but needs a starting point.
**Risk:** AI produces generic, plausible-but-wrong, or vague content.
**Mentee's job:** Scrutinise specificity. Is the acceptance criterion actually testable? Is the gap description precise?

**Example:** Using Prompt 2.1 (User Story Generation) to draft stories, then refining them to be specific and measurable.

---

### Mode 3: Critical Challenge (High Stakes)
AI is used to challenge the mentee's own analysis — finding gaps in their reasoning, identifying blind spots.

**When to use:** After the mentee has formed a view and before they submit.
**Risk:** AI may agree too readily or defer to the mentee's view without genuine challenge.
**Mentee's job:** Actively prompt AI to disagree. Ask: "What have I missed? What is wrong with my analysis?"

**Example:** Using Prompt 5.3 (Difficult Question Preparation) to stress-test the executive narrative before presenting to the FCA.

---

## Red Lines: Where AI Consistently Fails in BA Contexts

These are the mistakes AI makes repeatedly. The mentee must watch for all of them.

---

### 1. Hallucinated Regulatory Citations
AI will cite FCA references that sound real but don't exist. It commonly:
- Cites section numbers that don't exist
- Attributes requirements to the wrong regulatory instrument
- Invents "FCA Guidance FG22/X" that isn't in the Handbook

**Always verify against:** https://www.handbook.fca.org.uk
**Never trust a citation you haven't verified.**

---

### 2. Vague Acceptance Criteria
AI generates acceptance criteria like:
> "The system must verify the customer's identity before account activation"

This is not testable. It doesn't say *how* verification happens, *what* constitutes success, or *what* the system does on failure.

**What it should look like:**
> "Given a client has submitted all required identity documents, when the system executes the Experian Verify check, then the system must store the verification result (pass/fail/error) in the compliance record within 30 seconds, and if the result is 'fail', the account must remain in 'pending verification' status until manually reviewed."

**Rule: If you cannot write a UAT test case from an acceptance criterion, it is not a valid acceptance criterion.**

---

### 3. Invented Process Steps
When generating process maps or requirement descriptions, AI will sometimes add steps that weren't in the evidence — because they "seem right." This is dangerous because it looks authoritative.

**Rule: Every process step must map to evidence from a stakeholder interview, a document, or an observed system. If AI adds a step with no evidence basis, remove it.**

---

### 4. Generic Vendor Recommendations
AI will recommend enterprise-grade vendors it thinks are impressive (e.g., Oracle FCCM, AWS AML") without knowing whether they're appropriate for a 250-person fintech.

**Always verify:** Does this vendor actually serve SMEs? What is their UK FCA compliance history? What is their typical contract minimum?

---

### 5. Conflating Complexity with Completeness
AI tends to make requirements and test scenarios more complex than necessary when it is uncertain — adding layers of error handling and edge cases that don't reflect real-world priority.

**Rule: Is this scenario actually likely to occur? Is this error handling worth the development effort? Apply MoSCoW to AI output too.**

---

## How to Critique AI Output: A Checklist

For every AI output received, the mentee should run through:

**Accuracy**
- [ ] Are the regulatory citations real? (Verify against FCA Handbook)
- [ ] Are the facts about Meridian's systems accurate based on the brief?
- [ ] Is the vendor named real and appropriate?

**Specificity**
- [ ] Are acceptance criteria written as outcomes, not process steps?
- [ ] Can I write a UAT test case from this?
- [ ] Is every process step backed by evidence?

**Completeness**
- [ ] What has AI missed or assumed away?
- [ ] Are there stakeholder perspectives not represented?
- [ ] What would a sceptical engineer say about this?

**Consistency**
- [ ] Does this contradict something in an earlier deliverable?
- [ ] Are severity ratings consistent across the gap analysis?
- [ ] Is the priority consistent with the reasoning given?

**Plausibility**
- [ ] Is this achievable in the timeline and budget stated?
- [ ] Is this technically feasible given the current system landscape?
- [ ] Is the AI solving the actual problem or a simplified version of it?

---

## Prompt Library Quick Reference

| Task | Prompt | Best Used When |
|------|--------|---------------|
| Discovery | 1.1 Interview Questions | Before each stakeholder interview |
| Discovery | 1.2 Process Structuring | After interview, to convert notes to structured steps |
| Discovery | 1.3 Gap Identification | After AS-IS map, to identify regulatory gaps |
| Discovery | 1.4 Severity Assessment | After gap list, to prioritise and justify |
| Requirements | 2.1 User Story Generation | After gap analysis, to draft stories from gaps |
| Requirements | 2.2 NFR Generation | After FR requirements, to identify non-functional needs |
| Requirements | 2.3 Conflict Detection | Before finalising requirements, to find contradictions |
| Solution Design | 3.1 Vendor Research | When evaluating build vs. buy decisions |
| Solution Design | 3.2 Integration Risk | When assessing feasibility of integrations |
| UAT | 4.1 Test Scenario Generation | To draft scenarios from acceptance criteria |
| UAT | 4.2 Cross-System Scenarios | To identify failure paths across systems |
| UAT | 4.3 Edge Case Discovery | To find gaps in test coverage |
| Presentation | 5.1 Executive Summary | First draft for Marcus |
| Presentation | 5.2 Slide Scaffolding | When structuring the deck |
| Presentation | 5.3 Q&A Preparation | After draft deck, to stress-test the narrative |

---
