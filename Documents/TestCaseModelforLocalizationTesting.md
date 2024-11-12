##  Test Case Model for Localization Testing

| **Test Case ID** | **Test Scenario** | **Test Steps** | **Expected Result** | **Actual Result** | **Pass/Fail** | **Comments** |
|------------------|-------------------|----------------|---------------------|------------------|---------------|-------------|
| **UI-LANG-001**  | Verify UI text localization in Finnish | 1. Set language to Finnish  <br> 2. Open homepage <br> 3. Check all visible text (e.g., buttons, labels, headings) | All UI text should be displayed in Finnish as per translations | | | |
| **UI-LANG-002**  | Verify UI text localization in Arabic | 1. Set language to Arabic <br> 2. Open homepage <br> 3. Check all visible text (e.g., buttons, labels, headings) | All UI text should be displayed in Arabic as per translations | | | |
| **DB-LANG-001**  | Verify localized welcome message in database | 1. Set language to English <br> 2. Retrieve welcome message from database | Message should be displayed in English | | | |
| **DB-LANG-002**  | Verify localized welcome message in database for Finnish | 1. Set language to Finnish <br> 2. Retrieve welcome message from database | Message should be displayed in Finnish | | | |
| **DB-LANG-003**  | Verify fallback message for unsupported language | 1. Set language to unsupported value (e.g., 'ES') <br> 2. Retrieve welcome message | Default message should be displayed (e.g., "Welcome!") | | | |
