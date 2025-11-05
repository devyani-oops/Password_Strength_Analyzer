Cybersecurity Interview Questions & Answers
## 1. What is cybersecurity and why is it important?
Cybersecurity is the practice of protecting systems, networks, programs, and data from digital attacks. It's important because:

Protects sensitive personal and business information

Prevents financial losses from cyber attacks

Maintains business continuity

Protects national security infrastructure

Ensures regulatory compliance

Maintains customer trust and brand reputation

## 2. What's the difference between a threat, a vulnerability, and a risk?
Threat: Any potential danger to information or systems (e.g., hackers, malware, natural disasters)

Vulnerability: Weakness in a system that can be exploited by threats (e.g., unpatched software, weak passwords)

Risk: The potential for loss or damage when a threat exploits a vulnerability

## 3. Define CIA triad (Confidentiality, Integrity, Availability)
Confidentiality: Ensuring information is accessible only to authorized users

Integrity: Maintaining accuracy and completeness of data

Availability: Ensuring systems and data are accessible when needed

## 4. What is the difference between IDS and IPS?
IDS (Intrusion Detection System): Monitors network traffic and alerts on suspicious activity (passive)

IPS (Intrusion Prevention System): Actively blocks and prevents detected threats (active)

## 5. What is the difference between symmetric and asymmetric encryption?
Symmetric: Uses same key for encryption and decryption (faster, but key distribution is challenging)

Asymmetric: Uses public/private key pairs (slower, but solves key distribution problem)

## 6. What is the principle of least privilege?
Users and systems should have only the minimum permissions necessary to perform their tasks.

## 7. Explain the difference between hashing and encryption
Hashing: One-way function that converts data to fixed-length string (irreversible)

Encryption: Two-way function that converts data using a key (reversible with the key)

## 8. What is two-factor authentication (2FA) and how does it work?
2FA requires two different types of credentials:

Something you know (password)

Something you have (phone, token) or something you are (biometrics)

## 9. What is the difference between black hat, white hat, and grey hat hackers?
Black hat: Malicious hackers who break laws

White hat: Ethical hackers working with permission

Grey hat: Hackers who may violate laws but without malicious intent

## 10. What are some common cyber attack vectors?
Phishing emails

Malware

Unpatched software

Weak passwords

Social engineering

USB drops

Watering hole attacks

## 11. What is a firewall and how does it work?
A firewall is a network security device that monitors and controls incoming/outgoing traffic based on predetermined security rules.

## 12. What is a DMZ in network security?
A DMZ (Demilitarized Zone) is a perimeter network that exposes external-facing services while keeping internal networks protected.

## 13. What are the different types of firewalls?
Packet-filtering firewalls

Stateful inspection firewalls

Proxy firewalls

Next-generation firewalls (NGFW)

Web application firewalls (WAF)

## 14. What is port scanning and how is it used in cyber attacks?
Port scanning identifies open ports and services on a target system. Attackers use it to find vulnerable services to exploit.

## 15. What is ARP poisoning and how can it be prevented?
ARP poisoning manipulates ARP tables to redirect traffic. Prevention:

Static ARP entries

ARP monitoring tools

Network segmentation

Port security

## 16. What are TCP and UDP? How do they differ in security context?
TCP: Connection-oriented, reliable, slower (HTTP, SSH, FTP)

UDP: Connectionless, unreliable, faster (DNS, VoIP)
Security: TCP's handshake makes it more traceable, UDP is often used in DDoS attacks.

## 17. What is VPN and how does it ensure secure communication?
VPN (Virtual Private Network) creates encrypted tunnels over public networks using protocols like IPsec, SSL/TLS to ensure confidentiality and integrity.

## 18. What is MAC flooding?
MAC flooding overwhelms switch CAM tables to force it into broadcast mode, allowing attackers to sniff network traffic.

## 19. How do you secure a Wi-Fi network?
Use WPA3 encryption

Change default credentials

Disable WPS

Hide SSID

Implement MAC filtering

Regular firmware updates

Strong passwords

## 20. What are the roles of SSL/TLS in network security?
Encryption of data in transit

Server authentication

Data integrity protection

Secure web browsing (HTTPS)

## 21. What is OS hardening? Name a few techniques.
OS hardening is securing an operating system by reducing its attack surface:

Disable unnecessary services

Apply security patches

Configure firewalls

Remove default accounts

Enable auditing and logging

Implement password policies

## 22. What is a rootkit and how does it work?
A rootkit is malicious software designed to gain unauthorized access while hiding its presence from detection tools.

## 23. What is patch management and why is it important?
Patch management is the process of distributing and applying updates to software. Important for:

Fixing security vulnerabilities

Maintaining system stability

Ensuring compliance

## 24. How do you secure a Linux server?
Disable root SSH login

Use key-based authentication

Configure firewall (iptables/ufw)

Regular updates

Disable unnecessary services

Implement fail2ban

