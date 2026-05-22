# 🛡️ Wi-Fi Security Analyzer v2.0.1

<p align="center">
  <img src="https://img.shields.io/badge/Security-Simulation-red?style=for-the-badge&logo=target" alt="Security Simulation">
  <img src="https://img.shields.io/badge/Language-Python%203.10-blue?style=for-the-badge&logo=python" alt="Python Language">
  <img src="https://img.shields.io/badge/Platform-Kali%20Linux-purple?style=for-the-badge&logo=kalilinux" alt="Kali Linux Platform">
  <img src="https://img.shields.io/badge/Framework-Scapy%20Core-orange?style=for-the-badge" alt="Scapy Framework">
</p>

---

### 👤 Investigator Information
- **Principal Developer:** Ravindra Kumar
- **Academic Domain:** B.Tech Information Technology
- **Project Scope:** Academic Lab & Seminar Evaluation Module

---

## 🗺️ Quick Navigation
* [Abstract & Project Overview](#-abstract--project-overview)
* [Core Technical Specifications](#-core-technical-specifications)
* [System Architecture Workflow](#-system-architecture-workflow)
* [Live Project Execution Logs](#%EF%B8%8F-live-project-execution-logs)
* [Structural Defensive Mitigation Matrix](#-structural-defensive-mitigation-matrix)
* [Project Development Roadmap](#-project-development-roadmap)
* [Institutional Compliance & Disclaimer](#%EF%B8%8F-academic-disclaimer--institutional-compliance)

---

## 📝 Abstract & Project Overview
An advanced automation utility engineered to evaluate authentication handshake vulnerabilities and baseline structural gaps within local 802.11 environments. The framework maps frequency domains, tracks unencrypted management broadcasts, and logs authentication metrics for verification checks.

## ⚙️ Core Technical Specifications
* **Operating System Environment:** Linux Kernel Architecture Matrix (Kali Core x86_64 Suite)
* **Dependency Layer:** Scapy Structural Protocol Dissector Layer
* **Hardware Interface Mode:** Physical Adapter Substates (Monitor Interface Mode `wlan0mon`)

---

## 📐 System Architecture Workflow
Below is the data parsing and socket injection layer mapping flow executed by the Python core engine:

```text
[Raw Wireless Spectrum] 
       │
       ▼
┌───────────────────────────────┐
│  wlan0mon Hardware Interface  │ ◄─── Root Level Privileges Enforced (UID=0)
└──────────────┬────────────────┘
               │ (Raw Socket Layer)
               ▼
┌───────────────────────────────┐
│     Scapy Dissector Core      │ ◄─── Filtering Management Frames (IEEE 802.11)
└──────────────┬────────────────┘
               │
               ├───────────────────────────┐
               ▼                           ▼
┌───────────────────────────────┐ ┌───────────────────────────────┐
│ 4-Way Handshake Capture (RX)  │ │ Target Deauth Injection (TX)  │
└──────────────┬────────────────┘ └───────────────────────────────┘
               │ (Output to PCAP)
               ▼
┌───────────────────────────────┐
│  Vulnerability Assessment Report│ ───► Threat Rating Generation (Scale 0-10)
└───────────────────────────────┘
