# Security Policy

## Supported Versions

We support the following versions with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 4.x     | :white_check_mark: |
| < 4.0   | :x:                |

## Reporting a Vulnerability

We take security vulnerabilities seriously. If you discover a security vulnerability, please follow these steps:

### Private Disclosure

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report security vulnerabilities via email to:
- **Email**: [joerg@jfheinrich.eu](mailto:joerg@jfheinrich.eu)
- **Subject**: `[SECURITY] pipreqs-action vulnerability report`

### What to Include

Please include the following information in your report:

1. **Description** of the vulnerability
2. **Steps to reproduce** the issue
3. **Potential impact** of the vulnerability
4. **Suggested fix** (if you have one)
5. **Your contact information** for follow-up

### Response Timeline

- **Initial Response**: Within 48 hours
- **Status Update**: Within 7 days
- **Resolution**: Within 30 days for critical issues

### Security Updates

Security updates will be:
1. **Developed** in a private repository
2. **Tested** thoroughly before release
3. **Released** as patch versions
4. **Announced** through GitHub releases
5. **Documented** in CHANGELOG.md

### Responsible Disclosure

We follow responsible disclosure practices:
- We will acknowledge receipt of your report
- We will keep you informed of our progress
- We will credit you in our security advisory (unless you prefer to remain anonymous)
- We will coordinate public disclosure timing with you

## Security Best Practices

When using this action:

### Input Validation
- Validate all inputs to the action
- Use quoted strings for file paths
- Avoid dynamic input construction

### Permissions
- Use minimal required permissions
- Follow the principle of least privilege
- Regularly review workflow permissions

### Dependencies
- Keep the action version pinned to specific releases
- Monitor for security updates
- Use dependabot for automated updates

### Example Secure Usage

```yaml
- name: Generate requirements.txt
  uses: jfheinrich-eu/pipreqs-action@a1b2c3d4e5f6789012345678901234567890abcd  # Pin to SHA for maximum security
  with:
    requirements_path: "requirements.txt"     # Use quoted strings
    project_path: "."                         # Use relative paths
    force_overwrite: "true"                   # Use quoted booleans
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }} # Use secrets properly
```

### Version Pinning Best Practices

**Most Secure (Recommended for production):**
```yaml
uses: jfheinrich-eu/pipreqs-action@a1b2c3d4e5f6789012345678901234567890abcd  # Full SHA
```

**Secure (Good for most use cases):**
```yaml
uses: jfheinrich-eu/pipreqs-action@v4.1.0  # Specific version tag
```

**Less Secure (Not recommended for production):**
```yaml
uses: jfheinrich-eu/pipreqs-action@v4      # Major version (can auto-update)
uses: jfheinrich-eu/pipreqs-action@main    # Branch (highly discouraged)
```

**Why SHA pinning is recommended:**
- **Immutable**: SHA commits cannot be changed or overwritten
- **Tamper-proof**: Prevents supply chain attacks via tag manipulation
- **Reproducible**: Guarantees exact same code execution
- **Auditable**: Clear tracking of what code is running

## Contact

For security-related questions or concerns:
- **Primary Contact**: Jörg Heinrich ([joerg@jfheinrich.eu](mailto:joerg@jfheinrich.eu))
- **GitHub**: [jfheinrich-eu](https://github.com/jfheinrich-eu)

Thank you for helping keep pipreqs-action and our users safe!
