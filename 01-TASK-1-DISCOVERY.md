# TASK 1 — Discovery & AS-IS Process Analysis
## Week 1–2 of the Capstone

---

## Learning Objectives

By the end of this task, the mentee will be able to:
- [ ] Conduct structured stakeholder identification and analysis using power/interest mapping
- [ ] Plan and execute a stakeholder discovery interview with clear objectives
- [ ] Use AI to prepare interview questions, challenge assumptions, and identify unknown unknowns
- [ ] Produce an AS-IS process map from interview and document evidence
- [ ] Cross-reference a process against FCA regulatory requirements to identify gaps
- [ ] Produce a Gap Analysis Report with severity ratings
- [ ] Use AI to draft process commentary, then critically review and refine the output

---

## The Brief: What The Mentee Receives

---

### Meridian Financial — Internal Memo (Reproduced for Mentee)

**TO:** Business Analysis Team
**FROM:** Sarah Chen, Head of Compliance
**DATE:** [Current Date]
**RE:** New Client Onboarding — Urgent Regulatory Review Required

---

We have received a formal regulatory notice from the FCA regarding our new client onboarding process. The FCA's review (ref: case no. **FCA/ONB/2024/0471**) has identified potential gaps in our KYC and AML compliance controls that need to be addressed within **90 days**.

Specifically, the FCA has flagged concerns around:
1. Adequacy of identity verification during account opening
2. Documentation of beneficial ownership information
3. Sanctions and PEP (Politically Exposed Person) screening procedures
4. Risk rating of new clients at onboarding
5. Clarity of audit trail for compliance reviews

I need the BA team to conduct a full discovery of the current onboarding process — from lead generation through to account activation — and produce:
- An accurate AS-IS process map
- A gap analysis against FCA requirements
- A preliminary list of requirements for the remediation work

This is time-critical. The CFO and I will need to present a remediation plan to the FCA in 6 weeks. Your analysis is the foundation of that presentation.

I have arranged for you to speak with the relevant stakeholders. The schedule is below.

**— Sarah Chen, Head of Compliance**

---

### Stakeholder Interview Schedule

The mentee will conduct (or simulate) interviews with the following stakeholders:

| # | Stakeholder | Role | Interview Focus |
|---|-------------|------|-----------------|
| 1 | Tom Bradley | Head of Operations | Current onboarding process, step-by-step |
| 2 | James Okafor | Product Manager | Product expectations, current tooling, known issues |
| 3 | Diana Vlasova | Lead Engineer | Technical constraints, current system integrations |
| 4 | Priya Sharma | Legal Counsel | Regulatory requirements, risk of non-compliance |
| 5 | Marcus Reid | CFO | Budget and risk appetite, business priorities |

*(Note to mentor: these can be conducted as role-play sessions, async video responses, or written Q&A documents. The format is flexible.)*

---

## Task 1 Deliverables

### Deliverable 1A: Stakeholder Register & Analysis

**Format:** Table + Power/Interest Grid (visual)

Produce a register of all stakeholders involved in or affected by the onboarding process. For each stakeholder include:
- Name and role
- Department
- Level of influence on the project (High/Medium/Low)
- Level of interest in the project (High/Medium/Low)
- Communication approach (how and when to engage)
- Key concerns or priorities (from interview evidence)

Then map them onto a power/interest grid:

```
                    HIGH INTEREST
                         │
      KEEP SATISFIED     │     KEY PLAYERS
      (inform regularly) │     (engage closely)
  ───────────────────────┼───────────────────────
      MONITOR            │     KEEP INFORMED
      (minimal effort)   │     (keep updated)
                         │
                    LOW INTEREST
    LOW POWER ───────────┴────────────── HIGH POWER
```

**AI note:** The mentee uses AI to:
- Draft the initial stakeholder list from the brief (who is missing from the memo?)
- Generate probing questions for each stakeholder interview
- Identify power/interest positioning based on interview evidence
- Flag stakeholders who may have conflicting priorities

---

### Deliverable 1B: AS-IS Process Map

**Format:** BPMN-style process map (level 1 + level 2 for critical path)

The process map covers: **Lead / Inquiry → Account Application → Identity Verification → Compliance Checks → Account Approval → Onboarding Complete → First Transaction**

