# GAPS — most-demanded work not yet covered by a simulation

Each uncovered item is a build brief: claim its `gap:*` issue, run
`python scripts/new_template.py --from-gap gap:<slug>`, and submit the sim as a PR.

## Financial Analyst — 75 postings from 46 companies (updated 2026-09-05)
Covered by 10 existing sims: executive reporting, forecast, forecast adjustment, forecasting, investment trade-off, pricing strategy analysis, recommendation, resource allocation, unit economic, variance analysis, variance analysis report

Uncovered processes (top by demand share — tools shown as context, not gaps):
1. **financial analysis** — 44% of postings [responsibilities] · [claim → gap:financial-analysis](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Afinancial-analysis)
   - tools seen: financial modeling software (27%), excel (21%), data visualization software (12%), sap (3%)
2. **cross-functional collaboration** — 36% of postings [responsibilities] · [claim → gap:cross-functional-collaboration](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Across-functional-collaboration)
   - typical flow: define planning calendar and timeline → financial modeling → coordinate forecast input from department → develop management report
   - tools seen: excel (30%), sql (15%), financial modeling software (15%), tableau (11%)
3. **financial modeling** — 36% of postings [deliverables] · [claim → gap:financial-modeling](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Afinancial-modeling)
   - typical flow: define planning calendar and timeline → coordinate forecast input from department → financial modeling → develop management report
   - tools seen: excel (70%), financial modeling software (56%), sql (30%), google sheets (22%)
4. **decision support** — 25% of postings [responsibilities] · [claim → gap:decision-support](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Adecision-support)
   - tools seen: financial modeling software (16%), excel (5%), data visualization software (5%)
5. **analytic** — 23% of postings [responsibilities] · [claim → gap:analytic](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aanalytic)
   - tools seen: excel (6%), gmail (6%), gemini (6%), google doc (6%)
6. **budgeting** — 23% of postings [responsibilities] · [claim → gap:budgeting](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Abudgeting)
   - tools seen: financial modeling software (47%), excel (41%), sap (12%), data visualization software (12%)
7. **financial report** — 21% of postings [deliverables] · [claim → gap:financial-report](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Afinancial-report)
   - tools seen: excel (56%), financial modeling software (50%), data visualization software (25%), sap (6%)
8. **report** — 19% of postings [responsibilities] · [claim → gap:report](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Areport)
   - tools seen: excel (29%), financial modeling software (14%), metabase (7%), salesforce (7%)
9. **financial performance analysis** — 17% of postings [responsibilities] · [claim → gap:financial-performance-analysis](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Afinancial-performance-analysis)
   - typical flow: financial modeling
   - tools seen: excel (54%), financial modeling software (54%), data visualization software (46%), sql (15%)
10. **financial reporting** — 15% of postings [responsibilities] · [claim → gap:financial-reporting](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Afinancial-reporting)
   - tools seen: financial modeling software (45%), excel (36%), data visualization software (18%), sap (9%)

## Data Analyst — 75 postings from 57 companies (updated 2026-09-05)
**No sims cover this family yet — the whole head is open.**
_(items from responsibilities withheld: vocabulary too fragmented to rank at current corpus size)_

Uncovered processes (top by demand share — tools shown as context, not gaps):
1. **report** — 52% of postings [deliverables] · [claim → gap:report](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Areport)
   - typical flow: identify data need → gather business requirement → collect data → extract and transform data → data modeling → clean data
   - tools seen: sql (54%), python (49%), tableau (46%), excel (28%)
2. **dashboard** — 49% of postings [deliverables] · [claim → gap:dashboard](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Adashboard)
   - typical flow: identify data need → define problem → stakeholder communication → gather business requirement → collect data → extract and transform data
   - tools seen: sql (81%), python (65%), tableau (57%), dbt (35%)
3. **prioritize analysis request** — 24% of postings [decisions] · [claim → gap:prioritize-analysis-request](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aprioritize-analysis-request)
   - typical flow: identify data need → stakeholder communication → collect data → extract and transform data → clean data → data analysis
   - tools seen: sql (83%), python (83%), tableau (61%), r (56%)
