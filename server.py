import os
import json
import urllib.request
import urllib.error
from http.server import SimpleHTTPRequestHandler, HTTPServer
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('GEMINI_API_KEY', '')

class WarRoomHandler(SimpleHTTPRequestHandler):
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
            "You are the Rajasthan Royals Lead Auction Strategist & Cricket Data Scientist in the IPL 2027 War Room. "
            "You have direct access to 200,999 deliveries (IPL 2022-2026 and T20Is) and the official Unstop submission data.\n"
            "UNSTOP SUPE RR SELECTOR RECOMMENDATIONS:\n"
            "TOP 10 BATSMEN:\n"
            "1. Naman Dhir (PPI: 92.41 | Press SR: 194.44 | Domestic 360° Finisher)\n"
            "2. Shreyas Iyer (PPI: 90.57 | Press SR: 179.20 | Marquee Middle-Order Anchor)\n"
            "3. Rishabh Pant (PPI: 89.68 | Press SR: 180.54 | Left-Hand Keeper-Batter)\n"
            "4. Fakhar Zaman (PPI: 96.68 | Press SR: 183.89 | Powerplay Disruptor)\n"
            "5. Asif Khan (PPI: 94.13 | Press SR: 196.52 | Highest Clutch Strike Rate)\n"
            "6. Najibullah Zadran (PPI: 92.52 | Press SR: 180.00 | Death Enforcer)\n"
            "7. Babar Azam (PPI: 91.73 | Press SR: 163.25 | 51.33 Press Avg)\n"
            "8. Phil Salt (PPI: 90.93 | Press SR: 187.27 | Powerplay Boundary Striker)\n"
            "9. Tim David (PPI: 90.60 | Press SR: 194.85 | Heavy Boundary Lever)\n"
            "10. Angelo Mathews (PPI: 87.89 | Press SR: 176.14 | 20.5% Dot Rate | Crisis Stabilizer)\n\n"
            "TOP 10 BOWLERS:\n"
            "1. Arshdeep Singh (PPI: 306.82 | 131 Clutch Wkts | 8.89 Econ | #1 Death Seamer)\n"
            "2. Bhuvneshwar Kumar (PPI: 177.25 | 68 Wkts | 8.87 Econ | Swing & Yorker Mastery)\n"
            "3. Yuzvendra Chahal (PPI: 180.78 | 71 Wkts | 8.91 Econ | Returning Spin Match-Winner)\n"
            "4. Harshal Patel (PPI: 163.53 | 64 Wkts | 9.54 Econ | Slower Dip Specialist)\n"
            "5. Jason Holder (PPI: 160.93 | 63 Wkts | 9.50 Econ | Bounce & Power All-Rounder)\n"
            "6. Mohammed Siraj (PPI: 140.08 | 47 Wkts | 41.7% Dot Balls | Aggressive Breakthrough)\n"
            "7. Haris Rauf (PPI: 132.24 | 43 Wkts | 8.76 Econ | 150+ kph Tearaway Spearhead)\n"
            "8. Maheesh Theekshana (PPI: 128.17 | 40 Wkts | 7.94 Econ | Middle Restriction Mystery)\n"
            "9. Mohammad Nawaz (PPI: 128.08 | 28 Wkts | 5.87 Econ | 42.4% Dots | Best Defensive Econ)\n"
            "10. Trent Boult (PPI: 128.22 | 40 Wkts | 8.45 Econ | New-Ball Swing Specialist)\n\n"
            "GOVERNANCE RULES:\n"
            "• Retained cores (Bumrah, Kohli, Klaasen, Rashid Khan, Gaikwad) and retired players (Dhawan, Karthik) are strictly UNAVAILABLE.\n"
            "• Contracted players await the official BCCI Nov 17, 2026 deadline for formal release ratification.\n"
            "Answer concisely in 2 to 4 crisp bullet points with exact statistics."
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
        if 'bumrah' in q or 'kohli' in q or 'varun' in q or 'rashid' in q or 'klaasen' in q:
            return (
                "**VERIFIED UNAVAILABLE ALERT:**\n"
                "• **Jasprit Bumrah** (MI ₹18 Cr), **Virat Kohli** (RCB ₹21 Cr), **Heinrich Klaasen** (SRH ₹23 Cr), and **Rashid Khan** (GT ₹18 Cr) "
                "are officially confirmed retentions and contractually bound to their franchises.\n"
                "• Under BCCI IPL regulations, they are **STRICTLY UNAVAILABLE** for the IPL 2027 auction and cannot be targeted."
            )
        elif 'naman' in q or 'finisher' in q:
            return (
                "**#1 DOMESTIC FINISHER: NAMAN DHIR**\n"
                "• **Pressure Strike Rate:** 194.44 (vs 168.42 baseline)\n"
                "• **Clutch Run Production:** 288 pressure balls with only 26.4% dot balls\n"
                "• **Tactical Value for RR:** Solves Rajasthan Royals' death-overs chase bottleneck while preserving an overseas slot."
            )
        elif 'arshdeep' in q or 'death' in q or 'bowler' in q:
            return (
                "**#1 DEATH BOWLING TARGET: ARSHDEEP SINGH**\n"
                "• **Clutch Record:** 131 pressure wickets across 1,783 high-leverage deliveries\n"
                "• **Death Economy:** 8.89 in overs 16–20 with 37.2% dot balls\n"
                "• **Pairing with Sandeep Sharma:** Creates an impermeable left-arm/right-arm death combination at Sawai Mansingh Stadium."
            )
        else:
            return (
                "**UNSTOP SUBMISSION SELECTION (TOP 10 BATSMEN & BOWLERS):**\n"
                "• **Top 10 Batsmen:** Naman Dhir, Shreyas Iyer, Rishabh Pant, Fakhar Zaman, Asif Khan, Najibullah Zadran, Babar Azam, Phil Salt, Tim David, Angelo Mathews.\n"
                "• **Top 10 Bowlers:** Arshdeep Singh, Bhuvneshwar Kumar, Yuzvendra Chahal, Harshal Patel, Jason Holder, Mohammed Siraj, Haris Rauf, Maheesh Theekshana, Mohammad Nawaz, Trent Boult."
            )

def run_server(port=8088):
    server_address = ('127.0.0.1', port)
    httpd = HTTPServer(server_address, WarRoomHandler)
    print(f"Rajasthan Royals War Room Server running at http://127.0.0.1:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
