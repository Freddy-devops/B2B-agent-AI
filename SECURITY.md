---

**`SECURITY.md`**

```markdown
# Security Policy & Regulatory Compliance

Security and data privacy are foundational to this enterprise multi-agent suite. This document outlines the security controls and compliance mechanisms engineered into this B2B architecture.

## 🛡️ Built-in Security Controls

### 1. Prompt Injection Firewall
All incoming messages from external parties are treated strictly as **untrusted raw data**.
* User payloads are encapsulated within explicit boundary tags (`<message_client>`).
* The primary analyst agent operates under security system prompts prohibiting the execution of override commands (`SYSTEM OVERRIDE`) embedded in incoming text.

### 2. Data Sovereignty & Multi-Tenancy Isolation
* **Tenant Isolation**: Each client organization is assigned a unique `client_id`. Data access and state management are strictly partitioned per tenant.
* **Right to be Forgotten (GDPR / CCPA)**: The `kill_switch_rgpd` tool performs targeted, surgical data purges for requesting clients without altering or risking data integrity for other tenants.

### 3. Automated Legal Compliance (EU AI Act & Transparency)
In compliance with the EU AI Act:
* Outbound emails directed to European Union residents automatically append a mandatory transparency disclaimer identifying the interaction as AI-assisted.

## 🔒 Reporting a Vulnerability

If you discover a security vulnerability within this repository, please report it via email to `beyamfred@gmail.com`. All inquiries will be handled with high priority.