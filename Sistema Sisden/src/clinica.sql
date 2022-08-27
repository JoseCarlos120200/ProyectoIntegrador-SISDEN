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
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events`
--

LOCK TABLES `events` WRITE;
/*!40000 ALTER TABLE `events` DISABLE KEYS */;
INSERT INTO `events` VALUES (1,'Cancelado','2022-08-24 09:00:00','2022-08-24 10:00:00','Briseida','Muñoz','Dolor de muela','777','Cdmx','1',0,''),(2,'','2022-08-24 10:00:00','2022-08-24 11:00:00','Briseida Elizabeth Elizabeth','Jimenez','OGARCIA','7775316104','Cdmx','1',0,''),(3,'','2022-08-24 11:00:00','2022-08-24 12:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','7775316104','Cdmx','1',0,''),(4,'','2022-08-24 11:00:00','2022-08-24 12:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','7775316104','Cdmx','2',0,''),(5,'','2022-08-25 11:00:00','2022-08-25 12:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','7775316104','Cdmx','1',0,''),(6,'Pagado','2022-08-25 11:00:00','2022-08-25 12:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','7775316104','Cdmx','2',500,'6'),(7,'','2022-08-25 12:00:00','2022-08-25 13:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','7775316104','Cdmx','1',0,''),(8,'','2022-08-25 12:00:00','2022-08-25 13:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','7775316104','Cdmx','2',0,''),(9,'','2022-08-24 13:00:00','2022-08-24 14:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','7775316104','Cdmx','1',0,''),(10,'','2022-08-24 12:00:00','2022-08-24 13:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','7775316104','Morelos','1',0,''),(11,'','2022-08-24 08:00:00','2022-08-24 09:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','7775316104','Puebla','1',0,''),(12,'','2022-08-24 08:00:00','2022-08-24 09:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','7775316104','Puebla','2',0,''),(13,'','2022-08-24 10:00:00','2022-08-24 11:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','7775316104','Puebla','1',0,''),(14,'Cancelado','2022-08-25 16:00:00','2022-08-25 17:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','777','Puebla','1',0,''),(15,'','2022-08-25 15:00:00','2022-08-25 16:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','7775316104','Cdmx','1',0,''),(16,'','2022-08-25 15:00:00','2022-08-25 16:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','7775316104','Morelos','1',0,''),(17,'','2022-08-25 15:00:00','2022-08-25 16:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','7775316104','Morelos','2',0,''),(18,'Pagado','2022-08-25 15:00:00','2022-08-25 16:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','7775316104','Cdmx','2',500,'18'),(19,'','2022-08-25 18:00:00','2022-08-25 19:00:00','Briseida Elizabeth Elizabeth','Jimenez','muelas de juicio','7775316104','Puebla','1',0,'');
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicio`
--

LOCK TABLES `servicio` WRITE;
/*!40000 ALTER TABLE `servicio` DISABLE KEYS */;
INSERT INTO `servicio` VALUES (1,'muelas de juicio',500,'extraer muelas del juicio');
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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'OGARCIA','pbkdf2:sha256:260000$fiRyeVmApEki8uvm$40d93cdea3f941010f3eedfafd228db15c41810ce625a691ff8cb2491300b010','Oscar Garcia','Activo','Admin','Cdmx','1','Matutino'),(2,'Elizabeth Muñoz','sha256$WH4rh5cj$de7e15404ca23a8427c6979af28c2937e33eca85eaabd91cda0bdfc1ce3b46bd','Elizabeth Muñoz','Activo','Admin','','',''),(3,'r','sha256$euufq0dK$9268907a860f96db7fb2c7faa935ed34ec8ae7c43733262d343347e946a6cf7d','Juan Peralta','Inactivo','Medico','','',''),(4,'bris','sha256$mG5M2YDW$8e27adefbc2c54672131db09ea72ecec7225bf6e75985b8887664f04600f3235','Briseida Jimenez','Inactivo','Admin','','',''),(5,'bris','sha256$D60kX0iK$f683598a678a69301809c3bddc1261801ddd48ae4d59be5f43c9087dd85dd234','Verónica García','Inactivo','Medico','','',''),(6,'Asistente','sha256$EYbYWJaA$f904b05478bd2c15413ca9ad8549b070b9110a4e59149bd21dbc3f0650bc7338','Felipe Campo','Activo','Asistente','','',''),(7,'Alexis','sha256$kBbazzWn$7d663ee055dd7161f00f5c5274b782c01e7343717c9a4afdbd81355ea0d354c3','vquez','','Admin','','',''),(8,'hector','sha256$2YlolCkv$97d48b683b40460af68b50ec7dd6dbca94a85304632bbfc3be438cff7c8df3c5','Hector','','Admin','','',''),(9,'Mauricio@drmuelitas.com','sha256$BE73jAxe$a6d1e3f8b3ce02cdcc77398c5d3eb7435b027de72124ae6ea1d2d5a0edd098de','Mauricio Aleman','','Medico','','',''),(10,'carlos','sha256$lb8ucQXv$d502f24bfea96cf40e95470484302352e7d0ef2071111f9d973d8d4b3e45b113','Carlos Garcia','Activo','Medico','Puebla','',''),(11,'toño','sha256$WGFPwCBc$5afb3450f4c839cb4fe633f027fbe30274ce4d0964c463c3809317eb036ccc41','antonio','Activo','Admin','Cdmx','',''),(12,'d','sha256$oNsEO9BK$a980ceb17dce1e33bc07738a12a0e23076ff61ed3cde06a6bce4362b8ad37555','d','Activo','Admin','Cdmx','',''),(13,'d','sha256$9odHQD0g$6cd0641f4682b4bf75aac7658634fb7975bad396c17cd37c4acf9e3b0c38bd62','d','Activo','Admin','Cdmx','',''),(14,'ximena','sha256$5fBfdiRd$b6c841a3d6b638ee7e46379c977cccd49bfeead45cb3bb05d1bd2be4b6570b34','ximena romero','Activo','Asistente','Morelos','',''),(15,'Ignacios','sha256$TFeyvYPy$fb9da6d5435fc805713df51baad922cddca2ad20682624a7aa07014decaeacac','Ignacio Sanchez','Activo','Medico','Puebla','',''),(16,'Ignacios','sha256$djKDHW13$64ebc0c8994debc42a7e69e942d2ccb298827d0aaae09ae5907655bf30b16fa2','Ignacio Sanchez','','Medico','','',''),(17,'persona','sha256$1rzeFGQz$4dad4ef32f53bdf1521c52bf3b3237c87df8028da277b68912abe273856cacbf','nombre','Activo','Admin','Cdmx','',''),(18,'b','sha256$vCvmRBcg$1f571251077ea312cb55f90647b4b64497ea611a52c4fe97126b964667c029fe','b','Activo','Medico','Cdmx','2','Matutino'),(19,'c','sha256$hwxxg2uV$ea841625f2d3fc3597da54e61668b58ee4aa6b071c80d0c67734f87c56693990','c','Activo','Medico','Cdmx','2','Vespertino'),(20,'e','sha256$xadneV20$7df6af648fbb1085b3842abea911015bb8025102a647fd1107954e2eadd79b43','d','Activo','Medico','Cdmx','1','Vespertino');
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

-- Dump completed on 2022-08-25  4:04:03
