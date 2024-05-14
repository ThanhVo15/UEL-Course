CREATE TABLE sales_outlet(
   sales_outlet_id      INTEGER  NOT NULL PRIMARY KEY AUTO_INCREMENT
  ,sales_outlet_type    VARCHAR(9) NOT NULL
  ,store_square_feet    INTEGER  NOT NULL
  ,store_address        VARCHAR(18) NOT NULL
  ,store_city           VARCHAR(16) NOT NULL
  ,store_state_province VARCHAR(2) NOT NULL
  ,store_telephone      VARCHAR(12) NOT NULL
  ,store_postal_code    INTEGER  NOT NULL
  ,store_longitude      NUMERIC(10,6) NOT NULL
  ,store_latitude       NUMERIC(9,6) NOT NULL
  ,manager              NUMERIC(4,1)
  ,Neighorhood          VARCHAR(17) NOT NULL
);
INSERT INTO sales_outlet(sales_outlet_id,sales_outlet_type,store_square_feet,store_address,store_city,store_state_province,store_telephone,store_postal_code,store_longitude,store_latitude,manager,Neighorhood) VALUES (2,'warehouse',3400,'164-14 Jamaica Ave','Jamaica','NY','972-871-0402',11432,-73.795168,40.705226,NULL,'Jamaica');
INSERT INTO sales_outlet(sales_outlet_id,sales_outlet_type,store_square_feet,store_address,store_city,store_state_province,store_telephone,store_postal_code,store_longitude,store_latitude,manager,Neighorhood) VALUES (3,'retail',1300,'32-20 Broadway','Long Island City','NY','777-718-3190',11106,-73.924008,40.761196,6.0,'Astoria');
INSERT INTO sales_outlet(sales_outlet_id,sales_outlet_type,store_square_feet,store_address,store_city,store_state_province,store_telephone,store_postal_code,store_longitude,store_latitude,manager,Neighorhood) VALUES (4,'retail',1300,'604 Union Street','Brooklyn','NY','619-347-5193',11215,-73.983984,40.677645,11.0,'Gowanus');
INSERT INTO sales_outlet(sales_outlet_id,sales_outlet_type,store_square_feet,store_address,store_city,store_state_province,store_telephone,store_postal_code,store_longitude,store_latitude,manager,Neighorhood) VALUES (5,'retail',900,'100 Church Street','New York','NY','343-212-5151',10007,-74.01013,40.71329,16.0,'Lower Manhattan');
INSERT INTO sales_outlet(sales_outlet_id,sales_outlet_type,store_square_feet,store_address,store_city,store_state_province,store_telephone,store_postal_code,store_longitude,store_latitude,manager,Neighorhood) VALUES (6,'retail',1000,'122 E Broadway','New York','NY','613-555-4989',10002,-73.992687,40.713852,21.0,'Lower East Side');
INSERT INTO sales_outlet(sales_outlet_id,sales_outlet_type,store_square_feet,store_address,store_city,store_state_province,store_telephone,store_postal_code,store_longitude,store_latitude,manager,Neighorhood) VALUES (7,'retail',1200,'224 E 57th Street','New York','NY','287-817-2330',10021,-73.96,40.77,26.0,'Upper East Side');
INSERT INTO sales_outlet(sales_outlet_id,sales_outlet_type,store_square_feet,store_address,store_city,store_state_province,store_telephone,store_postal_code,store_longitude,store_latitude,manager,Neighorhood) VALUES (8,'retail',1500,'687 9th Avenue','New York','NY','652-212-7020',10036,-73.990338,40.761887,31.0,'Hell''s Kitchen');
INSERT INTO sales_outlet(sales_outlet_id,sales_outlet_type,store_square_feet,store_address,store_city,store_state_province,store_telephone,store_postal_code,store_longitude,store_latitude,manager,Neighorhood) VALUES (9,'retail',1700,'175 8th Avenue','New York','NY','242-212-0080',10011,-74.000502,40.74276,36.0,'Chelsea');
INSERT INTO sales_outlet(sales_outlet_id,sales_outlet_type,store_square_feet,store_address,store_city,store_state_province,store_telephone,store_postal_code,store_longitude,store_latitude,manager,Neighorhood) VALUES (10,'retail',1600,'183 W 10th Street','New York','NY','674-646-6434',10014,-74.002722,40.734367,41.0,'Greenwich Village');
