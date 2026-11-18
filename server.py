import os
import json
import urllib.request
import urllib.error
from http.server import SimpleHTTPRequestHandler, HTTPServer
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('GEMINI_API_KEY', '')

class WarRoomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path in ('', '/', '/index.html'):
            self.path = '/dashboard.html'
        return super().do_GET()

    def end_headers(self):
        # Enable CORS and caching headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        if self.path == '/api/gemini-scout':
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8')
            
            try:
                req_data = json.loads(body)
                user_query = req_data.get('query', '').strip()
                
                if not user_query:
                    self.send_json({'reply': 'Please provide a scouting query or choose one of the quick war room prompts.'})
                    return
                    
                # Call Gemini API
                reply = self.call_gemini_scout(user_query)
                self.send_json({'reply': reply})
            except Exception as e:
                self.send_json({'reply': f"War Room Assistant Error: {str(e)}", 'error': True})
        else:
            self.send_error(404, "Endpoint Not Found")

    def send_json(self, data):
        response_bytes = json.dumps(data).encode('utf-8')
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(response_bytes)))
        self.end_headers()
        self.wfile.write(response_bytes)

    def call_gemini_scout(self, query):
        if not API_KEY:
            return self.deterministic_fallback(query)
            
        system_instruction = (
            "You are the Rajasthan Royals Lead Auction Strategist & Cricket Data Scientist in the IPL 2027 War Room (ITC Grand Goa, Dec 16, 2026). "
            "You have direct access to 200,999 deliveries (IPL 2022-2026 and T20Is) and the official BCCI 18 November 2026 Retention/Release database.\n"
            "RR SQUAD CONTEXT:\n"
            "• Retained Squad (19 Players): Yashasvi Jaiswal, Ravindra Jadeja (Trade), Mohammed Shami (Trade), Riyan Parag, Dhruv Jurel, Jofra Archer, Sandeep Sharma, Ravi Bishnoi, Nandre Burger, Dasun Shanaka, Donovan Ferreira, Lhuan-dre Pretorius, Manimaran Siddharth (Trade), Shubham Dubey, Vaibhav Sooryavanshi, Sushant Mishra, Aman Rao Perala, Brijesh Sharma, Yash Raj Punja.\n"
            "• Remaining Purse: ₹27.05 Cr | Open Slots: 6 (Max 3 Overseas).\n\n"
            "OFFICIAL TOP 10 AUCTION TARGETS:\n"
            "TOP 10 BATSMEN (100% VERIFIED AUCTION ELIGIBLE):\n"
            "1. Ajinkya Rahane (Indian | KKR | PPI: 68.88 | Press SR: 147.47 | No. 3 Anchor, replaces Samson | Max Bid: ₹4.5 Cr)\n"
            "2. Nitish Rana (Indian | DC | PPI: 66.60 | Press SR: 155.06 | Spin Destroyer in Middle Overs | Max Bid: ₹7.0 Cr)\n"
            "3. Nehal Wadhera (Indian | PBKS | PPI: 62.32 | Press SR: 145.20 | Left-Hand Clutch Finisher | Max Bid: ₹7.5 Cr)\n"
            "4. Shimron Hetmyer (Overseas | RR | PPI: 65.82 | Press SR: 155.92 | Proven RR Death Finisher Buy-back | Max Bid: ₹8.5 Cr)\n"
            "5. Rahul Tripathi (Indian | KKR | PPI: 57.98 | Press SR: 141.74 | Aggressive No. 3 Intent Striker | Max Bid: ₹5.0 Cr)\n"
            "6. Mahipal Lomror (Indian | MI | PPI: 66.37 | Press SR: 162.03 | Southpaw Power Hitter / SLA | Max Bid: ₹4.0 Cr)\n"
            "7. Abishek Porel (Indian | DC | PPI: 49.12 | Press SR: 132.88 | Indian Backup Wicketkeeper-Batter | Max Bid: ₹4.5 Cr)\n"
            "8. Asif Khan (Overseas | Int'l | PPI: 94.25 | Press SR: 196.52 | Budget Death Boundary Accelerator | Max Bid: ₹3.0 Cr)\n"
            "9. Rachin Ravindra (Overseas | KKR | PPI: 66.38 | Press SR: 147.70 | Top-Order / SLA All-Rounder | Max Bid: ₹7.0 Cr)\n"
            "10. Fakhar Zaman (Overseas | Int'l | PPI: 94.05 | Press SR: 183.89 | Powerplay Enforcer | Max Bid: ₹5.5 Cr)\n\n"
            "TOP 10 BOWLERS (100% VERIFIED AUCTION ELIGIBLE):\n"
            "1. Matheesha Pathirana (Overseas | KKR | PPI: 176.17 | 61 Clutch Wkts | 7.90 Press Econ | Generational Death Specialist | Max Bid: ₹12.0 Cr)\n"
            "2. Trent Boult (Overseas | MI | PPI: 128.22 | 40 Clutch Wkts | 8.45 Press Econ | Powerplay Swing Icon returning | Max Bid: ₹8.0 Cr)\n"
            "3. Avesh Khan (Indian | LSG | PPI: 148.58 | 57 Clutch Wkts | 9.76 Press Econ | 145+ kph Indian Death Seamer | Max Bid: ₹7.5 Cr)\n"
            "4. Mustafizur Rahman (Overseas | KKR | PPI: 147.76 | 48 Clutch Wkts | 7.87 Press Econ | Cutter & Change of Pace | Max Bid: ₹5.5 Cr)\n"
            "5. Wanindu Hasaranga (Overseas | LSG | PPI: 146.35 | 53 Clutch Wkts | 8.76 Press Econ | Mystery Spin All-Rounder | Max Bid: ₹6.5 Cr)\n"
            "6. Deepak Chahar (Indian | MI | PPI: 85.53 | 8.72 Press Econ | Powerplay Swing Specialist | Max Bid: ₹5.5 Cr)\n"
            "7. Maheesh Theekshana (Overseas | Int'l | PPI: 128.17 | 40 Clutch Wkts | 7.94 Press Econ | Carrom Mystery | Max Bid: ₹5.5 Cr)\n"
            "8. Tushar Deshpande (Indian | RR | PPI: 114.22 | 41 Clutch Wkts | Domestic Seam Backup | Max Bid: ₹4.0 Cr)\n"
            "9. Akash Deep (Indian | KKR | Test Seamer | Hit-the-Deck Seam Depth | Max Bid: ₹4.5 Cr)\n"
            "10. Haris Rauf (Overseas | Int'l | PPI: 132.24 | 43 Clutch Wkts | 8.76 Press Econ | 150+ kph Tearaway | Max Bid: ₹6.5 Cr)\n\n"
            "GOVERNANCE & AVAILABILITY RULES:\n"
            "• All 184 retained players across all 10 franchises (e.g., Bumrah, Kohli, Klaasen, Rashid Khan, Gaikwad, Samson, Hardik, Arshdeep, Shreyas, Pant, Gill) and retired players (Dhawan, Karthik, Dhoni) and withdrawn (Travis Head) are strictly UNAVAILABLE.\n"
            "• Answer concisely in 2 to 4 crisp bullet points with exact statistics and strategic reasoning."
        )

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"
        
        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": f"{system_instruction}\n\nUser Question: {query}"}
                    ]
                }
            ],
            "generationConfig": {
                "temperature": 0.15,
                "maxOutputTokens": 600
            }
        }

        try:
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode('utf-8'),
                headers={'Content-Type': 'application/json'},
                method='POST'
            )
            with urllib.request.urlopen(req, timeout=12) as response:
                result = json.loads(response.read().decode('utf-8'))
                text = result['candidates'][0]['content']['parts'][0]['text']
                return text
        except Exception as err:
            print(f"Gemini API call failed ({err}), falling back to deterministic answer.")
            return self.deterministic_fallback(query)

    def deterministic_fallback(self, query):
        q = query.lower()
        if 'bumrah' in q or 'kohli' in q or 'rashid' in q or 'klaasen' in q or 'samson' in q or 'hardik' in q or 'arshdeep' in q or 'shreyas' in q:
            return (
                "**VERIFIED UNAVAILABLE ALERT:**\n"
                "• **Jasprit Bumrah & Arshdeep Singh** (MI), **Virat Kohli** (RCB), **Heinrich Klaasen** (SRH), **Rashid Khan & Gill** (GT), "
                "**Sanju Samson** (CSK - Traded), **Hardik Pandya & Shreyas Iyer** (PBKS), and **Rishabh Pant** (DC - Traded) "
                "are officially confirmed retentions/trades in the BCCI Nov 18, 2026 list.\n"
                "• Under BCCI IPL regulations, they are **STRICTLY UNAVAILABLE** for the IPL 2027 auction and cannot be targeted."
            )
        elif 'rahane' in q or 'no 3' in q or 'anchor' in q or 'samson replacement' in q:
            return (
                "**#1 TARGET FOR RR NO. 3 ANCHOR: AJINKYA RAHANE**\n"
                "• **Pressure Metrics:** 147.47 Pressure SR | 31.58 Pressure Avg\n"
                "• **Tactical Value for RR:** Solves Rajasthan Royals' vacancy at No. 3 following Sanju Samson's trade to CSK. "
                "Anchors innings against collapse and allows Jaiswal, Parag, and Jurel to play aggressively.\n"
                "• **Valuation:** Estimated ₹2.5–4.0 Cr (Max Bid: ₹4.5 Cr)."
            )
        elif 'pathirana' in q or 'death' in q or 'bowler' in q:
            return (
                "**#1 DEATH BOWLING TARGET: MATHEESHA PATHIRANA**\n"
                "• **Clutch Record:** 61 pressure wickets across high-leverage deliveries with a stingy 7.90 pressure economy\n"
                "• **Tactical Value for RR:** Generational sling-action death bowler released by KKR. "
                "Pairs with Sandeep Sharma, Jofra Archer, and Mohammed Shami to form the competition's most feared death unit.\n"
                "• **Valuation:** Estimated ₹8.0–11.5 Cr (Max Bid: ₹12.0 Cr)."
            )
        elif 'purse' in q or 'budget' in q:
            return (
                "**RAJASTHAN ROYALS AUCTION BUDGET STRATEGY (₹27.05 CR PURSE):**\n"
                "• **Purse Remaining:** ₹27.05 Cr | **Slots to Fill:** 6 (Max 3 Overseas)\n"
                "• **Priority 1 (Death Pace Spearhead):** Matheesha Pathirana (Allocated ₹9.5 Cr) or Trent Boult (Allocated ₹7.0 Cr)\n"
                "• **Priority 2 (Indian Finisher):** Nehal Wadhera (Allocated ₹5.5 Cr) or Nitish Rana (Allocated ₹5.5 Cr)\n"
                "• **Priority 3 (No. 3 Anchor):** Ajinkya Rahane (Allocated ₹2.5 Cr)\n"
                "• **Priority 4–6 (Indian & Budget Depth):** Mahipal Lomror (₹2.5 Cr), Abishek Porel (₹2.5 Cr), Asif Khan (₹1.5 Cr)."
            )
        else:
            return (
                "**OFFICIAL IPL 2027 TARGETS (18 NOVEMBER 2026 BASELINE):**\n"
                "• **Top 10 Batters:** Ajinkya Rahane, Nitish Rana, Nehal Wadhera, Shimron Hetmyer, Rahul Tripathi, Mahipal Lomror, Abishek Porel, Asif Khan, Rachin Ravindra, Fakhar Zaman.\n"
                "• **Top 10 Bowlers:** Matheesha Pathirana, Trent Boult, Avesh Khan, Mustafizur Rahman, Wanindu Hasaranga, Deepak Chahar, Maheesh Theekshana, Tushar Deshpande, Akash Deep, Haris Rauf."
            )

def run_server(port=None):
    if port is None:
        port = int(os.environ.get('PORT', 8088))
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, WarRoomHandler)
    print(f"Rajasthan Royals War Room Server running at http://0.0.0.0:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
