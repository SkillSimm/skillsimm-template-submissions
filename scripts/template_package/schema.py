"""Pydantic models for the YAML template package files (TemplateMCP spec §2).

Standalone on purpose: only pydantic — no app imports — so the module can be
vendored into the submissions repo's CI and the mcp-server image unchanged.
"""
from __future__ import annotations

from typing import Any, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

ActorMode = Literal["human", "human_with_ai", "team_with_ai", "ai"]
TaskType = Literal[
    "multiple_choice",
    "numeric_input",
    "structured_response",
    "open_response",
    "document_review",
]
GradingType = Literal["answer_key", "rubric", "numeric", "llm_judge", "none"]
AIAssist = Literal["suggests", "critiques", "grades", "decides"]

_SLUG_HELP = "lowercase letters, digits and underscores, starting with a letter"


def _check_slug(v: str) -> str:
    import re

    if not re.fullmatch(r"[a-z][a-z0-9_]*", v):
        raise ValueError(f"must be a slug ({_SLUG_HELP}); got {v!r}")
    return v


class GradingRule(BaseModel):
    """One step's grading rule. Field requirements per type are enforced by the
    validator (spec §4 decision tree), not here, so issues come back as
    readable findings instead of a pydantic stack."""

    model_config = ConfigDict(extra="forbid")

    type: GradingType
    points: float = 1
    # answer_key (multiple_choice)
    options: Optional[list[str]] = None
    correct_answer: Optional[str] = None
    distractors: Optional[list[str]] = None
    # numeric
    expected_value: Optional[float] = None
    expected_range: Optional[list[float]] = Field(default=None, min_length=2, max_length=2)
    tolerance: Optional[float] = None
    formula: Optional[str] = None
    # rubric / llm_judge
    criteria: Optional[list[str]] = None
    anchor_examples: Optional[list[dict[str, Any]]] = None  # [{"level": ..., "example": ...}]


class StepSpec(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str
    title: str
    actor_mode: ActorMode
    task_type: TaskType
    task_description: str
    role: Optional[str] = None
    depends_on: list[str] = Field(default_factory=list)
    # How the AI participates when actor_mode is human_with_ai / team_with_ai.
    ai_assist: Optional[AIAssist] = None
    grading: Optional[GradingRule] = None

    _slug = field_validator("id")(_check_slug)


class TemplateMeta(BaseModel):
    """template.yaml — package identity."""

    model_config = ConfigDict(extra="forbid")

    id: str
    title: str
    objective: str
    audience: Optional[str] = None
    roles: list[str] = Field(default_factory=list)
    version: str = "1.0.0"
    team_size: int = 5
    ai_chat_enabled: bool = True
    group_communication_allowed: bool = True

    _slug = field_validator("id")(_check_slug)


class TeamSizeRange(BaseModel):
    model_config = ConfigDict(extra="forbid")

    min: Optional[int] = None
    max: Optional[int] = None


class MarketplaceMetadata(BaseModel):
    """metadata.yaml — mirrors the `metadata` block of template.json that
    seed._registry_fields_from_master maps onto Template registry columns."""

    model_config = ConfigDict(extra="forbid")

    domain: Optional[str] = None
    industry: Optional[str] = None
    difficulty: Optional[str] = None
    duration_minutes: Optional[int] = None
    team_size: Optional[TeamSizeRange] = None
    task_type: Optional[str] = None
    scoring_type: Optional[str] = None
    license: Optional[str] = None
    author: Optional[str] = None
    research_ready: bool = False
    ai_modes: list[str] = Field(default_factory=list)
    tags: list[str] = Field(default_factory=list)
    learning_goals: list[str] = Field(default_factory=list)


class CreatorProfile(BaseModel):
    """creator.yaml — who submitted the package."""

    model_config = ConfigDict(extra="forbid")

    name: str
    email: Optional[str] = None
    github: Optional[str] = None
    organization: Optional[str] = None
    # fixed_fee | revenue_share | per_run | open_source | enterprise_only
    royalty_preference: Optional[str] = None


class TemplatePackage(BaseModel):
    """A fully parsed package folder."""

    template: TemplateMeta
    steps: list[StepSpec]
    # grading.yaml rules keyed by step id; a step's inline grading wins.
    grading: dict[str, GradingRule] = Field(default_factory=dict)
    metadata: Optional[MarketplaceMetadata] = None
    creator: Optional[CreatorProfile] = None
    sample_inputs: Optional[Any] = None
    expected_outputs: Optional[Any] = None
    readme: Optional[str] = None
    license_text: Optional[str] = None

    def grading_for(self, step: StepSpec) -> Optional[GradingRule]:
        return step.grading or self.grading.get(step.id)
