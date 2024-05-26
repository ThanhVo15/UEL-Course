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
-- Table structure for table `dates`
--

DROP TABLE IF EXISTS `dates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dates` (
  `transaction_date` date NOT NULL,
  `Week_ID` int NOT NULL,
  `Week_Desc` varchar(7) COLLATE utf8mb3_bin NOT NULL,
  `Month_ID` int NOT NULL,
  `Month_Name` varchar(5) COLLATE utf8mb3_bin NOT NULL,
  `Quarter_ID` int NOT NULL,
  `Quarter_Name` varchar(2) COLLATE utf8mb3_bin NOT NULL,
  `Year_ID` int NOT NULL,
  `Dates_ID` int DEFAULT NULL,
  PRIMARY KEY (`transaction_date`),
  KEY `idx_year_id` (`Year_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dates`
--

LOCK TABLES `dates` WRITE;
/*!40000 ALTER TABLE `dates` DISABLE KEYS */;
INSERT INTO `dates` VALUES ('2019-04-01',14,'Week 14',4,'April',2,'Q2',2019,1),('2019-04-02',14,'Week 14',4,'April',2,'Q2',2019,2),('2019-04-03',14,'Week 14',4,'April',2,'Q2',2019,3),('2019-04-04',14,'Week 14',4,'April',2,'Q2',2019,4),('2019-04-05',14,'Week 14',4,'April',2,'Q2',2019,5),('2019-04-06',14,'Week 14',4,'April',2,'Q2',2019,6),('2019-04-07',14,'Week 14',4,'April',2,'Q2',2019,7),('2019-04-08',15,'Week 15',4,'April',2,'Q2',2019,8),('2019-04-09',15,'Week 15',4,'April',2,'Q2',2019,9),('2019-04-10',15,'Week 15',4,'April',2,'Q2',2019,10),('2019-04-11',15,'Week 15',4,'April',2,'Q2',2019,11),('2019-04-12',15,'Week 15',4,'April',2,'Q2',2019,12),('2019-04-13',15,'Week 15',4,'April',2,'Q2',2019,13),('2019-04-14',15,'Week 15',4,'April',2,'Q2',2019,14),('2019-04-15',16,'Week 16',4,'April',2,'Q2',2019,15),('2019-04-16',16,'Week 16',4,'April',2,'Q2',2019,16),('2019-04-17',16,'Week 16',4,'April',2,'Q2',2019,17),('2019-04-18',16,'Week 16',4,'April',2,'Q2',2019,18),('2019-04-19',16,'Week 16',4,'April',2,'Q2',2019,19),('2019-04-20',16,'Week 16',4,'April',2,'Q2',2019,20),('2019-04-21',16,'Week 16',4,'April',2,'Q2',2019,21),('2019-04-22',17,'Week 17',4,'April',2,'Q2',2019,22),('2019-04-23',17,'Week 17',4,'April',2,'Q2',2019,23),('2019-04-24',17,'Week 17',4,'April',2,'Q2',2019,24),('2019-04-25',17,'Week 17',4,'April',2,'Q2',2019,25),('2019-04-26',17,'Week 17',4,'April',2,'Q2',2019,26),('2019-04-27',17,'Week 17',4,'April',2,'Q2',2019,27),('2019-04-28',17,'Week 17',4,'April',2,'Q2',2019,28),('2019-04-29',18,'Week 18',4,'April',2,'Q2',2019,29),('2019-04-30',18,'Week 18',4,'April',2,'Q2',2019,30);
/*!40000 ALTER TABLE `dates` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-25 17:31:05
