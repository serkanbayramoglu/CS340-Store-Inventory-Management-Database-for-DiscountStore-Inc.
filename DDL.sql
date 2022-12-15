-- Project Group 78
-- Database Duo 
--   Emma Babcock
--   Serkan Bayramoglu
-- ------------------------------------------------------

-- MariaDB dump 10.19  Distrib 10.4.24-MariaDB, for Linux (x86_64)
--
-- Host: classmysql.engr.oregonstate.edu    Database: cs340_bayramos
-- ------------------------------------------------------
-- Server version	10.6.7-MariaDB-log

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
-- Table structure for table `Brands`
--

DROP TABLE IF EXISTS `Brands`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Brands` (
  `brand_id` int(11) NOT NULL AUTO_INCREMENT,
  `brand_name` varchar(45) NOT NULL,
  `company_name` varchar(45) NOT NULL,
  `company_contact_details` varchar(200) NOT NULL,
  `service_contact_details` varchar(200) NOT NULL,
  `company_website` varchar(100) NOT NULL,
  PRIMARY KEY (`brand_id`),
  UNIQUE KEY `brand_name_UNIQUE` (`brand_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Brands`
--

LOCK TABLES `Brands` WRITE;
/*!40000 ALTER TABLE `Brands` DISABLE KEYS */;
INSERT INTO `Brands` VALUES 
(1,'Sony','Sony Group Corporation','Tel: +1(123)3214567 Address: #1','Tel: +1(222)4412546 Address: #6','https://www.sony.com/en/'),
(2,'Samsung','Samsung Group','Tel: +1(114)3671456 Address: #2','Tel: +1(124)1298342 Address: #7','https://www.samsung.com/us/'),
(3,'Beko','Arçelik A.Ş.','Tel: +1(324)4784569 Address: #3','Tel: +1(324)4184829 Address: #8','https://www.beko.com/us-en'),
(4,'Vizio','Vizio Inc.','Tel: +1(212)3091270 Address: #4','Tel: +1(212)3091382 Address: #9','https://www.vizio.com/en/home'),
(5,"Lowe's","Lowe's Companies, Inc. ",'Tel: +1(212)3103941 Address: #5','Tel: +1(212)3234215 Address: #10','https://www.lowes.com/');
/*!40000 ALTER TABLE `Brands` ENABLE KEYS */;
UNLOCK TABLES;
--
-- Table structure for table `Customers`
--

DROP TABLE IF EXISTS `Customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Customers` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `surname` varchar(45) DEFAULT NULL,
  `phone_number` varchar(15) NOT NULL,
  `signup_date` date NOT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customers`
--

