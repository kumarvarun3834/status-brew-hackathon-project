import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import grey
from PyPDF2 import PdfFileReader, PdfFileWriter
import os
# this file creates pdf of your doc

lst=[]

# gpt generated file system just fixed bugs in it

def pdf_creation(baseurl, TOKEN, df, chat_id,start=0,files=1) -> None:
    # files=0
    temp_df=df
    # db= {"message_id":None,"file_name":None,"file_link":None,"mime_type":None,"file_size":None}
    # while df!=pd.DataFrame(db):
    # while len(temp_df)>2:
    # while df != None:
    # while  df.index[-1]==temp_df.index[-1]:
    # while True:
    
    temp_df=0
    # files+=1
    if len(df)-start>=22:
        print("this running------------------")
        temp_df=df.loc[start:start+22]
        print(files)
    #    df=df.drop( ,axis=0,inplace=True)
    else:
        print("that running-------------------")
        print(files)
        temp_df=df.loc[start:]
        # pdf_generator(baseurl,TOKEN,temp_df,chat_id,f'({files})')

    if files not in lst :
        lst.append(files)
        # pdf_generator(baseurl,TOKEN,temp_df,chat_id,f'({files})')   

    print(temp_df)
    # df.drop(index=temp_df.index, inplace=True)
    # start=21*files
    # if files>start:
    # if 21*(files-1)<len(df)<=21*files:
    pdf_generator(baseurl,TOKEN,temp_df,chat_id,f'({files})')
                        
    if len(df)>(22*files):
        print("recursion hell again")
        pdf_creation(baseurl, TOKEN, df, chat_id,22*files+1,files+1)

    # df = pd.DataFrame() if df is None else df

def pdf_generator(baseurl, TOKEN, df, chat_id,pdfnum) -> None:

    pdf_output = f'{chat_id}{pdfnum}.pdf'
    
    # Create PDF
    c = canvas.Canvas(pdf_output, pagesize=letter)
    width, height = letter
    x_offset, y_offset = 50, height - 50
    row_height = 30
    col_widths = [100] * len(df.columns)  # Adjust column widths as needed

    # Draw table header
    c.setFont("Helvetica-Bold", 12)
    for i, col_name in enumerate(df.columns):
        c.drawString(x_offset + sum(col_widths[:i]), y_offset, col_name)

    y_offset -= row_height
    c.setFont("Helvetica", 10)
    for index, row in df.iterrows():
        for i, cell_value in enumerate(row):
            text = str(cell_value)
            wrapped_text = text[:int(col_widths[i] / 6)] + (text[int(col_widths[i] / 6):] and '...')
            c.drawString(x_offset + sum(col_widths[:i]), y_offset, wrapped_text)
        y_offset -= row_height
    
    # Draw gridlines
    y_offset = height - 50
    c.setStrokeColor(grey)
    for i in range(len(df) + 2):
        c.line(x_offset - 10, y_offset, x_offset + sum(col_widths), y_offset)
        y_offset -= row_height

    x_offset = 50
    y_offset = height - 50
    for i in range(len(df.columns) + 1):
        c.line(x_offset, y_offset, x_offset, y_offset - (len(df) + 1) * row_height)
        x_offset += col_widths[i % len(col_widths)]

    c.save()

    import share_file
    # for file_path in output_files:
    share_file.send_file(baseurl, TOKEN, chat_id, pdf_output)
    os.remove(pdf_output)
