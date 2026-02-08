# Security Policy (Ndlovu Core)

## Rules
- Never commit API keys, tokens, passwords, or private URLs.
- Use `.env` locally. Commit only `.env.example`.

## If a key is exposed
1. Revoke the key immediately in the provider dashboard.
2. Create a new key.
3. Remove the leaked key from git history if it was committed.
4. Document the incident in the vault (Tamara).

## Reporting
If you find a vulnerability, do not post it publicly. Document it privately first.