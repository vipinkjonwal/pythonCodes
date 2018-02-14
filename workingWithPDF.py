import PyPDF2

def rotatePDF(inFile,outFile,angle):
    pdfObject = open(inFile,'rb')

    pdfReader = PyPDF2.PdfFileReader(pdfObject)
    pdfWriter = PyPDF2.PdfFileWriter()

    for page in range(pdfReader.numPages):

        pageObj = pdfReader.getPage(page)
        pageObj.rotateClockwise(angle)

        pdfWriter.addPage(pageObj)

    newFile = open(outFile,'wb')
    pdfWriter.write(newFile)
    pdfObject.close()
    newFile.close()

def extractText(inFile):
    pdfFileObj = open('mypdf.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print(pdfReader.numPages)
    pageObj = pdfReader.getPage(0)

    print(pageObj.extractText())
    pdfFileObj.close()

extractText('mypdf.pdf')