-- STEP 1 — Create Databases
CREATE DATABASE EcommerceDB;

-- Select Database
USE EcommerceDB;

-- Customers Table
CREATE TABLE Customers (
    customer_id      INT AUTO_INCREMENT PRIMARY KEY,
    full_name        VARCHAR(100) NOT NULL,
    email            VARCHAR(120) NOT NULL UNIQUE,
    phone            CHAR(10),
    city             VARCHAR(50),
    address          TEXT,
    created_at       DATETIME DEFAULT NOW(),
    is_active        BOOLEAN DEFAULT TRUE,
    profile_picture  BLOB,
    preferences      JSON
);

-- Products Table
CREATE TABLE Products (
    product_id     INT AUTO_INCREMENT PRIMARY KEY,
    name           VARCHAR(100) NOT NULL,
    category       ENUM('Electronics', 'Clothing', 'Furniture', 'Other') NOT NULL,
    price          DECIMAL(10,2) NOT NULL,
    rating         FLOAT DEFAULT 0,
    stock          SMALLINT DEFAULT 0,
    tags           SET('New','Sale','Featured','Limited'),
    specs          JSON,
    created_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Orders Table
CREATE TABLE Orders (
    order_id       BIGINT AUTO_INCREMENT PRIMARY KEY,
    customer_id    INT NOT NULL,
    order_date     DATE NOT NULL,
    order_time     TIME,
    payment_status VARCHAR(20) DEFAULT 'Pending',
    total_amount   DECIMAL(12,2) NOT NULL,
    location       POINT,

    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- OrderItems Table
CREATE TABLE OrderItems (
    order_item_id   INT AUTO_INCREMENT PRIMARY KEY,
    order_id        BIGINT NOT NULL,
    product_id      INT NOT NULL,
    quantity        TINYINT NOT NULL CHECK (quantity > 0),
    price           DECIMAL(10,2) NOT NULL,
    subtotal        DECIMAL(10,2) 
        GENERATED ALWAYS AS (quantity * price) STORED,

    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- Includes: JSON, ENUM, SET, BLOB, POINT, generated columns, FK constraints.
