---
layout: post
title: Consumer Complaints – EDA
description: 
# thumbnail: ../../../../assets/images/pandas/encoding-categorical-data.png
author: Dipak Pulami Magar
date:   2025-12-08 10:12:45 +0545
categories: pandas
status: published
---

### Understanding the Dataset/Dataset Overview
Our dataset has 64,814 rows/observations in 18 columns as shown below with their descriptions
1. date_received (date): the date the CFPB sent the complaint to the company
2. product_name (text): The type of product the consumer identified in the complaint
3. sub_product (text): The type of sub-product the consumer identified in the complaint (not all Products have Sub-products)
4. issue (text): The issue the consumer identified in the complaint (possible values are dependent on Product)
5. sub-issue (text): The sub-issue the consumer identified in the complaint (possible values are dependent on Product and Issue, and not all Issues have corresponding Sub-issues)
6. cosumer_compliant_narrative (text):
7. company_public_response (text): This is how the company responded. For example, “Closed with explanation.”
8. company (text): 
9. state_name (text): The state of the mailing address provided by the consumer
10. zip_code (text): 
11. tags (text): 
12. consumer_consent_provided (text): 
13. submitted_via (varchar(50)): How the complaint was submitted to the CFPB
14. date_sent_to_company (date):
15. company_response_to_consumer: 
16. timely_response (text): whether the company gave a timely response (Yes/No)
17. consumer_disputed (text): 
18. complaint_id: the unique identification number for a complaint

product_name: 11
- Bank account or service
- Consumer Loan
- Credit card
- Credit reporting
- Debt collection
- Money transfers
- Mortgage
- Other financial service
- Payday loan
- Prepaid card
- Student loan

sub_product: 46
- 
- (CD) Certificate of deposit
- Auto
- Cashing a check without an account
- Check cashing
- Checking account
- Conventional adjustable mortgage (ARM)
- Conventional fixed mortgage
- Credit card
- Credit repair
- Debt settlement
- Domestic (US) money transfer
- Electronic Benefit Transfer / EBT card
- Federal student loan
- FHA mortgage
- Foreign currency exchange
- General purpose card
- Gift or merchant card
- Government benefit payment card
- Home equity loan or line of credit
- I do not know
- ID prepaid card
- Installment loan
- International money transfer
- Medical
- Mobile wallet
- Money order
- Mortgage
- Non-federal student loan
- Other (i.e. phone, health club, etc.)
- Other bank product/service
- Other mortgage
- Other special purpose card
- Pawn loan
- Payday loan
- Payroll card
- Personal line of credit
- Refund anticipation check
- Reverse mortgage
- Savings account
- Second mortgage
- Title loan
- Transit card
- VA mortgage
- Vehicle lease
- Vehicle loan


column, count, unique
issue,, 91, 
sub_issue,, 68


1, date_received, date, date, YES, 
2, product_name, text, text, YES, 
3, sub_product, text, text, YES, 
4, issue, text, text, YES, 
5, sub_issue, text, text, YES, 
6, cosumer_compliant_narrative, text, text, YES, 
7, company_public_response, text, text, YES, 
8, company, text, text, YES, 
9, state_name, text, text, YES, 
10, zip_code, text, text, YES, 
11, tags, text, text, YES, 
12, consumer_consent_provided, text, text, YES, 
13, submitted_via, varchar(50), varchar, YES, 
14, date_sent_to_company, date, date, YES, 
15, company_response_to_consumer, text, text, YES, 
16, timely_response, text, text, YES, 
17, consumer_disputed, text, text, YES, 
18, complaint_id, int, int, YES, 



|sn |columns                      |data_type   |
|---|-----------------------------|------------|
|1  | date_received               | date       |
|2  | product_name                | text       |
|3  | sub_product                 | text       |
|4  | issue                       | text       |
|5  | sub_issue                   | text       | text   | YES  |      |
|6  | cosumer_compliant_narrative | text       | text   | YES  |      |
|7  | company_public_response     | text       | text   | YES  |      |
|8  | company                     | text       | text   | YES  |      |
|9  | state_name                  | text       | text   | YES  |      |
|10 | zip_code                    | text       | text   | YES  |      |
|11 | tags                        | text       | text   | YES  |      |
|12 | consumer_consent_provided   | text       | text   | YES  |      |
|13 | submitted_via               | varchar(50)| varchar| YES  |      |
|14 | date_sent_to_company        | date       | date   | YES  |      |
|15 | company_response_to_consumer| text       | text   | YES  |      |
|16 | timely_response             | text       | 
|17 | consumer_disputed           | text       | 
|18 | complaint_id                | int        |
