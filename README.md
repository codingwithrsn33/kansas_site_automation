# Kansas SOS Business Crawler 🏢

A sophisticated automation solution for comprehensive business intelligence gathering from the Kansas Secretary of State website. This enterprise-grade tool systematically extracts and structures business entity data with **advanced CAPTCHA solving capabilities**, robust error handling, and professional output management.

## 🚀 Overview

The Kansas SOS Business Crawler is designed to automate the extraction of business entity information through intelligent web navigation, **automatic CAPTCHA resolution**, multi-layered data extraction, and comprehensive error management. It transforms unstructured web data into structured, analyzable business intelligence.

## ✨ Key Features

### 🤖 Intelligent Automation
- **Smart Navigation**: Natural browsing pattern from homepage to business search
- **Form Automation**: Automated search parameter configuration
- **Dynamic Element Detection**: Adaptive element identification with multiple fallback strategies
- **CAPTCHA Automation**: Integrated 2Captcha service for automatic solving

### 🛡️ CAPTCHA Management
- **Automatic Solving**: 2Captcha API integration for reCAPTCHA v2
- **Manual Fallback**: Built-in manual solving option when automated service fails
- **Balance Tracking**: Real-time monitoring of 2Captcha balance and cost estimation
- **Multi-point Protection**: CAPTCHA detection at navigation, search, and detail pages

### 📊 Comprehensive Data Extraction
- **Business Identification**: Entity names, IDs, and registration details
- **Entity Classification**: Business types, status, and jurisdiction information
- **Contact Information**: Resident agents and office addresses
- **Compliance Data**: Reporting requirements and filing deadlines

### 🛡️ Enterprise Reliability
- **Multi-layer Error Handling**: Primary, secondary, and tertiary extraction methods
- **Session Persistence**: Robust recovery from interruptions and timeouts
- **Data Validation**: Completeness checking and quality assurance

### 💾 Professional Output
- **Structured JSON**: Clean, normalized business data
- **Hierarchical Storage**: Organized by extraction status and data type
- **Audit Trail**: Comprehensive logging and activity monitoring

## 🔧 Automation & CAPTCHA Features

### 🎯 Automated CAPTCHA Solving
The crawler features **built-in CAPTCHA automation** using the 2Captcha service:

```python
# 2Captcha Integration Example
self.solver = TwoCaptcha(API_KEY)
result = self.solver.recaptcha(
    sitekey=site_key,
    url=page_url
)
```
⚡ Performance Metrics
CAPTCHA Success Rate: 95%+ with 2Captcha integration

Solving Time: 10-30 seconds per CAPTCHA

Cost Efficiency: $0.00077 per CAPTCHA (~3,800 solves per $3)

Balance Management: Automatic balance checking and warnings

🔄 Fallback Mechanisms
Primary: 2Captcha automated solving

Secondary: Manual solving with user prompts

Tertiary: Session recovery and retry logic

🏗️ Architecture
Navigation Flow
text
Homepage (sos.ks.gov) → CAPTCHA Check → Business Search → 
Automated Setup → CAPTCHA Check → Search Execution → 
Data Extraction → Structured Storage
Extraction Strategy
Primary Method: Direct element targeting using known CSS selectors

Secondary Method: Table-based parsing and pattern recognition

Tertiary Method: Text analysis and regular expression matching

CAPTCHA Flow
text
CAPTCHA Detection → Site Key Extraction → 2Captcha API Call → 
Response Injection → Solution Verification → Continue Automation
🚀 Getting Started
Installation
bash
# Clone repository
git clone https://github.com/codingwithrsn33/Kansas-Site-Crawling.git
cd Kansas-Site-Crawling

# Install dependencies
pip install playwright twocaptcha

# Install Playwright browsers
playwright install chromium

# Optional: Configure 2Captcha API key
export CAPTCHA_API_KEY="your_2captcha_api_key_here"
Execution
bash
python sos_crawler.py
⚙️ Automation Configuration
2Captcha Setup
Sign Up: Register at 2captcha.com

Add Funds: Minimum $3 recommended (~3,800 CAPTCHAs)

API Integration: Add your API key to the crawler

python
# Configuration in sos_crawler.py
self.captcha_api_key = "9f5b2e46ccade5230e0f09f590e1960a"
Performance Settings
python
# For faster crawling (with CAPTCHA solving)
self.micro_delay(0.2, 0.5)  # Shorter delays between actions

# For reliable crawling (recommended)
self.reliable_delay(2, "CAPTCHA processing")  # Documented delays

# CAPTCHA solving timeout
self.captcha_timeout = 30  # Seconds to wait for CAPTCHA solution
📋 Default Search Configuration
The system automatically processes these business entity types:

