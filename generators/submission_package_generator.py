from docx import Document


def generate_submission_package(
    cover_page_path,
    resume_path,
    output_path
):

    print(
        "Submission Package Generation Started"
    )

    cover_doc = Document(
        cover_page_path
    )

    resume_doc = Document(
        resume_path
    )

   
    for element in resume_doc.element.body:
        cover_doc.element.body.append(
            element
        )

    cover_doc.save(
        output_path
    )

    print(
        "Submission Package Generated"
    )