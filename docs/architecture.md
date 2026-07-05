# Clinical Documentation Agent Architecture

Clinical documentation agent that generates structured clinical notes from physician dictation, applies medical coding suggestions, ensures compliance with documentation standards, and identifies documentation gaps.

## Domain Tools

- **transcribe_dictation**: Transcribe physician dictation into structured clinical note
- **suggest_codes**: Suggest ICD-10, CPT, and HCPCS codes from clinical documentation
- **check_completeness**: Check clinical documentation for required elements and gaps
- **apply_template**: Apply a documentation template for a specific encounter type
- **audit_quality**: Audit documentation quality and CDI opportunities