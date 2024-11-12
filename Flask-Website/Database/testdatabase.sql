-- Create the TestChatAppDatabase
CREATE DATABASE IF NOT EXISTS TestChatAppDatabase;

-- Use the test database
USE TestChatAppDatabase;

-- Create the User table
CREATE TABLE IF NOT EXISTS User (
    UserID INT PRIMARY KEY AUTO_INCREMENT,
    Username VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Password VARCHAR(100) NOT NULL,
    RegistrationDate DATE NOT NULL,
    LastLogin DATE
);

-- Create the UserIssue table
CREATE TABLE IF NOT EXISTS UserIssue (
    IssueID INT PRIMARY KEY AUTO_INCREMENT,
    IssueDescription TEXT NOT NULL,
    IssueCategory VARCHAR(50) NOT NULL,
    UserID INT,
    FOREIGN KEY (UserID) REFERENCES User(UserID)
);

-- Create the ChatHistory table
CREATE TABLE IF NOT EXISTS ChatHistory (
    ChatID INT PRIMARY KEY AUTO_INCREMENT,
    UserID INT,
    MessageTimeStamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    MessageContent TEXT NOT NULL,
    AIResponse TEXT,
    FOREIGN KEY (UserID) REFERENCES User(UserID)
);

-- Create the Translations table
CREATE TABLE IF NOT EXISTS translations (
    TranslationID INT PRIMARY KEY AUTO_INCREMENT,
    TableName VARCHAR(50) NOT NULL,
    ColumnName VARCHAR(50) NOT NULL,
    RowID INT NOT NULL,
    LanguageCode CHAR(2) NOT NULL,
    TranslatedText TEXT NOT NULL,
    UNIQUE(TableName, ColumnName, RowID, LanguageCode)
);

-- Insert sample welcome messages into the Translations table
INSERT INTO translations (TableName, ColumnName, RowID, LanguageCode, TranslatedText)
VALUES
    ('user', 'WelcomeMessage', 1, 'EN', 'Welcome to our site!'),
    ('user', 'WelcomeMessage', 1, 'FI', 'Tervetuloa sivustollemme!'),
    ('user', 'WelcomeMessage', 1, 'AR', 'مرحبًا بكم في موقعنا!');

-- Set character encoding to UTF-8mb4
SET NAMES 'utf8mb4';
SET CHARACTER SET 'utf8mb4';

-- Convert tables to use UTF-8mb4 character set and collation
ALTER TABLE User CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE ChatHistory CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