4. **data model** — 21% of postings [deliverables] · [claim → gap:data-model](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Adata-model)
   - typical flow: define problem → gather business requirement → design solution → data modeling → etl → build visualization
   - tools seen: sql (88%), tableau (69%), python (62%), dbt (50%)
5. **data visualization** — 20% of postings [deliverables] · [claim → gap:data-visualization](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Adata-visualization)
   - typical flow: collect data → clean data → data analysis → report generation → communicate finding
   - tools seen: tableau (60%), sql (60%), python (60%), excel (53%)
6. **documentation** — 16% of postings [deliverables] · [claim → gap:documentation](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Adocumentation)
   - typical flow: stakeholder communication → define problem → collect data → design solution → dashboard → data analysis
   - tools seen: sql (92%), tableau (58%), dbt (50%), python (50%)
7. **data quality** — 15% of postings [decisions] · [claim → gap:data-quality](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Adata-quality)
   - typical flow: collect data → clean data → data analysis → report generation → communicate finding
   - tools seen: sql (91%), python (82%), excel (73%), tableau (73%)
8. **determine data quality threshold** — 12% of postings [decisions] · [claim → gap:determine-data-quality-threshold](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Adetermine-data-quality-threshold)
   - typical flow: identify data need → collect data → extract and transform data → clean data → data analysis → build dashboard and report
   - tools seen: sql (100%), python (89%), tableau (78%), excel (56%)
9. **analysis report** — 9% of postings [deliverables] · [claim → gap:analysis-report](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aanalysis-report)
   - typical flow: data analysis → communicate finding → presentation
   - tools seen: sql (86%), python (71%), tableau (29%), r (29%)
10. **presentation** — 9% of postings [deliverables] · [claim → gap:presentation](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Apresentation)
   - typical flow: collect data → data analysis
   - tools seen: excel (71%), tableau (71%), sql (71%), power bi (57%)

## Security Analyst — 65 postings from 51 companies (updated 2026-09-05)
**No sims cover this family yet — the whole head is open.**

Uncovered processes (top by demand share — tools shown as context, not gaps):
1. **incident response** — 38% of postings [responsibilities] · [claim → gap:incident-response](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aincident-response)
   - typical flow: detect incident → analyze alert → analyze security incident → conduct vulnerability assessment → incident response → contain and remediate
   - tools seen: siem (44%), edr (16%), intrusion detection system (16%), firewall (16%)
2. **prioritize security incident** — 34% of postings [decisions] · [claim → gap:prioritize-security-incident](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aprioritize-security-incident)
   - typical flow: alert triage → analyze incident → incident response → security documentation
   - tools seen: siem (36%), vulnerability scanner (27%), intrusion detection system (18%), firewall (18%)
3. **incident report** — 34% of postings [deliverables] · [claim → gap:incident-report](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aincident-report)
   - typical flow: detect incident → alert triage → monitor security event → analyze incident → analyze alert → analyze security incident
   - tools seen: siem (50%), intrusion detection system (23%), vulnerability scanner (23%), firewall (23%)
4. **implement security measure** — 28% of postings [responsibilities] · [claim → gap:implement-security-measure](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aimplement-security-measure)
   - typical flow: alert triage → analyze incident → incident response → security documentation
   - tools seen: vulnerability scanner (44%), siem (44%), intrusion detection system (33%), firewall (28%)
5. **access monitoring** — 26% of postings [responsibilities] · [claim → gap:access-monitoring](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aaccess-monitoring)
   - typical flow: alert triage → analyze incident → incident response → security documentation
   - tools seen: vulnerability scanner (41%), siem (35%), intrusion detection system (29%), access management software (29%)
6. **security documentation** — 26% of postings [deliverables] · [claim → gap:security-documentation](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Asecurity-documentation)
   - typical flow: alert triage → monitor security event → analyze incident → incident response → security documentation
   - tools seen: active directory software (35%), access management software (29%), siem (18%), arcsight enterprise threat and risk management (18%)
7. **analyze security incident** — 22% of postings [responsibilities] · [claim → gap:analyze-security-incident](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aanalyze-security-incident)
   - typical flow: alert triage → analyze incident → incident response → security documentation
   - tools seen: vulnerability scanner (43%), siem (36%), intrusion detection system (29%), antiviru software (21%)
