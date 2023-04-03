-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: 4171852_timesaver
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Dumping data for table `atividade_diaria`
--

LOCK TABLES `atividade_diaria` WRITE;
/*!40000 ALTER TABLE `atividade_diaria` DISABLE KEYS */;
INSERT INTO `atividade_diaria` VALUES (1,1,7,'2023-03-22 06:23:19','2023-03-22 06:24:57'),(2,1,4,'2023-03-22 06:23:20','2023-03-22 06:25:05'),(3,1,6,'2023-03-22 06:23:20','2023-03-23 17:02:22'),(4,1,1,'2023-03-22 06:23:20','2023-03-22 06:23:20'),(5,1,1,'2023-03-22 06:23:20','2023-03-22 06:23:20'),(6,1,1,'2023-03-23 17:15:22','2023-03-23 17:15:22');
/*!40000 ALTER TABLE `atividade_diaria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `clinicas`
--

LOCK TABLES `clinicas` WRITE;
/*!40000 ALTER TABLE `clinicas` DISABLE KEYS */;
/*!40000 ALTER TABLE `clinicas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `conselhos`
--

LOCK TABLES `conselhos` WRITE;
/*!40000 ALTER TABLE `conselhos` DISABLE KEYS */;
INSERT INTO `conselhos` VALUES (1,'CBOO','2023-03-20 18:46:24','2023-03-20 18:46:24'),(2,'COREM','2023-03-20 18:46:24','2023-03-20 18:46:24'),(3,'CRAS','2023-03-20 18:46:24','2023-03-20 18:46:24'),(4,'CRBM','2023-03-20 18:46:24','2023-03-20 18:46:24'),(5,'CREF','2023-03-20 18:46:24','2023-03-20 18:46:24'),(6,'CREFITO','2023-03-20 18:46:24','2023-03-20 18:46:24'),(7,'CRF','2023-03-20 18:46:24','2023-03-20 18:46:24'),(8,'CRFA','2023-03-20 18:46:24','2023-03-20 18:46:24'),(9,'CRM','2023-03-20 18:46:24','2023-03-20 18:46:24'),(10,'CRN','2023-03-20 18:46:24','2023-03-20 18:46:24'),(11,'CRO','2023-03-20 18:46:24','2023-03-20 18:46:24'),(12,'CRP','2023-03-20 18:46:24','2023-03-20 18:46:24'),(13,'CRTR','2023-03-20 18:46:24','2023-03-20 18:46:24'),(14,'ABQ','2023-03-20 18:46:24','2023-03-20 18:46:24'),(15,'RMS','2023-03-20 18:46:24','2023-03-20 18:46:24');
/*!40000 ALTER TABLE `conselhos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `empresas`
--

LOCK TABLES `empresas` WRITE;
/*!40000 ALTER TABLE `empresas` DISABLE KEYS */;
INSERT INTO `empresas` VALUES (1,1,'Unimed','test','leonardo','2023-03-21 22:35:18','2023-03-23 00:38:23'),(6,1,'Stenci','test','leonardo','2023-03-23 09:37:30','2023-03-23 17:47:44');
/*!40000 ALTER TABLE `empresas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `funcionarios`
--

LOCK TABLES `funcionarios` WRITE;
/*!40000 ALTER TABLE `funcionarios` DISABLE KEYS */;
/*!40000 ALTER TABLE `funcionarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `profissionais`
--

LOCK TABLES `profissionais` WRITE;
/*!40000 ALTER TABLE `profissionais` DISABLE KEYS */;
INSERT INTO `profissionais` VALUES (1,1,'1','1',1,'1',1,'1','1','2023-03-21 23:31:18','2023-03-21 23:31:18');
/*!40000 ALTER TABLE `profissionais` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `sessions`
--

LOCK TABLES `sessions` WRITE;
/*!40000 ALTER TABLE `sessions` DISABLE KEYS */;
INSERT INTO `sessions` VALUES (1,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 06:11:09','2023-03-20 06:11:09'),(2,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 06:11:34','2023-03-20 06:11:34'),(3,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 06:12:50','2023-03-20 06:12:50'),(4,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 06:13:11','2023-03-20 06:13:11'),(5,1,'trmg8s2obaf7r4v71gcaunf1ac','127.0.0.1','2023-03-20 06:13:17','2023-03-20 06:13:17'),(6,1,'trmg8s2obaf7r4v71gcaunf1ac','127.0.0.1','2023-03-20 06:13:21','2023-03-20 06:13:21'),(7,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 06:13:35','2023-03-20 06:13:35'),(8,1,'trmg8s2obaf7r4v71gcaunf1ac','127.0.0.1','2023-03-20 06:13:36','2023-03-20 06:13:36'),(9,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 06:15:29','2023-03-20 06:15:29'),(10,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 06:15:32','2023-03-20 06:15:32'),(11,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 06:15:34','2023-03-20 06:15:34'),(12,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 06:16:15','2023-03-20 06:16:15'),(13,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 06:16:16','2023-03-20 06:16:16'),(14,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 06:16:16','2023-03-20 06:16:16'),(15,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 06:16:29','2023-03-20 06:16:29'),(16,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 06:16:30','2023-03-20 06:16:30'),(17,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 06:16:39','2023-03-20 06:16:39'),(18,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 06:16:43','2023-03-20 06:16:43'),(19,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 06:16:52','2023-03-20 06:16:52'),(20,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 06:19:28','2023-03-20 06:19:28'),(21,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 06:19:28','2023-03-20 06:19:28'),(22,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:16:40','2023-03-20 16:16:40'),(23,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:28:30','2023-03-20 16:28:30'),(24,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:28:30','2023-03-20 16:28:30'),(25,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:28:30','2023-03-20 16:28:30'),(26,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:28:35','2023-03-20 16:28:35'),(27,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:28:35','2023-03-20 16:28:35'),(28,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:28:35','2023-03-20 16:28:35'),(29,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:28:36','2023-03-20 16:28:36'),(30,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:28:36','2023-03-20 16:28:36'),(31,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:31:41','2023-03-20 16:31:41'),(32,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:31:42','2023-03-20 16:31:42'),(33,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:31:42','2023-03-20 16:31:42'),(34,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:31:42','2023-03-20 16:31:42'),(35,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:31:48','2023-03-20 16:31:48'),(36,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:35:29','2023-03-20 16:35:29'),(37,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:39:02','2023-03-20 16:39:02'),(38,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:39:03','2023-03-20 16:39:03'),(39,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:39:13','2023-03-20 16:39:13'),(40,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:39:34','2023-03-20 16:39:34'),(41,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:41:32','2023-03-20 16:41:32'),(42,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:41:34','2023-03-20 16:41:34'),(43,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:41:36','2023-03-20 16:41:36'),(44,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:41:37','2023-03-20 16:41:37'),(45,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:41:40','2023-03-20 16:41:40'),(46,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:41:44','2023-03-20 16:41:44'),(47,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:41:45','2023-03-20 16:41:45'),(48,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:43:15','2023-03-20 16:43:15'),(49,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:43:24','2023-03-20 16:43:24'),(50,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:43:28','2023-03-20 16:43:28'),(51,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:43:36','2023-03-20 16:43:36'),(52,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:43:37','2023-03-20 16:43:37'),(53,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:43:39','2023-03-20 16:43:39'),(54,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:43:42','2023-03-20 16:43:42'),(55,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:44:02','2023-03-20 16:44:02'),(56,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:44:03','2023-03-20 16:44:03'),(57,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:47:02','2023-03-20 16:47:02'),(58,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:47:02','2023-03-20 16:47:02'),(59,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:47:33','2023-03-20 16:47:33'),(60,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:47:36','2023-03-20 16:47:36'),(61,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:47:39','2023-03-20 16:47:39'),(62,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:47:42','2023-03-20 16:47:42'),(63,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:47:56','2023-03-20 16:47:56'),(64,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:47:58','2023-03-20 16:47:58'),(65,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:48:02','2023-03-20 16:48:02'),(66,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:50:20','2023-03-20 16:50:20'),(67,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:50:21','2023-03-20 16:50:21'),(68,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:50:47','2023-03-20 16:50:47'),(69,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:50:48','2023-03-20 16:50:48'),(70,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:50:53','2023-03-20 16:50:53'),(71,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:50:53','2023-03-20 16:50:53'),(72,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:50:55','2023-03-20 16:50:55'),(73,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:50:59','2023-03-20 16:50:59'),(74,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:51:00','2023-03-20 16:51:00'),(75,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:51:03','2023-03-20 16:51:03'),(76,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:51:06','2023-03-20 16:51:06'),(77,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:51:07','2023-03-20 16:51:07'),(78,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:51:08','2023-03-20 16:51:08'),(79,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:51:19','2023-03-20 16:51:19'),(80,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:51:21','2023-03-20 16:51:21'),(81,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:51:24','2023-03-20 16:51:24'),(82,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:51:29','2023-03-20 16:51:29'),(83,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:51:30','2023-03-20 16:51:30'),(84,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:51:35','2023-03-20 16:51:35'),(85,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:51:36','2023-03-20 16:51:36'),(86,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:52:06','2023-03-20 16:52:06'),(87,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:52:11','2023-03-20 16:52:11'),(88,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:52:12','2023-03-20 16:52:12'),(89,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:52:19','2023-03-20 16:52:19'),(90,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 16:52:51','2023-03-20 16:52:51'),(91,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 17:41:57','2023-03-20 17:41:57'),(92,1,'hsgicruj6fsom9norfvolh62fa','127.0.0.1','2023-03-20 17:47:52','2023-03-20 17:47:52'),(93,1,'puseprq0dija8hbjhml932i8eh','127.0.0.1','2023-03-20 17:48:35','2023-03-20 17:48:35'),(94,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 17:53:15','2023-03-20 17:53:15'),(95,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 17:53:30','2023-03-20 17:53:30'),(96,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 17:54:35','2023-03-20 17:54:35'),(97,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 17:55:12','2023-03-20 17:55:12'),(98,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 17:56:34','2023-03-20 17:56:34'),(99,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 17:57:03','2023-03-20 17:57:03'),(100,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 17:57:22','2023-03-20 17:57:22'),(101,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 17:57:59','2023-03-20 17:57:59'),(102,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 17:58:16','2023-03-20 17:58:16'),(103,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 17:59:14','2023-03-20 17:59:14'),(104,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 18:57:44','2023-03-20 18:57:44'),(105,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-20 18:59:20','2023-03-20 18:59:20'),(106,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-23 00:36:44','2023-03-23 00:36:44'),(107,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-23 16:38:30','2023-03-23 16:38:30'),(108,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-23 16:40:22','2023-03-23 16:40:22'),(109,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-23 16:42:08','2023-03-23 16:42:08'),(110,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-23 16:44:08','2023-03-23 16:44:08'),(111,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-23 16:45:13','2023-03-23 16:45:13'),(112,1,'efqigknsc2p8a3d7bqgckn27pm','127.0.0.1','2023-03-23 17:48:42','2023-03-23 17:48:42');
/*!40000 ALTER TABLE `sessions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `userlevel`
--

LOCK TABLES `userlevel` WRITE;
/*!40000 ALTER TABLE `userlevel` DISABLE KEYS */;
INSERT INTO `userlevel` VALUES (1,'admin','2023-03-20 06:05:28');
/*!40000 ALTER TABLE `userlevel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'17434838728','17434838728','teste@localhost',1,NULL,'$2y$10$7loYLdW44v0LBqngO8BreexhpIxNqHPlouvL92NIifWE1hYETUBbO','2023-03-20 06:05:28','2023-03-20 06:05:28');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-23 16:21:55
