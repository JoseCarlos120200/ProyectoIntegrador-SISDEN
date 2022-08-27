-- MariaDB dump 10.19  Distrib 10.4.24-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: clinica
-- ------------------------------------------------------
-- Server version	10.4.24-MariaDB

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
-- Table structure for table `clinica`
--

DROP TABLE IF EXISTS `clinica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `clinica` (
  `id` int(4) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  `dirección` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clinica`
--

LOCK TABLES `clinica` WRITE;
/*!40000 ALTER TABLE `clinica` DISABLE KEYS */;
INSERT INTO `clinica` VALUES (1,'Cdmx','Av.Revolución'),(2,'Morelos','Av.Independencia'),(3,'Puebla','Av.Guerrero');
/*!40000 ALTER TABLE `clinica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `events`
--

DROP TABLE IF EXISTS `events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `events` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `start_event` datetime NOT NULL,
  `end_event` datetime NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `apellido` varchar(200) NOT NULL,
  `servicio` varchar(200) NOT NULL,
  `telefono` varchar(200) NOT NULL,
  `clinica` varchar(250) NOT NULL,
  `consultorio` varchar(1) NOT NULL,
  `precio` int(9) NOT NULL,
  `Medico` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events`
--

LOCK TABLES `events` WRITE;
/*!40000 ALTER TABLE `events` DISABLE KEYS */;
INSERT INTO `events` VALUES (1,'Cancelado','2022-08-24 09:00:00','2022-08-24 10:00:00','Briseida','Muñoz','Dolor de muela','777','Cdmx','1',0,''),(2,'','2022-08-24 10:00:00','2022-08-24 11:00:00','Briseida Elizabeth Elizabeth','Jimenez','OGARCIA','7775316104','Cdmx','1',0,''),(3,'','2022-08-24 11:00:00','2022-08-24 12:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','7775316104','Cdmx','1',0,''),(4,'','2022-08-24 11:00:00','2022-08-24 12:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','7775316104','Cdmx','2',0,''),(5,'','2022-08-25 11:00:00','2022-08-25 12:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','7775316104','Cdmx','1',0,''),(6,'Pagado','2022-08-25 11:00:00','2022-08-25 12:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','7775316104','Cdmx','2',500,'6'),(7,'','2022-08-25 12:00:00','2022-08-25 13:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','7775316104','Cdmx','1',0,''),(8,'','2022-08-25 12:00:00','2022-08-25 13:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','7775316104','Cdmx','2',0,''),(9,'','2022-08-24 13:00:00','2022-08-24 14:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','7775316104','Cdmx','1',0,''),(10,'','2022-08-24 12:00:00','2022-08-24 13:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','7775316104','Morelos','1',0,''),(11,'','2022-08-24 08:00:00','2022-08-24 09:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','7775316104','Puebla','1',0,''),(12,'','2022-08-24 08:00:00','2022-08-24 09:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','7775316104','Puebla','2',0,''),(13,'','2022-08-24 10:00:00','2022-08-24 11:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','7775316104','Puebla','1',0,''),(14,'Cancelado','2022-08-25 16:00:00','2022-08-25 17:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','777','Puebla','1',0,''),(15,'','2022-08-25 15:00:00','2022-08-25 16:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','7775316104','Cdmx','1',0,''),(16,'Pagado','2022-08-25 15:00:00','2022-08-25 16:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','7775316104','Morelos','1',700,'efren'),(17,'','2022-08-25 15:00:00','2022-08-25 16:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','7775316104','Morelos','2',0,''),(18,'Pagado','2022-08-25 15:00:00','2022-08-25 16:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','7775316104','Cdmx','2',500,'18'),(19,'','2022-08-25 18:00:00','2022-08-25 19:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','7775316104','Puebla','1',0,''),(20,'Cancelado','2022-08-25 10:00:00','2022-08-25 11:00:00','Alexis','Velazquez','muelas de juicio','777','Morelos','1',0,''),(21,'Pagado','2022-08-25 18:00:00','2022-08-25 19:00:00','Ignacio','Sanchez','Blanqueamiento de diente','777','Morelos','1',2000,'Alejandro'),(22,'Cancelado','2022-08-25 16:00:00','2022-08-25 17:00:00','ximena','romero','Atención a caries','777','Morelos','1',0,'');
/*!40000 ALTER TABLE `events` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servicio`
--

DROP TABLE IF EXISTS `servicio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `servicio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `servicio` varchar(200) NOT NULL,
  `precio` double NOT NULL,
  `descripcion` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicio`
--

LOCK TABLES `servicio` WRITE;
/*!40000 ALTER TABLE `servicio` DISABLE KEYS */;
INSERT INTO `servicio` VALUES (1,'muelas de juicio',500,'extraer muelas del juicio'),(2,'Radiografía de dientes',700,'Radiografía de la boca'),(3,'Radiografía de dientes',700,'Radiografía de la boca'),(4,'Blanqueamiento de diente',2000,'Estiliza la sonrisa'),(5,'Atención a caries',400,'Limpieza de caries profesional');
/*!40000 ALTER TABLE `servicio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` smallint(5) NOT NULL AUTO_INCREMENT,
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `fullname` varchar(200) NOT NULL,
  `estado` varchar(30) NOT NULL,
  `rol` varchar(200) NOT NULL,
  `clinica` varchar(200) NOT NULL,
  `consultorio` varchar(5) NOT NULL,
  `turno` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'OGARCIA','pbkdf2:sha256:260000$fiRyeVmApEki8uvm$40d93cdea3f941010f3eedfafd228db15c41810ce625a691ff8cb2491300b010','Oscar Garcia','Activo','Admin','Cdmx','1','Matutino'),(2,'Elizabeth Muñoz','sha256$WH4rh5cj$de7e15404ca23a8427c6979af28c2937e33eca85eaabd91cda0bdfc1ce3b46bd','Elizabeth Muñoz','Activo','Admin','','',''),(18,'bob','sha256$vCvmRBcg$1f571251077ea312cb55f90647b4b64497ea611a52c4fe97126b964667c029fe','bob','Activo','Medico','Cdmx','2','Matutino'),(19,'coral','sha256$hwxxg2uV$ea841625f2d3fc3597da54e61668b58ee4aa6b071c80d0c67734f87c56693990','coral','Activo','Medico','Cdmx','2','Vespertino'),(20,'efren','sha256$xadneV20$7df6af648fbb1085b3842abea911015bb8025102a647fd1107954e2eadd79b43','efren','Activo','Medico','Morelos','1','Vespertino'),(22,'Karla','sha256$8tO966mk$b9e339674f91f43eca8224ef27f3f5662c0b2a6f64198501cee6cf474eb3a53d','Karla','Activo','Admin','Morelos','',''),(25,'Karla','sha256$vvcF6l3u$214ed918026626cc3a62573b8e23ab6fab28ac963e38d191ec52784b20ba108b','Karla','Inactivo','Admin','Cdmx','',''),(26,'Alex','sha256$K8q8yRxZ$91e0f80e6f96b781dfcdb8b4a68bb454d751ae2195704c3442bc741a4b677c54','miguel velazquez','Inactivo','Medico','Cdmx','',''),(27,'ximena','sha256$1HufddeI$44928e3f586f5aa0a02c9f10dcc6e6d290e7bc2a3fa14f660502162e74ac7ed6','Ximena','Activo','Medico','Morelos','',''),(28,'isanchez','sha256$LvSIZMCS$19619caa7a09e8eb6a834353249f6bcf34268ae6d87ca527cab8c1164b06c9a2','isanchez','Activo','Medico','Morelos','',''),(29,'Xime','sha256$6Gaz3x2Q$8f45a7b5bc0fdc1e1bd99f08e087c3c2f7d844a003d4033b48d74857b0536987','Xime','Activo','Admin','Morelos','',''),(30,'juan','sha256$AxmhAEvS$7e503be404778cef3b3f415205c92bb07ae706bc58ac9706d9e91345f30440f4','juan','Activo','Admin','Morelos','',''),(31,'pablo','sha256$tzd6Y9La$a89e611d8a9f03f13481b3ce1364c487de15139a6cc61a46fa56d861dd7d546a','pablo','Activo','Admin','Morelos','',''),(32,'Alejandro','sha256$th7PZD7i$386485e1d8a9d4192e5c8ca26305720907d37ad8d94c76614e1969d5203a4148','Alejandro','Activo','Asistente','Morelos','','');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-08-26 21:35:07