8. **conduct vulnerability assessment** — 18% of postings [responsibilities] · [claim → gap:conduct-vulnerability-assessment](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aconduct-vulnerability-assessment)
   - typical flow: alert triage → monitor security event → analyze incident → incident response → security documentation
   - tools seen: vulnerability scanner (67%), intrusion detection system (50%), siem (50%), firewall (42%)
9. **risk assessment** — 18% of postings [responsibilities] · [claim → gap:risk-assessment](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Arisk-assessment)
   - tools seen: access management software (42%), active directory software (42%), automated audit trail analysis software (17%), computer forensic software (17%)
10. **incident severity classification** — 17% of postings [decisions] · [claim → gap:incident-severity-classification](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aincident-severity-classification)
   - typical flow: alert triage → analyze alert → analyze security incident → incident response → security documentation → incident report
   - tools seen: siem (55%), firewall (36%), vulnerability scanner (27%), antiviru software (27%)

## Account Manager — 5 postings from 3 companies (updated 2026-09-05)
**No sims cover this family yet — the whole head is open.**

Uncovered processes (top by demand share — tools shown as context, not gaps):
1. **cross-functional collaboration** — 40% of postings [responsibilities] · [claim → gap:cross-functional-collaboration](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Across-functional-collaboration)
   - typical flow: financial performance analysis → investment planning → territory plan → competitive analysis → build growth roadmap → negotiation guide
   - tools seen: ai tool (100%), salesforce (50%), bi tool (50%), agentic enablement capabilitie (50%)
2. **territory plan** — 40% of postings [responsibilities] · [claim → gap:territory-plan](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aterritory-plan)
   - typical flow: financial performance analysis → prospect and build pipeline → territory plan → develop new account → build growth roadmap → expand existing customer
   - tools seen: ai tool (100%), salesforce (50%), bi tool (50%), notion (50%)
3. **client relationship management** — 40% of postings [responsibilities] · [claim → gap:client-relationship-management](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aclient-relationship-management)
   - typical flow: financial performance analysis → investment planning → territory plan → competitive analysis → build growth roadmap → negotiation guide
   - tools seen: ai tool (100%), salesforce (50%), bi tool (50%), agentic enablement capabilitie (50%)
4. **executive presentation** — 40% of postings [responsibilities] · [claim → gap:executive-presentation](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aexecutive-presentation)
   - typical flow: investment planning → prospect and build pipeline → competitive analysis → develop new account → cross-functional collaboration → expand existing customer
   - tools seen: ai tool (100%), agentic enablement capabilitie (50%), partner program tech stack (50%), notion (50%)
5. **long range plan** — 40% of postings [deliverables] · [claim → gap:long-range-plan](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Along-range-plan)
   - typical flow: financial performance analysis → investment planning → territory plan → competitive analysis → build growth roadmap → negotiation guide
   - tools seen: ai tool (100%), salesforce (50%), bi tool (50%), agentic enablement capabilitie (50%)
6. **recommendation** — 40% of postings [deliverables] · [claim → gap:recommendation](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Arecommendation)
   - typical flow: financial performance analysis → investment planning → territory plan → competitive analysis → build growth roadmap → negotiation guide
   - tools seen: ai tool (100%), salesforce (50%), bi tool (50%), agentic enablement capabilitie (50%)
7. **playbook** — 40% of postings [deliverables] · [claim → gap:playbook](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aplaybook)
   - typical flow: prospect and build pipeline → conduct technical discovery → develop new account → build and deliver demo → expand existing customer → advise on integration and compliance
   - tools seen: ai tool (100%), notion (100%), llm (50%), dlp/siem (50%)
8. **product vision** — 20% of postings [responsibilities] · [claim → gap:product-vision](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aproduct-vision)
   - typical flow: financial performance analysis → territory plan → build growth roadmap → negotiation guide → cross-functional collaboration → customer monitoring
   - tools seen: salesforce (100%), bi tool (100%), ai tool (100%)
9. **customer monitoring** — 20% of postings [responsibilities] · [claim → gap:customer-monitoring](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Acustomer-monitoring)
   - typical flow: financial performance analysis → territory plan → build growth roadmap → negotiation guide → cross-functional collaboration → customer monitoring
   - tools seen: salesforce (100%), bi tool (100%), ai tool (100%)
