"""skillsimm-ats-ingest — fetch and filter live job postings from public ATS APIs.

Keyless sources: Greenhouse, Lever, Ashby (public JSON endpoints, full
descriptions, no scraping). Keyed optional sources: USAJobs, Adzuna
(free API keys via env vars; they no-op with a log line when unset).
"""
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("skillsimm-ats-ingest")
except PackageNotFoundError:  # running from a source checkout
    __version__ = "0.0.0.dev"

from .normalize import Posting, strip_html  # noqa: F401
from .filters import matches_family, title_matches  # noqa: F401
from .boards import load_boards  # noqa: F401
