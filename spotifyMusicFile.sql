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
  `level_0` bigint(20) DEFAULT NULL,
  `index` bigint(20) DEFAULT NULL,
  `Name` text DEFAULT NULL,
  `Artists` text DEFAULT NULL,
  `Add Date` text DEFAULT NULL,
  `Popularity` double DEFAULT NULL,
  KEY `ix_search_history_level_0` (`level_0`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `search_history`
--

LOCK TABLES `search_history` WRITE;
/*!40000 ALTER TABLE `search_history` DISABLE KEYS */;
INSERT INTO `search_history` VALUES (22,22,'Lost Cause','Billie Eilish','2021-07-02T04:00:00Z',89),(5,5,'Levitating (feat. DaBaby)','Dua Lipa','2021-07-02T04:00:00Z',92),(0,0,'Planet Her','Doja Cat','2021-07-02T04:00:00Z',87);
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
INSERT INTO `today_top_hits` VALUES (0,'Planet Her','Doja Cat','2021-07-02T04:00:00Z',87),(1,'Bad Habits','Ed Sheeran','2021-07-02T04:00:00Z',91),(2,'good 4 u','Olivia Rodrigo','2021-07-02T04:00:00Z',94),(3,'MONTERO (Call Me By Your Name)','Lil Nas X','2021-07-02T04:00:00Z',70),(4,'Chosen','Måneskin','2021-07-02T04:00:00Z',96),(5,'Levitating (feat. DaBaby)','Dua Lipa','2021-07-02T04:00:00Z',92),(6,'Save Your Tears (Remix)','The Weeknd','2021-07-02T04:00:00Z',95),(7,'Kiss Me More (feat. SZA)','Doja Cat','2021-07-02T04:00:00Z',98),(8,'Todo De Ti','Rauw Alejandro','2021-07-02T04:00:00Z',98),(9,'Leave The Door Open','Bruno Mars','2021-07-02T04:00:00Z',95),(10,'Butter','BTS','2021-07-02T04:00:00Z',91),(11,'Justice','Justin Bieber','2021-07-02T04:00:00Z',97),(12,'deja vu','Olivia Rodrigo','2021-07-02T04:00:00Z',89),(13,'Build a Bitch','Bella Poarch','2021-07-02T04:00:00Z',93),(14,'Yonaguni','Bad Bunny','2021-07-02T04:00:00Z',98),(15,'Leave Before You Love Me','Marshmello','2021-07-02T04:00:00Z',88),(16,'Dreamland','Glass Animals','2021-07-02T04:00:00Z',85),(17,'Beautiful Mistakes (feat. Megan Thee Stallion)','Maroon 5','2021-07-02T04:00:00Z',86),(18,'Qué Más Pues?','J Balvin','2021-07-02T04:00:00Z',94),(19,'Astronaut In The Ocean','Masked Wolf','2021-07-02T04:00:00Z',93),(20,'CALL ME IF YOU GET LOST','Tyler, The Creator','2021-07-02T04:00:00Z',86),(21,'When It\'s All Said And Done... Take Time','Giveon','2021-07-02T04:00:00Z',80),(22,'Lost Cause','Billie Eilish','2021-07-02T04:00:00Z',89),(23,'Goosebumps (Remix)','Travis Scott','2021-07-02T04:00:00Z',90),(24,'RAPSTAR','Polo G','2021-07-02T04:00:00Z',93),(25,'Future Nostalgia (The Moonlight Edition)','Dua Lipa','2021-07-02T04:00:00Z',87),(26,'SOUR','Olivia Rodrigo','2021-07-02T04:00:00Z',95),(27,'Run','OneRepublic','2021-07-02T04:00:00Z',89),(28,'Heartbreak Anthem (with David Guetta & Little Mix)','Galantis','2021-07-02T04:00:00Z',89),(29,'Friday (feat. Mufasa & Hypeman) [Dopamine Re-Edit]','Riton','2021-07-02T04:00:00Z',94),(30,'Thot Shit','Megan Thee Stallion','2021-07-02T04:00:00Z',86),(31,'Hold On','Justin Bieber','2021-07-02T04:00:00Z',87),(32,'F*CK LOVE (SAVAGE)','The Kid LAROI','2021-07-02T04:00:00Z',89),(33,'Teatro d\'ira - Vol. I','Måneskin','2021-07-02T04:00:00Z',95),(34,'Rasputin','Majestic','2021-07-02T04:00:00Z',91),(35,'Little Bit of Love','Tom Grennan','2021-07-02T04:00:00Z',83),(36,'Reckless','Madison Beer','2021-07-02T04:00:00Z',83),(37,'Best Friend (feat. Doja Cat)','Saweetie','2021-07-02T04:00:00Z',87),(38,'Late At Night','Roddy Ricch','2021-07-02T04:00:00Z',86),(39,'seaside_demo','SEB','2021-07-02T04:00:00Z',82),(40,'t r a n s p a r e n t s o u l feat. Travis Barker','WILLOW','2021-07-02T04:00:00Z',88),(41,'Solar Power','Lorde','2021-07-02T04:00:00Z',87),(42,'By Your Side (feat. Tom Grennan)','Calvin Harris','2021-07-02T04:00:00Z',86),(43,'Your Love (9PM)','ATB','2021-07-02T04:00:00Z',90),(44,'Black Hole','Griff','2021-07-02T04:00:00Z',81),(45,'Our Song','Anne-Marie','2021-07-02T04:00:00Z',85),(46,'Girls Like Us','Zoe Wees','2021-07-02T04:00:00Z',83),(47,'Small Town Boy','Duncan Laurence','2021-07-02T04:00:00Z',76),(48,'Your Power','Billie Eilish','2021-07-02T04:00:00Z',89),(49,'Up','Cardi B','2021-07-02T04:00:00Z',87);
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

-- Dump completed on 2021-07-05  5:51:00
