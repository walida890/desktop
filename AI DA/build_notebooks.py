"""
Build script for Task 1 notebook
"""
import nbformat as nbf

nb = nbf.v4.new_notebook()
nb.metadata = {
    "kernelspec": {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3"
    },
    "language_info": {
        "name": "python",
        "version": "3.10.0"
    }
}

cells = []

# ─── TITLE CELL ───────────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""# Task 1 — Discovery & AS-IS Process Analysis
## AI-Augmented Business Analyst Capstone
**Company:** Meridian Financial | **Scenario:** FCA KYC/AML Onboarding Remediation

---

## Overview

In this task you will conduct a full discovery exercise for Meridian Financial — a UK FCA-regulated fintech that has received a regulatory notice from the FCA regarding gaps in its client onboarding KYC/AML process.

By the end of this notebook you will have produced:
1. A **Stakeholder Register & Analysis** (power/interest grid)
2. An **AS-IS Process Map** (onboarding flow)
3. A **Regulatory Gap Analysis** (against FCA PS17/14 and MLR 2017)
4. A **Discovery Summary Report** (executive-facing)

## AI Tools Used in This Task

| BA Activity | AI Tool | Prompt |
|-------------|---------|--------|
| Interview preparation | ChatGPT / Claude | Prompt 1.1 — Stakeholder questions |
| Process structuring | ChatGPT / Claude | Prompt 1.2 — Process step formatting |
| Gap identification | ChatGPT / Claude | Prompt 1.3 — Regulatory gap analysis |
| Severity assessment | ChatGPT / Claude | Prompt 1.4 — Risk rating |

> **Note:** For this notebook we provide the AI prompts inline. In your actual mentorship programme, you will use these prompts with your AI tool and paste the outputs into the relevant cells.

---
"""))

# ─── SECTION 1: SETUP ──────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""## 1. Setup & Environment

Run the cell below to import the libraries needed for this notebook.
"""))

cells.append(nbf.v4.new_code_cell("""# Core data & analysis libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import os
import json
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Text processing
import re
from collections import defaultdict

# Visualisation
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

# Output directory
os.makedirs('../outputs', exist_ok=True)

print("✓ Environment ready")
print(f"  Working directory: {os.getcwd()}")
"""))

# ─── SECTION 2: STAKEHOLDER REGISTER ──────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""## 2. Stakeholder Register & Analysis

### Your Task

You have been sent the internal memo from Sarah Chen (Head of Compliance). Your first job is to identify all the stakeholders involved in the Meridian onboarding process — both those mentioned in the memo and any that are **missing but relevant**.

Use **Prompt 1.1** from the AI Prompt Library to generate probing interview questions. Based on the memo and your own knowledge of a fintech onboarding process, build your initial stakeholder register.

> **Activity:** Complete the `stakeholders` DataFrame below. Add as many rows as you identify.
"""))

cells.append(nbf.v4.new_code_cell("""# ─────────────────────────────────────────────────────────────────────────────
# COMPLETE THIS TABLE
# Add rows for every stakeholder you can identify (minimum 8 required)
# Columns: name, role, department, influence, interest, communication_approach
# influence: High / Medium / Low
# interest: High / Medium / Low
# ─────────────────────────────────────────────────────────────────────────────

stakeholders_data = {
    'name': [
        'Sarah Chen',       # ← EXAMPLE — replace / build on this
        # TODO: Add more stakeholders below
        '',
        '',
        '',
        '',
        '',
        '',
        '',
    ],
    'role': [
        'Head of Compliance',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
    ],
    'department': [
        'Compliance',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
    ],
    'influence': [
        'High',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
    ],
    'interest': [
        'High',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
    ],
    'communication_approach': [
        'Formal meeting / written report',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
    ],
    'key_concerns': [
        'FCA regulatory deadline, audit trail completeness',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
    ]
}

