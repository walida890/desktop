# TASK 4 — UAT Planning & Test Scenario Design
## Week 7–8 of the Capstone

---

## Learning Objectives

By the end of this task, the mentee will be able to:
- [ ] Design a UAT test strategy that covers all high and medium priority requirements
- [ ] Write high-quality, testable scenario outlines from acceptance criteria
- [ ] Identify cross-functional test scenarios (what spans multiple systems)
- [ ] Build a traceability matrix linking requirements → test scenarios → test cases
- [ ] Use AI to generate test case drafts, then challenge them for coverage and edge cases
- [ ] Define the defect management process (how bugs are logged, graded, and resolved)
- [ ] Plan a phased UAT approach that fits within the sprint cadence

---

## The Brief: What The Mentee Receives

---

### Meridian Financial — Email from Diana Vlasova (Lead Engineer)

**TO:** Business Analysis Team
**FROM:** Diana Vlasova, Lead Engineer
**DATE:** [Task 4 Start Date]
**RE: UAT Strategy — What Are We Actually Testing?

---

I've reviewed the requirements package and the solution design. Engineering is comfortable with the scope for Sprint 1. We're ready to start building next week.

Here's what I need from you before we can sign off on the sprint plan:

**A UAT test strategy document** that tells us:
1. What we are testing (scope — what's in and what's explicitly out)
2. How we'll know if the system is working (test scenario coverage by requirement)
3. What success looks like (exit criteria — when can we say UAT is complete?)
4. How we'll run this (phasing, environments, data requirements)

And alongside that:

**A full set of test scenario outlines** for every Sprint 1 requirement. I'm not asking for detailed test cases yet — I want outlines first so I can review coverage with the QA team. But every outline must be:
- Traceable to a specific requirement and acceptance criterion
- Clearly scoped (preconditions, inputs, expected output, pass/fail criteria)
- Written so a QA analyst could execute it without asking a BA what to do

A few things I want to flag from previous projects:
- We often miss **cross-system scenarios** — things that span Salesforce and the microservice, or that involve a third-party API response
- We often miss **failure path testing** — what happens when the API call to Experian times out, or Dow Jones returns an error
- We often miss **data validation at the boundary** — what happens when a field is the wrong type, too long, or empty

I want those explicitly called out in the test strategy.

**— Diana Vlasova**

---

### Sprint 1 Scope (from Task 3 Solution Design)

The following requirements are in scope for Sprint 1 (Must Have, estimated ≤ 10 weeks):

| Req ID | Requirement | Type | Sprint |
|--------|-------------|------|--------|
| FR-001 | Mandatory BO declaration before account activation | FR | Sprint 1 |
| FR-002 | Automated PEP/sanctions screening via Dow Jones API | FR | Sprint 1 |
| FR-003 | Identity verification evidence captured and stored | FR | Sprint 1 |
| FR-004 | Automated compliance audit log entry on every onboarding step | FR | Sprint 1 |
| FR-005 | Risk rating assigned automatically at application submission | FR | Sprint 1 |
| NFR-001 | Audit log retention: 5 years minimum | NFR | Sprint 1 |
| NFR-003 | API response time: KYC verification ≤ 30 seconds | NFR | Sprint 1 |
| NFR-005 | FCA report generation capability (monthly compliance review) | NFR | Sprint 1 |

---

## Task 4 Deliverables

### Deliverable 4A: UAT Test Strategy

**Format:** 4–6 page strategy document

The test strategy must cover:

**1. Scope of Testing**
- What is in scope (Sprint 1 requirements)
- What is explicitly out of scope (Sprint 2+ requirements, regression testing of existing flows, performance testing)
- Assumptions made about system behaviour