LOCK TABLES `Customers` WRITE;
/*!40000 ALTER TABLE `Customers` DISABLE KEYS */;
INSERT INTO `Customers` VALUES 
(1,'Rachel ','Smith','(340) 344-0958',"2022/03/15"),
(2,'John',"O'Connor",'(745) 345-0927',"2022/02/24"),
(3,'John',NULL,'(724) 309-5982',"2022/01/19"),
(4,'Mike','Browlyn','(740) 356-0327',"2020/11/13"),
(5,'Sarah','Johnson','(720) 322-7316',"2021/09/07");
/*!40000 ALTER TABLE `Customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Items`
--

DROP TABLE IF EXISTS `Items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Items` (
  `item_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_group` varchar(100) NOT NULL,
  `brand` int(11) NOT NULL,
  `guarantee_terms` varchar(400) NOT NULL,
  `producer_model_number` varchar(45) UNIQUE NOT NULL,
  `product_dimensions` varchar(45) DEFAULT NULL,
  `package_dimensions` varchar(45) DEFAULT NULL,
  `product_description` varchar(200) DEFAULT NULL,
  `current_price_pu` decimal(7,2) NOT NULL,
  `available_quantity_warehouse` int(11) NOT NULL DEFAULT 0,
  `section_warehouse` varchar(45) DEFAULT NULL,
  `available_quantity_store` int(11) NOT NULL DEFAULT 0,
  `section_store` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`item_id`),
  KEY `fk_Product Items_Brands1_idx` (`brand`),
  CONSTRAINT `fk_Product Items_Brands1` FOREIGN KEY (`brand`) REFERENCES `Brands` (`brand_id`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Items`
--

LOCK TABLES `Items` WRITE;
/*!40000 ALTER TABLE `Items` DISABLE KEYS */;
INSERT INTO `Items` VALUES 
(1,'Televisions',1,'2 years excluding accidental demages','XR-55A90J','50.47" x 27.91" x 12.48''','56.93" x 33.19" x 17.09''','55" Smart Google TV','2199.99',4,'Electronics - 3C',2,'Electronics - 1A'),
(2,'Cell Phones',2,'1 year excluding screen cracks','SM-S908X','6.43" x 3.07" x 0.35"','7.00" x 3.45" x 1.05"','Samsung Galaxy S22 Ultra','1199.99',6,'Electronics - 1C',5,'Electronics - 3C'),
(3,'Lawnmowers',5,'3 years mechanical, 1 year electrical','HRN216VKA','61.00" x 40.80" x 22.60"','66.50" x 45.19" x 24.90"','Honda 21" Self-Propelled Lawn Mower','549',4,'Outdoor Tools & Equipment - 4A',3,'Outdoor Tools & Equipment  - 4B'),
(4,'Washers',3,'3 years mechanical, excluding control unit','WMY10148C2','33.06" x 23.63" x 26.38"','37.08" x 26.98" x 31.00"','24" Front Load Washer','1189',10,'Household Appliances - 6B',4,'Household Appliances - 5D'),
(5,'Cell Phones',1,'1 year all inclusive','XQBC62/B','6.43" x 3.07" x 0.35"','7.00" x 3.45" x 1.05"','Sony XPERIA 1 III Dual-SIM 256GB 5G Smartphone','1099',1,'Electronics - 1A',2,'Electronics - 1B'),
(6,'Televisions',2,'3 years excl. water related damages','QN65Q900RBFXZA','55.42" x 31.96" x 15.88"','62.90" x 37.33" x 21.19"','65" Samsung 8K QLED TV','4499.99',3,'Electronics - 3D',5,'Electronics - 3A');
/*!40000 ALTER TABLE `Items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `OrderDetails`
--

DROP TABLE IF EXISTS `OrderDetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `OrderDetails` (
  `order_details_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` int(11) DEFAULT NULL,
  `item_id` int(11) DEFAULT NULL,
  `order_quantity` smallint(3) NOT NULL,
  `order_price_pu` decimal(7,2) NOT NULL,
  PRIMARY KEY (`order_details_id`),
  KEY `fk_OrderDetails_Items1_idx` (`item_id`),
  KEY `fk_OrderDetails_Orders1_idx` (`order_id`),
  CONSTRAINT `fk_OrderDetails_Items1` FOREIGN KEY (`item_id`) REFERENCES `Items` (`item_id`) ON DELETE SET NULL ON UPDATE NO ACTION,
  CONSTRAINT `fk_OrderDetails_Orders1` FOREIGN KEY (`order_id`) REFERENCES `Orders` (`order_id`) ON DELETE SET NULL ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `OrderDetails`
--

LOCK TABLES `OrderDetails` WRITE;
/*!40000 ALTER TABLE `OrderDetails` DISABLE KEYS */;
INSERT INTO `OrderDetails` VALUES 
(1,1,1,2,1341.99),
(2,1,5,1,824.25),
(3,2,1,5,1583.99),
(4,2,2,4,899.99),
(5,2,3,4,389.79),
(6,3,1,4,1561.99),
(7,3,2,2,911.99),
(8,3,3,5,428.22),
(9,3,5,6,692.37),
(10,4,2,4,719.99),
(11,4,4,15,903.64),
(12,5,2,6,911.99),
(13,5,6,10,2699.99),
(14,6,1,5,1451.99),
(15,6,3,6,433.71),
(16,7,1,7,1517.99),
(17,7,3,4,384.3),
(18,7,6,7,3419.99),
(19,8,1,7,1649.99),
(20,8,5,2,857.22);
/*!40000 ALTER TABLE `OrderDetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Orders`
--

DROP TABLE IF EXISTS `Orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Orders` (
  `order_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_invoice_number` varchar(45) NOT NULL,
  `order_date` date NOT NULL,
  `expected_arrival_date` date DEFAULT NULL,
  `arrival_date` date DEFAULT NULL,
  `total_price` decimal(10,2) NOT NULL,
  `has_arrived` varchar(3) NOT NULL DEFAULT 'No',
  `supplier_id` int(11),
  PRIMARY KEY (`order_id`),
  UNIQUE KEY `order_invoice_number_UNIQUE` (`order_invoice_number`),
  KEY `fk_Orders_Suppliers1_idx` (`supplier_id`),
  CONSTRAINT `fk_Orders_Suppliers1` FOREIGN KEY (`supplier_id`) REFERENCES `Suppliers` (`supplier_id`) ON DELETE SET NULL ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Orders`
--

LOCK TABLES `Orders` WRITE;
/*!40000 ALTER TABLE `Orders` DISABLE KEYS */;
INSERT INTO `Orders` VALUES 
(1,'132',"2022/01/19","2022/02/01","2022/02/02",3508.23,'Yes',1),
(2,'134',"2022/01/19","2022/01/22","2022/01/22",13079.094,'Yes',3),
(3,'234',"2022/02/22","2022/02/26","2022/02/25",14367.2764,'Yes',2),
(4,'275',"2022/02/24","2022/02/28",NULL,16434.576,'Yes',4),
(5,'309',"2022/02/26","2022/03/03",NULL,32471.8944,'Yes',4),
(6,'311',"2022/03/03","2022/03/06",NULL,9862.227,'No',3),
(7,'313',"2022/03/15","2022/03/20",NULL,36103.0985,'No',5),
(8,'315',"2022/04/14","2022/04/17",NULL,13264.3875,'No',1);
/*!40000 ALTER TABLE `Orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Sales`
--

DROP TABLE IF EXISTS `Sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Sales` (
  `sale_id` int(11) NOT NULL AUTO_INCREMENT,
  `invoice_number` varchar(45) NOT NULL,
  `invoice_date` date NOT NULL,
  `sales_price_pu` decimal(7,2) NOT NULL,
  `sales_quantity` tinyint(2) NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `item_id` int(11) DEFAULT NULL,
  `sales_manager` varchar(45) NOT NULL,
  PRIMARY KEY (`sale_id`),
  KEY `fk_Sales_Customers1_idx` (`customer_id`),
  KEY `fk_Sales_Products1_idx` (`item_id`),
  CONSTRAINT `fk_Sales_Customers1` FOREIGN KEY (`customer_id`) REFERENCES `Customers` (`customer_id`) ON DELETE SET NULL ON UPDATE NO ACTION,
  CONSTRAINT `fk_Sales_Products1` FOREIGN KEY (`item_id`) REFERENCES `Items` (`item_id`) ON DELETE SET NULL ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Sales`
--

LOCK TABLES `Sales` WRITE;
/*!40000 ALTER TABLE `Sales` DISABLE KEYS */;
INSERT INTO `Sales` VALUES 
(1,'453',"2022/04/13",2199.99,2,3,1,'Kevin Robinson'),
(2,'234',"2022/04/26",4499.99,1,3,6,'James Mason'),
(3,'567',"2022/04/27",1199.99,5,1,2,'James Mason'),
(4,'643',"2022/04/28",1099.00,3,NULL,5,'Sara Kirk'),
(5,'643',"2022/04/28",2199.99,2,NULL,1,'Sara Kirk'),
(6,'714',"2022/04/30",4499.99,1,4,6,'Kevin Robinson'),
(7,'714',"2022/04/30",1099.00,1,4,5,'Kevin Robinson'),
(8,'714',"2022/04/30",1189.00,1,4,4,'Kevin Robinson'),
(9,'903',"2022/05/10",549.00,2,NULL,3,'Sara Kirk'),
(10,'952',"2022/05/21",2199.99,1,2,1,'Sara Kirk');
/*!40000 ALTER TABLE `Sales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Suppliers`
--

DROP TABLE IF EXISTS `Suppliers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Suppliers` (
  `supplier_id` int(11) NOT NULL AUTO_INCREMENT,
  `supplier_name` varchar(45) NOT NULL,
  `contact_details` varchar(200) NOT NULL,
  `contact_person` varchar(100) NOT NULL,
  `account_manager` varchar(45) NOT NULL,
  PRIMARY KEY (`supplier_id`),
  UNIQUE KEY `supplier_name_UNIQUE` (`supplier_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Suppliers`
--

LOCK TABLES `Suppliers` WRITE;
/*!40000 ALTER TABLE `Suppliers` DISABLE KEYS */;
INSERT INTO `Suppliers` VALUES 
(1,'Sony Electronics Operations Co, Ltd','Tel: +1(121)1535567 Address: #11','Yi Huang','Pan Yunajun'),
(2,'Advantest Corp.','Tel: +1(131)5256444 Address: #12','Lien Huang','Teng Yuan'),
(3,'Dongguan Taimei Electric Co., Ltd.','Tel: +1(216)2145872 Address: #13','Gu Pong','Mao Sieh'),
(4,'Amtran Technology Co., Ltd.','Tel: +1(212)2175981 Address: #14','Zhao Min','Su Tay'),
(5,'Stanley Black & Decker Corporation','Tel: +1(214)3145239 Address: #15','Tracey Lang','Matthew Sutherland');
/*!40000 ALTER TABLE `Suppliers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Suppliers_has_Items`
--

DROP TABLE IF EXISTS `SuppliersForItems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SuppliersForItems` (
  `suppliers_for_items_id` int(11) NOT NULL AUTO_INCREMENT,
  `supplier_id` int(11) NOT NULL,
  `item_id` int(11) NOT NULL,
  PRIMARY KEY (`suppliers_for_items_id`),
  KEY `fk_SuppliersForItems_Items1_idx` (`item_id`),
  KEY `fk_SuppliersForItems_Suppliers1_idx` (`supplier_id`),
  CONSTRAINT `supplier_item1` UNIQUE(`supplier_id`, `item_id`),
  CONSTRAINT `fk_SuppliersForItems_Items1` FOREIGN KEY (`item_id`) REFERENCES `Items` (`item_id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `fk_SuppliersForItems_Suppliers1` FOREIGN KEY (`supplier_id`) REFERENCES `Suppliers` (`supplier_id`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Suppliers_has_Items`
--

LOCK TABLES `SuppliersForItems` WRITE;
/*!40000 ALTER TABLE `SuppliersForItems` DISABLE KEYS */;
INSERT INTO `SuppliersForItems` VALUES 
(1,1,1),
(2,1,5),
(3,2,1),
(4,2,2),
(5,2,3),
(6,2,4),
(7,2,5),
(8,3,1),
(9,3,2),
(10,3,3),
(11,4,2),
(12,4,4),
(13,4,6),
(14,5,1),
(15,5,2),
(16,5,3),
(17,5,6);
/*!40000 ALTER TABLE `SuppliersForItems` ENABLE KEYS */;
UNLOCK TABLES;

/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-28 13:40:36