df_stakeholders = pd.DataFrame(stakeholders_data)
print(f"Stakeholders registered: {len(df_stakeholders)}")
df_stakeholders
"""))

# ─── POWER/INTEREST GRID ────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""### 2.1 Power/Interest Grid

Plot your stakeholders on the power/interest grid. Each stakeholder should be labelled with their name.
"""))

cells.append(nbf.v4.new_code_cell("""# Map influence (x) and interest (y) to numeric values for plotting
influence_map = {'Low': 1, 'Medium': 2, 'High': 3}
interest_map = {'Low': 1, 'Medium': 2, 'High': 3}

fig, ax = plt.subplots(figsize=(10, 8))

# Plot each stakeholder
for _, row in df_stakeholders.iterrows():
    x = influence_map.get(row['influence'], 2)
    y = interest_map.get(row['interest'], 2)
    ax.scatter(x, y, s=300, zorder=3)
    ax.annotate(row['name'], (x, y), textcoords="offset points",
                xytext=(8, 8), fontsize=9, fontweight='bold')

# Zone labels
ax.axhline(y=2, color='gray', linestyle='--', alpha=0.4)
ax.axvline(x=2, color='gray', linestyle='--', alpha=0.4)
ax.set_xlim(0.5, 3.5)
ax.set_ylim(0.5, 3.5)
ax.set_xticks([1, 2, 3])
ax.set_yticks([1, 2, 3])
ax.set_xticklabels(['Low Power', 'Medium Power', 'High Power'])
ax.set_yticklabels(['Low Interest', 'Medium Interest', 'High Interest'])
ax.set_xlabel('Power / Influence', fontsize=12)
ax.set_ylabel('Interest in Project', fontsize=12)
ax.set_title('Meridian Financial — Stakeholder Power/Interest Grid', fontsize=14, fontweight='bold')

# Zone annotations
ax.text(1.5, 3.3, 'KEEP SATISFIED', ha='center', fontsize=9, color='darkblue', style='italic')
ax.text(2.5, 3.3, 'KEY PLAYERS — ENGAGE CLOSELY', ha='center', fontsize=9, color='darkred', fontweight='bold')
ax.text(1.5, 1.5, 'MONITOR', ha='center', fontsize=9, color='gray', style='italic')
ax.text(2.5, 1.5, 'KEEP INFORMED', ha='center', fontsize=9, color='darkgreen', style='italic')

plt.tight_layout()
plt.savefig('../outputs/stakeholder_grid.png', dpi=150, bbox_inches='tight')
plt.show()
print("✓ Grid saved to ../outputs/stakeholder_grid.png")
"""))

# ─── SECTION 3: AS-IS PROCESS MAP ─────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""## 3. AS-IS Process Map

### 3.1 The Onboarding Flow

Based on the Discovery interviews you conducted (or the simulated interview summaries below), document the current onboarding process.

Use **Prompt 1.2** to convert rough notes into structured process steps.

> **Context:** The current onboarding process runs as follows (from Discovery interviews):
> - Tom Bradley (Head of Ops) described the flow as: inbound inquiry → sales screening → account application form → manual ID check → compliance review → account setup → first payment
> - James Okafor (Product) noted the current form is a web form on the Meridian website feeding into Salesforce
> - Diana Vlasova (Engineering) confirmed the onboarding microservice was built 3 years ago and is not well documented
> - Priya Sharma (Legal) said compliance sign-off is currently a manual email chain
> - No automated PEP/sanctions check is in the flow — Diana's team runs Dow Jones manually

Complete the process steps table below with all the steps you can identify.
"""))

cells.append(nbf.v4.new_code_cell("""# ─────────────────────────────────────────────────────────────────────────────
# COMPLETE THE AS-IS PROCESS MAP
# Add all steps from Lead to First Transaction
# Columns: step_no, step_name, owner_role, systems, inputs, outputs, decision_gate, pain_point
# decision_gate: Yes/No — if Yes, describe the conditions in pain_point
# ─────────────────────────────────────────────────────────────────────────────

