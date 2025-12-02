# Kansas SOS Business Data Crawler

## 📋 Project Overview
A comprehensive web crawler built with Playwright to extract business entity data from the Kansas Secretary of State website. The crawler automates the process of searching for businesses and extracting complete corporate information with reliable error handling and CAPTCHA solving capabilities.

## ✨ Features

### 🚀 Core Functionality
- **Complete Automation**: Navigates from homepage to search page automatically
- **Multi-term Search**: Searches for various business types (AA, LLC, INC, CORP, etc.)
- **Data Extraction**: Extracts 30+ business fields including addresses, officers, filing dates
- **Error Handling**: Robust error recovery with detailed logging
- **Data Validation**: Checks for data completeness and quality

### 🛡️ CAPTCHA Handling
- **2Captcha Integration**: Automatic CAPTCHA solving service
- **Manual Fallback**: Manual solving option when automated service fails
- **Balance Tracking**: Monitors 2Captcha balance and estimates remaining solves
- **Multi-step Protection**: Handles CAPTCHAs at navigation, search, and detail pages

### 📁 Output Management
- **Individual JSON Files**: Each business saved separately
- **Combined Dataset**: All businesses combined into master JSON file
- **HTML Fallback**: Saves HTML when JSON parsing fails
- **Screenshots**: Captures screenshots at key steps for debugging
- **Comprehensive Logging**: Detailed log files with timestamps

## 🏗️ Architecture

### Project Structure
kansas_business_data/
├── json/ # Individual business JSON files
├── html_fallback/ # HTML files when JSON fails
├── errors/ # Error logs and failed extractions
├── logs/ # Application logs
├── screenshots/ # Debug screenshots
└── all_businesses_[timestamp].json # Combined dataset

text

### Data Flow
1. **Navigation**: Homepage → Search Page
2. **Search Setup**: Configure search parameters
3. **Results Extraction**: Parse business listings
4. **Detail Extraction**: Click each business and extract data
5. **Data Saving**: Save to JSON with validation
6. **Iteration**: Return to search for next term

## 🔧 Installation

### Prerequisites
- Python 3.8+
- Playwright browser binaries
- 2Captcha API key (optional)

### Setup
```bash
# Clone or download the project
cd kansas_business_data_crawler

# Install dependencies
pip install playwright twocaptcha

# Install Playwright browsers
playwright install chromium

# Optional: Set up 2Captcha API key
export CAPTCHA_API_KEY="your_2captcha_api_key_here"

```
🚀 Usage
Basic Usage
bash
python sos_crawler.py
Configuration Options
The crawler can be configured by modifying these parameters:

Search Terms: Edit search_terms list in run_reliable_crawler() method

Business Limit: Change number of businesses processed per term

Delay Settings: Adjust timing in reliable_delay() method

Output Directory: Modify output_dir variable

📊 Data Output
Sample Business Record
json
{
  "business_id": "1234567",
  "business_name": "EXAMPLE LLC",
  "type": "Limited Liability Company",
  "formation_date": "2020-01-15",
  "jurisdiction": "Kansas",
  "status": "Active",
  "resident_agent": "John Smith",
  "principal_office_address": "123 Main St | Kansas City, KS 66101",
  "registered_office_address": "456 Registered Ave | Overland Park, KS 66204",
  "last_reporting_year": "2023",
  "next_report_due_date": "2024-04-15",
  "search_term": "LLC",
  "extracted_at": "2024-01-15T14:30:00",
  "source_url": "https://www.sos.ks.gov/...",
  "data_completeness": "complete"
}
Extracted Fields
Core Information: Business ID, Name, Type, Status

Dates: Formation, Filing, Forfeiture, Reinstatement

Addresses: Principal and Registered offices

Compliance: Last reporting year, Next report due

Officers: Resident Agent, Officers/Directors

Business Details: NAICS code, Business purpose

Metadata: Search term, Extraction timestamp, Source URL

⚙️ Configuration
2Captcha Setup
Sign up at 2captcha.com

Get your API key

Add funds to your account ($3 ≈ 3,800 CAPTCHAs)

Update the API key in the script:

python
self.captcha_api_key = "your_api_key_here"
Performance Settings
python
# For faster crawling (less reliable)
self.micro_delay(0.2, 0.5)  # Shorter delays

# For reliable crawling (recommended)
self.reliable_delay(2, "reason")  # Longer, documented delays

# For maximum reliability
wait_until="networkidle"  # Wait for full page load
🛠️ Troubleshooting
Common Issues
1. CAPTCHA Solving Fails
Solution: Check 2Captcha balance and API key

Fallback: Manual solving option built-in

Debug: Check captcha_stats in output

2. No Results Found
Check: Search terms may be too specific

Verify: Website structure hasn't changed

Test: Try broader search terms like "AA" or "LLC"

3. Browser Crashes
Increase: Timeout values in wait_for_selector

Check: Internet connection stability

Reduce: Number of parallel processes if using them

4. Incomplete Data
Enable: Screenshots for debugging

Check: HTML fallback files

Increase: Wait times before extraction

Debug Mode
The script includes comprehensive logging:

python
# Check logs
tail -f kansas_business_data/logs/detailed.log

# View screenshots
ls kansas_business_data/screenshots/

# Check errors
ls kansas_business_data/errors/
📈 Performance
Time Estimates
Component	Fast Mode	Reliable Mode
Navigation	2-3 sec	5-10 sec
Search Setup	1 sec	2-3 sec
Results Extraction	1-2 sec	3-5 sec
Business Detail	2-3 sec	5-8 sec
Total per Business	~5 sec	~15 sec
2Captcha Costs
Balance: $2.87 ≈ 3,726 CAPTCHAs

Cost per CAPTCHA: $0.00077

Estimated Usage: 1-3 CAPTCHAs per business

Total Businesses Possible: 1,200-3,700

🔒 Privacy & Legal
Important Considerations
Terms of Service: Review Kansas SOS website terms

Rate Limiting: Implement delays to avoid being blocked

Data Usage: Use extracted data responsibly

CAPTCHA Solving: 2Captcha is a paid service - comply with their terms

Best Practices
Add delays between requests

Respect robots.txt

Don't overload the server

Use data for legitimate purposes only

Consider implementing a user agent rotation

🚀 Advanced Features
Customization Options
Field Selection: Modify extract_complete_business_data() to choose which fields to extract

Parallel Processing: Implement ThreadPoolExecutor for faster crawling

Proxy Support: Add proxy rotation to avoid IP blocking

Database Storage: Modify save_business_data_completely() to store in SQL database

Scheduled Runs: Add scheduling with cron or APScheduler

Extending the Crawler
python
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

👨‍💻 Developer
Rohan Subhash Darekar
📞 Contact: 9075237180

