select * from auth_user;

desc products_table;
desc category;

INSERT INTO `products`.`products_table`
(`name`,
`summary`,
`color`,
`size`,
`price`,
`Buy`,
`user`)
VALUES
('Happy Ninja','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.',
'Black,Blue','small,large',18.00,'add to cart',1);


INSERT INTO `products`.`products_table`
(`name`,
`summary`,
`color`,
`size`,
`price`,
`Buy`,
`user`)
VALUES
('Happy Ninja','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.',
'Green','small,medium',35.00,'add to cart',1);

INSERT INTO `products`.`products_table`
(`name`,
`summary`,
`color`,
`size`,
`price`,
`Buy`,
`user`)
VALUES
('Ninja Sithouette','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.',
'Black','small,medium,large,XL',20.00,'add to cart',1);

INSERT INTO `products`.`products_table`
(`name`,
`summary`,
`price`,
`Buy`,
`user`)
VALUES
('Ninja Sithouette','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.',
35.00,'add to cart',1);

desc products_table;
select * from products_table;
INSERT INTO CATEGORY(cName,noOfItems) VALUES ('Electronics',10);
SELECT * FROM Category;
INSERT INTO CATEGORY(cName,noOfItems) VALUES ('BeautyProducts',15);
INSERT INTO CATEGORY(cName,noOfItems) VALUES ('Clothes',12);
INSERT INTO CATEGORY(cName,noOfItems) VALUES ('HomeAppliances',20);
INSERT INTO CATEGORY(cName,noOfItems) VALUES ('Toys',30);
UPDATE products_table set cId=1;
SELECT name,summary,color,size,price,buy,cname FROM products_table NATURAL JOIN category where cId=1;
select * from category;
select * from products_table;
SELECT name,summary,color,size,price,buy,cname FROM products_table NATURAL JOIN category;
INSERT INTO CATEGORY values(2,'Food',0,30);
INSERT INTO CATEGORY(cName,noOfItems) VALUES ('Accesories',40);