process_steps = {
    'step_no': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'step_name': [
        'Inbound Inquiry',
        'Sales Screening',
        'Account Application',
        'ID Document Collection',
        'Identity Verification',
        'Compliance Review',
        'Risk Rating Assignment',
        'Account Setup',
        'First Transaction'
    ],
    'owner_role': [
        'Sales',
        'Sales',
        'Product / Operations',
        'Operations',
        'Operations',
        'Compliance',
        'Compliance',
        'Operations / Engineering',
        'Operations'
    ],
    'systems': [
        'Website / CRM',
        'Email / CRM',
        'Web Form → Salesforce FSC',
        'Email / Google Drive',
        'Manual (no system)',
        'Email (manual)',
        'Manual (spreadsheet)',
        'Salesforce FSC / Onboarding Microservice',
        'Core Banking System'
    ],
    'inputs': [
        'Inbound enquiry (website / referral)',
        'Client basic info (company name, contact)',
        'Completed application form',
        'Client-submitted documents (passport, proof of address)',
        'ID documents',
        'Client entity details, ID verification result',
        'Application data, compliance notes',
        'Approved application, compliance clearance',
        'Activated account'
    ],
    'outputs': [
        'Qualified lead',
        'Screened lead (passed/failed initial criteria)',
        'Submitted application',
        'Documents stored in Google Drive',
        'Verification result (pass/fail/manual review)',
        'Compliance clearance (or rejection)',
        'Client risk rating (Low/Medium/High)',
        'Active account in Salesforce FSC + core banking',
        'First successful payment'
    ],
    'decision_gate': [
        'Yes — Does lead meet minimum criteria?',
        'Yes — Does client pass sales screening?',
        'No',
        'No',
        'Yes — Does ID verification pass?',
        'Yes — Does compliance approve?',
        'No',
        'No',
        'No'
    ],
    'pain_point': [
        'No structured qualification process',
        'Inconsistent screening criteria across sales team',
        'Form does not capture beneficial ownership information',
        'Documents stored in Google Drive — not compliance-grade storage',
        'Manual process; no automated check; no audit trail',
        'Manual email chain; no structured sign-off; no documented rationale',
        'Risk rating assigned in a spreadsheet; not linked to client record',
        'Salesforce sync relies on manual data entry by Operations',
        'No proactive monitoring after first transaction'
    ]
}

df_process = pd.DataFrame(process_steps)
print(f"Process steps documented: {len(df_process)}")
df_process[['step_no','step_name','owner_role','decision_gate']]
"""))

# ─── PROCESS MAP VISUALISATION ─────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""### 3.2 Process Map Visualization

The cell below generates a visual flow diagram of the onboarding process.
"""))