For each process step, the map must show:
- Step name and number
- Owner (who is responsible)
- Key inputs and outputs
- Systems involved
- Decision points (yes/no gates)
- Pain points or known issues (annotated separately)

**Critical path must include:**
1. Lead capture and initial screening
2. KYC document collection
3. Identity verification (passport, proof of address)
4. Beneficial ownership declaration
5. PEP and sanctions screening
6. Risk rating assignment
7. Compliance sign-off
8. Account activation
9. First transaction monitoring

The process map must be detailed enough that a new joiner could follow it without asking questions.

**AI note:** The mentee uses AI to:
- Convert rough interview notes into structured process step descriptions
- Identify decision points the mentee may have missed
- Map process steps to regulatory requirements (which step addresses which FCA rule?)
- Suggest common failure points at each step based on industry data

---

### Deliverable 1C: Regulatory Gap Analysis

**Format:** Structured table + narrative

For each FCA requirement flagged by the FCA notice (and any additional gaps discovered during discovery), the mentee produces:

| Gap ID | FCA Reference | Requirement | Current Process Step | Gap Description | Severity (H/M/L) | Business Risk |
|--------|--------------|-------------|---------------------|-----------------|-------------------|---------------|
| G-001 | PS17/14, §4.2 | Identity verification must include documentary and non-documentary checks | Step 3: ID Verification | No non-documentary check procedure exists | High | Regulatory fine, AML breach |
| G-002 | MLR 2017, Reg 28 | Beneficial ownership info must be collected for legal entities | Step 4: BO Declaration | BO form exists but is not mandatory; 40% of clients skip | High | FCA enforcement |
| G-003 | ... | ... | ... | ... | ... | ... |

The severity rating must be justified with both **regulatory risk** (what the FCA could do) and **business risk** (what could go wrong for a client or for Meridian).

**AI note:** The mentee uses AI to:
- Research FCA PS17/14 and MLR 2017 requirements (with citations)
- Draft gap descriptions in plain language
- Assess severity by comparing against FCA enforcement precedents
- Identify which gaps create other regulatory cross-dependencies

**Critical AI red lines the mentor must check:**
- Is the AI citing real FCA references or hallucinating?
- Is the AI conflating different regulatory frameworks?
- Are the severity ratings based on evidence or on AI speculation?

---

### Deliverable 1D: Discovery Summary Report

**Format:** 3–4 page document + process map

The report is the mentee's first professional BA output. It must:
1. Summarise the current onboarding process (AS-IS)
2. Present the key regulatory gaps found
3. Recommend prioritisation of gaps (with rationale)
4. Identify what further investigation is needed before requirements can be written

The report must be written for a **senior audience** — Sarah Chen, Marcus Reid, and Priya Sharma will read it. No BA jargon, no unexplained acronyms, clear plain English.

---

## AI Prompt Library: Task 1

These prompts are given to the mentee as templates. The critical skill is knowing how to critique the output.

---

### Prompt 1.1: Interview Question Generation

```
You are a Senior Business Analyst preparing interview questions for a discovery session.

Context:
- We are investigating the current new client onboarding process at a UK fintech (open banking payments)
- The FCA has flagged gaps in KYC/AML compliance
- The interviewee is [ROLE: e.g., Head of Operations]
- Their perspective is [1-2 sentences on their role in onboarding]

Generate 12 probing questions for this interview. Include:
- 4 questions about the process (what happens, when, by whom)
- 3 questions about pain points and known failures
- 3 questions about regulatory concerns or compliance pressures
- 2 questions that challenge assumptions ("why do you do it this way rather than...")

For each question, note WHY it matters — what you expect to learn from it.
```

**Critique checklist for mentee:**
- Are any questions leading or biased?
- Are any questions too technical for a first interview?
- Are you asking "what" before "why"?
- What would you follow up if the answer is vague?

---

### Prompt 1.2: Process Step Structuring

```
You are a Business Analyst documenting an AS-IS process from interview notes.

The following are raw notes from an interview with [ROLE]. Transform them into a structured process step format.

Raw notes:
[Paste interview notes here]

For each step, provide:
1. Step name
2. Owner (role, not individual name)
3. Key inputs
4. Key outputs
5. Systems used
6. Decision point (yes/no — if yes, what are the conditions?)
7. Known issue or pain point (if any)

Flag any steps where the notes are ambiguous or contradictory.
```

