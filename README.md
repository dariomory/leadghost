![leadghost](images/logo.jpeg)

# LeadGhost

[![PyPI version](https://img.shields.io/pypi/v/leadghost.svg)](https://pypi.org/project/leadghost/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

A LinkedIn lead generation automation tool for scraping job postings and extracting lead information.

> **⚠️ WARNING:** This tool interacts with LinkedIn's services. Users are responsible for ensuring their use complies with LinkedIn's [Terms of Service](https://www.linkedin.com/legal/user-agreement), [Robots.txt](https://www.linkedin.com/robots.txt), and any applicable laws and regulations. The authors of this tool are not responsible for any misuse, account restrictions, or legal consequences resulting from its use. Use at your own risk.

- GitHub: [https://github.com/dariomory/leadghost/](https://github.com/dariomory/leadghost/)
- PyPI package: [https://pypi.org/project/leadghost/](https://pypi.org/project/leadghost/)
- Created by: **[Dario Mory](https://mory.dev)** | GitHub [https://github.com/dariomory](https://github.com/dariomory)
- Free software: Apache License 2.0

## Features

- **Automated lead extraction**: Scrape LinkedIn job postings and extract company information
- **Email generation**: Automatically generate and validate potential email addresses for leads
- **Configurable filtering**: Blacklist companies, set company size limits, and filter by keywords
- **Automatic mode**: Run scheduled jobs using CSV configuration files
- **Human-like behavior**: Configurable random delays to avoid detection

## Installation

```bash
pip install leadghost
```

Or install with [uv](https://github.com/astral-sh/uv):

```bash
uv pip install leadghost
```

## Usage

### Quick Start

After installation, run the CLI:

```bash
leadghost run
```

### Interactive Mode

1. Run `leadghost run` to start the tool
2. Enter search keyword and location when prompted
3. Enter the number of jobs to scrape
4. Log in to your LinkedIn account (if not already logged in)
5. The tool will scrape job postings and extract lead information

### Automatic Mode

Configure `config.txt`:

```ini
[leadmonster]
auto_mode = True
max_leads_per_company = 5
max_random_delay = 5
```

Create `auto.csv` with your search configurations:

```csv
search,location,keywords,max_company_size,job_count,date_filter
"software engineer","San Francisco","developer,engineer",500,100,weekly
"marketing manager","New York","marketing,seo",200,50,daily
```

Then run:

```bash
leadghost run
```

### Blacklisting Companies

Enter company names in `blacklist.txt` (one per line) to exclude them from results:

```
Microsoft
Intel
Pioneer Square
```

### Settings

- `max_leads_per_company`: Maximum number of leads to extract per company
- `max_random_delay`: Random delay (in seconds) between page navigations to avoid detection

### Scheduling on Windows

With automatic mode enabled, use Windows Task Scheduler:

1. Open `Task Scheduler`
2. Right-click on `Task Scheduler Library` → `New Task`
3. Under `Actions`, select the `leadghost` executable location
4. Set your desired schedule under `Triggers`

## Development

To set up for local development:

```bash
# Clone the repository
git clone git@github.com:dariomory/leadghost.git
cd leadghost

# Install in editable mode with uv
uv sync
```

This installs the package in development mode with all dependencies.

Run tests:

```bash
uv run pytest
```

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Code of Conduct

This project adheres to the Contributor Covenant [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is provided for educational and research purposes only. Users are responsible for:
- Complying with LinkedIn's Terms of Service
- Obtaining proper consent before contacting leads
- Ensuring compliance with applicable data protection laws (GDPR, CCPA, etc.)
- Using the tool in an ethical and legal manner

The authors assume no liability for any misuse of this software.
