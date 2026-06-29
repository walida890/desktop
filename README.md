# Meridian Financial Capstone

**British Airways / Coachiva AI-Augmented BA Programme**

A 5-task business analysis portfolio built around a real UK fintech regulatory compliance problem.

---

## What's in this repo

```
desktop/
└── AI DA/                    ← All BA programme files
    ├── README.md             ← Programme guide (start here)
    ├── 00-PROGRAMME-OVERVIEW.md
    ├── 01-TASK-1-DISCOVERY.md
    ├── 02-TASK-2-REQUIREMENTS.md
    ├── 03-TASK-3-SOLUTION-DESIGN.md
    ├── 04-TASK-4-UAT-TESTING.md
    ├── 05-TASK-5-PRESENTATION.md
    ├── AI-PRACTICE-GUIDE.md  ← AI tools guide
    ├── build_all.py
    ├── build_notebooks.py
    ├── build_task2.py
    ├── build_tasks345.py
    └── notebooks/            ← Jupyter notebooks for each task
        ├── Task_1_Discovery_ASIS_Analysis.ipynb
        ├── Task_2_Requirements_Engineering.ipynb
        ├── Task_3_Solution_Design.ipynb
        ├── Task_4_UAT_Testing.ipynb
        └── Task_5_Presentation.ipynb
```

---

## The 5 Tasks

| Task | Name | Output |
|------|------|--------|
| 1 | Discovery & AS-IS Analysis | Stakeholder register, gap analysis, discovery report |
| 2 | Requirements Engineering | Requirements package (FR + NFR), prioritised backlog |
| 3 | Solution Design | Requirements-to-systems mapping, integration gaps |
| 4 | UAT Planning & Test Scenarios | UAT strategy, test scenario register |
| 5 | Executive Presentation | 10-slide deck, FCA submission draft |

---

## How the files work (simple explanation)

Think of this repo like a **school project folder** with a planner inside.

### The outer layer (root README.md)
The **root README.md** is the cover page — it tells you what's inside and how the project is organized. It's the first thing people see when they open the repo.

### The AI DA folder
Everything for the actual BA programme lives **inside `AI DA/`**. It's like a sub-folder that contains the whole project.

### What each file does

| File | What it is | How you use it |
|------|-----------|----------------|
| `README.md` | The programme guide | Read this first to understand what you're doing |
| `00-PROGRAMME-OVERVIEW.md` | The full plan | Tells you the scenario, characters, and what AI to use |
| `AI-PRACTICE-GUIDE.md` | AI rulebook | Teaches you how to use AI properly (and where it goes wrong) |
| `01-TASK-1-DISCOVERY.md` | Task 1 instructions | Your first assignment — what to do and what to submit |
| `02-TASK-2-REQUIREMENTS.md` | Task 2 instructions | Your second assignment |
| `03-TASK-3-SOLUTION-DESIGN.md` | Task 3 instructions | Your third assignment |
| `04-TASK-4-UAT-TESTING.md` | Task 4 instructions | Your fourth assignment |
| `05-TASK-5-PRESENTATION.md` | Task 5 instructions | Your final assignment |
| `notebooks/*.ipynb` | Working files | You open these in Jupyter to do the actual work |

### The notebooks folder
The `.ipynb` files are **Jupyter notebooks** — interactive documents where you can write code and text together. Each task has one. You:
1. Open it
2. Read the instructions inside
3. Fill in the answers
4. Save it

### The build_*.py files
These are **helper scripts** that build the notebooks automatically. You don't need to touch these — they're for generating the notebooks, not for doing the tasks.
