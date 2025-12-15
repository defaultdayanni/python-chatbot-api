USE ChatbotDB;
GO

CREATE TABLE conversations (
    id INT IDENTITY(1,1) PRIMARY KEY,
    user_message NVARCHAR(MAX) NOT NULL,
    bot_response NVARCHAR(MAX) NOT NULL,
    created_at DATETIME DEFAULT GETDATE()
);
GO
