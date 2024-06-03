CREATE TABLE sales_targets(
   sales_outlet_id  INTEGER  NOT NULL
  ,beans_goal       INTEGER  NOT NULL
  ,beverage_goal    INTEGER  NOT NULL
  ,food_goal        INTEGER  NOT NULL
  ,merchandise_goal INTEGER  NOT NULL
  ,total_goal       INTEGER  NOT NULL
  ,Date_ID          INTEGER  NOT NULL
  ,Year_ID          INTEGER  NOT NULL
);
INSERT INTO sales_targets(sales_outlet_id,beans_goal,beverage_goal,food_goal,merchandise_goal,total_goal,Date_ID,Year_ID) VALUES (3,720,13500,3420,360,18000,4,2019);
INSERT INTO sales_targets(sales_outlet_id,beans_goal,beverage_goal,food_goal,merchandise_goal,total_goal,Date_ID,Year_ID) VALUES (4,720,13500,3420,360,18000,4,2019);
INSERT INTO sales_targets(sales_outlet_id,beans_goal,beverage_goal,food_goal,merchandise_goal,total_goal,Date_ID,Year_ID) VALUES (5,1000,18750,4750,500,25000,4,2019);
INSERT INTO sales_targets(sales_outlet_id,beans_goal,beverage_goal,food_goal,merchandise_goal,total_goal,Date_ID,Year_ID) VALUES (6,720,13500,3420,360,18000,4,2019);
INSERT INTO sales_targets(sales_outlet_id,beans_goal,beverage_goal,food_goal,merchandise_goal,total_goal,Date_ID,Year_ID) VALUES (7,720,13500,3420,360,18000,4,2019);
INSERT INTO sales_targets(sales_outlet_id,beans_goal,beverage_goal,food_goal,merchandise_goal,total_goal,Date_ID,Year_ID) VALUES (8,900,16875,4275,450,22500,4,2019);
INSERT INTO sales_targets(sales_outlet_id,beans_goal,beverage_goal,food_goal,merchandise_goal,total_goal,Date_ID,Year_ID) VALUES (9,720,13500,3420,360,18000,4,2019);
INSERT INTO sales_targets(sales_outlet_id,beans_goal,beverage_goal,food_goal,merchandise_goal,total_goal,Date_ID,Year_ID) VALUES (10,720,13500,3420,360,18000,4,2019);

ALTER TABLE sales_targets Add constraint fk_sales_targets_sales_outlet_id foreign key (sales_outlet_id) references sales_outlet(sales_outlet_id);
ALTER TABLE sales_targets add constraint fk_sales_targets_year_ID foreign key (Year_ID) references dates(Year_ID);