Category	Search Terms	Target Entities
Test Samples	AA, AAB, AAC	Validation and testing
Corporate Entities	LLC, INC, CORP	Business structures
Industry Focus	SERVICE, KANSAS	Regional and service businesses
📁 Output Structure
text
kansas_business_data/
├── 📊 json/                           # Successful extractions
│   └── business_{name}_{timestamp}.json
├── 🔧 html_fallback/                  # Source preservation
│   └── {context}_{timestamp}.html
├── 📝 errors/                         # Diagnostic information
│   ├── error_{term}_{timestamp}.json
│   └── diagnostic_data/
├── 📸 screenshots/                    # Debug screenshots
├── 📋 crawler.log                     # System activity
└── 📊 captcha_stats.json             # CAPTCHA solving statistics
📊 Data Schema
Business Entity Record
json
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
    "principal_office_address": "123 Main St, Kansas City, KS 66101"
  },
  "automation_metadata": {
    "captcha_solved": true,
    "captcha_method": "2captcha",
    "solving_time_seconds": 15.5
  },
  "metadata": {
    "extraction_timestamp": "2024-01-15T10:30:00Z",
    "search_term": "LLC",
    "processing_status": "success"
  }
}
⚙️ Configuration
Search Parameters
Modify the search terms in the main execution method:

python
search_terms = [
    "LLC", "INC", "CORP", 
    "SERVICE", "CONSTRUCTION",
    "CONSULTING", "TECHNOLOGY"
]
Processing Limits
Adjust the number of entities processed per search term:

python
# Process first 5 businesses per search term
for business in businesses[:5]:
    process_business(business)
CAPTCHA Settings
python
# Enable/disable automated CAPTCHA solving
self.use_captcha_solver = True

# Set manual solving preference
self.manual_captcha_fallback = True

# Configure solving attempts
self.max_captcha_attempts = 3
🎯 Performance Features
Rate Management
Configurable delays between requests

Respectful crawling practices

Adaptive timing based on response patterns

CAPTCHA-aware rate limiting

Quality Assurance
Data validation at extraction points

Cross-reference verification

Completeness scoring

CAPTCHA success rate monitoring

Monitoring
Real-time progress tracking

Success rate analytics

Performance metrics collection

CAPTCHA cost tracking

📈 Automation Performance
Time Estimates (with CAPTCHA)
Component	Fast Mode	Reliable Mode
Navigation + CAPTCHA	10-15 sec	15-25 sec
Search Setup	1-2 sec	2-3 sec
Results Extraction	1-2 sec	3-5 sec
Business Detail	2-3 sec	5-8 sec
Total per Business	~15 sec	~30 sec
CAPTCHA Cost Analysis
Cost per CAPTCHA: $0.00077

Typical Balance: $2.87 ≈ 3,726 CAPTCHAs

Usage Pattern: 1-3 CAPTCHAs per business

Business Capacity: 1,200-3,700 businesses per $3

Solving Success Rate: 95%+ with 2Captcha

🔧 Technical Specifications
Requirements
Python: 3.7+

Browser Automation: Playwright with Chromium

CAPTCHA Service: 2Captcha API key (optional)

Memory: 2GB+ RAM recommended

Storage: 1GB+ for output data

Supported Data Elements
Business identification numbers

Entity names and types

Registration dates and status

Geographic information

Compliance timelines

Contact details

CAPTCHA solving metadata

📈 Enterprise Integration
Data Export
Structured JSON format

Batch processing capabilities

Incremental extraction support

Metadata enrichment

CAPTCHA statistics reporting

Monitoring & Analytics
Extraction success rates

Processing efficiency metrics

Error pattern analysis

Performance trend tracking

CAPTCHA cost optimization

🛠️ Operational Excellence
Error Recovery
Automatic retry mechanisms

Session state preservation

Graceful degradation

Comprehensive diagnostics

CAPTCHA solving fallbacks

Maintenance
Regular dependency updates

Extraction rule validation

Performance optimization

Storage management

CAPTCHA service monitoring

🔒 Privacy & Compliance
CAPTCHA Service Terms
Comply with 2Captcha terms of service

Respect website CAPTCHA implementation

Use automated solving responsibly

Monitor usage to prevent abuse

Best Practices
Implement appropriate delays

Respect robots.txt directives

Don't overload target servers

Use data for legitimate purposes

Maintain CAPTCHA service ethics

👨‍💻 Developer Information
Rohan Subhash Darekar
Python Developer & Automation Specialist
📞 +91 9075237180
📧 rohandarekar307@gmail.com
🔗 GitHub Profile