10. **financial performance analysis** — 20% of postings [responsibilities] · [claim → gap:financial-performance-analysis](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Afinancial-performance-analysis)
   - typical flow: financial performance analysis → territory plan → build growth roadmap → negotiation guide → cross-functional collaboration → customer monitoring
   - tools seen: salesforce (100%), bi tool (100%), ai tool (100%)

## Cloud Data Engineer — 28 postings from 15 companies (updated 2026-09-05)
**No sims cover this family yet — the whole head is open.**
_(items from responsibilities withheld: vocabulary too fragmented to rank at current corpus size)_

Uncovered processes (top by demand share — tools shown as context, not gaps):
1. **solution architecture design** — 21% of postings [decisions] · [claim → gap:solution-architecture-design](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Asolution-architecture-design)
   - tools seen: python (67%), eval framework (33%), delta lake (33%), apache spark (33%)
2. **system** — 21% of postings [deliverables] · [claim → gap:system](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Asystem)
   - tools seen: llm (50%), memcached (33%), tidb (33%), dynamodb (33%)
3. **documentation** — 21% of postings [deliverables] · [claim → gap:documentation](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Adocumentation)
   - typical flow: design architecture
   - tools seen: python (83%), aws (50%), sql (50%), databrick (50%)
4. **prioritize analysis request** — 18% of postings [decisions] · [claim → gap:prioritize-analysis-request](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aprioritize-analysis-request)
   - typical flow: design solution
   - tools seen: python (60%), java (40%), javascript (40%), typescript (40%)
5. **architecture and design decision** — 18% of postings [decisions] · [claim → gap:architecture-and-design-decision](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aarchitecture-and-design-decision)
   - tools seen: gcp (60%), typescript (60%), azure (60%), aws (60%)
6. **storage infrastructure** — 14% of postings [deliverables] · [claim → gap:storage-infrastructure](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Astorage-infrastructure)
   - tools seen: memcached (50%), tidb (50%), dynamodb (50%), postgresql (50%)
7. **tool** — 14% of postings [deliverables] · [claim → gap:tool](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Atool)
   - tools seen: memcached (50%), tidb (50%), dynamodb (50%), postgresql (50%)
8. **pipeline** — 14% of postings [deliverables] · [claim → gap:pipeline](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Apipeline)
   - tools seen: python (50%), delta lake (50%), apache spark (50%), gcp (50%)
9. **proof-of-value result** — 14% of postings [deliverables] · [claim → gap:proof-of-value-result](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aproof-of-value-result)
   - typical flow: identify target account → run proof-of-value → negotiate and close → enable field
   - tools seen: gcp (100%), azure (100%), aws (100%), databrick lakebase (50%)
10. **custom application** — 14% of postings [deliverables] · [claim → gap:custom-application](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Acustom-application)
   - typical flow: design architecture
   - tools seen: python (75%), gcp (50%), azure (50%), aws (50%)

## Data Engineer — 10 postings from 2 companies (updated 2026-09-05)
**No sims cover this family yet — the whole head is open.**

Uncovered processes (top by demand share — tools shown as context, not gaps):
1. **cross-functional collaboration** — 50% of postings [responsibilities] · [claim → gap:cross-functional-collaboration](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Across-functional-collaboration)
   - typical flow: define strategy → develop feature → experiment with model → deploy to production → monitor and iterate
   - tools seen: snowflake (60%), workday (40%), dbt (40%), quicksilver (40%)
2. **technical strategy document** — 50% of postings [deliverables] · [claim → gap:technical-strategy-document](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Atechnical-strategy-document)
   - typical flow: define strategy → develop feature → experiment with model → deploy to production → monitor and iterate
   - tools seen: scala (60%), java (60%), python (60%), deep learning (40%)
3. **evaluate trade-off** — 40% of postings [decisions] · [claim → gap:evaluate-trade-off](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aevaluate-trade-off)
   - typical flow: define strategy → develop feature → experiment with model → deploy to production → monitor and iterate
   - tools seen: workday (50%), dbt (50%), quicksilver (50%), notion (50%)
