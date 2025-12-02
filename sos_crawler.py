import time
import random
from playwright.sync_api import sync_playwright
import json
import os
from datetime import datetime
import re
import logging
from twocaptcha import TwoCaptcha

class KansasSOSCrawler:
    def __init__(self, headless=False):
        print("🚀 Kansas SOS Business Crawler - FAST AUTOMATION")
        print("✅ Optimized for speed with minimal delays")
        print("="*60)
        
        # Initialize 2Captcha solver
        self.captcha_api_key = "9f5b2e46ccade5230e0f09f590e1960a"
        self.solver = None
        self.captcha_stats = {'attempts': 0, 'success': 0}
        
        try:
            self.solver = TwoCaptcha(self.captcha_api_key)
            # Check balance
            balance = self.solver.balance()
            print(f"💰 2Captcha Balance: ${balance}")
            print("✅ 2Captcha service initialized successfully!")
        except Exception as e:
            print(f"❌ 2Captcha initialization failed: {e}")
            print("⚠️  Will use manual fallback mode")
        
        # Setup browser
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(
            headless=headless,
            args=['--disable-blink-features=AutomationControlled']
        )
        self.context = self.browser.new_context(
            viewport={'width': 1200, 'height': 800},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        )
        self.page = self.context.new_page()
        self.output_dir = "kansas_business_data"
        
        # Setup directories and logging
        self.setup_directories()
        self.setup_logging()
        
    def setup_directories(self):
        """Create comprehensive output directory structure"""
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(f"{self.output_dir}/json", exist_ok=True)
        os.makedirs(f"{self.output_dir}/html_fallback", exist_ok=True)
        os.makedirs(f"{self.output_dir}/errors", exist_ok=True)
        print("✅ Created comprehensive output directories")

    def setup_logging(self):
        """Setup logging for error tracking"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(f"{self.output_dir}/crawler.log"),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        self.logger.info("Kansas SOS Crawler started with complete automation")

    def quick_delay(self, min_sec=0.5, max_sec=1.5):
        """Fast random delay for speed optimization"""
        time.sleep(random.uniform(min_sec, max_sec))
        
    def check_and_solve_captcha_fast(self):
        """Fast CAPTCHA checking and solving"""
        self.captcha_stats['attempts'] += 1
        print(f"🛡️ Checking for CAPTCHA (Attempts: {self.captcha_stats['attempts']}, Success: {self.captcha_stats['success']})...")
        
        # Quick check for CAPTCHA
        time.sleep(0.5)
        
        # Check for CAPTCHA elements
        captcha_selectors = [
            ".g-recaptcha",
            "iframe[src*='recaptcha']",
            "#recaptcha",
            "[data-sitekey]"
        ]
        
        has_captcha = False
        site_key = None
        
        for selector in captcha_selectors:
            element = self.page.query_selector(selector)
            if element:
                has_captcha = True
                print(f"✅ Found reCAPTCHA: {selector}")
                
                # Try to get site key
                if selector == ".g-recaptcha" or selector == "[data-sitekey]":
                    site_key = element.get_attribute("data-sitekey")
                elif selector == "iframe[src*='recaptcha']":
                    src = element.get_attribute("src")
                    if src:
                        match = re.search(r'k=([^&]+)', src)
                        if match:
                            site_key = match.group(1)
                break
        
        if not has_captcha:
            print("✅ No CAPTCHA detected")
            return True
        
        # Try to solve with 2Captcha
        if self.solver and site_key:
            try:
                print(f"🤖 Solving reCAPTCHA...")
                print(f"🔑 Site key: {site_key}")
                
                result = self.solver.recaptcha(
                    sitekey=site_key,
                    url=self.page.url,
                    invisible=False
                )
                
                if result and 'code' in result:
                    self.captcha_stats['success'] += 1
                    print(f"✅ reCAPTCHA solved: {result['code'][:20]}...")
                    
                    # Inject the solution
                    self.page.evaluate(f"""
                        document.getElementById('g-recaptcha-response').innerHTML = '{result['code']}';
                        if (typeof ___grecaptcha_cfg !== 'undefined') {{
                            Object.entries(___grecaptcha_cfg.clients).forEach(([key, client]) => {{
                                if (client.callback) {{
                                    client.callback('{result['code']}');
                                }}
                            }});
                        }}
                    """)
                    
                    self.quick_delay(1, 2)
                    print("✅ reCAPTCHA solved successfully!")
                    return True
                    
            except Exception as e:
                print(f"❌ 2Captcha solving failed: {e}")
        
        # Manual fallback
        print("\n" + "="*60)
        print("🛑 MANUAL CAPTCHA REQUIRED")
        print("Please solve the CAPTCHA in browser")
        print("Press Enter here when done...")
        print("="*60)
        input("Press Enter AFTER solving CAPTCHA...")
        print("✅ Continuing automation...")
        self.quick_delay()
        return True

    def navigate_and_search_fast(self, search_term):
        """Fast navigation and search setup - WITH HOMEPAGE FIRST"""
        print(f"🔍 Setting up search for: '{search_term}'")
        
        try:
            # 1. FIRST: Go to the main homepage
            homepage_url = "https://sos.ks.gov/"
            print(f"🌐 Visiting homepage: {homepage_url}")
            self.page.goto(homepage_url, wait_until="domcontentloaded")
            self.quick_delay(1, 2)
            
            # Optional: Check for CAPTCHA on homepage
            self.check_and_solve_captcha_fast()
            
            # 2. SECOND: Navigate to Business Search page
            search_url = "https://www.sos.ks.gov/eforms/BusinessEntity/Search.aspx"
            print(f"🔍 Navigating to search page: {search_url}")
            self.page.goto(search_url, wait_until="domcontentloaded")
            self.quick_delay(1, 2)
            
            # Check CAPTCHA on search page
            self.check_and_solve_captcha_fast()
            
            # 3. Setup search parameters
            print("⚙️ Setting up search parameters...")
            
            # Select Business Name radio
            biz_name_radio = self.page.query_selector("#MainContent_rblSearchType_0")
            if biz_name_radio:
                biz_name_radio.click()
            
            # Select Contains radio
            contains_radio = self.page.query_selector("#MainContent_rblNameSearchType_0")
            if contains_radio:
                contains_radio.click()
            
            # Enter search term
            search_input = self.page.query_selector("#MainContent_txtSearchEntityName")
            if search_input:
                search_input.fill("")
                search_input.fill(search_term)
                print(f"✅ Entered search term: '{search_term}'")
            
            # 4. Perform search
            search_btn = self.page.query_selector("#MainContent_btnSearchEntity")
            if search_btn:
                search_btn.click()
                print("🔎 Performing search...")
                self.quick_delay(2, 3)
                
                # Check CAPTCHA after search
                self.check_and_solve_captcha_fast()
                return True
            
            return False
            
        except Exception as e:
            print(f"❌ Search setup failed: {e}")
            return False

    def extract_business_links_from_results(self):
        """Extract business links from results page - FAST VERSION"""
        print("📋 Extracting business links...")
        businesses = []
        
        try:
            # Look for results table
            results_table = self.page.query_selector("table.gvResults")
            if not results_table:
                print("❌ No results table found")
                return businesses
            
            # Extract rows quickly
            rows = results_table.query_selector_all("tr")
            print(f"Found {len(rows)} rows")
            
            # Process rows (skip header)
            for i in range(1, min(6, len(rows))):  # Limit to 5 results for speed
                row = rows[i]
                cells = row.query_selector_all("td")
                
                if len(cells) >= 3:
                    biz_id = cells[0].text_content().strip()
                    biz_name = cells[1].text_content().strip()
                    
                    if biz_name and len(biz_name) > 1:
                        businesses.append({
                            'name': biz_name,
                            'id': biz_id,
                            'row_index': i
                        })
                        print(f"  ✅ {biz_name[:40]}...")
            
            return businesses
            
        except Exception as e:
            print(f"❌ Error extracting links: {e}")
            return businesses

    def click_business_fast(self, business_info):
        """Click on business link quickly"""
        print(f"  👆 Clicking: {business_info['name'][:30]}...")
        
        try:
            # Find the select button in the row
            row_index = business_info['row_index']
            select_button = self.page.query_selector(f"table.gvResults tr:nth-child({row_index + 1}) input[value='Select Business']")
            
            if select_button:
                select_button.click()
                self.quick_delay(2, 3)
                
                # Check for CAPTCHA
                self.check_and_solve_captcha_fast()
                return True
            
            return False
            
        except Exception as e:
            print(f"  ❌ Click failed: {e}")
            return False

    def extract_business_details_fast(self):
        """Fast business details extraction"""
        business_data = {}
        
        try:
            # Quick extraction of main fields
            fields = {
                'business_id': '#MainContent_lblEntityID',
                'business_name': '#MainContent_lblEntityName',
                'type': '#MainContent_lblEntityType',
                'status': '#MainContent_lblEntityStatus',
                'formation_date': '#MainContent_lblFormationDate',
                'resident_agent': '#MainContent_lblResidentAgentName'
            }
            
            for field, selector in fields.items():
                element = self.page.query_selector(selector)
                if element:
                    business_data[field] = element.text_content().strip()
            
            # Extract addresses quickly
            address_parts = []
            addr1 = self.page.query_selector("#MainContent_lblPOAddress")
            if addr1:
                address_parts.append(addr1.text_content().strip())
            
            city = self.page.query_selector("#MainContent_lblPOAddressCity")
            state = self.page.query_selector("#MainContent_lblPOAddressState")
            zip_code = self.page.query_selector("#MainContent_lblPOAddressZip")
            
            if city or state or zip_code:
                location = f"{city.text_content().strip() if city else ''}, {state.text_content().strip() if state else ''} {zip_code.text_content().strip() if zip_code else ''}".strip(", ")
                if location:
                    address_parts.append(location)
            
            if address_parts:
                business_data['address'] = " | ".join(address_parts)
            
            return business_data
            
        except Exception as e:
            print(f"  ❌ Extraction error: {e}")
            return business_data

    def return_to_results_fast(self):
        """Quick return to results page"""
        try:
            return_btn = self.page.query_selector("#MainContent_btnReturnToSearchResults")
            if return_btn:
                return_btn.click()
            else:
                self.page.go_back()
            self.quick_delay()
            return True
        except Exception as e:
            print(f"  ❌ Return failed: {e}")
            return False

    def save_business_data(self, data, search_term, index):
        """Save business data quickly"""
        try:
            if data.get('business_name'):
                clean_name = re.sub(r'[^\w]', '_', data['business_name'])[:30]
                filename = f"{self.output_dir}/json/{search_term}_{index}_{clean_name}.json"
            else:
                filename = f"{self.output_dir}/json/{search_term}_{index}_unknown.json"
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            print(f"    💾 Saved: {filename}")
            return filename
            
        except Exception as e:
            print(f"    ❌ Save failed: {e}")
            return None

    def run_fast_crawler(self):
        """Main fast crawling method"""
        search_terms = ["AA", "AAB", "AAC", "LLC", "INC"]
        all_data = []
        
        print("🚀 STARTING FAST CRAWLER")
        print(f"📊 Search terms: {search_terms}")
        print("="*60)
        
        for search_term in search_terms:
            print(f"\n{'='*50}")
            print(f"SEARCHING: '{search_term}'")
            print(f"CAPTCHA Stats: Attempts={self.captcha_stats['attempts']}, Success={self.captcha_stats['success']}")
            print(f"{'='*50}")
            
            # Navigate and search
            if not self.navigate_and_search_fast(search_term):
                print(f"❌ Failed to search for '{search_term}'")
                continue
            
            # Extract business links
            businesses = self.extract_business_links_from_results()
            
            if not businesses:
                print(f"❌ No results for '{search_term}'")
                continue
            
            print(f"📊 Found {len(businesses)} businesses")
            
            # Process businesses (limit to 2 for speed)
            for i, business in enumerate(businesses[:2]):
                print(f"\n  [{i+1}/{min(2, len(businesses))}] Processing: {business['name'][:40]}...")
                
                # Click business
                if self.click_business_fast(business):
                    # Extract details
                    details = self.extract_business_details_fast()
                    
                    # Add metadata
                    details['search_term'] = search_term
                    details['extracted_at'] = datetime.now().isoformat()
                    details['source_url'] = self.page.url
                    
                    # Save data
                    saved_file = self.save_business_data(details, search_term, i)
                    
                    if details.get('business_name'):
                        all_data.append(details)
                        print(f"    ✅ Extracted: {details.get('business_name')}")
                    else:
                        print(f"    ⚠️  Partial data extracted")
                    
                    # Return for next business
                    if i < len(businesses[:2]) - 1:
                        self.return_to_results_fast()
                else:
                    print(f"    ❌ Failed to access business details")
            
            # Quick delay between search terms
            if search_term != search_terms[-1]:
                print("\n🔄 Preparing for next search term...")
                self.quick_delay()
        
        # Save combined data
        if all_data:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            combined_file = f"{self.output_dir}/all_businesses_{timestamp}.json"
            
            combined_data = {
                'total_companies': len(all_data),
                'search_terms_used': search_terms,
                'extraction_date': datetime.now().isoformat(),
                'companies': all_data
            }
            
            with open(combined_file, 'w', encoding='utf-8') as f:
                json.dump(combined_data, f, indent=2, ensure_ascii=False)
            
            print(f"\n🎉 CRAWLING COMPLETED!")
            print(f"📊 Total records: {len(all_data)}")
            print(f"📁 Combined file: {combined_file}")
            print(f"📁 Individual files in: {self.output_dir}/json/")
            
        else:
            print(f"\n❌ No data collected")
        
        # Close browser
        self.close()

    def close(self):
        """Close browser resources"""
        try:
            if hasattr(self, 'context'):
                self.context.close()
            if hasattr(self, 'browser'):
                self.browser.close()
            if hasattr(self, 'playwright'):
                self.playwright.stop()
            print("✅ Browser closed successfully")
        except Exception as e:
            print(f"❌ Error closing: {e}")

def main():
    print("Kansas SOS Business Crawler - FAST AUTOMATION")
    print("="*60)
    print("Features:")
    print("✅ Ultra-fast crawling with minimal delays")
    print("✅ 2Captcha integration for CAPTCHA solving")
    print("✅ First visits homepage, then search page")
    print("✅ Fast page navigation and extraction")
    print("✅ Error handling and logging")
    print("="*60)
    
    crawler = KansasSOSCrawler(headless=False)
    
    try:
        crawler.run_fast_crawler()
    except KeyboardInterrupt:
        print("\n⏹️ Crawling stopped by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
    finally:
        crawler.close()

if __name__ == "__main__":
    main()