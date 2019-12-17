# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 12:46:00 2019

@author: Shankar Bathula
"""
import re
import pandas as pd
def order_table_data():
    with open('PdfExtractData.txt') as file:
        data = file.read()
        orderd_table1 = re.findall("52.*", data)
        orderd_table2 = re.findall("29.*", data)
        orderd_table2 = orderd_table2[1:]
        table = orderd_table1 + orderd_table2
    return table


with open('PdfExtractData.txt') as file:
    data = file.read()     
    invoice_id = re.findall(r'[A-Z0-9{8}]\w+', data)
    invoice_id = invoice_id[1]
    invoice_date = re.search(r'(\d+/\d+/\d+)', data)
    invoice_date = invoice_date.group(1)
    total = re.compile(r'\$.+')
    total_amount = total.findall(data)
    total_amount = str(total_amount[-1])
    total_amount = total_amount.split()[1]
    customer = re.compile(r'^([A-Z]{1}.+?)(?:,)', flags = re.M)
    customer_id = customer.findall(data)
    tax = re.compile(r'.*Tax(.*)')
    tax_amount = tax.findall(data)
    tax_amount = ' '.join(tax_amount)
    tax_amount = tax_amount.split()[1]
    customer_name = customer_id[0].split()[1:3]
    customer_name = ' '.join(customer_name)
    purchase_order = customer_id[0].split()[0]
    print("Invoice Number :",invoice_id)
    print("Customer Name :",customer_name)
    print("Invoice Date :",invoice_date)    
    print("Purchase Order :",purchase_order)
    print("Tax Amount :",tax_amount[0])
    print("Total :",total_amount)
#    df = pd.DataFrame({"InvoiceID":invoice_id, "CustomerName":customer_name, "InvoiceDate":invoice_date,
#                       "purchase_order":purchase_order, "tax_amount":tax_amount,"total_amount":total_amount},
#                      index=['InvoiceID', 'CustomerName', 'InvoiceDate', 'purchase_order', 'tax_amount','total_amount'])
    df1 = pd.DataFrame([invoice_id, customer_name, invoice_date,purchase_order,tax_amount,total_amount],
                      index=['InvoiceID', 'CustomerName', 'InvoiceDate', 'purchase_order', 'tax_amount','total_amount'],)
    #print(df)
    orders_data = []
    shiped_data = []
    b_o_data = []
    item_number_data = []
    descrb_data = []
    unit_price_data = []
    ext_price_data = []
    
    
    tb_data = order_table_data()
    for order in tb_data: 
        order =''.join(order)
        orderd = order.split()[0]
        shiped = order.split()[1]
        b_o =  order.split()[2]
        item_number =  order.split()[3]
        description = order.split()[4:9]
        descrb = ' '.join(description)
        discount = order.split()[10]
        unit_price = order.split()[12]
        ext_price = order.split()[14]
        orders_data.append(orderd)
        shiped_data.append(shiped)
        b_o_data.append(b_o)
        item_number_data.append(item_number)
        descrb_data.append(descrb)
        unit_price_data.append(unit_price)
        ext_price_data.append(ext_price)
#        print("Orderd :",orderd)
#        print("Shipped :",shiped)
#        print("B/O :",b_o)
#        print("Item number:",item_number)
#        print("Description :",descrb)
#        print("Discount :",discount)
#        print("Unit Price :",unit_price)
#        print("Ext. Price :",ext_price)
    df2 = pd.DataFrame([orders_data,shiped_data,b_o_data,item_number_data,descrb_data, unit_price_data,ext_price_data],
                        index=['orders_data','shiped_data','b_o_data','item_number_data',
                                                            'descrb_data', 'unit_price_data','ext_price_data'])
    print("data frame :",df2)
    frames = [df1, df2]
    df = pd.concat(frames)
    print(df)
    df.to_excel("output1.xlsx")

            
