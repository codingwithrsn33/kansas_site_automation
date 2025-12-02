Kansas SOS Business Data Crawler 🏢

Automated Business Intelligence Extraction for Kansas Secretary of State

📌 Table of Contents

Overview

Key Features

Architecture

Project Structure

Getting Started

Default Search Config

Data Schema

Configuration

Performance Metrics

Technical Specifications

Operational Excellence

Legal & Compliance

Advanced Features

Developer

🚀 Overview

The Kansas SOS Business Data Crawler is an enterprise-grade automation tool that extracts structured business intelligence from the Kansas Secretary of State website, including:

Entity identification

Jurisdiction & compliance details

Contact information

Filing timelines

Metadata tracking

Built with Playwright, 2Captcha, and robust fallback strategies.

✨ Key Features
🤖 Intelligent Automation

Smart human-like navigation

Adaptive element detection

CAPTCHA solving (auto + manual fallback)

Form auto-filling

📊 Comprehensive Data Extraction

Entity names, IDs, classifications

Registered agent & office addresses

Compliance & reporting deadlines

Metadata & timestamps

🛡️ Enterprise Reliability

Multi-layer error recovery

Session persistence

Quality assurance validation

Robust timeout handling

💾 Professional Output

Normalized JSON output

Hierarchical storage

Full audit logging

HTML fallback for debugging

🏗️ Architecture
Navigation Flow

Homepage → CAPTCHA → Search Page → Input Parameters → Search Results → Business Details → JSON Storage

Extraction Strategy

Primary: CSS-based element extraction

Secondary: Table parsing

Tertiary: Regex & text interpretation

📁 Project Structure
kansas_business_data/
├── json/                 # Individual business JSON files
├── html_fallback/        # Saved HTML pages if JSON fails
├── errors/               # Extraction failures
├── logs/                 # Application logs
├── screenshots/          # Debug screenshots
└── all_businesses_[timestamp].json

🚀 Getting Started
Clone & Install
git clone https://github.com/codingwithrsn33/Kansas-Site-Crawling.git
cd Kansas-Site-Crawling

pip install playwright twocaptcha
playwright install chromium

Run
python sos_crawler.py

📋 Default Search Config
Category	Search Terms	Purpose
Test Samples	AA, AAB, AAC	System validation
Corporate Entities	LLC, INC, CORP	General business data
Industry Focus	SERVICE, KANSAS	Local & service industry
📊 Data Schema
Sample JSON Output
{
  "identification": {
    "business_id": "1234567",
    "business_name": "Example Company LLC",
    "entity_type": "Limited Liability Company"
  },
  "registration": {
    "formation_date": "2020-01-15",
    "jurisdiction": "Kansas",
    "entity_status": "Active"
  },
  "compliance": {
    "last_reporting_year": "2023",
    "next_report_due_date": "2024-04-15"
  },
  "contact_information": {
    "resident_agent": "John Doe",
    "principal_office_address": "123 Main St | Kansas City, KS 66101",
    "registered_office_address": "456 Registered Ave | Overland Park, KS 66204"
  },
  "metadata": {
    "extraction_timestamp": "2024-01-15T10:30:00Z",
    "search_term": "LLC",
    "processing_status": "success",
    "data_completeness": "complete"
  }
}

⚙️ Configuration
Search Terms
search_terms = ["AA", "AAB", "AAC", "LLC", "INC", "CORP", "SERVICE", "KANSAS"]

Limit Processed Businesses
for business in businesses[:3]:
    process_business(business)

CAPTCHA Setup
self.captcha_api_key = "your_2captcha_api_key"
self.solver = None   # Enable manual solving

📈 Performance Metrics
Execution Speed
Component	Fast Mode	Reliable Mode
Navigation	2–3 sec	5–10 sec
Search Setup	1 sec	2–3 sec
Results Extraction	1–2 sec	3–5 sec
Business Detail	2–3 sec	5–8 sec
Total	5 sec	15 sec
2Captcha Cost Analysis

Cost per CAPTCHA → $0.00077

$2.87 balance → 3,726 CAPTCHAs

Usage per business → 1–3 CAPTCHAs

Total capacity → 1,200–3,700 businesses

🔧 Technical Specifications
Requirements

Python 3.8+

Playwright + Chromium

2GB RAM recommended

Stable internet connection

Extracted Fields (30+)

IDs

Names

Status

Addresses

Dates

Compliance info

🛠️ Operational Excellence
Error Recovery

Automatic retries

Fallback extraction layers

Session restoration

Maintenance

Validation rule testing

Storage cleanup

Dependency updates

🔒 Privacy & Legal Compliance

Please ensure you:

Respect Kansas SOS Terms of Service

Follow rate limits

Use data ethically & legally

Follow 2Captcha usage terms

🚀 Advanced Features
Add More Search Terms
search_terms = ["LLC", "INC", "CORP", "CO", "LP", "LLP", "PC"]

Add Custom Fields
custom_fields = {
    "tax_id": "#TaxIDSelector",
    "license_number": "#LicenseSelector"
}

Retry Logic
max_retries = 3
retry_delay = 5

👨‍💻 Developer

Rohan Subhash Darekar
Python Developer

📞 +91 9075237180
📧 rohandarekar307@gmail.com

🔗 GitHub: https://github.com/codingwithrsn33
