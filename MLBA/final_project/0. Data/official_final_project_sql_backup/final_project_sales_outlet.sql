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
-- Table structure for table `sales_outlet`
--

DROP TABLE IF EXISTS `sales_outlet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sales_outlet` (
  `sales_outlet_id` int NOT NULL AUTO_INCREMENT,
  `sales_outlet_type` varchar(9) COLLATE utf8mb3_bin NOT NULL,
  `store_square_feet` int NOT NULL,
  `store_address` varchar(18) COLLATE utf8mb3_bin NOT NULL,
  `store_city` varchar(16) COLLATE utf8mb3_bin NOT NULL,
  `store_state_province` varchar(2) COLLATE utf8mb3_bin NOT NULL,
  `store_telephone` varchar(12) COLLATE utf8mb3_bin NOT NULL,
  `store_postal_code` int NOT NULL,
  `store_longitude` decimal(10,6) NOT NULL,
  `store_latitude` decimal(9,6) NOT NULL,
  `manager` decimal(4,1) DEFAULT NULL,
  `Neighorhood` varchar(17) COLLATE utf8mb3_bin NOT NULL,
  PRIMARY KEY (`sales_outlet_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sales_outlet`
--

LOCK TABLES `sales_outlet` WRITE;
/*!40000 ALTER TABLE `sales_outlet` DISABLE KEYS */;
INSERT INTO `sales_outlet` VALUES (2,'warehouse',3400,'164-14 Jamaica Ave','Jamaica','NY','972-871-0402',11432,-73.795168,40.705226,NULL,'Jamaica'),(3,'retail',1300,'32-20 Broadway','Long Island City','NY','777-718-3190',11106,-73.924008,40.761196,6.0,'Astoria'),(4,'retail',1300,'604 Union Street','Brooklyn','NY','619-347-5193',11215,-73.983984,40.677645,11.0,'Gowanus'),(5,'retail',900,'100 Church Street','New York','NY','343-212-5151',10007,-74.010130,40.713290,16.0,'Lower Manhattan'),(6,'retail',1000,'122 E Broadway','New York','NY','613-555-4989',10002,-73.992687,40.713852,21.0,'Lower East Side'),(7,'retail',1200,'224 E 57th Street','New York','NY','287-817-2330',10021,-73.960000,40.770000,26.0,'Upper East Side'),(8,'retail',1500,'687 9th Avenue','New York','NY','652-212-7020',10036,-73.990338,40.761887,31.0,'Hell\'s Kitchen'),(9,'retail',1700,'175 8th Avenue','New York','NY','242-212-0080',10011,-74.000502,40.742760,36.0,'Chelsea'),(10,'retail',1600,'183 W 10th Street','New York','NY','674-646-6434',10014,-74.002722,40.734367,41.0,'Greenwich Village');
/*!40000 ALTER TABLE `sales_outlet` ENABLE KEYS */;
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
