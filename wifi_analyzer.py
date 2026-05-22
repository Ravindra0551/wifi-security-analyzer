#!/usr/bin/env python3
"""
Project Name: Wi-Fi Security Analyzer
Lead Developer: Ravindra Kumar
Year: 2026
Description: Automated CLI terminal tool to simulate 802.11 network scanning, 
             handshake interception, and offline cryptographic auditing.
"""

import time
import sys
import os
from datetime import datetime

# ANSI Terminal Colors for Realistic UI
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
WHITE = "\033[97m"
BOLD = "\033[1m"
RESET = "\033[0m"

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def step_1_init():
    clear_screen()
    print(f"{CYAN}{BOLD}================================================================================")
    print(f"          WIFI SECURITY ANALYZER v2.0.1 (STABLE) - CORE SUBSYSTEM        ")
    print(f"================================================================================{RESET}")
    print(f"[{CYAN}+{RESET}] AUTHORIZED BY      : {WHITE}{BOLD}RAVINDRA KUMAR{RESET}")
    print(f"[{CYAN}+{RESET}] STATION DEPLOYMENT : CYBER RESEARCH LAB - BLOCK D")
    print(f"[{CYAN}+{RESET}] SESSION HASH       : RE_0x7FFF9A2C_2026")
    print("-" * 80)
    time.sleep(0.5)
    
    print(f"[{CYAN}SYSTEM{RESET}] Checking Hardware Platform Architectures... x86_64 Core Detected")
    time.sleep(0.4)
    print(f"[{CYAN}SYSTEM{RESET}] Privilege Authentication Level: {WHITE}ROOT USER (UID=0){RESET}")
    time.sleep(0.4)
    print(f"[{CYAN}IMAGE{RESET}] Attaching Dynamic Link Libraries (libscapy_native.so)... [{GREEN}SUCCESS{RESET}]")
    time.sleep(0.6)
    
    print(f"\n{YELLOW}[WARN] Found 2 conflicting processes: NetworkManager (PID 912), wpa_supplicant (PID 1044).{RESET}")
    time.sleep(0.5)
    print(f"[{CYAN}INFO{RESET}] Killing conflicting processes to prevent channel hopping interference...")
    time.sleep(0.8)
    print(f"[{CYAN}INFO{RESET}] Interface 'wlan0' mapping initiated...")
    time.sleep(0.5)
    print(f"[{CYAN}INFO{RESET}] Mode switching: Managed ----> {WHITE}MONITOR MODE{RESET}")
    time.sleep(1.0)
    
    print(f"\n{GREEN}[SUCCESS] Wireless interface successfully renamed to: {WHITE}wlan0mon{RESET}")
    print(f"[{CYAN}STATUS{RESET}] RFCOMM & Hardware Hooks Unlocked. Raw socket insertion layer operational.")
    print(f"\nPress [ENTER] to engage wireless structural array telemetry mapping...")
    input()

def step_2_scan():
    clear_screen()
    print(f"[{CYAN}+{RESET}] Sniffing 802.11 wireless data streams on interface: {WHITE}wlan0mon{RESET}")
    print(f"[{CYAN}+{RESET}] Tracking Frequency Domain: 2412MHz - 2472MHz [Active Hopping Layer Enabled]\n")
    
    print(f"{CYAN}BSSID              PWR   CH  BEACONS  #DATA  SPEED  ENC   CIPHER  AUTH  ESSID{RESET}")
    print("-" * 80)
    
    networks = [
        "00:11:22:33:44:55  -38    6      412    284   54e   WPA2  CCMP    PSK   Lab_WiFi_Secure",
        "AA:BB:CC:DD:EE:FF  -72   11       85      9   54    WPA   TKIP    PSK   Guest_Net_Public",
        "12:34:56:78:9A:BC  -29    1     1420   1105   270   WPA3  CCMP    SAE   Admin_Core_5G",
        "44:55:66:77:88:99  -91    9       19      0   11    WEP   WEP     OPN   Legacy_Device_AP",
        "BC:9A:78:56:34:12  -55    6      110     14   54e   WPA2  CCMP    PSK   Faculty_Staff_Net"
    ]
    
    for net in networks:
        time.sleep(0.4)
        print(net)
        
    print(f"\n[{CYAN}POLL{RESET}] Active Stations (Clients linked to target arrays):")
    time.sleep(0.3)
    print(f"  - Station: F8:E6:1A:BC:DE:33  --> Connected to BSSID [00:11:22:33:44:55] ({WHITE}Lab_WiFi_Secure{RESET})")
    time.sleep(0.3)
    print(f"  - Station: 40:4E:36:77:AA:BB  --> Connected to BSSID [12:34:56:78:9A:BC] (Admin_Core_5G)")
    
    print(f"\n{BOLD}[{CYAN}ACTION{RESET}{BOLD}] Target profile isolated. Press [ENTER] to trigger Active Handshake Extraction...{RESET}")
    input()

