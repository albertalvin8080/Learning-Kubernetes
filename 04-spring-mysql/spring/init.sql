CREATE TABLE product (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL,
    price DECIMAL(12,3) NOT NULL
);

INSERT INTO product (name, price) VALUES ('TV', 1000.90), ('Nothing', 0.00);