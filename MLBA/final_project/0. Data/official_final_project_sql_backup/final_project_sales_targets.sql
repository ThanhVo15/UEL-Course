-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: final_project
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `sales_targets`
--

DROP TABLE IF EXISTS `sales_targets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sales_targets` (
  `sales_outlet_id` int NOT NULL,
  `beans_goal` int NOT NULL,
  `beverage_goal` int NOT NULL,
  `food_goal` int NOT NULL,
  `merchandise_goal` int NOT NULL,
  `total_goal` int NOT NULL,
  `Date_ID` int NOT NULL,
  `Year_ID` int NOT NULL,
  KEY `fk_sales_targets_sales_outlet_id` (`sales_outlet_id`),
  KEY `fk_sales_targets_year_ID` (`Year_ID`),
  CONSTRAINT `fk_sales_targets_sales_outlet_id` FOREIGN KEY (`sales_outlet_id`) REFERENCES `sales_outlet` (`sales_outlet_id`),
  CONSTRAINT `fk_sales_targets_year_ID` FOREIGN KEY (`Year_ID`) REFERENCES `dates` (`Year_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sales_targets`
--

LOCK TABLES `sales_targets` WRITE;
/*!40000 ALTER TABLE `sales_targets` DISABLE KEYS */;
INSERT INTO `sales_targets` VALUES (3,720,13500,3420,360,18000,4,2019),(4,720,13500,3420,360,18000,4,2019),(5,1000,18750,4750,500,25000,4,2019),(6,720,13500,3420,360,18000,4,2019),(7,720,13500,3420,360,18000,4,2019),(8,900,16875,4275,450,22500,4,2019),(9,720,13500,3420,360,18000,4,2019),(10,720,13500,3420,360,18000,4,2019);
/*!40000 ALTER TABLE `sales_targets` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-25 17:31:06
