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
-- Table structure for table `staffs`
--

DROP TABLE IF EXISTS `staffs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staffs` (
  `staff_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(8) COLLATE utf8mb3_bin NOT NULL,
  `last_name` varchar(8) COLLATE utf8mb3_bin NOT NULL,
  `position` varchar(15) COLLATE utf8mb3_bin NOT NULL,
  `start_date` date NOT NULL,
  `location` varchar(2) COLLATE utf8mb3_bin NOT NULL,
  `user_name` varchar(25) COLLATE utf8mb3_bin DEFAULT NULL,
  `password_acc` varchar(25) COLLATE utf8mb3_bin DEFAULT NULL,
  `email` varchar(100) COLLATE utf8mb3_bin DEFAULT NULL,
  `phone` varchar(50) COLLATE utf8mb3_bin DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staffs`
--

LOCK TABLES `staffs` WRITE;
/*!40000 ALTER TABLE `staffs` DISABLE KEYS */;
INSERT INTO `staffs` VALUES (1,'Sue','Tindale','CFO','2001-08-03','HQ','SueTindaleHQ','@Obama123','SueTindaleHQ@bms.com','20010803'),(2,'Ian','Tindale','CEO','2001-08-03','HQ','IanTindaleHQ','@Obama123','IanTindaleHQ@bms.com','20010803'),(3,'Marny','Hermione','Roaster','2007-10-24','WH','MarnyHermioneWH','@Obama123','MarnyHermioneWH@bms.com','20071024'),(4,'Chelsea','Claudia','Roaster','2003-07-03','WH','ChelseaClaudiaWH','@Obama123','ChelseaClaudiaWH@bms.com','20030703'),(5,'Alec','Isadora','Roaster','2008-04-02','WH','AlecIsadoraWH','@Obama123','AlecIsadoraWH@bms.com','20080402'),(6,'Xena','Rahim','Store Manager','2016-07-24','3','XenaRahim3','@Obama123','XenaRahim3@bms.com','20160724'),(7,'Kelsey','Cameron','Coffee Wrangler','2003-10-18','3','KelseyCameron3','@Obama123','KelseyCameron3@bms.com','20031018'),(8,'Hamilton','Emi','Coffee Wrangler','2005-02-09','3','HamiltonEmi3','@Obama123','HamiltonEmi3@bms.com','20050209'),(9,'Caldwell','Veda','Coffee Wrangler','2013-09-09','3','CaldwellVeda3','@Obama123','CaldwellVeda3@bms.com','20130909'),(10,'Ima','Winifred','Coffee Wrangler','2016-12-10','3','ImaWinifred3','@Obama123','ImaWinifred3@bms.com','20161210'),(11,'Ruth','Leslie','Store Manager','2009-06-17','4','RuthLeslie4','@Obama123','RuthLeslie4@bms.com','20090617'),(12,'Britanni','Jorden','Coffee Wrangler','2006-03-25','4','BritanniJorden4','@Obama123','BritanniJorden4@bms.com','20060325'),(13,'Berk','Derek','Coffee Wrangler','2009-12-11','4','BerkDerek4','@Obama123','BerkDerek4@bms.com','20091211'),(14,'Damon','Sasha','Coffee Wrangler','2010-06-05','4','DamonSasha4','@Obama123','DamonSasha4@bms.com','20100605'),(15,'Remedios','Mari','Coffee Wrangler','2014-05-09','4','RemediosMari4','@Obama123','RemediosMari4@bms.com','20140509'),(16,'Reed','Eve','Store Manager','2006-03-30','5','ReedEve5','@Obama123','ReedEve5@bms.com','20060330'),(17,'Quail','Octavia','Coffee Wrangler','2014-12-05','5','QuailOctavia5','@Obama123','QuailOctavia5@bms.com','20141205'),(18,'Ezekiel','Rashad','Coffee Wrangler','2005-11-13','5','EzekielRashad5','@Obama123','EzekielRashad5@bms.com','20051113'),(19,'Peter','Paloma','Coffee Wrangler','2014-03-12','5','PeterPaloma5','@Obama123','PeterPaloma5@bms.com','20140312'),(20,'Ronan','Magee','Coffee Wrangler','2002-02-13','5','RonanMagee5','@Obama123','RonanMagee5@bms.com','20020213'),(21,'Melodie','Mercedes','Store Manager','2018-09-29','6','MelodieMercedes6','@Obama123','MelodieMercedes6@bms.com','20180929'),(22,'Marny','Dennis','Coffee Wrangler','2014-03-03','6','MarnyDennis6','@Obama123','MarnyDennis6@bms.com','20140303'),(23,'Blythe','Arsenio','Coffee Wrangler','2018-11-22','6','BlytheArsenio6','@Obama123','BlytheArsenio6@bms.com','20181122'),(24,'Garrett','Doris','Coffee Wrangler','2007-01-27','6','GarrettDoris6','@Obama123','GarrettDoris6@bms.com','20070127'),(25,'Aline','Melanie','Coffee Wrangler','2017-03-14','6','AlineMelanie6','@Obama123','AlineMelanie6@bms.com','20170314'),(26,'Joelle','Christen','Store Manager','2013-11-11','7','JoelleChristen7','@Obama123','JoelleChristen7@bms.com','20131111'),(27,'Ainsley','Evelyn','Coffee Wrangler','2003-07-31','7','AinsleyEvelyn7','@Obama123','AinsleyEvelyn7@bms.com','20030731'),(28,'Joseph','Byron','Coffee Wrangler','2014-05-17','7','JosephByron7','@Obama123','JosephByron7@bms.com','20140517'),(29,'Orson','Benedict','Coffee Wrangler','2016-07-26','7','OrsonBenedict7','@Obama123','OrsonBenedict7@bms.com','20160726'),(30,'Amela','Chadwick','Coffee Wrangler','2005-09-17','7','AmelaChadwick7','@Obama123','AmelaChadwick7@bms.com','20050917'),(31,'Dawn','Anthony','Store Manager','2009-07-02','8','DawnAnthony8','@Obama123','DawnAnthony8@bms.com','20090702'),(32,'Alisa','Lysandra','Coffee Wrangler','2005-02-02','8','AlisaLysandra8','@Obama123','AlisaLysandra8@bms.com','20050202'),(33,'Cairo','Vaughan','Coffee Wrangler','2015-02-18','8','CairoVaughan8','@Obama123','CairoVaughan8@bms.com','20150218'),(34,'Yasir','Lillith','Coffee Wrangler','2016-02-16','8','YasirLillith8','@Obama123','YasirLillith8@bms.com','20160216'),(35,'Xavier','Zachary','Coffee Wrangler','2014-01-07','8','XavierZachary8','@Obama123','XavierZachary8@bms.com','20140107'),(36,'Anthony','Kaitlin','Store Manager','2004-04-19','9','AnthonyKaitlin9','@Obama123','AnthonyKaitlin9@bms.com','20040419'),(37,'Hop','Bianca','Coffee Wrangler','2015-02-11','9','HopBianca9','@Obama123','HopBianca9@bms.com','20150211'),(38,'Ezekiel','Bertha','Coffee Wrangler','2008-10-15','9','EzekielBertha9','@Obama123','EzekielBertha9@bms.com','20081015'),(39,'Vance','Samuel','Coffee Wrangler','2016-06-09','9','VanceSamuel9','@Obama123','VanceSamuel9@bms.com','20160609'),(40,'Brent','Herman','Coffee Wrangler','2001-10-25','9','BrentHerman9','@Obama123','BrentHerman9@bms.com','20011025'),(41,'Adrian','Macon','Store Manager','2001-10-13','10','AdrianMacon10','@Obama123','AdrianMacon10@bms.com','20011013'),(42,'Kylie','Candace','Coffee Wrangler','2011-01-30','10','KylieCandace10','@Obama123','KylieCandace10@bms.com','20110130'),(43,'Tatum','Laurel','Coffee Wrangler','2015-01-31','10','TatumLaurel10','@Obama123','TatumLaurel10@bms.com','20150131'),(44,'Tamekah','Maya','Coffee Wrangler','2005-05-17','10','TamekahMaya10','@Obama123','TamekahMaya10@bms.com','20050517'),(45,'Pandora','Neville','Coffee Wrangler','2019-03-21','10','PandoraNeville10','@Obama123','PandoraNeville10@bms.com','20190321'),(46,'Desiree','Anika','Store Manager','2008-06-15','FL','DesireeAnikaFL','@Obama123','DesireeAnikaFL@bms.com','20080615'),(47,'Hope','Sheila','Coffee Wrangler','2003-01-31','FL','HopeSheilaFL','@Obama123','HopeSheilaFL@bms.com','20030131'),(48,'Clare','Oscar','Coffee Wrangler','2003-02-21','FL','ClareOscarFL','@Obama123','ClareOscarFL@bms.com','20030221'),(49,'Gemma','Eaton','Coffee Wrangler','2013-05-04','FL','GemmaEatonFL','@Obama123','GemmaEatonFL@bms.com','20130504'),(50,'Dale','Joshua','Coffee Wrangler','2015-10-01','FL','DaleJoshuaFL','@Obama123','DaleJoshuaFL@bms.com','20151001'),(51,'Lawrence','Roberts','Store Manager','2001-08-03','FL','LawrenceRobertsFL','@Obama123','LawrenceRobertsFL@bms.com','20010803'),(52,'Melinda','Zeus','Coffee Wrangler','2003-08-17','FL','MelindaZeusFL','@Obama123','MelindaZeusFL@bms.com','20030817'),(53,'Sawyer','Kasper','Coffee Wrangler','2007-11-11','FL','SawyerKasperFL','@Obama123','SawyerKasperFL@bms.com','20071111'),(54,'Ezekiel','Griffin','Coffee Wrangler','2005-09-13','FL','EzekielGriffinFL','@Obama123','EzekielGriffinFL@bms.com','20050913'),(55,'Coby','Shelly','Coffee Wrangler','2015-11-17','FL','CobyShellyFL','@Obama123','CobyShellyFL@bms.com','20151117');
/*!40000 ALTER TABLE `staffs` ENABLE KEYS */;
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
