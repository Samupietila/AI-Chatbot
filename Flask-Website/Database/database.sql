-- Create the ChatAppDatabase
CREATE DATABASE IF NOT EXISTS ChatAppDatabase;

-- Use the database
USE ChatAppDatabase;

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