cells.append(nbf.v4.new_code_cell("""import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(18, 14))
ax.set_xlim(0, 18)
ax.set_ylim(0, 14)
ax.axis('off')
ax.set_title('Meridian Financial — AS-IS Onboarding Process Map', fontsize=16, fontweight='bold', pad=20)

# Color scheme
step_color = '#E3F2FD'        # Normal step
decision_color = '#FFF9C4'    # Decision gate
pain_color = '#FFCDD2'        # Pain point
system_color = '#E8F5E9'      # System/tech

# Draw steps
step_height = 1.2
step_width = 2.8
y_positions = [11, 9, 7, 5, 3]
x_positions = [3, 7, 11, 15, 7]  # x positions for 9 steps (adjusting layout)

step_positions = {
    1: (2, 11), 2: (6, 11), 3: (10, 11),
    4: (14, 11), 5: (14, 7), 6: (14, 3),
    7: (10, 3), 8: (6, 3), 9: (2, 3)
}

step_boxes = {}

for i, row in df_process.iterrows():
    x, y = step_positions[row['step_no']]
    color = decision_color if row['decision_gate'].startswith('Yes') else step_color
    if row['pain_point'] and row['pain_point'] != 'No':
        color = pain_color

    box = FancyBboxPatch((x - step_width/2, y - step_height/2), step_width, step_height,
                          boxstyle="round,pad=0.1", facecolor=color,
                          edgecolor='#333', linewidth=1.5)
    ax.add_patch(box)

    step_boxes[row['step_no']] = (x, y)
    ax.text(x, y + 0.3, f"Step {row['step_no']}", ha='center', fontsize=7,
            color='#666', fontstyle='italic')
    ax.text(x, y - 0.1, row['step_name'], ha='center', fontsize=9,
            fontweight='bold', wrap=True)
    ax.text(x, y - 0.65, row['owner_role'], ha='center', fontsize=7, color='#555')

    if row['pain_point'] and row['pain_point'] != 'No':
        ax.text(x, y - 1.1, f"⚠ {row['pain_point'][:50]}..." if len(row['pain_point']) > 50 else f"⚠ {row['pain_point']}",
                ha='center', fontsize=6.5, color='#C62828',
                bbox=dict(boxstyle='round', facecolor='#FFEBEE', edgecolor='#EF9A9A'))

# Draw arrows
arrow_props = dict(arrowstyle='->', color='#333', lw=1.5)
# Main flow: 1→2→3→4, then down to 5→6, then left to 7→8→9
connections = [(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9)]
for src, dst in connections:
    x1, y1 = step_positions[src]
    x2, y2 = step_positions[dst]
    ax.annotate('', xy=(x2, y2 + step_height/2),
                xytext=(x1, y1 - step_height/2),
                arrowprops=dict(arrowstyle='->', color='#333', lw=1.5))

# Legend
legend_elements = [
    mpatches.Patch(facecolor=step_color, edgecolor='#333', label='Process Step'),
    mpatches.Patch(facecolor=decision_color, edgecolor='#333', label='Decision Gate'),
    mpatches.Patch(facecolor=pain_color, edgecolor='#333', label='Known Pain Point'),
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=9)

plt.tight_layout()
plt.savefig('../outputs/as_is_process_map.png', dpi=150, bbox_inches='tight')
plt.show()
print("✓ Process map saved to ../outputs/as_is_process_map.png")
"""))

# ─── SECTION 4: GAP ANALYSIS ──────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""## 4. Regulatory Gap Analysis

### 4.1 Regulatory Framework

The FCA has flagged gaps in Meridian's onboarding process. The key regulatory instruments are:

| Regulation | What It Requires |
|-----------|----------------|
| **FCA PS17/14** | Systems and controls for AML — customer due diligence must be adequate |
| **FCA MLR 2017, Reg 28** | Beneficial ownership information must be collected for legal entities |
| **FCA MLR 2017, Reg 35** | Politically Exposed Persons (PEPs) must be identified and screened |
| **FCA Consumer Duty (FG22/5)** | Fair customer outcomes in new customer onboarding |
| **JMLSG Guidance Ch.5** | Industry guidance on onboarding CDD procedures |

### 4.2 Gap Identification

Use **Prompt 1.3** (inline below) to identify regulatory gaps. Review the AI output critically before accepting it.

> **Activity:** Run the cell below to generate a draft gap analysis. Then review and update the `df_gaps` table with your own findings.
"""))

cells.append(nbf.v4.new_code_cell("""# ─────────────────────────────────────────────────────────────────────────────
# GAP ANALYSIS — Complete from your discovery evidence
# Each gap must map to a process step (1-9) and a regulatory reference
# Severity: High / Medium / Low
# ─────────────────────────────────────────────────────────────────────────────

