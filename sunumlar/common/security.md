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

## Recent example

::: {style="font-size:18px"}
- [Nx: An AI-first build platform](https://nx.dev/), they use vibe coding.

1. NX created a feature for checking pull request formatting using Claude Code.
2. This feature puts subject line of github PR to bash without sanitizing.
3. Somebody realized this security hole and they patched it.
4. Unfortunately, hole remained in a branch, which allows running github actions.
5. On 24 August, someone submitted a pull request to NX with exploit code in it. The NX project used NX to automatically test the exploit, like it does all pull requests — by running it!
6. The NX CI thus handed the attacker NX’s official GitHub key and its publishing key for NPM.
7. So on 26 August, the attacker added malware to NX, and pushed the malwared versions as official releases!

8. The malware stole a lot of people’s login keys and, apparently, their crypto wallets.


[source github nx](https://github.com/nrwl/nx/security/advisories/GHSA-cxm3-wv7p-598c)

[source Pivot to AI](https://pivot-to-ai.com/2025/08/29/vibe-coded-build-system-nx-gets-hacked-steals-vibe-coders-crypto/)
:::

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
