



-- section 1   user, user-address




-- Users Table
CREATE TABLE users (
    user_id INT PRIMARY KEY IDENTITY(1,1),
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone_number VARCHAR(20),
    created_at DATETIME DEFAULT GETDATE()
);




CREATE TABLE addresses (
    AddressID INT PRIMARY KEY IDENTITY(1,1),
    user_id INT,
    AddressTitle VARCHAR(50), -- e.g. "Home", "Office"
    AddressLine1 VARCHAR(255),
    City VARCHAR(100),
    State VARCHAR(100),
    ZipCode VARCHAR(20),
    IsDefault BIT DEFAULT 0, -- 1 if this is their primary address
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);



-- section 2 products 





CREATE TABLE products (
    product_id INT PRIMARY KEY IDENTITY(1,1),
    name VARCHAR(150) NOT NULL,
    description NVARCHAR(MAX),
    price DECIMAL(10, 2) NOT NULL,
    image_url VARCHAR(255),
    


    category VARCHAR(50) NOT NULL,
    CONSTRAINT CK_Product_Category CHECK (category IN ('Skin Care', 'Medication', 'Home Care', 'Mom & Baby', 'Hair Care', 'Vitamins & Supplements')),
    

    active_ingredients VARCHAR(255), 
    dosage_form VARCHAR(50),         
    package_size VARCHAR(50),        
    requires_prescription BIT DEFAULT 0,
    

    is_popular BIT DEFAULT 0,   
    is_new_offer BIT DEFAULT 0, 
    
    created_at DATETIME DEFAULT GETDATE()
);


-- Inventory Table
CREATE TABLE inventory (
    inventory_id INT PRIMARY KEY IDENTITY(1,1),
    product_id INT NOT NULL,
    batch_number VARCHAR(50),
    expiry_date DATE NOT NULL,
    quantity_in_stock INT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);






-- section 3   cart, cart-items






CREATE TABLE carts (
    cart_id INT PRIMARY KEY IDENTITY(1,1),
    user_id INT, 
    session_id VARCHAR(100),
    created_at DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);



CREATE TABLE cart_items (
    cart_item_id INT PRIMARY KEY IDENTITY(1,1),
    cart_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    added_at DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (cart_id) REFERENCES carts(cart_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);





-- section 4   order, order-items








CREATE TABLE orders (
    order_id INT PRIMARY KEY IDENTITY(1,1),
    user_id INT NOT NULL,
    shipping_address_id INT, 
    

    subtotal DECIMAL(10, 2) NOT NULL,
    tax_amount DECIMAL(10, 2) DEFAULT 0.00,
    shipping_cost DECIMAL(10, 2) DEFAULT 0.00,
    total_amount DECIMAL(10, 2) NOT NULL,
    

    order_status VARCHAR(20) DEFAULT 'Processing',
    CONSTRAINT CK_Order_Status CHECK (order_status IN ('Processing', 'Shipped', 'Delivered', 'Cancelled', 'Returned')),

    payment_method VARCHAR(50) DEFAULT 'Cash on Delivery',
    CONSTRAINT CK_Payment_Method CHECK (payment_method IN ('Cash on Delivery')),

    payment_status VARCHAR(20) DEFAULT 'Pending',
    CONSTRAINT CK_Payment_Status CHECK (payment_status IN ('Pending', 'Paid')),
    
    created_at DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (shipping_address_id) REFERENCES user_addresses(address_id)
);



CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY IDENTITY(1,1),
    order_id    INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    price_at_purchase DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);





-- section 5   reviews, contact-messages







-- Contact Messages Table
CREATE TABLE contact_messages (
    message_id INT PRIMARY KEY IDENTITY(1,1),
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    message NVARCHAR(MAX) NOT NULL,
    submitted_at DATETIME DEFAULT GETDATE()
);


-- Reviews Table
CREATE TABLE reviews (
    review_id INT PRIMARY KEY IDENTITY(1,1),
    product_id INT NOT NULL,
    user_id INT NOT NULL,
    rating INT,
    CONSTRAINT CK_Review_Rating CHECK (rating >= 1 AND rating <= 5),
    comment NVARCHAR(MAX),
    created_at DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);



delete DATABASE pharmaEase