4. **prioritize team effort** — 40% of postings [decisions] · [claim → gap:prioritize-team-effort](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aprioritize-team-effort)
   - typical flow: define strategy → develop feature → experiment with model → deploy to production → monitor and iterate
   - tools seen: deep learning (50%), gradient-boosted tree (50%), build scalable system for long term (50%), transformer-based model (50%)
5. **proof-of-value result** — 40% of postings [deliverables] · [claim → gap:proof-of-value-result](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aproof-of-value-result)
   - tools seen: scala (100%), java (100%), python (100%), public cloud platform (50%)
6. **production system** — 30% of postings [responsibilities] · [claim → gap:production-system](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aproduction-system)
   - typical flow: scope business problem with stakeholder → scope business problem → stakeholder communication → design and build ai system → design architecture → develop dbt model
   - tools seen: dbt (100%), git (100%), snowflake (100%), github (100%)
7. **reliability infrastructure** — 30% of postings [responsibilities] · [claim → gap:reliability-infrastructure](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Areliability-infrastructure)
   - typical flow: scope business problem with stakeholder → scope business problem → stakeholder communication → design and build ai system → design architecture → develop dbt model
   - tools seen: dbt (100%), git (100%), snowflake (100%), github (100%)
8. **select modeling approache** — 30% of postings [decisions] · [claim → gap:select-modeling-approache](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aselect-modeling-approache)
   - typical flow: define strategy → develop feature → experiment with model → evaluate model → deploy to production → monitor and iterate
   - tools seen: deep learning (67%), gradient-boosted tree (67%), build scalable system for long term (67%), transformer-based model (67%)
9. **application** — 20% of postings [responsibilities] · [claim → gap:application](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aapplication)
   - typical flow: scope business problem with stakeholder → scope business problem → design and build ai system → design architecture → deploy and maintain production system → build and containerize
   - tools seen: workday (100%), dbt (100%), quicksilver (100%), notion (100%)
10. **python** — 20% of postings [responsibilities] · [claim → gap:python](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Apython)
   - typical flow: scope business problem with stakeholder → scope business problem → design and build ai system → design architecture → deploy and maintain production system → build and containerize
   - tools seen: workday (100%), dbt (100%), quicksilver (100%), notion (100%)

## Data Scientist — 30 postings from 10 companies (updated 2026-09-05)
**No sims cover this family yet — the whole head is open.**
_(items from responsibilities, deliverables withheld: vocabulary too fragmented to rank at current corpus size)_

Uncovered processes (top by demand share — tools shown as context, not gaps):
1. **define requirement and evaluate tradeoff** — 23% of postings [decisions] · [claim → gap:define-requirement-and-evaluate-tradeoff](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Adefine-requirement-and-evaluate-tradeoff)
   - typical flow: prototype new modeling idea → run offline experiment → drive best-performing approache into production → build and maintain evidence extraction pipeline
   - tools seen: cursor (71%), catboost (43%), kubeflow (43%), xgboost (43%)
2. **resource allocation** — 13% of postings [decisions] · [claim → gap:resource-allocation](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aresource-allocation)
   - tools seen: sql (50%), python (50%), data visualization (25%), machine learning (25%)
3. **architecture and design decision** — 13% of postings [decisions] · [claim → gap:architecture-and-design-decision](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aarchitecture-and-design-decision)
   - tools seen: cursor (50%), claude (50%), python (50%), kotlin (25%)
4. **select modeling approache** — 13% of postings [decisions] · [claim → gap:select-modeling-approache](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aselect-modeling-approache)
   - typical flow: prototype new modeling idea → run offline experiment → drive best-performing approache into production → build and maintain evidence extraction pipeline
   - tools seen: catboost (75%), kubeflow (75%), xgboost (75%), airflow (75%)
5. **risk assessment** — 13% of postings [decisions] · [claim → gap:risk-assessment](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Arisk-assessment)
   - typical flow: perform independent challenge of model → identify weaknesse and opportunitie → partner with audit and compliance
   - tools seen: scikit-learn (50%), sql (50%), cloud-based coding environment (50%), python (50%)
