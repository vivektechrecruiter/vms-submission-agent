# VMS Submission Agent - Project Structure

## Root Folder

D:\Python\vms_submission_app

---

## Prompts

prompts/

* resume_extraction.txt
* jd_extraction_prompt.txt
* skill_match_prompt.txt

Purpose:

Contains all OpenAI prompts used by the application.

---

## Services

services/

* document_formatter.py
* document_merge_service.py
* jd_extraction_service.py
* json_service.py
* openai_service.py
* resume_context_builder.py
* skill_match_service.py

Purpose:

Business logic and AI integration layer.

---

## Generators

generators/

* direct_resume_generator.py
* resume_generator.py
* submission_generator.py

Purpose:

Generate recruiter-facing Word documents.

---

## Parsers

parsers/

* resume_reader.py
* jd_parser.py

Purpose:

Read raw resume and JD content.

---

## Output Files

output/

Expected Outputs:

* candidate.json
* jd.json
* skill_match.json
* formatted_resume.docx
* submission_document.docx

---

## Current Core Workflow

Resume
↓
resume_reader.py
↓
resume_extraction.txt
↓
candidate.json

JD
↓
jd_parser.py
↓
jd_extraction_prompt.txt
↓
jd.json

candidate.json
+
jd.json
↓
skill_match_prompt.txt
↓
skill_match.json

candidate.json
+
skill_match.json
+
recruiter_inputs.json
↓
submission_generator.py
↓
submission_document.docx
