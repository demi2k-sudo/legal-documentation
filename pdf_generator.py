import pdfkit



# Specify the output filename

def HtmlToPdf(html:str)->str:
    
    """
    html(str) : html as string
    pdf_file(str) : the file the output pdf is to be stored
    Use this function to convert HTML into a PDF file
    """
    config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
    # Convert the HTML string to PDF
    a = pdfkit.from_string(html,configuration=config, options={ "enable-local-file-access": "", "page-size": "Letter", "margin-top": "0.2in", "margin-right": "0in", "margin-bottom": "0in", "margin-left": "0in" })

    return a