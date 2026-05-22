# Wi-Fi Security Analyzer v2.0.1
Developed by **Ravindra Kumar**

An advanced Python-based network audit simulation utility engineered to evaluate authentication handshake protocols and baseline configurations for local 802.11 structures.

## 🛠️ Software & Hardware Requirements
- **Operating System:** Kali Linux / Ubuntu LTS
- **Language:** Python 3.10+ Stable Runtime
- **Libraries Required:** Scapy Interface Core
- **Adapter Mode:** Native Monitor Substates (wlan0mon)

---

## 🖥️ SCREENSHOT 01: Monitor Mode Initialization Output

```text
ravindra@cyber-lab-laptop:~$ sudo python3 wifi_analyzer.py
================================================================================
          WIFI SECURITY ANALYZER v2.0.1 (STABLE) - CORE CORE SUBSYSTEM        
================================================================================
[+] AUTHORIZED BY      : RAVINDRA KUMAR
[+] STATION DEPLOYMENT : CYBER RESEARCH LAB - BLOCK D
[+] SESSION HASH       : RE_0x7FFF9A2C_2026
--------------------------------------------------------------------------------
[SYSTEM] Checking Hardware Platform Architectures... x86_64 Core Detected
[SYSTEM] Privilege Authentication Level: ROOT USER (UID=0)
[IMAGE] Attaching Dynamic Link Libraries (libscapy_native.so)... [SUCCESS]

[WARN] Found 2 conflicting processes: NetworkManager (PID 912), wpa_supplicant (PID 1044).
[INFO] Killing conflicting processes to prevent channel hopping interference...
[INFO] Interface 'wlan0' mapping initiated...
[INFO] Mode switching: Managed ----> MONITOR MODE

[SUCCESS] Wireless interface successfully renamed to: wlan0mon
[STATUS] Raw socket insertion layer operational.
