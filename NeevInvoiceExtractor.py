# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 13:50:49 2019

@author: Shankar Bathula
"""
import re
import os
import pandas as pd
import PyPDF2
def pdf_extract_raw_data():
    file =  open(r"C:\Users\admin\Documents\UiPath\OracleInvoiceProcess\Stitchfix_invoice.pdf", 'rb')
    pdfReader = PyPDF2.PdfFileReader(file)
     
    print(" No. Of Pages :", pdfReader.numPages)
     
    pageObject = pdfReader.getPage(0)

    data = pageObject.extractText()
    
    split_data = data.split('\n')
    print(split_data)
    company_name = split_data[0]
    bill_company = split_data[7]
    invoice = split_data[11]
    invoice =invoice.split()[1]
    date = split_data[13]
    terms = split_data[15]
    due_date = split_data[17]
    purchase_order = split_data[20]
    project_name = split_data[21]
    item_date = split_data[29]
    item = split_data[30]
    item_descrb = split_data[32:33]
    item_descrb = ' '.join(item_descrb)
    hours_days = split_data[33]
    rate = split_data[34]
    amount = split_data[35]
    total_due = split_data[37]
    total_due = total_due.split()[1]
    df = pd.DataFrame([company_name,bill_company,invoice, date, terms, due_date,purchase_order,project_name,item,item_date,item_descrb,hours_days, rate,amount,total_due], 
	                  index=['company_name','bill_company','invoice','date','terms','due_date','purchase_order','project_name','item','item_date','item_descrb','hours_days','rate','amount','total_due'])
    path = r"C:\Users\admin\Documents\UiPath\OracleInvoiceProcess"
    df.to_csv(os.path.join(path + "neev_stitch1.csv"))       
    return df
#pdf_extract_raw_data()
