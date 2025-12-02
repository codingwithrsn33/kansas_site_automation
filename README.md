# Kansas SOS Business Data Crawler 🏢

A comprehensive automation solution for business intelligence gathering from the Kansas Secretary of State website. This enterprise-grade tool systematically extracts business entity data with intelligent navigation, CAPTCHA solving, and professional output management.

## 🚀 Overview
The Kansas SOS Business Crawler automates the extraction of business entity information through intelligent web navigation, multi-layered data extraction, and comprehensive error management. It transforms unstructured web data into structured, analyzable business intelligence.

## ✨ Key Features

### 🤖 Intelligent Automation
- **Smart Navigation**: Natural browsing from homepage to business search with CAPTCHA handling
- **Form Automation**: Automated search parameter configuration
- **Dynamic Detection**: Adaptive element identification with multiple fallback strategies
- **CAPTCHA Management**: Automatic solving with 2Captcha integration

### 📊 Comprehensive Data Extraction
- **Business Identification**: Entity names, IDs, and registration details
- **Entity Classification**: Business types, status, and jurisdiction information
- **Contact Information**: Resident agents and complete office addresses
- **Compliance Data**: Reporting requirements and filing deadlines
- **Metadata**: Extraction timestamps and source tracking

### 🛡️ Enterprise Reliability
- **Multi-layer Error Handling**: Primary, secondary, and tertiary extraction methods
- **CAPTCHA Management**: Automated solving with manual intervention fallback
- **Session Persistence**: Robust recovery from interruptions and timeouts
- **Data Validation**: Completeness checking and quality assurance

### 💾 Professional Output
- **Structured JSON**: Clean, normalized business data (30+ fields)
- **Hierarchical Storage**: Organized by extraction status and data type
- **Audit Trail**: Comprehensive logging and activity monitoring
- **HTML Fallback**: Source preservation for debugging

## 🏗️ Architecture

### Navigation Flow
Homepage (sos.ks.gov) → CAPTCHA Check → Search Page → Automated Setup → Search Execution → Results Processing → Business Detail Extraction → Structured Storage

### Extraction Strategy
1. **Primary Method**: Direct element targeting using known CSS selectors
2. **Secondary Method**: Table-based parsing and pattern recognition
3. **Tertiary Method**: Text analysis and regular expression matching

### Project Structure

kansas_business_data/
├── 📊 json/ # Individual business JSON files
├── 🔧 html_fallback/ # HTML files when JSON fails
├── 📝 errors/ # Error logs and failed extractions
├── 📋 logs/ # Application logs
├── 📸 screenshots/ # Debug screenshots
└── 📁 all_businesses_[timestamp].json # Combined dataset


## 🚀 Getting Started

### Installation
```bash
# Clone repository
git clone https://github.com/codingwithrsn33/Kansas-Site-Crawling.git
cd Kansas-Site-Crawling

# Install dependencies
pip install playwright twocaptcha

# Install Playwright browsers
playwright install chromium

# Optional: Set up 2Captcha API key
export CAPTCHA_API_KEY="your_2captcha_api_key_here"

Execution

python sos_crawler.py

📋 Default Search Configuration
The system automatically processes these business entity types:

Category	Search Terms	Target Entities
Test Samples	AA, AAB, AAC	Validation and testing
Corporate Entities	LLC, INC, CORP	Business structures
Industry Focus	SERVICE, KANSAS	Regional and service businesses
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
Modify the search terms in the main execution method:
search_terms = ["AA", "AAB", "AAC", "LLC", "INC", "CORP", "SERVICE", "KANSAS"]

Processing Limits
Adjust the number of entities processed per search term:
# Process first 3 businesses per search term
for business in businesses[:3]:
    process_business(business)

CAPTCHA Configuration

# Enable 2Captcha service
self.captcha_api_key = "your_2captcha_api_key"

# Or use manual fallback
self.solver = None  # Disable automated solving

🎯 Performance Features
Rate Management
Configurable delays between requests (0.2-1.5 seconds)

Respectful crawling practices

Adaptive timing based on response patterns

Quality Assurance
Data validation at extraction points

Cross-reference verification

Completeness scoring for each record

Monitoring
Real-time progress tracking

Success rate analytics

Performance metrics collection

CAPTCHA solving statistics

📈 Performance Metrics
Time Estimates
Component	Fast Mode	Reliable Mode
Navigation	2-3 sec	5-10 sec
Search Setup	1 sec	2-3 sec
Results Extraction	1-2 sec	3-5 sec
Business Detail	2-3 sec	5-8 sec
Total per Business	~5 sec	~15 sec
2Captcha Cost Analysis
Cost per CAPTCHA: $0.00077

Balance $2.87: ≈ 3,726 CAPTCHAs

Usage per Business: 1-3 CAPTCHAs

Total Businesses Possible: 1,200-3,700

🔧 Technical Specifications
Requirements
Python: 3.8+

Browser Automation: Playwright with Chromium

Memory: 2GB+ RAM recommended

Storage: 1GB+ for output data

Supported Data Elements
Business identification numbers

Entity names and types

Registration dates and status

Geographic information

Compliance timelines

Contact details (30+ fields)

🛠️ Operational Excellence
Error Recovery
Automatic retry mechanisms

Session state preservation

Graceful degradation

Comprehensive diagnostics

Maintenance Features
Regular dependency updates

Extraction rule validation

Performance optimization

Storage management

🔒 Privacy & Legal Compliance
Important Considerations
Terms of Service: Respect Kansas SOS website terms

Rate Limiting: Implement delays to avoid being blocked

Data Usage: Use extracted data responsibly

CAPTCHA Solving: Comply with 2Captcha service terms

Best Practices
Add appropriate delays between requests

Respect robots.txt directives

Don't overload the server

Use data for legitimate purposes only

Consider implementing user agent rotation

🚀 Advanced Features
Customization Options
Field Selection: Modify extract_complete_business_data() to choose specific fields

Parallel Processing: Implement ThreadPoolExecutor for faster crawling

Proxy Support: Add proxy rotation to avoid IP blocking

Database Storage: Modify save_business_data_completely() to store in SQL database

Scheduled Runs: Add scheduling with cron or APScheduler

Extending the Crawler

# Add new search terms
search_terms = ["LLC", "INC", "CORP", "CO", "LP", "LLP", "PC"]

# Add custom fields
custom_fields = {
    'tax_id': '#TaxIDSelector',
    'license_number': '#LicenseSelector'
}

# Implement retry logic
max_retries = 3
retry_delay = 5

📚 Dependencies
Python Packages
playwright: Browser automation

twocaptcha: CAPTCHA solving service

json: Data serialization

logging: Application logging

datetime: Timestamp handling

re: Regular expressions

os: File system operations

Browser Requirements
Chromium (installed via Playwright)

2GB+ RAM recommended

Stable internet connection

👨‍💻 Developer Information
Rohan Subhash Darekar
Python Developer
📞 +91 9075237180
📧 rohandarekar307@gmail.com
🔗 GitHub Profile

