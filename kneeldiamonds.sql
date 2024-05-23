-- Run this block if you already have a database and need to re-create it
DELETE FROM metals;
DELETE FROM sizes;
DELETE FROM styles;
DELETE FROM orders;

DROP TABLE IF EXISTS metals;
DROP TABLE IF EXISTS sizes;
DROP TABLE IF EXISTS styles;
DROP TABLE IF EXISTS orders;
-- End block




CREATE TABLE `metals` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `sizes` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carets` FLOAT NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `styles` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` TEXT NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `orders` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal_id` INTEGER NOT NULL,
    `size_id` INTEGER NOT NULL,
    `style_id` INTEGER NOT NULL,
    FOREIGN KEY (`metal_id`) REFERENCES `Metals`(`id`),
    FOREIGN KEY (`size_id`) REFERENCES `Sizes`(`id`),
    FOREIGN KEY (`style_id`) REFERENCES `Styles`(`id`)
);


INSERT INTO `Styles` VALUES (null, 'Classic', 500.00);
INSERT INTO `Styles` VALUES (null, 'Modern', 712.00);
INSERT INTO `Styles` VALUES (null, 'Vintage', 965.00);


INSERT INTO `Sizes` VALUES (null, 0.5, 405.00);
INSERT INTO `Sizes` VALUES (null, 0.75, 782.00);
INSERT INTO `Sizes` VALUES (null, 1.0, 1470.00);
INSERT INTO `Sizes` VALUES (null, 1.5, 1997.00);
INSERT INTO `Sizes` VALUES (null, 2.0, 3638.00);


INSERT INTO `Metals` VALUES (null, 'Sterling Silver', 12.42);
INSERT INTO `Metals` VALUES (null, '14K Gold', 736.40);
INSERT INTO `Metals` VALUES (null, '24K Gold', 1258.99);
INSERT INTO `Metals` VALUES (null, 'Platinum', 795.47);
INSERT INTO `Metals` VALUES (null, 'Palladium', 1241.00);

INSERT INTO `Orders` VALUES (null, 1, 1, 1);
INSERT INTO `Orders` VALUES (null, 3, 3, 3);
INSERT INTO `Orders` VALUES (null, 2, 2, 2);
INSERT INTO `Orders` VALUES (null, 5, 5, 3);
INSERT INTO `Orders` VALUES (null, 4, 4, 1);