gaps_data = {
    'gap_id': ['G-001', 'G-002', 'G-003', 'G-004', 'G-005', 'G-006', 'G-007'],
    'gap_name': [
        'No non-documentary identity verification',
        'Beneficial ownership not collected',
        'PEP screening not automated',
        'No automated audit trail',
        'No client risk rating at onboarding',
        'Documents stored in Google Drive',
        'No sanctions screening step'
    ],
    'process_step': [5, 3, 5, 'ALL', 7, 4, 5],
    'regulatory_reference': [
        'FCA PS17/14 §4.2 (CDD adequacy)',
        'FCA MLR 2017 Reg 28 (BO information)',
        'FCA MLR 2017 Reg 35 (PEP screening)',
        'FCA PS17/14 §6 (audit trail)',
        'FCA PS17/14 §4 (risk assessment)',
        'FCA PS17/14 §5 (record keeping)',
        'FCA MLR 2017 Reg 35 (sanctions)'
    ],
    'gap_description': [
        'Current process relies solely on client-submitted documents with no independent verification call (e.g., Experian). FCA requires both documentary and non-documentary checks.',
        'The account application form does not include a beneficial ownership declaration. Staff do not collect BO data. Reg 28 requires collection for all legal entities.',
        'PEP screening is run manually by Diana\'s team in Dow Jones. No automated trigger exists. Screening is dependent on someone remembering to run it.',
        'There is no central audit log. Compliance sign-offs are via email. The compliance team exports Salesforce reports manually for FCA reviews — this is not a compliant audit trail.',
        'Client risk rating is assigned retrospectively in a spreadsheet after account opening. No risk scoring exists at the point of application.',
        'Client identity documents are uploaded to Google Drive. Google Drive is not a compliance-grade document storage system. Documents must be held in a system with appropriate access controls and retention policies.',
        'Sanctions screening is not performed as a distinct step. The manual PEP check in Dow Jones does not cover all sanctions list requirements.'
    ],
    'severity': ['High', 'High', 'High', 'High', 'Medium', 'High', 'High'],
    'business_risk': [
        'Regulatory enforcement — FCA can take action for inadequate CDD',
        'Regulatory enforcement — Reg 28 breach; criminal liability for Meridian',
        'PEP client could slip through without screening — reputational and legal risk',
        'FCA review would find inadequate records — enforcement action likely',
        'High-risk clients onboarded without elevated due diligence — AML breach risk',
        'FCA would criticise document storage as inadequate — potential fine',
        'Sanctions breach — criminal liability under UK sanctions regulations'
    ],
    'evidence_source': [
        'Diana Vlasova interview: "ID verification is done by email"',
        'Tom Bradley interview: "We don\'t ask about ownership structure"',
        'Diana Vlasova interview: "I run Dow Jones by hand when I remember"',
        'Priya Sharma interview: "Compliance sign-off is just an email chain"',
        'James Okafor interview: "Risk rating is done in a spreadsheet after"',
        'Tom Bradley interview: "Documents go into a shared Drive folder"',
        'Priya Sharma interview: "We don\'t have a separate sanctions check"'
    ]
}

df_gaps = pd.DataFrame(gaps_data)
print(f"Regulatory gaps identified: {len(df_gaps)}")
df_gaps[['gap_id','gap_name','severity','regulatory_reference']]
"""))

# ─── GAP SEVERITY CHART ────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""### 4.3 Gap Severity Visualization
"""))

