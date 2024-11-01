Database translation instructions and examples

In this process, we implemented field-level localizaiton in our database to support multiple languages—Finnish, English, and Arabic—by adding a dedicated translations table. This approach enables specific fields, such as usernames, message content, and issue descriptions, to store translations directly in the database, without duplicating entire records for each language.

Set the database to use UTF-8



SET NAMES 'utf8mb4';

SET CHARACTER SET 'utf8mb4';

ALTER TABLE user CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci; ALTER TABLE chathistory CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;



Create translations table



CREATE TABLE translations ( TranslationID INT PRIMARY KEY AUTO_INCREMENT, TableName VARCHAR(50) NOT NULL, ColumnName VARCHAR(50) NOT NULL, RowID INT NOT NULL, LanguageCode CHAR(2) NOT NULL, TranslatedText TEXT NOT NULL, UNIQUE(TableName, ColumnName, RowID, LanguageCode) );



Example to insert sample data to table



Inserting into the `user` table



INSERT INTO user (Username, Email, Password, RegistrationDate, LastLogin)

VALUES ('JohnDoe', 'john@example.com', 'password123', CURDATE(), NULL);



Inserting into the `chathistory` table

ALTER TABLE chathistory MODIFY ChatID INT AUTO_INCREMENT;

INSERT INTO chathistory (UserID, MessageTimeStamp, MessageContent, AIResponse) VALUES (1, NOW(), 'Hello, how can I help you?', 'I am here to assist.');



Inserting into the `userissue` table



INSERT INTO userissue (IssueID, IssueDescription, IssueCategory, UserID)

VALUES (1, 'App crashes on startup', 'Bug', 1);



Username translations for user with UserID 1



INSERT INTO translations (TableName, ColumnName, RowID, LanguageCode, TranslatedText)

VALUES

('user', 'Username', 1, 'EN', 'JohnDoe'),

('user', 'Username', 1, 'FI', 'JohannesDoe'),

('user', 'Username', 1, 'AR', 'جون دو');



MessageContent translations for ChatID 1



INSERT INTO translations (TableName, ColumnName, RowID, LanguageCode, TranslatedText)

VALUES

('chathistory', 'MessageContent', 1, 'EN', 'Hello, how can I help you?'),

('chathistory', 'MessageContent', 1, 'FI', 'Hei, miten voin auttaa?'),

('chathistory', 'MessageContent', 1, 'AR', 'مرحبًا، كيف يمكنني مساعدتك؟');



IssueDescription translations for IssueID 1



INSERT INTO translations (TableName, ColumnName, RowID, LanguageCode, TranslatedText)

VALUES

('userissue', 'IssueDescription', 1, 'EN', 'App crashes on startup'),

('userissue', 'IssueDescription', 1, 'FI', 'Sovellus kaatuu käynnistyksessä'),

('userissue', 'IssueDescription', 1, 'AR', 'التطبيق يتعطل عند بدء التشغيل');



Retrieve localized data based on language preference

Change 'FI' to preferred language code



SELECT u.UserID,

COALESCE(t.TranslatedText, u.Username) AS Username

FROM user u

LEFT JOIN translations t ON t.TableName = 'user'

AND t.ColumnName = 'Username'

AND t.RowID = u.UserID

AND t.LanguageCode = 'FI'

WHERE u.UserID = 1;



Update or insert new translations



-- Update or insert a new translation for `user` table's `Username`

INSERT INTO translations (TableName, ColumnName, RowID, LanguageCode, TranslatedText)

VALUES ('user', 'Username', 1, 'FI', 'JohannesDoe')

ON DUPLICATE KEY UPDATE TranslatedText = 'JohannesDoe';



Delete a Translation



DELETE FROM translations

WHERE TableName = 'user' AND ColumnName = 'Username' AND RowID = 1 AND LanguageCode = 'FI';

