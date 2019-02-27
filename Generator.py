import pdfkit

#pdfkit.from_file('Templates/index.html', 'certificate.pdf')

style = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in'
}

#pdfkit.from_file('Templates/index.html', 'Output/certificate.pdf')

pdfkit.from_file('Templates/index.html', 'Output/certificate.pdf', options=style)