6. **recommend compensation structure update** — 10% of postings [decisions] · [claim → gap:recommend-compensation-structure-update](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Arecommend-compensation-structure-update)
   - typical flow: audit job role → perform independent challenge of model → submit benchmarking survey → identify weaknesse and opportunitie → evaluate market positioning → collaborate with model owner to remediate
   - tools seen: excel (67%), sigma computing (67%), claude code (67%), google sheets (67%)
7. **product roadmap** — 10% of postings [decisions] · [claim → gap:product-roadmap](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aproduct-roadmap)
   - typical flow: identify growth opportunitie → run offline experiment → launch and scale feature → monitor funnel performance → iterate and optimize
   - tools seen: cursor (100%), claude (67%), claude code (33%), sql (33%)
8. **determine risk control for production** — 10% of postings [decisions] · [claim → gap:determine-risk-control-for-production](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Adetermine-risk-control-for-production)
   - typical flow: prototype new modeling idea → prototype modeling idea → run offline experiment → build feature pipeline → drive best-performing approache into production → train and tune model
   - tools seen: catboost (100%), kubeflow (100%), xgboost (100%), airflow (100%)
9. **underwriting strategy change** — 7% of postings [decisions] · [claim → gap:underwriting-strategy-change](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aunderwriting-strategy-change)
   - typical flow: data analysis → analyze data and monitor portfolio performance → develop credit strategie → develop and optimize credit strategie → implement strategie → risk model
   - tools seen: sql (100%), python (100%), data visualization (50%), machine learning (50%)
10. **which product feature to launch** — 7% of postings [decisions] · [claim → gap:which-product-feature-to-launch](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Awhich-product-feature-to-launch)
   - typical flow: data analysis → analyze data and monitor portfolio performance → develop credit strategie → develop and optimize credit strategie → implement strategie → risk model
   - tools seen: sql (100%), python (100%), data visualization (50%), machine learning (50%)

## Machine Learning Engineer — 10 postings from 2 companies (updated 2026-09-05)
**No sims cover this family yet — the whole head is open.**

Uncovered processes (top by demand share — tools shown as context, not gaps):
1. **set technical strategy** — 60% of postings [responsibilities] · [claim → gap:set-technical-strategy](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aset-technical-strategy)
   - typical flow: provision environment → execute test → teardown environment
   - tools seen: transformer (50%), agentic ml (50%), tree-based model (50%), deep learning (50%)
2. **own design and scalability of system** — 60% of postings [responsibilities] · [claim → gap:own-design-and-scalability-of-system](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aown-design-and-scalability-of-system)
   - typical flow: provision environment → design access control pattern → execute test → teardown environment → api → develop integration
   - tools seen: kotlin (67%), terraform (67%), aws (67%), buildkite (67%)
3. **build vs buy trade-off** — 60% of postings [decisions] · [claim → gap:build-vs-buy-trade-off](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Abuild-vs-buy-trade-off)
   - typical flow: provision environment → execute test → teardown environment
   - tools seen: transformer (50%), agentic ml (50%), tree-based model (50%), deep learning (50%)
4. **improve observability and incident response** — 40% of postings [responsibilities] · [claim → gap:improve-observability-and-incident-response](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aimprove-observability-and-incident-response)
   - typical flow: design access control pattern → design platform feature → api → develop integration → monitor and optimize service
   - tools seen: buildkite (100%), python (100%), oidc (100%), ping identity (50%)
5. **develop integration** — 40% of postings [responsibilities] · [claim → gap:develop-integration](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Adevelop-integration)
   - typical flow: design access control pattern → design platform feature → api → develop integration → monitor and optimize service
   - tools seen: buildkite (100%), python (100%), oidc (100%), ping identity (50%)
6. **automation script** — 40% of postings [deliverables] · [claim → gap:automation-script](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aautomation-script)
   - typical flow: provision environment → design access control pattern → execute test → teardown environment → api → develop integration
   - tools seen: kotlin (100%), terraform (100%), aws (100%), buildkite (100%)
7. **design access control pattern** — 40% of postings [decisions] · [claim → gap:design-access-control-pattern](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Adesign-access-control-pattern)
   - typical flow: design access control pattern → design platform feature → api → develop integration → monitor and optimize service
   - tools seen: buildkite (100%), python (100%), oidc (100%), ping identity (50%)
