DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS reviews;

CREATE TABLE books (id INTEGER PRIMARY KEY, name TEXT NOT NULL, release_date DATETIME);
CREATE TABLE reviews (id INTEGER, book_id INTEGER, review TEXT, rating INTEGER, PRIMARY KEY (id, book_id) );

INSERT INTO books (name, release_date) VALUES ('Book1',CURRENT_TIMESTAMP);
INSERT INTO books (name, release_date) VALUES ('Book2',CURRENT_TIMESTAMP);
INSERT INTO reviews (book_id, review, rating) VALUES (1,'I did not like this book.',2);
INSERT INTO reviews (book_id, review, rating) VALUES (1,'I loved this book.',5);
INSERT INTO reviews (book_id, review, rating) VALUES (2,'What a weird book.',3);


