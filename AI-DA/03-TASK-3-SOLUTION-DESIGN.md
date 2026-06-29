# TASK 3 — Solution Design & Integration Gap Analysis
## Week 5–6 of the Capstone

---

## Learning Objectives

By the end of this task, the mentee will be able to:
- [ ] Assess the feasibility of proposed requirements against the current technical environment
- [ ] Conduct a gap analysis between requirements and current system capabilities
- [ ] Map data flows between systems and identify required integrations
- [ ] Produce a solution options assessment (build vs. buy vs. configure)
- [ ] Identify data model gaps (what data we need to capture that we don't currently)
- [ ] Use AI to research vendor solutions and compare options
- [ ] Produce a system context diagram and integration overview

---

## The Brief: What The Mentee Receives

---

### Meridian Financial — Email from James Okafor (Product Manager)

**TO:** Business Analysis Team
**FROM:** James Okafor, Product Manager
**DATE:** [Task 3 Start Date]
**RE: Technical Feasibility — What Are We Actually Building?

---

The requirements package has been reviewed by Diana and the engineering team. We've had a rough estimation session and we have some bad news:

1. **Not all requirements can be delivered in 10 weeks with 3 engineers.** We need to make hard choices.
2. **Diana has flagged that the current Salesforce FSC configuration cannot support some of the new requirements without significant customisation** — this will blow our timeline.
3. **We need to decide whether to extend Salesforce FSC, build a new onboarding microservice, or integrate a third-party KYC/AML platform.**

I need you to do a technical feasibility assessment. Specifically:

1. **Map each high-priority requirement to the system(s) that must implement it**
2. **Assess the gap between what we need and what our current systems can do**
3. **Research and compare 2–3 solution options for the biggest gaps (KYC verification, PEP/sanctions screening, BO declaration)**
4. **Assess data flow — what data needs to move between systems, and is our current integration architecture capable?**
5. **Recommend a solution approach — build, buy, or configure — with rationale**

Diana's team will review your technical assessment. Priya (Legal) will need to sign off on any third-party compliance tooling.

**Deadline: End of Week 6**

**— James Okafor**

---

### Current System Landscape (Reference Data from Discovery)

```
┌─────────────────────────────────────────────────────────────┐
│                   MERIDIAN FINANCIAL                         │
│                  SYSTEM LANDSCAPE                            │
└─────────────────────────────────────────────────────────────┘

  CLIENT SIDE              MERIDIAN SYSTEMS                EXTERNAL
  ───────────              ─────────────────                ────────
                                                             
  Web Application    ←→   API Gateway                      ────────
                           │                                    
                      ┌────┴─────┐                           
                      │          │                           
              Salesforce FSC   Custom Onboarding             
              (Account Mgmt)   Microservice                  


  Email System       ←→   Gmail / Google Workspace          ────────
                                                             
                      ┌──────────────────────────────────┐   
                      │         Core Banking System      │   
                      │    (Account ledger, payments)    │   
                      └──────────────────────────────────┘   
                                                             
                                                    ↕         
                                              ┌─────────────┐ 
                                              │  Experian   │ ← Identity
                                              │  Verify API │   Verification
                                              └─────────────┘ 
                                              ┌─────────────┐ 
                                              │  Dow Jones  │ ← PEP/Sanctions
                                              │  Risk Intel │   Screening
                                              └─────────────┘ 
                                              ┌─────────────┐ 
                                              │  Companies  │ ← BO Verification
                                              │    House    │   (UK)
                                              └─────────────┘ 

```

**Known system limitations discovered in Task 1:**
- Salesforce FSC does not have a native beneficial ownership data model
- Current onboarding microservice has no BO declaration form — it's a manual email process
- PEP/sanctions screening is currently manual (Diana's team runs Dow Jones queries by hand)
- No automated audit trail — compliance team exports Salesforce reports manually for FCA reviews
- Current KYC process relies on customer-submitted documents uploaded to Google Drive (not a compliance-grade storage system)

---

## Task 3 Deliverables

### Deliverable 3A: Requirements-to-Systems Mapping

**Format:** Requirements traceability matrix (table)

For each high and medium priority requirement from Task 2, the mentee maps:

| Req ID | Requirement | Primary System | Supporting Systems | Data Inputs Required | Data Outputs Produced | Implementation Approach |
|--------|-------------|---------------|------------------|---------------------|----------------------|----------------------|
| FR-001 | Mandatory BO declaration | Custom Microservice | Salesforce FSC, Companies House API | Client entity details, BO individual details | BO record, compliance flag | Build |
| ... | ... | ... | ... | ... | ... | ... |

The implementation approach column must note: **Build / Configure / Buy / Integrate**

---

### Deliverable 3B: Integration Gap Analysis

**Format:** Structured gap table + data flow diagram (visual)

For each new or changed integration required:

| Gap ID | Integration | Current State | Required State | Gap Description | Integration Risk (H/M/L) |
|--------|------------|--------------|----------------|-----------------|------------------------|
| IG-001 | BO Declaration → Companies House | Manual lookup by email | Automated API call | No API integration exists; currently manual | High — 3rd party dependency |
| IG-002 | Salesforce FSC ↔ Onboarding Microservice | Basic account sync | Bidirectional data sync | Microservice not designed for real-time sync; requires redesign | Medium |
| IG-003 | Audit log → FCA reporting | Manual CSV export | Automated report generation | No automated reporting exists | High — regulatory risk |
| ... | ... | ... | ... | ... | ... |

**Data Flow Diagram Requirements:**
Produce a **level 1 system context diagram** and a **level 2 data flow** for the highest-risk integrations showing:
- All systems in scope
- Data flows between systems (what data, in which direction)
- Data transformation points (where data is validated, enriched, or filtered)
- Failure modes (what happens if an integration fails — is there a manual fallback?)

---

### Deliverable 3C: Solution Options Assessment

**Format:** Options comparison table + recommendation

For the three largest technical gaps, the mentee produces a structured options assessment:

**Gap 1: Beneficial Ownership Verification**
| | Option A: Build In-House | Option B: Companies House API Integration | Option C: Third-Party BO Platform (e.g., Enumacloud, Kyckr) |
|---|---|---|---|
| Description | Custom form + manual Companies House lookup | Automated API call to Companies House | Integrate a specialist BO verification platform |
| Estimated Effort | High (6–8 weeks) | Medium (2–3 weeks) | Low (1–2 weeks + vendor setup) |
| Cost | High (engineering time) | Low (API costs only) | Medium (subscription + API costs) |
| Compliance Risk | Low (full control) | Medium (depends on API coverage) | Low (vendor specialises in this) |
| Speed to Market | Slow | Fast | Fastest |
| Recommendation | ❌ | ✅ | ⚠️ (evaluate vendors) |

**Each options assessment must include:**
1. **Description**: What this option actually involves
2. **Pros and cons**: Technical, commercial, and compliance perspectives
3. **Estimated effort and cost**: Order of magnitude (T-shirt sizing is fine)
4. **Risk**: What could go wrong with this approach
5. **Recommendation**: Buy / Build / Configure / Reject — with clear rationale

**Final recommendation** must address:
- Which option is recommended for each gap
- Which options should be excluded and why
- What the phased approach should look like (what we do in Sprint 1 vs. later sprints)
- Any vendor names that should be evaluated (with caveats — mentee must verify vendor claims independently)

---

### Deliverable 3D: Data Model Gap Analysis

**Format:** Entity-relationship sketch (text-based or visual) + gap list

For the new data entities required by the requirements:

| Data Entity | Description | Fields Required | Source System | Target System | Gap |
|-------------|------------|----------------|--------------|--------------|-----|
| BeneficialOwner | Individual who owns or controls >25% of client entity | Name, DOB, Nationality, Address, Ownership %, Role | Client / Companies House | Onboarding Microservice → Salesforce FSC | Entity does not exist in current data model |
| ComplianceAudit | Record of compliance check performed | Check date, Check type, Result, Officer, Flag | All systems | Central Audit Repository | No central audit store;碎片 scattered across systems |
| RiskRating | Client risk score assigned at onboarding | Score, Rating basis, Review date, Officer | Onboarding Microservice | Salesforce FSC | No automated risk scoring; manual process |

For each gap:
- What data currently exists (even if unstructured)
- What the new data model must capture
- What happens to data that can't currently be captured (temporary workaround?)

---

## AI Prompt Library: Task 3

---

### Prompt 3.1: Vendor Research for Compliance Tooling

```
You are a Market Intelligence Analyst specialising in UK financial services compliance technology.

Research and compare three categories of third-party compliance tooling suitable for a UK fintech (open banking, SME payroll) that needs to remediate KYC/AML onboarding gaps.

Categories to research:
1. Automated KYC/Identity Verification platforms (e.g., Onfido, Jumio, Veriff, iDenfy)
2. Beneficial Ownership verification platforms (e.g., Kyckr, Enumacloud, Companies House API)
3. PEP/Sanctions screening platforms (note: Dow Jones is already in use — what are alternatives?)

For each category:
- Compare 3 platforms (pricing model, FCA compliance history, UK market presence, integration complexity)
- Identify key questions Meridian should ask any vendor before contracting
- Flag any regulatory considerations (FCA authorisation status, data processing agreements, offshore data considerations)
- Identify realistic timelines from contract signature to production integration

Format as a structured comparison table. Note: do not invent specific pricing — provide ranges based on market knowledge. Flag where specific information would need to be confirmed directly with the vendor.

Warning: Only include vendors you are confident exist. If you are uncertain about a vendor's FCA compliance status, say so explicitly.
```

**Critique checklist:**
- Is the AI recommending vendors that actually exist and serve the UK market?
- Are the pricing estimates realistic for a Series B fintech, or enterprise-grade pricing quoted as SME pricing?
- Is the AI flagging FCA-specific considerations or just general compliance?
- Are the integration timelines realistic, or is the AI underestimating vendor onboarding?

---

### Prompt 3.2: Integration Risk Assessment

```
You are a Solutions Architect reviewing the integration complexity for a UK fintech onboarding remediation project.

Current landscape:
- Salesforce Financial Services Cloud (primary account management)
- Custom onboarding microservice (Node.js, PostgreSQL) — built 3 years ago, limited documentation
- Experian Verify API (identity verification — already integrated)
- Dow Jones Risk Intelligence (PEP/sanctions — already integrated, currently manual)
- Core banking system (proprietary, maintained by third-party vendor)
- Google Drive (document storage — NOT a compliance-grade system)

Proposed new requirements:
[List high-priority requirements from Task 2]

Integration dependencies:
- Salesforce FSC ↔ Onboarding Microservice (bidirectional sync needed)
- Onboarding Microservice → Companies House API (new integration)
- Onboarding Microservice → Third-party BO platform (new integration)
- Audit log → Salesforce FSC (data migration and ongoing sync)

Assess:
1. Which integrations are highest risk (complexity, third-party dependency, timeline)?
2. What are the likely technical challenges with the Salesforce FSC ↔ Microservice sync? (Given the microservice was not designed for this)
3. What data transformation layer is needed between systems?
4. What happens if the Companies House API or third-party BO platform is unavailable — what is the manual fallback?
5. What security considerations exist for the new integrations (API keys, data residency, penetration testing)?
6. What integration testing approach would be required to validate these work correctly?

Be specific and technical. Flag anything that would require significant redesign or that poses a risk to the 10-week timeline.
```

**Critique checklist:**
- Is the AI being realistic about the complexity of syncing a legacy microservice with Salesforce FSC?
- Is the AI suggesting adequate fallback procedures, or just saying "have a manual process"?
- Is the AI considering data transformation requirements (e.g., field mapping between systems)?
- Is the AI flagging API rate limits or third-party uptime risks that could affect the delivery?

---

## Task 3 Completion Checklist

- [ ] All high and medium priority requirements mapped to systems
- [ ] All new integrations identified and gap-assessed
- [ ] Solution options produced for top 3 technical gaps
- [ ] Recommendation made with clear rationale for each option
- [ ] Data model gaps identified for all new data entities
- [ ] System context diagram produced
- [ ] Integration risks rated and documented
- [ ] Fallback procedures identified for all third-party dependencies
- [ ] Vendor recommendations are real and verifiable
- [ ] AI-generated content reviewed — no hallucinated vendor names or capabilities

---
