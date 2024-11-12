##  Test Case Model for Localization Testing

| **Test Case ID** | **Test Scenario** | **Test Steps** | **Expected Result** | **Actual Result** | **Pass/Fail** | **Comments** |
|------------------|-------------------|----------------|---------------------|------------------|---------------|-------------|

| **DB-LANG-001**  | Verify localized welcome message in database | 1. Set language to English <br> 2. Retrieve welcome message from database | Message should be displayed in English | | | |
| **DB-LANG-002**  | Verify localized welcome message in database for Finnish | 1. Set language to Finnish <br> 2. Retrieve welcome message from database | Message should be displayed in Finnish | | | |
| **DB-LANG-003**  | Verify fallback message for unsupported language | 1. Set language to unsupported value (e.g., 'ES') <br> 2. Retrieve welcome message | Default message should be displayed (e.g., "Welcome!") | | | |
