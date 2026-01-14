# Metrics & Evaluation Plan: Medical AI Assistant

## Product Metrics (Business Outcomes)

### Primary Metrics
| Metric | Target | Baseline | Cadence |
|--------|--------|----------|----------|
| Triage Accuracy | ≥92% | ~85% | Weekly |
| ED Wait Time Reduction | 15-20% | 300 min avg | Monthly |
| Clinician Adoption Rate | ≥75% at 6mo | 0% | Monthly |
| Patient Safety Incidents | 0 critical | N/A | Real-time |
| Clinician Satisfaction (NPS) | ≥50 | Baseline TBD | Quarterly |

### Secondary Metrics
| Metric | Target | Cadence |
|--------|--------|----------|
| Diagnosis support usage rate | ≥40% of eligible cases | Weekly |
| Escalation accuracy | 100% | Real-time |
| System uptime | ≥99.9% | Daily |
| False alarm rate | <5% | Weekly |

## AI/Model Metrics

### Triage Agent
- **Accuracy:** ESI level matching gold standard (≥92%)
- **Recall by Severity:** ESI-1 recall ≥98% (no missed critical patients)
- **Latency:** <2 seconds per prediction
- **Confidence calibration:** Expected Calibration Error (ECE) < 0.05

### Diagnosis Agent
- **Top-1 Accuracy:** ≥90% for top diagnosis in list
- **Top-3 Recall:** ≥95% for correct diagnosis in top 3 suggestions
- **Hallucination Rate:** <0.1% on critical cases
- **Explainability Score:** Each suggestion must have confidence & reasoning

### Safety Agent
- **False Negative Rate (red flags):** 0% (all critical cases caught)
- **Specificity:** ≥95% (minimize false escalations)
- **Guardrail Activation Rate:** <2% (system confidence < 70%)

## Evaluation Approach

### Offline Evaluation
- **Dataset:** 1,000 de-identified patient cases with gold standard labels
- **Train/Val/Test Split:** 60/20/20
- **Metrics:** Accuracy, precision, recall, F1, AUC-ROC, calibration

### Online A/B Test (Pilot Phase)
- **Hypothesis:** AI-assisted triage reduces ED wait time by 15%
- **Control:** Standard triage (no AI)
- **Treatment:** AI-assisted triage
- **Sample Size:** 500 patients per arm (power = 0.8, α = 0.05)
- **Duration:** 2 weeks
- **Success Criteria:** p-value < 0.05, lift ≥12%

### Fairness & Bias Testing
- **Stratification:** Test accuracy by age, gender, race, chief complaint
- **Equity Goal:** No demographic group <88% accuracy (≤4% gap)
- **Documentation:** Monthly bias audit report

### Safety Monitoring
- **Real-time Dashboards:** Hallucination rate, escalation rate, user feedback
- **Incident Response:** Any critical error → immediate review + model update
- **Post-Deployment Monitoring:** Track clinician overrides as proxy for model drift

## Success Timeline
- **Week 1-2:** Offline evaluation, model validation
- **Week 3-4:** Pilot A/B test with 50 patients
- **Week 5-6:** Expand pilot to 500 patients
- **Week 7-8:** Full ED rollout if metrics met
