# Industry Notepad V1.0
# Copyright (C) 2024, Sourceduty 

TEMPLATES = {
    'Technology': {
        'Software Development': '''Software Development Plan

Project Overview
- Project Name: 
- Project Manager: 
- Start Date: 
- End Date: 

Objectives
- Objective 1: 
- Objective 2: 
- Objective 3: 

Milestones
- Milestone 1: 
- Milestone 2: 
- Milestone 3: 

Resources
- Resource 1: 
- Resource 2: 
- Resource 3: 
        ''',
        'IT Infrastructure': '''IT Infrastructure Setup

Network Design
- Topology: 
- IP Addressing: 
- Subnetting: 

Hardware
- Server Specifications: 
- Workstation Requirements: 
- Networking Equipment: 

Security
- Firewall Configuration: 
- VPN Setup: 
- User Access Control: 

Backup & Recovery
- Backup Schedule: 
- Recovery Plan: 
        ''',
        'System Architecture': '''System Architecture Document

System Overview
- Purpose: 
- Scope: 

Architecture Design
- Layer 1: 
- Layer 2: 
- Layer 3: 

Technology Stack
- Frontend: 
- Backend: 
- Database: 

Integration Points
- External Systems: 
- APIs: 
        ''',
        'Tech Support Guide': '''Tech Support Guide

Common Issues
- Issue 1: 
- Issue 2: 
- Issue 3: 

Troubleshooting Steps
- Step 1: 
- Step 2: 
- Step 3: 

Contact Information
- Support Line: 
- Email Support: 

Escalation Procedure
- Level 1: 
- Level 2: 
        ''',
        'API Documentation': '''API Documentation

API Overview
- Base URL: 
- Version: 

Authentication
- Method: 
- API Key: 

Endpoints
- Endpoint 1: 
  - Method: 
  - Parameters: 
  - Response: 

- Endpoint 2: 
  - Method: 
  - Parameters: 
  - Response: 
        '''
    },
    'Healthcare': {
        'Patient Intake Form': '''Patient Intake Form

Personal Information
- Name: 
- Date of Birth: 
- Contact Information: 

Medical History
- Allergies: 
- Current Medications: 
- Past Surgeries: 

Insurance Information
- Provider: 
- Policy Number: 
- Group Number: 
        ''',
        'Medical Report': '''Medical Report

Patient Information
- Name: 
- Date of Birth: 
- Medical Record Number: 

Diagnosis
- Condition: 
- Symptoms: 
- Duration: 

Treatment Plan
- Medications: 
- Therapy: 
- Follow-Up Date: 

Physician's Notes
- Notes: 
        ''',
        'Prescription Template': '''Prescription Template

Physician Information
- Name: 
- License Number: 
- Contact Information: 

Patient Information
- Name: 
- Date of Birth: 
- Address: 

Medication Prescribed
- Drug Name: 
- Dosage: 
- Instructions: 

Refills
- Number of Refills: 
- Expiration Date: 
        ''',
        'Doctor Referral Letter': '''Doctor Referral Letter

Referring Doctor Information
- Name: 
- Practice Name: 
- Contact Information: 

Patient Information
- Name: 
- Date of Birth: 
- Medical Record Number: 

Reason for Referral
- Condition: 
- Symptoms: 
- Previous Treatments: 

Referral Details
- Specialist Name: 
- Appointment Date: 
- Additional Notes: 
        ''',
        'Health Insurance Claim': '''Health Insurance Claim Form

Policy Holder Information
- Name: 
- Policy Number: 
- Group Number: 

Patient Information
- Name: 
- Date of Birth: 
- Relationship to Policy Holder: 

Claim Details
- Date of Service: 
- Provider Name: 
- Amount Billed: 

Authorization
- Signature: 
- Date: 
        '''
    },
    'Finance': {
        'Invoice': '''Invoice

Invoice Information
- Invoice Number: 
- Date of Issue: 
- Due Date: 

Bill To
- Company Name: 
- Contact Person: 
- Address: 

Itemized List
- Item 1: Description, Quantity, Price
- Item 2: Description, Quantity, Price

Total Amount
- Subtotal: 
- Taxes: 
- Total: 
        ''',
        'Financial Report': '''Financial Report

Report Overview
- Reporting Period: 
- Prepared By: 
- Date: 

Income Statement
- Revenue: 
- Expenses: 
- Net Income: 

Balance Sheet
- Assets: 
- Liabilities: 
- Equity: 

Cash Flow Statement
- Operating Activities: 
- Investing Activities: 
- Financing Activities: 
        ''',
        'Budget Plan': '''Budget Plan

Budget Overview
- Project/Department: 
- Prepared By: 
- Date: 

Income Sources
- Source 1: 
- Source 2: 

Expenses
- Category 1: 
- Category 2: 

Summary
- Total Income: 
- Total Expenses: 
- Net Budget: 
        ''',
        'Tax Filing Worksheet': '''Tax Filing Worksheet

Taxpayer Information
- Name: 
- Social Security Number: 
- Filing Status: 

Income Details
- Wages: 
- Interest Income: 
- Dividends: 

Deductions
- Standard Deduction: 
- Itemized Deductions: 

Tax Calculation
- Taxable Income: 
- Tax Owed: 
- Refund Due: 
        ''',
        'Expense Tracker': '''Expense Tracker

Date
- Description: 
- Category: 
- Amount: 

Monthly Summary
- Total Expenses: 
- Total Income: 
- Net Balance: 

Notes
- Additional Information: 
        '''
    },
    'Education': {
        'Lesson Plan': '''Lesson Plan

Lesson Information
- Subject: 
- Grade Level: 
- Duration: 

Learning Objectives
- Objective 1: 
- Objective 2: 
- Objective 3: 

Materials Needed
- Material 1: 
- Material 2: 

Lesson Procedure
- Introduction: 
- Activity: 
- Conclusion: 
        ''',
        'Student Report': '''Student Report

Student Information
- Name: 
- Grade Level: 
- Teacher: 

Academic Performance
- Subject 1: 
- Subject 2: 
- Subject 3: 

Behavior & Participation
- Notes: 

Recommendations
- Teacher's Recommendations: 
        ''',
        'Classroom Schedule': '''Classroom Schedule

Monday
- 9:00 AM - Subject 1
- 10:00 AM - Subject 2
- 11:00 AM - Subject 3

Tuesday
- 9:00 AM - Subject 1
- 10:00 AM - Subject 2
- 11:00 AM - Subject 3

Wednesday
- 9:00 AM - Subject 1
- 10:00 AM - Subject 2
- 11:00 AM - Subject 3
        ''',
        'Assignment Sheet': '''Assignment Sheet

Assignment Details
- Subject: 
- Assigned Date: 
- Due Date: 

Instructions
- Instruction 1: 
- Instruction 2: 
- Instruction 3: 

Submission Guidelines
- Format: 
- Submission Method: 
        ''',
        'Grading Rubric': '''Grading Rubric

Criteria 1: 
- Excellent: 
- Good: 
- Needs Improvement: 

Criteria 2: 
- Excellent: 
- Good: 
- Needs Improvement: 

Criteria 3: 
- Excellent: 
- Good: 
- Needs Improvement: 

Total Score: 
        '''
    },
    'Construction': {
        'Project Plan': '''Construction Project Plan

Project Information
- Project Name: 
- Project Manager: 
- Start Date: 
- End Date: 

Scope of Work
- Task 1: 
- Task 2: 
- Task 3: 

Resource Allocation
- Material 1: 
- Material 2: 
- Labor: 

Milestones
- Milestone 1: 
- Milestone 2: 
        ''',
        'Safety Checklist': '''Construction Safety Checklist

Site Preparation
- Check 1: 
- Check 2: 

Personal Protective Equipment
- Helmet: 
- Gloves: 
- Boots: 

Machinery & Tools
- Inspection: 
- Maintenance: 

Emergency Procedures
- Contact Information: 
- First Aid Kit: 
        ''',
        'Blueprint Outline': '''Blueprint Outline

Project Overview
- Project Name: 
- Location: 

Structural Layout
- Foundation Plan: 
- Wall Layout: 
- Roof Design: 

Electrical & Plumbing
- Electrical Plan: 
- Plumbing Layout: 

Materials
- Concrete: 
- Steel: 
- Wood: 
        ''',
        'Contractor Agreement': '''Contractor Agreement

Parties Involved
- Client Name: 
- Contractor Name: 
- Project Name: 

Scope of Work
- Description: 

Payment Terms
- Amount: 
- Schedule: 

Timeline
- Start Date: 
- Completion Date: 

Signatures
- Client: 
- Contractor: 
        ''',
        'Construction Timeline': '''Construction Timeline

Week 1
- Task 1: 
- Task 2: 

Week 2
- Task 1: 
- Task 2: 

Week 3
- Task 1: 
- Task 2: 

Completion
- Final Inspection: 
- Handover: 
        '''
    },
    'Retail': {
        'Sales Report': '''Sales Report

Report Overview
- Reporting Period: 
- Prepared By: 
- Date: 

Sales Summary
- Total Sales: 
- Number of Transactions: 
- Average Sale Amount: 

Top Products
- Product 1: 
- Product 2: 
- Product 3: 

Sales by Region
- Region 1: 
- Region 2: 
        ''',
        'Inventory Checklist': '''Inventory Checklist

Product List
- Product 1: 
- Product 2: 
- Product 3: 

Stock Levels
- Product 1: 
- Product 2: 
- Product 3: 

Reorder Points
- Product 1: 
- Product 2: 
- Product 3: 

Notes
- Additional Information: 
        ''',
        'Customer Feedback Form': '''Customer Feedback Form

Customer Information
- Name: 
- Contact Information: 

Purchase Details
- Product/Service Purchased: 
- Date of Purchase: 

Feedback
- Rating (1-5): 
- Comments: 

Suggestions
- Suggestions for Improvement: 
        ''',
        'Marketing Plan': '''Marketing Plan

Marketing Objectives
- Objective 1: 
- Objective 2: 
- Objective 3: 

Target Audience
- Audience 1: 
- Audience 2: 

Strategies
- Strategy 1: 
- Strategy 2: 

Budget
- Total Budget: 
- Allocation: 
        ''',
        'Store Layout': '''Store Layout

Entrance
- Location: 

Sales Floor
- Sections: 
- Shelving: 

Checkout Area
- Location: 
- Equipment: 

Storage
- Location: 
- Inventory Management: 
        '''
    }
}
