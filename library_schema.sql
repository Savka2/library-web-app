-- Структура базы данных веб-приложения «Библиотека»
CREATE TABLE Books (
    Book_ID INT PRIMARY KEY,
    Title VARCHAR(100) NOT NULL,
    Author VARCHAR(60) NOT NULL,
    Genre VARCHAR(30) NOT NULL
);
CREATE TABLE Readers (
    Reader_ID INT PRIMARY KEY,
    Surname VARCHAR(45) NOT NULL,
    Name VARCHAR(45) NOT NULL,
    Phone VARCHAR(16) NOT NULL
);
CREATE TABLE Issues (
    Issue_ID INT PRIMARY KEY,
    Book_ID INT NOT NULL,
    Reader_ID INT NOT NULL,
    Issue_Date DATE NOT NULL,
    Return_Date DATE,
    Rental_Price DECIMAL(8, 2) NOT NULL,
    FOREIGN KEY (Book_ID) REFERENCES Books(Book_ID) ON DELETE CASCADE,
    FOREIGN KEY (Reader_ID) REFERENCES Readers(Reader_ID) ON DELETE CASCADE
);
