# TASK 2 — Requirements Engineering
## Week 3–4 of the Capstone

---

## Learning Objectives

By the end of this task, the mentee will be able to:
- [ ] Write structured requirements from a gap analysis (epic → feature → user story → acceptance criteria)
- [ ] Distinguish between functional and non-functional requirements
- [ ] Apply a prioritisation framework (MoSCoW) to requirements
- [ ] Use AI to generate requirement drafts, then critically review for specificity, testability, and ambiguity
- [ ] Identify dependencies between requirements and flag conflicts
- [ ] Produce a requirements package that Engineering can estimate from

---

## The Brief: What The Mentee Receives

---

### Meridian Financial — Email from James Okafor (Product Manager)

**TO:** Business Analysis Team
**FROM:** James Okafor, Product Manager
**DATE:** [Task 2 Start Date]
**RE:** Requirements for Onboarding Remediation — Next Steps

---

Sarah has shared the Discovery Report with the product and engineering team. Good work — the gap analysis is clear and the prioritisation makes sense. The CFO has signed off on the budget for remediation.

We now need a full requirements package for the engineering team. Here's what I need from you:

1. **All high and medium priority gaps** from the Discovery Report must be converted into requirements
2. Requirements must be specific enough for Engineering to estimate — no vague statements
3. I need both **functional** and **non-functional** requirements clearly separated
4. The requirements must be traceable back to the gaps and regulatory references in the Discovery Report
5. I need a **prioritised backlog** — we can't do everything in 90 days, so I need your recommendation on what to build first

A few things to note:
- We are building on our existing platform (Salesforce Financial Services Cloud + a custom onboarding microservice)
- Engineering capacity is approximately 3 engineers for 12 weeks
- We have a scheduled release on [Date +10 weeks] — the priority requirements must fit this window
- Diana (Lead Engineer) has asked that every requirement includes clear acceptance criteria — no "and other such requirements" language

I've attached the Discovery Report from Task 1 for reference.

**— James Okafor**

---

### Attachments Referenced
- Task 1 Discovery Report (AS-IS process map, gap analysis, stakeholder analysis)
- Gap Analysis table (G-001 through G-0XX)

---

## Task 2 Deliverables

### Deliverable 2A: Requirements Package

**Format:** Structured document (requirements register + detail sections)

The requirements package contains two types of requirements:

---

#### Functional Requirements (FR)

Each functional requirement follows this structure:

```
Requirement ID: FR-001
Requirement Title: [Clear, specific title]
Requirement Description: [What the system MUST do — specific, measurable, unambiguous]
Source Gap: G-00X (from Discovery Report)
Regulatory Reference: [FCA PS17/14 §X.X or MLR 2017 Reg X]
Priority: Must Have / Should Have / Could Have / Won't Have (MoSCoW)
Acceptance Criteria:
  - [AC-1] Given [context] when [action] then [expected result]
  - [AC-2] Given [context] when [action] then [expected result]
  - [AC-3] ...
Dependencies: FR-00X (list any requirements that must be delivered first or concurrently)
Constraints: [Technical constraints — platform, integration, data limitations]
Assumptions: [What we are assuming is true about the solution or the business]
```

---

#### Non-Functional Requirements (NFR)

Each NFR follows this structure:

```
NFR ID: NFR-001
NFR Title: [Performance / Security / Usability / Scalability / Compliance]
Requirement: [Specific, measurable standard the system must meet]
Measurement: [How we will verify this has been met — a test, a metric, a standard]
Regulatory Reference: [If applicable]
Priority: Must Have / Should Have / Could Have / Won't Have
```

**Required NFR categories to cover:**
- **Performance**: Response times for verification checks (max seconds)
- **Security**: Data encryption standards (in transit and at rest), access control
- **Availability**: Uptime SLA for the onboarding system
- **Compliance**: Audit log completeness, data retention periods per FCA requirements
- **Usability**: Accessibility standards (WCAG 2.1 AA), mobile compatibility

---

### Deliverable 2B: Requirements Backlog (Prioritised)

**Format:** Tabular backlog + prioritisation narrative

| Req ID | Requirement Title | Type | Priority | Estimated Effort (T-shirt) | Sprint | Dependencies |
|--------|------------------|------|----------|---------------------------|--------|--------------|
| FR-001 | Mandatory BO declaration before account activation | FR | Must Have | M | Sprint 1 | None |
| NFR-001 | Audit log retention: 5 years minimum | NFR | Must Have | S | Sprint 1 | None |
| ... | ... | ... | ... | ... | ... | ... |

**Prioritisation must follow MoSCoW:**
- **Must Have**: Non-negotiable — regulatory requirement or blocking risk (do first)
- **Should Have**: Important but can be deferred if necessary (do second)
- **Could Have**: Desirable but not critical (do if capacity allows)
- **Won't Have**: Explicitly excluded from this release (document why)

