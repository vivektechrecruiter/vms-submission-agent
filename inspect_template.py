from docx import Document

doc = Document(
    "templates/tcs_submission_template.docx"
)

table = doc.tables[0]

for i, row in enumerate(table.rows):
    print(f"\nROW {i}")

    for j, cell in enumerate(row.cells):
        print(
            f"COL {j}: "
            f"{repr(cell.text)}"
        )