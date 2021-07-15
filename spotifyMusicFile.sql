-- MariaDB dump 10.17  Distrib 10.4.8-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: spotify_music
-- ------------------------------------------------------
-- Server version	10.4.8-MariaDB-1:10.4.8+maria~bionic-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `search_history`
--

DROP TABLE IF EXISTS `search_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `search_history` (
  `level_0` double DEFAULT NULL,
  `index` bigint(20) DEFAULT NULL,
  `Name` text DEFAULT NULL,
  `Artists` text DEFAULT NULL,
  `Add Date` text DEFAULT NULL,
  `Popularity` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `search_history`
--

LOCK TABLES `search_history` WRITE;
/*!40000 ALTER TABLE `search_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `search_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `today_top_hits`
--

DROP TABLE IF EXISTS `today_top_hits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `today_top_hits` (
  `index` bigint(20) DEFAULT NULL,
  `Name` text DEFAULT NULL,
  `Artists` text DEFAULT NULL,
  `Add Date` text DEFAULT NULL,
  `Popularity` bigint(20) DEFAULT NULL,
  KEY `ix_today_top_hits_index` (`index`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `today_top_hits`
--

LOCK TABLES `today_top_hits` WRITE;
/*!40000 ALTER TABLE `today_top_hits` DISABLE KEYS */;
INSERT INTO `today_top_hits` VALUES (0,'Stay (with Justin Bieber)','The Kid LAROI','2021-07-12T04:00:00Z',90),(1,'Bad Habits','Ed Sheeran','2021-07-12T04:00:00Z',95),(2,'Chosen','Måneskin','2021-07-12T04:00:00Z',98),(3,'Motley Crew','Post Malone','2021-07-12T04:00:00Z',84),(4,'NDA','Billie Eilish','2021-07-12T04:00:00Z',84),(5,'good 4 u','Olivia Rodrigo','2021-07-12T04:00:00Z',90),(6,'Kiss Me More (feat. SZA)','Doja Cat','2021-07-12T04:00:00Z',97),(7,'Butter / Permission to Dance','BTS','2021-07-12T04:00:00Z',92),(8,'Levitating (feat. DaBaby)','Dua Lipa','2021-07-12T04:00:00Z',91),(9,'MONTERO (Call Me By Your Name)','Lil Nas X','2021-07-12T04:00:00Z',65),(10,'Save Your Tears (Remix)','The Weeknd','2021-07-12T04:00:00Z',95),(11,'Leave The Door Open','Bruno Mars','2021-07-12T04:00:00Z',94),(12,'Justice','Justin Bieber','2021-07-12T04:00:00Z',96),(13,'Yonaguni','Bad Bunny','2021-07-12T04:00:00Z',97),(14,'Planet Her','Doja Cat','2021-07-12T04:00:00Z',89),(15,'Butter','BTS','2021-07-12T04:00:00Z',87),(16,'Dreamland','Glass Animals','2021-07-12T04:00:00Z',84),(17,'Todo De Ti','Rauw Alejandro','2021-07-12T04:00:00Z',97),(18,'Leave Before You Love Me','Marshmello','2021-07-12T04:00:00Z',88),(19,'deja vu','Olivia Rodrigo','2021-07-12T04:00:00Z',85),(20,'Build a Bitch','Bella Poarch','2021-07-12T04:00:00Z',92),(21,'Qué Más Pues?','J Balvin','2021-07-12T04:00:00Z',95),(22,'Beautiful Mistakes (feat. Megan Thee Stallion)','Maroon 5','2021-07-12T04:00:00Z',81),(23,'Astronaut In The Ocean','Masked Wolf','2021-07-12T04:00:00Z',92),(24,'When It\'s All Said And Done... Take Time','Giveon','2021-07-12T04:00:00Z',79),(25,'Thot Shit','Megan Thee Stallion','2021-07-12T04:00:00Z',87),(26,'Friday (feat. Mufasa & Hypeman) [Dopamine Re-Edit]','Riton','2021-07-12T04:00:00Z',93),(27,'Teatro d\'ira - Vol. I','Måneskin','2021-07-12T04:00:00Z',95),(28,'Run','OneRepublic','2021-07-12T04:00:00Z',88),(29,'SOUR','Olivia Rodrigo','2021-07-12T04:00:00Z',95),(30,'Goosebumps (Remix)','Travis Scott','2021-07-12T04:00:00Z',89),(31,'Heartbreak Anthem (with David Guetta & Little Mix)','Galantis','2021-07-12T04:00:00Z',89),(32,'Future Nostalgia (The Moonlight Edition)','Dua Lipa','2021-07-12T04:00:00Z',86),(33,'Reckless','Madison Beer','2021-07-12T04:00:00Z',84),(34,'F*CK LOVE (SAVAGE)','The Kid LAROI','2021-07-12T04:00:00Z',88),(35,'Lost Cause','Billie Eilish','2021-07-12T04:00:00Z',87),(36,'CALL ME IF YOU GET LOST','Tyler, The Creator','2021-07-12T04:00:00Z',87),(37,'RAPSTAR','Polo G','2021-07-12T04:00:00Z',91),(38,'seaside_demo','SEB','2021-07-12T04:00:00Z',77),(39,'Little Bit of Love','Tom Grennan','2021-07-12T04:00:00Z',82),(40,'Rasputin','Majestic','2021-07-12T04:00:00Z',90),(41,'Best Friend (feat. Doja Cat)','Saweetie','2021-07-12T04:00:00Z',86),(42,'Late At Night','Roddy Ricch','2021-07-12T04:00:00Z',85),(43,'Your Love (9PM)','ATB','2021-07-12T04:00:00Z',89),(44,'By Your Side (feat. Tom Grennan)','Calvin Harris','2021-07-12T04:00:00Z',86),(45,'t r a n s p a r e n t s o u l feat. Travis Barker','WILLOW','2021-07-12T04:00:00Z',87),(46,'Up','Cardi B','2021-07-12T04:00:00Z',86),(47,'Girls Like Us','Zoe Wees','2021-07-12T04:00:00Z',82),(48,'Our Song','Anne-Marie','2021-07-12T04:00:00Z',84),(49,'Black Hole','Griff','2021-07-12T04:00:00Z',80);
/*!40000 ALTER TABLE `today_top_hits` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-15 14:37:59