File integrity monitoring

SELinux/AppArmor

## 25. What is privilege escalation and how can it be prevented?
Privilege escalation is gaining higher-level permissions than originally intended. Prevention:

Principle of least privilege

Regular patching

User account monitoring

Application sandboxing

Input validation

## 26. What are some tools to monitor system logs and detect anomalies?
Splunk

ELK Stack (Elasticsearch, Logstash, Kibana)

Graylog

OSSEC

Wazuh

SolarWinds

## 27. What is the Windows Security Event Log and what are key events to monitor?
Windows Security Event Log records security-related events. Key events:

4624/4625: Successful/failed logons

4720: User account created

4732: User added to privileged group

7045: Service installed

4719: System audit policy changed

## 28. What are secure coding practices to prevent vulnerabilities?
Input validation

Output encoding

Parameterized queries

Authentication and authorization checks

Error handling without information disclosure

Secure cryptographic practices

Regular code reviews

## 29. What is sandboxing in cybersecurity?
Sandboxing isolates running programs to prevent system failures or software vulnerabilities from spreading.

## 30. How would you protect an application from SQL Injection?
Use parameterized queries/prepared statements

Input validation and sanitization

Stored procedures

Least privilege database accounts

Web Application Firewall (WAF)

Regular security testing

## 31. What is a zero-day vulnerability?
A zero-day vulnerability is a security flaw unknown to the vendor, with no available patch, making it highly dangerous.

## 32. What is ransomware? How do you prevent it?
Ransomware encrypts files and demands payment for decryption. Prevention:

Regular backups

Email filtering

User training

Application whitelisting

Patch management

Anti-malware solutions

## 33. What is a man-in-the-middle (MITM) attack?
MITM attacks intercept communication between two parties without their knowledge. Prevention: Encryption, certificate validation.

## 34. What is Cross-Site Scripting (XSS)?
XSS injects malicious scripts into web pages viewed by other users. Types: Reflected, Stored, DOM-based.

## 35. What is a buffer overflow attack?
Buffer overflow occurs when a program writes more data to a buffer than it can hold, potentially allowing code execution.

## 36. What are DDoS attacks and how can they be mitigated?
DDoS (Distributed Denial of Service) overwhelms systems with traffic. Mitigation:

Traffic filtering

CDN services (Cloudflare, Akamai)

Rate limiting

Load balancing

DDoS protection services

## 37. What is phishing and how do you defend against it?
Phishing uses deceptive emails to steal information. Defense:

User training

Email filtering

Multi-factor authentication

URL analysis tools

Anti-phishing toolbars

## 38. What is session hijacking?
Session hijacking steals session IDs to impersonate legitimate users. Prevention: Secure cookies, HTTPS, session timeouts.

## 39. What is a botnet?
A botnet is a network of compromised computers controlled remotely to perform coordinated attacks.

## 40. What are common indicators of compromise (IoCs)?
Unusual network traffic

Failed login attempts

Unauthorized configuration changes

Unusual system behavior

Suspicious processes

Modified system files

## 41. What are the top OWASP vulnerabilities?
Broken Access Control

Cryptographic Failures

Injection

Insecure Design

Security Misconfiguration

Vulnerable Components

Authentication Failures

Software/Data Integrity

Security Logging Failures

Server-Side Request Forgery

## 42. What is penetration testing? How is it different from vulnerability scanning?
Penetration testing: Simulates real attacks to exploit vulnerabilities

Vulnerability scanning: Automated scanning to identify potential vulnerabilities

## 43. What tools do you use for penetration testing?
Nmap (scanning)

Metasploit (exploitation)

Burp Suite (web apps)

Wireshark (traffic analysis)

John the Ripper (password cracking)

Aircrack-ng (wireless)

## 44. What is Wireshark and how is it used in cybersecurity?
Wireshark is a network protocol analyzer used for:

Network troubleshooting

Traffic analysis

Security incident investigation

Protocol development

## 45. What is Metasploit and how does it work?
Metasploit is a penetration testing framework that provides:

Exploit development

Vulnerability validation

Payload generation

Post-exploitation modules

## 46. What is Nmap and what are its common use cases?
Nmap is a network scanning tool used for:

Network discovery

Port scanning

Service detection

OS fingerprinting

Vulnerability detection

## 47. What is the difference between static and dynamic code analysis?
Static analysis: Analyzes source code without executing it

Dynamic analysis: Tests code while it's running

## 48. What is a security information and event management (SIEM) system?
SIEM collects, analyzes, and correlates security events from multiple sources to provide real-time monitoring and incident response.

## 49. What is threat hunting?
Proactive search for cyber threats that evade existing security solutions, using hypothesis-based investigations.

## 50. What's the purpose of an incident response plan?
Provide structured approach to security incidents

Minimize damage and recovery time

Preserve evidence

Maintain business continuity

Meet legal/regulatory requirements

Improve future security posture