8. **prioritize platform feature** — 40% of postings [decisions] · [claim → gap:prioritize-platform-feature](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aprioritize-platform-feature)
   - typical flow: design platform feature
   - tools seen: github action (100%), docker (100%), buildkite (75%), python (75%)
9. **mentor junior analyst** — 30% of postings [responsibilities] · [claim → gap:mentor-junior-analyst](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Amentor-junior-analyst)
   - tools seen: transformer (100%), agentic ml (100%), tree-based model (100%), deep learning (100%)
10. **define and advocate technical solution** — 30% of postings [responsibilities] · [claim → gap:define-and-advocate-technical-solution](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Adefine-and-advocate-technical-solution)
   - tools seen: transformer (100%), agentic ml (100%), tree-based model (100%), deep learning (100%)

## Platform Engineer — 23 postings from 1 companies (updated 2026-09-05)
**No sims cover this family yet — the whole head is open.**

Uncovered processes (top by demand share — tools shown as context, not gaps):
1. **own and deliver quarterly goal** — 78% of postings [responsibilities] · [claim → gap:own-and-deliver-quarterly-goal](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aown-and-deliver-quarterly-goal)
   - typical flow: define project → ideate and plan → design system → implement code → test with user or stakeholder → deploy and monitor
   - tools seen: kubernetes (94%), kotlin (94%), python (94%), aws (94%)
2. **lead engineer through ambiguity** — 74% of postings [responsibilities] · [claim → gap:lead-engineer-through-ambiguity](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Alead-engineer-through-ambiguity)
   - typical flow: define project → ideate and plan → design system → implement code → test with user or stakeholder → deploy and monitor
   - tools seen: kubernetes (94%), kotlin (94%), python (94%), aws (94%)
3. **foster culture of quality and ownership** — 70% of postings [responsibilities] · [claim → gap:foster-culture-of-quality-and-ownership](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Afoster-culture-of-quality-and-ownership)
   - typical flow: ideate and plan → test with user or stakeholder → make kill or scale decision
   - tools seen: kubernetes (94%), kotlin (94%), python (94%), aws (94%)
4. **identify and solve project process technology issue** — 61% of postings [responsibilities] · [claim → gap:identify-and-solve-project-process-technology-issue](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aidentify-and-solve-project-process-technology-issue)
   - typical flow: identify and solve project process technology issue → define project → design system → implement code → test with user or stakeholder → deploy and monitor
   - tools seen: kubernetes (100%), kotlin (100%), python (100%), aws (100%)
5. **develop talent through feedback and guidance** — 57% of postings [responsibilities] · [claim → gap:develop-talent-through-feedback-and-guidance](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Adevelop-talent-through-feedback-and-guidance)
   - typical flow: ideate and plan → test with user or stakeholder → make kill or scale decision
   - tools seen: kubernetes (92%), kotlin (92%), python (92%), aws (92%)
6. **kpi reporting** — 52% of postings [deliverables] · [claim → gap:kpi-reporting](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Akpi-reporting)
   - typical flow: ideate and plan
   - tools seen: kubernetes (92%), kotlin (92%), python (92%), aws (92%)
7. **collaborate with product management design analytic** — 48% of postings [responsibilities] · [claim → gap:collaborate-with-product-management-design-analytic](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Acollaborate-with-product-management-design-analytic)
   - typical flow: test with user or stakeholder → deploy and monitor → make kill or scale decision
   - tools seen: kubernetes (91%), kotlin (91%), python (91%), aws (91%)
8. **create and monitor metrics** — 48% of postings [responsibilities] · [claim → gap:create-and-monitor-metrics](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Acreate-and-monitor-metrics)
   - typical flow: test with user or stakeholder → make kill or scale decision
   - tools seen: kubernetes (91%), kotlin (91%), python (91%), aws (91%)
9. **support on-call effort** — 43% of postings [responsibilities] · [claim → gap:support-on-call-effort](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Asupport-on-call-effort)
   - tools seen: kubernetes (90%), kotlin (90%), python (90%), aws (90%)
10. **design standard** — 43% of postings [deliverables] · [claim → gap:design-standard](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Adesign-standard)
   - typical flow: test with user or stakeholder → make kill or scale decision
   - tools seen: kubernetes (90%), kotlin (90%), python (90%), aws (90%)