cells.append(nbf.v4.new_code_cell("""severity_order = ['High', 'Medium', 'Low']
gap_counts = df_gaps['severity'].value_counts().reindex(severity_order, fill_value=0)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Bar chart
colors = {'High': '#C62828', 'Medium': '#EF6C00', 'Low': '#2E7D32'}
bar_colors = [colors[s] for s in severity_order]
axes[0].bar(severity_order, gap_counts.values, color=bar_colors, edgecolor='#333')
axes[0].set_title('Gaps by Severity', fontsize=13, fontweight='bold')
axes[0].set_xlabel('Severity')
axes[0].set_ylabel('Number of Gaps')
for i, v in enumerate(gap_counts.values):
    axes[0].text(i, v + 0.1, str(v), ha='center', fontweight='bold', fontsize=12)

# Gaps by process step
df_gaps['step_label'] = df_gaps['process_step'].astype(str)
step_gaps = df_gaps.groupby('step_label').size()
axes[1].barh(step_gaps.index, step_gaps.values, color='#1565C0', edgecolor='#333')
axes[1].set_title('Gaps by Process Step', fontsize=13, fontweight='bold')
axes[1].set_xlabel('Number of Gaps')
axes[1].set_ylabel('Process Step')

plt.suptitle('Meridian Financial — Regulatory Gap Analysis Summary', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('../outputs/gap_analysis_summary.png', dpi=150, bbox_inches='tight')
plt.show()
print("✓ Gap analysis chart saved to ../outputs/gap_analysis_summary.png")
"""))

# ─── SECTION 5: DISCOVERY REPORT ──────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""## 5. Discovery Summary Report

### 5.1 Export Your Gap Analysis

The cell below exports your completed gap analysis to a CSV file for use in Task 2.
"""))

cells.append(nbf.v4.new_code_cell("""# Export deliverables
df_stakeholders.to_csv('../outputs/stakeholder_register.csv', index=False)
df_process.to_csv('../outputs/as_is_process_map.csv', index=False)
df_gaps.to_csv('../outputs/regulatory_gap_analysis.csv', index=False)

print("✓ Exported to ../outputs/:")
for f in ['stakeholder_register.csv', 'as_is_process_map.csv', 'regulatory_gap_analysis.csv']:
    print(f"  — {f}")
print()
print("These files will be used as inputs for Task 2: Requirements Engineering.")
"""))

# ─── SECTION 6: AI PROMPTS ────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""## 6. AI Prompt Library — Task 1

Use these prompts with your AI tool. Copy the prompt text, paste it into ChatGPT or Claude, then paste the output back into the relevant cells above.

---

### Prompt 1.1: Interview Question Generation

```
You are a Senior Business Analyst preparing interview questions for a discovery session.

Context:
- We are investigating the current new client onboarding process at a UK fintech (open banking payments)
- The FCA has flagged gaps in KYC/AML compliance
- The interviewee is [ROLE — e.g., Head of Operations]
- Their perspective is [their role in the onboarding process]

Generate 12 probing questions for this interview:
- 4 questions about the process (what happens, when, by whom)
- 3 questions about pain points and known failures
- 3 questions about regulatory concerns
- 2 questions that challenge assumptions ("why do you do it this way?")

For each question, note what you expect to learn.
```

---

### Prompt 1.3: Regulatory Gap Identification

```
You are a Financial Services Compliance Analyst. A UK fintech has received an FCA notice about KYC/AML gaps.

Current AS-IS process steps:
[paste process steps from df_process above]

FCA requirements that apply:
- FCA PS17/14: AML systems and controls
- FCA MLR 2017 Reg 28: Beneficial ownership
- FCA MLR 2017 Reg 35: PEPs and sanctions
- JMLSG Guidance Chapter 5: Onboarding CDD

For each requirement, identify: which process step it maps to, the gap, evidence, and severity.
```

---

### Prompt 1.4: Gap Severity Assessment

```
Review the following gaps and for each provide:
1. Regulatory consequence (what FCA could do)
2. Business consequence (what could go wrong operationally)
3. Likelihood (how likely is actual harm)
4. Overall risk rating (Critical/High/Medium/Low)
5. Immediate action (next 2 weeks)

Gaps: [paste df_gaps]
```
"""))

# Assign cells to notebook
nb.cells = cells

# Write to file
output_path = '/opt/data/capstone/notebooks/Task_1_Discovery_ASIS_Analysis.ipynb'
with open(output_path, 'w') as f:
    nbf.write(nb, f)

print(f"✓ Notebook written to {output_path}")
