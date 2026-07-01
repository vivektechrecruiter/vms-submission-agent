# VMS Submission Agent - Architecture

## High-Level Workflow

Resume
↓
Resume Extraction Engine
↓
candidate.json

JD
↓
JD Extraction Engine
↓
jd.json

candidate.json + jd.json
↓
Qualification Engine
↓
skill_match.json

candidate.json
+
Recruiter Inputs
+
skill_match.json
↓
Submission Generator
↓
Submission Document.docx

---

# System Components

## Resume Extraction Layer

Files:

* resume_extraction_service.py
* resume_extraction_prompt.txt

Output:

candidate.json

Purpose:

Extract structured candidate information from resumes.

---

## Resume Formatting Layer

Files:

* document_formatter.py
* direct_resume_generator.py

Purpose:

Generate standardized recruiter-ready resumes.

Output:

Formatted Resume.docx

---

## JD Extraction Layer

Files:

* jd_extraction_service.py
* jd_extraction_prompt.txt

Output:

jd.json

Purpose:

Extract structured hiring requirements.

---

## Qualification Engine

Files:

* skill_match_service.py
* skill_match_prompt.txt

Input:

candidate.json
+
jd.json

Output:

skill_match.json

Purpose:

Evaluate candidate fit.

Classifications:

* Strong Fit
* Partial Fit
* No Fit

Recommendations:

* Submit Immediately
* Screen Further
* Do Not Submit

---

## Submission Generator

Files:

* submission_generator.py

Inputs:

candidate.json
recruiter_inputs.json
skill_match.json

Output:

Submission.docx

Contains:

* Candidate Cover Page
* Relevant Skills Table
* Supplier Comments
* Formatted Resume

---

# Core JSON Outputs

## candidate.json

Stores:

* Personal Information
* Summary
* Skills
* Experience
* Education
* Certifications

---

## jd.json

Stores:

* Role
* Skills
* Responsibilities
* Requirements

---

## skill_match.json

Stores:

* Qualification Status
* Match Score
* Recommendation
* Skill Gaps
* Screening Questions
* Submission Skills
* Supplier Comments

---

# Qualification Engine Logic

Strong Fit

85%+

Recommendation:

Submit Immediately

---

Partial Fit

70%-84%

Recommendation:

Screen Further

---

No Fit

Below 70%

Recommendation:

Do Not Submit

---

# Submission Rules

Only Top 3 Skills

Never show all JD skills.

Only show:

* Skills important to Hiring Manager
* Skills supported by resume evidence
* Skills useful for shortlisting

These skills populate the submission table.