The prioritisation narrative must explain:
1. Why high-priority requirements are ranked above lower ones
2. Which requirements are blocked by others (can't build FR-B until FR-A is done)
3. Which requirements are risky (high effort, high uncertainty) and how that affects their position
4. What was deliberately deprioritised and why

---

### Deliverable 2C: Requirements Review Notes

**Format:** Annotated document

James has specifically asked Diana (Lead Engineer) to review the requirements before they go to sprint planning. The mentee produces a set of **Requirements Review Notes** — a self-review of the requirements package before it goes to Engineering.

This includes:
- A note on each requirement where the mentee is uncertain about technical feasibility
- A list of open questions for Diana that must be answered before Engineering can estimate
- A section on where AI-generated requirements were reviewed and refined (with notes on what was changed and why)
- Any conflicts or contradictions between requirements that need to be resolved

---

## AI Prompt Library: Task 2

---

### Prompt 2.1: User Story Generation from Gap

```
You are a Senior Business Analyst writing user stories for a UK fintech onboarding remediation project.

The following gap was identified in the Discovery Report:

Gap ID: G-00X
Gap Description: [paste gap description]
Regulatory Reference: [paste regulatory reference]
Current Process Step: [paste step]

Write 3 user stories for addressing this gap. Each user story must follow this format:

Story Title: [As a... I want... so that...]

Story Text:
- As a [ROLE — who is this for? Compliance, Operations, Customer, Engineer?]
- I want [specific action or capability]
- So that [business or regulatory outcome]

Acceptance Criteria (minimum 3 per story):
- Given [precondition] when [action] then [observable result]
- Given [precondition] when [action] then [observable result]
- Given [precondition] when [action] then [observable result]

For each story, also note:
- Which part of the regulatory requirement does this address?
- What could go wrong if this story is implemented incorrectly?
- What test scenario would verify this story is working correctly?
```

**Critique checklist:**
- Are the acceptance criteria actually testable? (Can you write a UAT test case from them?)
- Is the "so that" outcome a real business or regulatory benefit, or just a description of what the system does?
- Are any acceptance criteria written as process steps rather than outcomes?

---

### Prompt 2.2: NFR Generation

```
You are a Financial Services Technology Architect. Generate Non-Functional Requirements for a UK fintech's client onboarding system.

Context:
- The system handles KYC/AML data for new clients (passport, proof of address, biometric data)
- It must comply with FCA requirements, UK GDPR, and PCI-DSS (for payment data)
- It is built on Salesforce Financial Services Cloud + a custom onboarding microservice
- Integration required with: Experian identity verification API, Dow Jones risk intelligence (PEP/sanctions screening), Meridian's core banking system

Generate requirements in the following categories. For each, be specific and measurable:

1. PERFORMANCE
   - API response times for third-party verification calls
   - Maximum acceptable latency for the onboarding flow
   - Concurrent user capacity

2. SECURITY
   - Encryption standards (in transit and at rest)
   - Access control requirements (role-based access minimum)
   - Penetration testing frequency requirement
   - Data masking requirements for sensitive fields

3. AVAILABILITY
   - Uptime SLA (expressed as percentage per year)
   - Maximum acceptable downtime window (maintenance)
   - Disaster recovery RTO and RPO

4. COMPLIANCE
   - Audit log requirements (what must be logged, for how long)
   - FCA reporting capability (suspicious activity flagging)
   - Data retention periods per UK GDPR and FCA requirements

5. USABILITY
   - WCAG 2.1 AA accessibility compliance requirement
   - Mobile responsiveness requirement
   - Maximum form field completion time (FCA Consumer Duty)

6. SCALABILITY
   - Expected onboarding volume (current and projected)
   - System must scale to [X] concurrent onboarding sessions without performance degradation

For each NFR, explain why this standard is required by regulation or is necessary for safe operation.
```

**Critique checklist:**
- Are the standards cited actually applicable to Meridian's situation? (Don't suggest PCI-DSS for KYC data unless payment card data is involved)
- Are the measurements realistic for a Series B fintech with 3 engineers?
- Is the NFR actually testable — can someone verify it has been met?

---

### Prompt 2.3: Requirements Conflict Detection

```
You are a Senior Business Analyst reviewing a requirements package for a UK fintech onboarding remediation.

Review the following requirements and identify any conflicts, contradictions, or logical impossibilities between them.

Requirements:
[paste full requirements list]

For each potential conflict, identify:
1. The two requirements in conflict
2. Why they conflict (mutually exclusive, contradicting each other, logically impossible together)
3. Recommended resolution (which should take priority and why)
4. Who should make the final call on the resolution

Also flag:
- Any requirements that are dependent on external parties (third-party APIs, regulatory bodies) and have no fallback
- Any requirements that are unrealistic given the 12-week timeline and 3-engineer team
- Any requirements that appear to be implementing a solution rather than describing a need
```

**Critique checklist:**
- Is the AI correctly identifying genuine conflicts vs. things that are just complex?
- Are the resolutions sensible, or is the AI just picking one requirement arbitrarily?
- Is the AI flagging technical impossibilities that a real engineer would catch?

---

## Task 2 Completion Checklist

- [ ] All high and medium gaps from Task 1 have corresponding requirements
- [ ] Every requirement has traceable source (gap ID + regulatory reference)
- [ ] All acceptance criteria are written as outcomes (not process steps)
- [ ] All acceptance criteria are testable (UAT test can be written from them)
- [ ] MoSCoW prioritisation is consistent and justified
- [ ] Dependencies between requirements are mapped
- [ ] Open questions for Engineering are documented
- [ ] At least one NFR per category (Performance, Security, Availability, Compliance, Usability, Scalability)
- [ ] Requirements Review Notes self-review is complete
- [ ] AI-generated requirements reviewed against red lines (no hallucinated regulatory references, no vague language)

---