**2. Testing Approach**
- Types of testing to be performed:
  - **Functional testing** (does the feature work as specified?)
  - **Integration testing** (do systems communicate correctly end-to-end?)
  - **Failure handling testing** (what happens when things go wrong?)
  - **Data validation testing** (are inputs validated at the system boundary?)
  - **Exploratory testing** (what else might break that we haven't planned for?)
- Phasing: when in the sprint does each type of testing occur?

**3. Test Environments**
- How many environments (development, SIT, UAT)
- How test data is provisioned
- How to reproduce production-like scenarios in test
- Access restrictions during UAT

**4. Defect Management**
- How defects are logged (tool — e.g., Jira, Linear)
- Severity definitions (Critical / High / Medium / Low)
- Resolution time expectations per severity
- Escalation path for blocking defects
- Definition of done: what conditions must be met before a defect is closed

**5. UAT Entry and Exit Criteria**
- **Entry criteria**: What must be true before UAT begins (environment ready, test data available, build signed off by Tech Lead)
- **Exit criteria**: What must be true before UAT is signed off (all P1/P2 defects closed, all critical test scenarios passed, traceability matrix complete)

**6. Roles and Responsibilities**
- Who writes test scenarios (BA)
- Who executes them (QA / Business Users / BA)
- Who reviews and signs off (Sarah Chen / James Okafor)
- Who resolves defects (Engineering)

---

### Deliverable 4B: Test Scenario Register

**Format:** Structured table

For each Sprint 1 requirement, the mentee produces test scenario outlines:

```
Test Scenario ID: TS-FR001-001
Test Scenario Title: BO Declaration — Complete Declaration Submitted Successfully
Requirement Reference: FR-001, AC-1
Test Type: Functional

Preconditions:
- Client is logged into the onboarding portal
- Client has completed identity verification (FR-003)
- Client entity details have been entered

Test Scenario Steps:
1. Client navigates to BO declaration screen
2. System displays mandatory fields (BO name, DOB, nationality, ownership %, role)
3. Client enters all mandatory fields and submits
4. System validates all fields (format, completeness)
5. System stores BO record in onboarding microservice
6. System syncs BO record to Salesforce FSC
7. System generates compliance audit log entry
8. Account proceeds to next onboarding step

Expected Result:
- BO record is created with correct data in both microservice and Salesforce FSC
- Audit log entry is created with timestamp, user ID, and action type
- Client is presented with confirmation and proceeds to next step

Pass Criteria:
- All fields stored correctly
- Salesforce FSC sync confirmed
- Audit log entry verified
- No error messages presented to client

Failure Handling:
- If Salesforce FSC sync fails: BO record is held in microservice with retry flag; client can proceed; ops alert triggered
- If required field missing: system returns validation error before submission

Test Scenario Owner: [QA / BA]
Phase: Sprint 1 UAT
```

**For each Sprint 1 requirement, minimum 3 scenarios:**
1. Happy path (everything works as expected)
2. Alternative path (e.g., partial data, retry required)
3. Failure path (e.g., API timeout, validation error, system error)

**Additional required cross-system scenarios:**

| Scenario ID | Title | Cross-System Coverage |
|-------------|-------|----------------------|
| TS-CS-001 | PEP screening returns a true positive match | Onboarding Microservice → Dow Jones API → Salesforce FSC |
| TS-CS-002 | Experian identity verification times out | Web App → Onboarding Microservice → Experian API |
| TS-CS-003 | Salesforce FSC is unavailable during sync | Onboarding Microservice → Salesforce FSC |
| TS-CS-004 | BO declaration submitted with invalid nationality | Onboarding Microservice → BO validation rules |
| TS-CS-005 | FCA compliance report generated | Audit Log → Salesforce FSC → Report Generation |

---

### Deliverable 4C: Traceability Matrix

**Format:** Requirements-to-Test-Scenario Matrix

| Req ID | Requirement | AC Ref | Test Scenario(s) | Status |
|--------|-------------|--------|-----------------|--------|
| FR-001 | Mandatory BO declaration | AC-1 | TS-FR001-001, TS-FR001-002, TS-FR001-003 | Not Tested |
| FR-001 | BO record synced to Salesforce FSC | AC-2 | TS-FR001-001, TS-CS-003 | Not Tested |
| FR-002 | PEP screening via Dow Jones API | AC-1 | TS-FR002-001, TS-FR002-002 | Not Tested |
| NFR-001 | Audit log retention 5 years | N/A | TS-NFR001-001 | Not Tested |

The matrix must confirm:
- Every requirement has at least one test scenario mapped to it
- Every acceptance criterion has at least one test scenario mapped to it
- No test scenario exists without a traceable requirement

---

## AI Prompt Library: Task 4

---

### Prompt 4.1: Generate Test Scenario Outlines from Acceptance Criteria

```
You are a Senior QA Analyst and Business Analyst writing test scenario outlines from requirements.

For each acceptance criterion below, generate:
1. A happy path scenario (everything works correctly)
2. An alternative path scenario (normal variation — partial data, retry, edge of valid)
3. A failure path scenario (something goes wrong — invalid input, API error, system error)

Acceptance Criterion: [paste AC from requirements]

For each scenario:
- Given [precondition — what must be true before we start]
- When [action taken — the trigger]
- Then [observable result — what we expect to happen]

Also note:
- What would FAIL this test (the negative case — when should this test fail?)
- What could go WRONG mid-scenario that would produce a different result
- What data would you need to construct this test (test data requirements)

Format as a structured scenario outline (see template above). Be specific — "system returns error" is not acceptable. What type of error? HTTP 500? Validation message? Screen freeze?
```

**Critique checklist:**
- Is the AI generating scenarios for every acceptance criterion, or missing some?
- Are the failure paths actually plausible failure modes, or artificial edge cases?
- Is the AI inventing test scenarios not derivable from the acceptance criteria?
- Are the preconditions actually achievable in a test environment?

---

### Prompt 4.2: Cross-System Scenario Generation

```
You are a Solutions Architect and QA Lead reviewing a fintech onboarding system.

The following systems are involved in the Sprint 1 onboarding flow:
- Web Application (client-facing, React)
- Onboarding Microservice (Node.js, PostgreSQL)
- Salesforce FSC (account management)
- Experian Verify API (identity verification — third party)
- Dow Jones Risk Intelligence API (PEP/sanctions screening — third party)
- Audit Log database (PostgreSQL, separate schema)

For each of the following failure scenarios, describe:
1. What the failure is
2. How each system in the chain would detect or be affected by the failure
3. What the expected system behaviour is (does it fail gracefully? retry? alert?)
4. How a test scenario would validate this failure handling
5. What test data would be required to simulate this failure

Failure Scenarios:
A. Experian API returns HTTP 503 (service unavailable) during identity verification
B. Dow Jones API returns a PEP match (true positive) for a client's director
C. Salesforce FSC is unreachable during a BO record sync operation
D. The audit log database connection times out mid-transaction
E. Client submits a BO declaration where the nationality field contains a SQL injection attempt
F. The FCA monthly compliance report is generated but contains zero records (data missing)

For each scenario: write a test scenario outline including failure path, expected system response, and pass/fail criteria.
```

**Critique checklist:**
- Is the AI correctly identifying which system is responsible for error handling at each step?
- Is the AI describing realistic retry/fallback behaviour, or just "show error to user"?
- Is the AI flagging security test scenarios (injection attacks) as a separate concern?
- Are the test data requirements realistic to construct in a non-production environment?

---

### Prompt 4.3: Edge Case Discovery

```
You are a Senior Business Analyst reviewing a set of test scenario outlines for a KYC/AML onboarding system.

Review the following test scenario outlines and identify:
1. Edge cases that are NOT covered (things that could go wrong that the scenarios don't test)
2. Assumptions hidden in the preconditions (things the scenarios assume are true but may not be)
3. Data validation gaps (what happens with unexpected data types, lengths, encodings?)
4. Concurrency scenarios (what happens if two users submit simultaneously, or if a session times out mid-submission?)
5. Regulatory edge cases (what happens when borderline cases trigger regulatory thresholds?)

Existing scenarios:
[paste scenario outlines]

Respond with a structured list of gaps, each including:
- Gap description
- Why this matters (risk or regulatory implication)
- Recommended additional scenario ID and title
- Suggested test data to construct the scenario
```

**Critique checklist:**
- Is the AI identifying genuinely risky edge cases, or obvious ones that should already be covered?
- Are the concurrency scenarios plausible for this architecture?
- Is the AI conflating edge cases with failure scenarios? (Edge cases can still produce correct results)

---

## Task 4 Completion Checklist

- [ ] UAT Test Strategy document is complete and signed off by Diana
- [ ] All Sprint 1 requirements have ≥3 test scenario outlines each
- [ ] All cross-system failure scenarios are documented
- [ ] Traceability matrix confirms 100% coverage of requirements → scenarios
- [ ] No scenario exists without a traceable requirement
- [ ] Defect severity definitions are agreed with QA and Engineering
- [ ] UAT entry and exit criteria are agreed with James and Diana
- [ ] Test data requirements are documented for all scenarios
- [ ] AI-generated test scenarios reviewed — all failure paths are plausible, no invented acceptance criteria

---
