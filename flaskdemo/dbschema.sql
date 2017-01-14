DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS review;

CREATE TABLE book (id INTEGER PRIMARY KEY, name TEXT NOT NULL, release_date DATETIME);
CREATE TABLE review (id INTEGER, book_id INTEGER, review TEXT, rating INTEGER, PRIMARY KEY (id), FOREIGN KEY (book_id) REFERENCES book(id));

INSERT INTO book (id, name, release_date) VALUES (1, 'Book1',CURRENT_TIMESTAMP);
INSERT INTO book (id, name, release_date) VALUES (2, 'Book2',CURRENT_TIMESTAMP);
INSERT INTO review (id, book_id, review, rating) VALUES (1,1,'I did not like this book.',2);
INSERT INTO review (id, book_id, review, rating) VALUES (2,1,'I loved this book.',5);
INSERT INTO review (id, book_id, review, rating) VALUES (3,2,'What a weird book.',3);


