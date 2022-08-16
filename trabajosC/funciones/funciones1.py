import subprocess
from subprocess import  Popen

LIBRE_OFFICE = r"C:\Program Files\LibreOffice\program\soffice.exe"

def convert_to_pdf_wd(input_docx, out_folder):
    p = Popen([LIBRE_OFFICE, '--headless', '--convert-to', 'pdf', '--outdir',
               out_folder, input_docx])
    print([LIBRE_OFFICE, '--convert-to', 'pdf', input_docx])
    p.communicate()

#sample_doc = 'media\manuscritos\Libre87.docx'
#out_folder = 'media\manuscritos'
#convert_to_pdf_wd(sample_doc, out_folder)

def generate_pdf_linux(doc_path, path):
    subprocess.call(['soffice',
        # '--headless',
        '--convert-to',
        'pdf',
        '--outdir',
        path,
        doc_path])
    return doc_path

#generate_pdf_linux("docx_path.docx", "output_path") 