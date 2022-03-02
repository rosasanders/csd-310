
CREATE TABLE users (
  'user_id' INT NULL AUTO_INCREMENT,
  'first_name' VARCHAR (75) NOT NULL,
  'last_name' VARCHAR (75) NOT NULL
  PRIMARY KEY(user_id),
);

CREATE TABLE wishlist (
  'wishlist_id' INT NOT NULL AUTO_INCREMENT,
  'user_id' INT NOT NULL AUTO_INCREMENT,
  'book_id' INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY(wishlist_id)
  FOREIGN KEY(user_id)
      REFERENCES users(user_id)
  FOREIGN KEY(book_id)
      REFERENCES book(book_id)
);
  
CREATE TABLE book (
  'book_id' INT NOT NULL AUTO_INCREMENT,
  'book_name' VARCHAR (200) NOT NULL,
  'details' VARCHAR (500),
  'author' VARCHAR (200) NOT NULL,
  PRIMARY KEY(book_id)
);

CREATE TABLE store (
  'stored_id' INT NOT NULL PRIMARY KEY,
  'locale' VARCHAR (550) NOT NULL
);

INSERT INTO store(locale)
    VALUES('1313 Madison Ave, New York, NY 10128');

INSERT INTO book(book_name, author, details)
    VALUES('Jane Eyre', 'Charlotte Bronte');

INSERT INTO book(book_name, author, details)
    VALUES('Because I Could Not Stop For Death', 'Emily Dickinson'');

INSERT INTO book(book_name, author, details)
    VALUES('The Hunchback of Notre Dame', 'Victor Hugo');

INSERT INTO book(book_name, author)
    VALUES('Le Bourgeois Gentilhomme', 'Moliere');

INSERT INTO book(book_name, author)
    VALUES('Tartuffe', 'Moliere');

INSERT INTO book(book_name, author)
    VALUES('Le Malade Imaginaire', 'Moliere');

INSERT INTO book(book_name, author)
    VALUES('The Great Gatsby', 'F. Scott Fitzgerald');

INSERT INTO book(book_name, author)
    VALUES('The Old Man and the Sea', 'Ernest Hemingway');

INSERT INTO book(book_name, author)
    VALUES('The Catcher and the Rye', 'J.D. Salinger');

INSERT INTO user(first_name, last_name) 
    VALUES('William', 'Shakespeare');

INSERT INTO user(first_name, last_name)
    VALUES('Rosaline', 'Capulet');

INSERT INTO user(first_name, last_name)
    VALUES('Duke', 'Orsino');

INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'William'), 
        (SELECT book_id FROM book WHERE book_name = 'Because I Could Not Stop For Death')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Rosaline'),
        (SELECT book_id FROM book WHERE book_name = 'Tartuffe')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Duke'),
        (SELECT book_id FROM book WHERE book_name = 'Le Malade Imaginaire')
    );