## Product Manager — 80 postings from 20 companies (updated 2026-09-05)
**No sims cover this family yet — the whole head is open.**
_(items from responsibilities, decisions, deliverables withheld: vocabulary too fragmented to rank at current corpus size)_

Uncovered processes (top by demand share — tools shown as context, not gaps):

## Risk Compliance Manager — 14 postings from 1 companies (updated 2026-09-05)
**No sims cover this family yet — the whole head is open.**

Uncovered processes (top by demand share — tools shown as context, not gaps):
1. **ensure compliance and governance** — 50% of postings [responsibilities] · [claim → gap:ensure-compliance-and-governance](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aensure-compliance-and-governance)
   - typical flow: risk assessment → ensure compliance and governance → executive reporting
   - tools seen: vulnerability management tool (14%), encryption standard (14%), endpoint protection (14%), identity governance tool (14%)
2. **lead and develop team** — 50% of postings [responsibilities] · [claim → gap:lead-and-develop-team](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Alead-and-develop-team)
   - typical flow: receive complaint → assess validity → determine resolution → user consultation → identify potential cause → drive improvement
   - tools seen: vulnerability management tool (14%), encryption standard (14%), endpoint protection (14%), identity governance tool (14%)
3. **policie and procedure** — 50% of postings [deliverables] · [claim → gap:policie-and-procedure](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Apolicie-and-procedure)
   - typical flow: risk assessment → ensure compliance and governance → executive reporting
   - tools seen: vulnerability management tool (14%), encryption standard (14%), endpoint protection (14%), identity governance tool (14%)
4. **risk assessment** — 50% of postings [deliverables] · [claim → gap:risk-assessment](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Arisk-assessment)
   - typical flow: risk assessment → ensure compliance and governance → executive reporting
   - tools seen: vulnerability management tool (14%), encryption standard (14%), endpoint protection (14%), identity governance tool (14%)
5. **executive reporting** — 43% of postings [responsibilities] · [claim → gap:executive-reporting](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Aexecutive-reporting)
   - typical flow: ensure compliance and governance → executive reporting
   - tools seen: vulnerability management tool (17%), encryption standard (17%), endpoint protection (17%), identity governance tool (17%)
6. **partner cross-functionally with product sales marketing analytic risk finance operation** — 43% of postings [responsibilities] · [claim → gap:partner-cross-functionally-with-product-sales-marketing-analytic-risk-finance-operation](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Apartner-cross-functionally-with-product-sales-marketing-analytic-risk-finance-operation)
   - typical flow: risk assessment
   - tools seen: vulnerability management tool (17%), encryption standard (17%), endpoint protection (17%), identity governance tool (17%)
7. **balance risk with business velocity** — 36% of postings [decisions] · [claim → gap:balance-risk-with-business-velocity](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Abalance-risk-with-business-velocity)
   - tools seen: ticketing system (20%), gcp (20%), cloud control plane (20%), cursor (20%)
8. **report** — 36% of postings [deliverables] · [claim → gap:report](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Areport)
   - typical flow: risk assessment → ensure compliance and governance → executive reporting
   - tools seen: ticketing system (20%), gcp (20%), cloud control plane (20%), cursor (20%)
9. **cross-functional collaboration** — 29% of postings [responsibilities] · [claim → gap:cross-functional-collaboration](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Across-functional-collaboration)
   - typical flow: risk assessment → ensure compliance and governance → executive reporting
10. **training resource** — 29% of postings [responsibilities] · [claim → gap:training-resource](https://github.com/SkillSimm/skillsimm-template-submissions/issues?q=is%3Aissue+label%3Agap%3Atraining-resource)
   - typical flow: receive complaint → assess validity → determine resolution → user consultation → identify potential cause → drive improvement
   - tools seen: vulnerability management tool (25%), encryption standard (25%), endpoint protection (25%), identity governance tool (25%)

---
_Generated by SkillSimm's demand-analysis pipeline from public ATS job
boards (Greenhouse/Lever/Ashby). Counts describe the sampled companies,
not "the market". Extraction v1 · canon v1._
