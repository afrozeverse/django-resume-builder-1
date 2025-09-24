from django.template.loader import render_to_string
from weasyprint import HTML

def html2pdf(template_src, context={}):
    html_string = render_to_string(template_src, context)
    # Convert HTML to PDF
    html = HTML(string=html_string, base_url=None)
    pdf = html.write_pdf()
    return pdf