**Critique checklist:**
- Are inputs/outputs actually what enters and leaves the step, or just activities?
- Is the system list specific (name and version) or vague?
- Are the decision criteria testable?
- Does the AI assume steps that weren't in the notes?

---

### Prompt 1.3: Regulatory Gap Identification

```
You are a Financial Services Compliance Analyst. A UK fintech has received an FCA regulatory notice about gaps in their client onboarding KYC/AML process.

Current AS-IS process steps:
[List steps from Process Map Deliverable]

FCA regulatory requirements that apply:
- FCA PS17/14: Systems and controls for AML (specifically §4.2 on customer due diligence)
- FCA MLR 2017, Regulation 28: Beneficial ownership
- FCA MLR 2017, Regulation 35: Politically Exposed Persons (PEPs)
- JMLSG Guidance Chapter 5: Onboarding and customer due diligence
- FCA Consumer Duty FG22/5: Fair customer outcomes in new customer onboarding

For each regulatory requirement, identify:
1. Which current process step addresses (or should address) this requirement
2. What the gap is between current practice and the requirement
3. What evidence would confirm the gap (a test, a record, an observation)
4. Severity of the gap if unaddressed (High/Medium/Low) and why

Include specific regulatory text citations where possible. If you are uncertain about a citation, say so — do not invent it.
```

**Critique checklist:**
- Are the regulatory citations real? (Verify against FCA Handbook — https://www.handbook.fca.org.uk)
- Is the gap described in plain language, or does it use compliance jargon?
- Is the severity consistent with the actual regulatory risk (not just the worst case)?
- Does the gap analysis miss any requirement entirely?

---

### Prompt 1.4: Gap Severity Assessment

```
You are a Senior Business Analyst and Risk Manager at a UK fintech.

Review the following regulatory gaps identified in our onboarding process. For each gap, provide:
1. Regulatory consequence: what the FCA could do if this gap is not remediated (fine, enforcement notice, approval withdrawal, etc.)
2. Business consequence: what could go wrong operationally or commercially if the gap is not remediated
3. Likelihood: how likely is it that the gap results in actual harm or regulatory action (High/Medium/Low)
4. Overall risk rating: combine severity and likelihood into a risk score (Critical/High/Medium/Low)
5. Recommended immediate action: what should we do in the next 2 weeks while a full remediation is planned

Gaps:
[G-001: paste]
[G-002: paste]
...

Be specific. Generic responses like "this could result in regulatory action" are not acceptable.
```

**Critique checklist:**
- Is the AI conflating likelihood with severity? (These are different)
- Are the regulatory consequences accurate? (e.g., can the FCA actually withdraw approval in this scenario?)
- Is the recommended immediate action actually actionable in 2 weeks, or is it just "fix it properly"?

---

## Task 1 Completion Checklist

Before submitting Task 1, the mentee must confirm:

- [ ] All 5 stakeholder interviews conducted (or evidence of attempt)
- [ ] Stakeholder register includes all stakeholders identified (minimum 8)
- [ ] Process map covers full end-to-end onboarding, including all decision gates
- [ ] Gap analysis covers all FCA requirements flagged in the brief
- [ ] Gap severity ratings are justified with evidence
- [ ] Discovery Report is written for senior stakeholders (Sarah, Marcus, Priya as the audience)
- [ ] AI output has been reviewed against the red lines checklist — no hallucinated citations
- [ ] Process map and gap analysis are internally consistent (gaps map to steps)

---

## Mentor Review Points: Task 1

The mentor reviews the submission for:
1. **Completeness**: Are all deliverables present and to standard?
2. **BA judgement**: Has the mentee made sound analytical decisions, or are they just reporting facts?
3. **AI output quality**: Are the AI-generated gaps and citations real? Is the process map accurate?
4. **Communication**: Could a non-BA read this and understand what the problem is?
5. **Prioritisation**: Is the gap prioritisation logical and justified?

The mentor does NOT expect perfection — this is a learning exercise. The focus is on BA thinking, not on having all the right answers.

---
