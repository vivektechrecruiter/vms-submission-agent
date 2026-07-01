from docxtpl import DocxTemplate

def generate_resume(template_path, output_path, context):
    doc = DocxTemplate(template_path)

    doc.render(context)

    doc.save(output_path)