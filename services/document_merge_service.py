from docx import Document
from docxcompose.composer import Composer


def merge_documents(
    cover_page_path,
    resume_path,
    output_path
):

    cover_doc = Document(
        cover_page_path
    )

    resume_doc = Document(
        resume_path
    )

    composer = Composer(
        cover_doc
    )

    composer.append(
        resume_doc
    )

    composer.save(
        output_path
    )