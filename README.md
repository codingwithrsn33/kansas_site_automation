Kansas SOS Business Data Crawler 🏢

A comprehensive automation solution for business intelligence gathering from the Kansas Secretary of State website. This enterprise-grade tool systematically extracts business entity data with intelligent navigation, CAPTCHA solving, and professional output management.

🚀 Overview

The Kansas SOS Business Crawler automates the extraction of business entity information through intelligent web navigation, multi-layered data extraction, and comprehensive error management. It transforms unstructured web data into structured, analyzable business intelligence.

✨ Key Features
🤖 Intelligent Automation

Smart Navigation: Natural browsing from homepage to business search with CAPTCHA handling

Form Automation: Automated search parameter configuration

Dynamic Detection: Adaptive element identification with multiple fallback strategies

CAPTCHA Management: Automatic solving with 2Captcha integration

📊 Comprehensive Data Extraction

Business Identification: Entity names, IDs, and registration details

Entity Classification: Business types, status, and jurisdiction information

Contact Information: Resident agents and complete office addresses

Compliance Data: Reporting requirements and filing deadlines

Metadata: Extraction timestamps and source tracking

🛡️ Enterprise Reliability

Multi-layer Error Handling: Primary, secondary, and tertiary extraction methods

CAPTCHA Management: Automated solving with manual intervention fallback

Session Persistence: Robust recovery from interruptions and timeouts

Data Validation: Completeness checking and quality assurance

💾 Professional Output

Structured JSON: Clean, normalized business data (30+ fields)

Hierarchical Storage: Organized by extraction status and data type

Audit Trail: Comprehensive logging and activity monitoring

HTML Fallback: Source preservation for debugging

🏗️ Architecture
Navigation Flow

Homepage → CAPTCHA Check → Search Page → Automated Setup → Search Execution → Results Processing → Business Detail Extraction → Storage

Extraction Strategy

Primary Method: Direct CSS selector targeting

Secondary Method: Table-based parsing & pattern recognition

Tertiary Method: Text analysis & regex matching

Project Structure
kansas_business_data/
├── json/               # Individual business JSON files
├── html_fallback/      # HTML files when JSON fails
├── errors/             # Error logs and failed extractions
├── logs/               # Application logs
├── screenshots/        # Debug screenshots
└── all_businesses_[timestamp].json

🚀 Getting Started
Installation
# Clone repository
git clone https://github.com/codingwithrsn33/Kansas-Site-Crawling.git
cd Kansas-Site-Crawling

# Install dependencies
pip install playwright twocaptcha

# Install browsers
playwright install chromium

# Optional: Set 2Captcha key
export CAPTCHA_API_KEY="your_2captcha_api_key_here"

Execution
python sos_crawler.py

📋 Default Search Configuration
Categories & Search Terms
Category	Search Terms	Purpose
Test Samples	AA, AAB, AAC	Validation
Corporate Entities	LLC, INC, CORP	Business data
Industry Focus	SERVICE, KANSAS	Regional data
📊 Data Schema
Business Entity Record
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
Search Parameters
search_terms = ["AA", "AAB", "AAC", "LLC", "INC", "CORP", "SERVICE", "KANSAS"]

Processing Limits
for business in businesses[:3]:
    process_business(business)

CAPTCHA Configuration
self.captcha_api_key = "your_2captcha_api_key"
self.solver = None   # Manual fallback

🎯 Performance Features
Rate Management

Adaptive request timing

Respectful crawling delays

Quality Assurance

Field validation

Completeness scoring

Cross-verification

Monitoring

Real-time status

Analytics

CAPTCHA stats

📈 Performance Metrics
Time Estimates
Component	Fast	Reliable
Navigation	2–3 sec	5–10 sec
Search Setup	1 sec	2–3 sec
Results Extraction	1–2 sec	3–5 sec
Business Detail	2–3 sec	5–8 sec
Total / Business	~5 sec	~15 sec
2Captcha Cost

Cost per CAPTCHA: $0.00077

With $2.87 → ≈ 3,726 CAPTCHAs

Businesses possible: 1,200 – 3,700

🔧 Technical Specifications
Requirements

Python 3.8+

Playwright + Chromium

2GB RAM recommended

Supported Fields

30+ business data points

IDs, addresses, compliance info

🛠️ Operational Excellence
Error Recovery

Automatic retries

Session preservation

Graceful fallback

Maintenance

Rule validation

Storage optimization

Dependency updates

🔒 Privacy & Legal Compliance

Respect website ToS

Rate limits

Use data ethically

🚀 Advanced Features
Custom Search Terms
search_terms = ["LLC", "INC", "CORP", "CO", "LP", "LLP", "PC"]

Add Custom Fields
custom_fields = {
    "tax_id": "#TaxIDSelector",
    "license_number": "#LicenseSelector"
}

Retry Logic
max_retries = 3
retry_delay = 5

📚 Dependencies

playwright

twocaptcha

json

logging

datetime

re

os

👨‍💻 Developer Information

Rohan Subhash Darekar
Python Developer
📞 +91 9075237180
📧 rohandarekar307@gmail.com

🔗 GitHub Profile
