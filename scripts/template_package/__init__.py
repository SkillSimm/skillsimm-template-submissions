"""Multi-file YAML template package — the interchange format for the
creator → GitHub review → registry pipeline (TemplateMCP spec §2).

A package is a folder:

    templates/<slug>/
      template.yaml         # identity: id, title, audience, objective, roles
      steps.yaml            # ordered steps with actor_mode / task_type / grading
      grading.yaml          # grading rules keyed by step id (inline rules win)
      metadata.yaml         # marketplace discovery block (optional)
      creator.yaml          # creator profile (optional)
      sample_inputs.json    # example run inputs (optional)
      expected_outputs.json # example expected outputs (optional)
      README.md             # required
      LICENSE.md            # required

The DB (`Template.steps_json`) stays the runtime source of truth; packages are
serialized/parsed at the GitHub boundary only. The same module is vendored into
the submissions repo (`scripts/`) and the mcp-server image — keep it free of
app imports so it stands alone.
"""
from .schema import (
    ActorMode,
    CreatorProfile,
    GradingRule,
    MarketplaceMetadata,
    StepSpec,
    TaskType,
    TemplateMeta,
    TemplatePackage,
)
from .validator import Issue, load_package, validate_package
from .convert import package_to_master, template_to_package

__all__ = [
    "ActorMode",
    "CreatorProfile",
    "GradingRule",
    "Issue",
    "MarketplaceMetadata",
    "StepSpec",
    "TaskType",
    "TemplateMeta",
    "TemplatePackage",
    "load_package",
    "package_to_master",
    "template_to_package",
    "validate_package",
]
