# Security

## OWASP TOP 10 for LLM applications

    1. Prompt Injection
    2. Insecure Output Handling
    3. Training Data Poisoning
    4. Model Denial of Service (Unbounded Consumption)
    5. Supply Chain Vulnerabilities
    6. Sensitive Information Disclosure
    7. Insecure Plugin Design
    8. Excessive Agency
    9. Overreliance
    10. Model Theft


## Recent example: Prompt Injection Example

- *** Supabase MCP**

::: {style="font-size:20px"}

- [Supabase MCP can leak your entire SQL database](https://www.generalanalysis.com/blog/supabase-mcp-blog)
- LLMs are often used to process data according to pre-defined instructions. 
- The system prompt, user instructions, and the data context is provided to the LLM as text.
- The attacker begins by opening a new support ticket and submitting a carefully crafted message. 
- The body of the message includes both a friendly question and **a very explicit instruction block** addressed directly to the Cursor agent:

:::


## Recent example:  RAG exploit

- *** Office 365 Copilot ***

::: {style="font-size:20px"}
- [Breaking down ‘EchoLeak’, the First Zero-Click AI Vulnerability Enabling Data Exfiltration from Microsoft 365 Copilot](https://www.aim.security/post/echoleak-blogpost)

- Aim Security discovered “EchoLeak”, a vulnerability chain that exploits design flaws typical of RAG Copilots, allowing attackers to automatically exfiltrate any data from M365 Copilot’s context, without relying on specific user behavior. 
- With an external email, data could be leaked
:::