def step_3_deauth():
    clear_screen()
    print("-" * 80)
    print(f"PROJECT WORKSPACE: {WHITE}{BOLD}RAVINDRA KUMAR{RESET} | ATTACK VECTOR: DEAUTH ENFORCEMENT")
    print("-" * 80)
    print(f"[{CYAN}+{RESET}] Targeted Gateway  : {WHITE}Lab_WiFi_Secure (00:11:22:33:44:55){RESET}")
    print(f"[{CYAN}+{RESET}] Targeted Station  : {WHITE}F8:E6:1A:BC:DE:33{RESET} (Targeted Client Device)")
    print(f"[{CYAN}INFO{RESET}] Constructing raw IEEE 802.11 Deauthentication Frame Object...\n")
    time.sleep(0.5)
    
    print(f"[{CYAN}TX{RESET}] Transmitting Deauth Packets (Reason Code 7: Class 3 frame received from nonassociated STA)")
    print(f"[{CYAN}TX{RESET}] Sending burst of 30 packets... [Sending...]")
    time.sleep(0.8)
    print(f"[{CYAN}TX{RESET}] Sending burst of 30 packets... [{GREEN}Sent{RESET}]")
    time.sleep(0.5)
    
    print(f"\n[{CYAN}RX{RESET}] Monitoring spectrum for EAPOL transport sequences...")
    messages = [
        "EAPOL Message 1 of 4 Captured (Anonce from AP)",
        "EAPOL Message 2 of 4 Captured (Snonce from Client + MIC)",
        "EAPOL Message 3 of 4 Captured (Group Key configuration)",
        "EAPOL Message 4 of 4 Captured (Acknowledgment confirmation)"
    ]
    
    for msg in messages:
        time.sleep(0.5)
        print(f"[{CYAN}RX{RESET}] {msg}")
        
    print(f"\n{CYAN}================================================================================")
    print(f"[SUCCESS] CRYPTOGRAPHIC 4-WAY HANDSHAKE ACQUIRED & VALIDATED")
    print(f"================================================================================{RESET}")
    print(f"[{CYAN}SAVED{RESET}] Micro-payload saved to volatile workspace disk memory: {WHITE}/tmp/handshake_001122.pcap{RESET}")
    print(f"[{CYAN}INFO{RESET}] Streaming binary matrix structures into verification engine...")
    print(f"\nPress [ENTER] to execute offline password security check...")
    input()

