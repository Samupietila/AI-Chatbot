| **Test Case ID** | **Test Scenario** | **Test Steps** | **Expected Result** | **Actual Result** | **Pass/Fail** | **Comments** |
|------------------|-------------------|----------------|---------------------|------------------|---------------|-------------|
| **UI-LANG-001**  | Verify UI text localization in Finnish | 1. Set language to Finnish  <br> 2. Open homepage <br> 3. Check all visible text (e.g., buttons, labels, headings) | All UI text should be displayed in Finnish as per translations | | | |
| **UI-LANG-002**  | Verify UI text localization in Arabic | 1. Set language to Arabic <br> 2. Open homepage <br> 3. Check all visible text (e.g., buttons, labels, headings) | All UI text should be displayed in Arabic as per translations | | | |
| **DB-LANG-001**  | Verify localized welcome message in database | 1. Set language to English <br> 2. Retrieve welcome message from database | Message should be displayed in English | | | |
| **DB-LANG-002**  | Verify localized welcome message in database for Finnish | 1. Set language to Finnish <br> 2. Retrieve welcome message from database | Message should be displayed in Finnish | | | |
| **DB-LANG-003**  | Verify fallback message for unsupported language | 1. Set language to unsupported value (e.g., 'ES') <br> 2. Retrieve welcome message | Default message should be displayed (e.g., "Welcome!") | | | |
| **BOT-LANG-001** | Verify chatbot responses in English | 1. Set chatbot language to English <br> 2. Ask a common question | Response should be in English | | | |
| **BOT-LANG-002** | Verify chatbot responses in Finnish | 1. Set chatbot language to Finnish <br> 2. Ask a common question | Response should be in Finnish | | | |
| **BOT-LANG-003** | Verify chatbot responses in Arabic | 1. Set chatbot language to Arabic <br> 2. Ask a common question | Response should be in Arabic | | | |
| **ERR-LANG-001** | Verify localized error messages for form inputs in Finnish | 1. Set language to Finnish <br> 2. Submit invalid form data (e.g., missing required fields) | Error messages should be displayed in Finnish | | | |
| **ERR-LANG-002** | Verify localized error messages for form inputs in Arabic | 1. Set language to Arabic <br> 2. Submit invalid form data (e.g., missing required fields) | Error messages should be displayed in Arabic | | | |
| **TIME-LANG-001** | Verify localized date/time formatting for Finnish locale | 1. Set language to Finnish <br> 2. Display a date/time field | Date/time should be formatted in Finnish style (e.g., dd.MM.yyyy HH:mm) | | | |
| **TIME-LANG-002** | Verify localized date/time formatting for Arabic locale | 1. Set language to Arabic <br> 2. Display a date/time field | Date/time should be formatted in Arabic style, respecting regional norms | | | |