def step_4_crack():
    clear_screen()
    print("-" * 80)
    print(f"PROJECT VULNERABILITY MATRIX RUNTIME | KEY MANAGER: {WHITE}{BOLD}RAVINDRA KUMAR{RESET}")
    print("-" * 80)
    print(f"[{CYAN}+{RESET}] Parsing Handshake PCAP Dump File... Ready")
    print(f"[{CYAN}+{RESET}] Loading High-Performance Wordlist Asset: rockyou_optimized.txt (14,582 entries)")
    print(f"[{CYAN}+{RESET}] Hardware Processing Core: Multithreaded CPU Matrix\n")
    time.sleep(0.5)
    
    print(f"[{CYAN}RUN{RESET}] Commencing Hash Calculation Dictionary Phase...")
    print("  - Speed: 845.2 Keys/Second | Target ESSID: Lab_WiFi_Secure\n")
    time.sleep(0.6)
    
    wordlist = [
        ("student2022", "REJECT"),
        ("password@123", "REJECT"),
        ("internetaccess", "REJECT"),
        ("p@ssword!", f"{WHITE}[KEY FOUND!]{RESET}")
    ]
    
    ticks = [1200, 2450, 4900, 6812]
    
    for i, (word, status) in enumerate(wordlist):
        time.sleep(0.7)
        status_color = RED if "REJECT" in status else GREEN
        print(f"[00:00:0{2*i+2}] Keys Matched: {ticks[i]}  | Current Pointer: {word:<15} --> {status_color}{status}{RESET}")
        
    print(f"\n{CYAN}--------------------------------------------------------------------------------")
    print(f"                    VALIDATED CRACKED RE-AUTH KEY STRUCTURE                     ")
    print(f"--------------------------------------------------------------------------------{RESET}")
    print(f"{RED}[ALERT] NETWORK PRE-SHARED KEY IS CRITICAL VULNERABLE: {WHITE}p@ssword!{RESET}")
    print(f"[{CYAN}INFO{RESET}] Key derivation calculation matched exactly with recorded message MIC stream checksum.")
    print(f"\nPress [ENTER] to compile the final security ledger...")
    input()

def step_5_report():
    clear_screen()
    print(f"{CYAN}================================================================================")
    print(f"            COMPREHENSIVE WIRELESS RISK EVALUATION & AUDIT REPORT               ")
    print(f"================================================================================{RESET}")
    print(f"PROJECT AUDITOR  : {WHITE}{BOLD}RAVINDRA KUMAR{RESET}")
    print(f"EVALUATION DATE  : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} IST")
    print(f"AUDIT THREAT LVL : {RED}{BOLD}CRITICAL RISK ASSESSMENT (SCORE: 9.2 / 10.0){RESET}")
    print("-" * 80)
    
    print(f"\n{CYAN}[DISCOVERED ARTIFACTS & THREAT VECTORS]{RESET}")
    print(f"» {RED}THREAT-01 [CRITICAL]{RESET}: Airwave handshake exposure. Weak dictionary passphrase allows")
    print("                      complete decryption of over-the-air communication blocks.")
    print(f"» {YELLOW}THREAT-02 [HIGH]{RESET}    : Router legacy WPS PIN configuration is exposed. Vouchsafes a ")
    print("                      direct entryway via online register cracking algorithms.")
    print(f"» {YELLOW}THREAT-03 [MEDIUM]{RESET}  : Missing Protected Management Frames (PMF). Allows arbitrary ")
    print("                      third-party actors to disconnect legitimate users at will.")
    
    print(f"\n{CYAN}[HARDENING PROTOCOLS SIGNED & PROPOSED BY RAVINDRA KUMAR]{RESET}")
    print(f"1. Migrate the access point network topology from WPA2-Personal to {WHITE}WPA3-SAE Enterprise{RESET}.")
    print("2. Disable Wi-Fi Protected Setup (WPS) entirely via the core hardware firmware panel.")
    print("3. Establish 16-character asymmetric key passwords utilizing non-repeating entropy keys.")
    print("4. Activate mandatory 802.11w Management Frame Protection guidelines across all lines.")
    
    print(f"\n[{CYAN}SYSTEM{RESET}] Diagnostic Log Array saved safely: {WHITE}/var/log/security/ravindra_wifi_audit.pcap{RESET}")
    print(f"[{CYAN}SYSTEM{RESET}] Session End. All monitor mode virtual loops closed. Network interface reset.")
    print(f"{CYAN}================================================================================{RESET}\n")

if __name__ == "__main__":
    try:
        step_1_init()
        step_2_scan()
        step_3_deauth()
        step_4_crack()
        step_5_report()
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Session forced to terminate by user request.{RESET}")
        sys.exit(0)