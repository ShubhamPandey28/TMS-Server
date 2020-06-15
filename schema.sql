
-- CREATING DATABASE SYSTEM. RIGHT NOW IT IS A DUMMY ONE

DROP DATABASE IF EXISTS SG_TMS;
CREATE DATABASE SG_TMS;

USE SG_TMS;

CREATE TABLE IF NOT EXISTS `cities` (
  `city_id` int(11) NOT NULL auto_increment,
  `city_name` varchar(100) NOT NULL,
  `city_state` varchar(100) NOT NULL,
  PRIMARY KEY  (`city_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1624 ;

--
-- Dumping data for table `cities`
--

INSERT INTO `cities` (`city_id`, `city_name`, `city_state`) VALUES
(1, 'Kolhapur', 'Maharashtra'),
(2, 'Port Blair', 'Andaman & Nicobar Islands'),
(3, 'Adilabad', 'Andhra Pradesh'),
(4, 'Adoni', 'Andhra Pradesh'),
(5, 'Amadalavalasa', 'Andhra Pradesh'),
(6, 'Amalapuram', 'Andhra Pradesh'),
(7, 'Anakapalle', 'Andhra Pradesh'),
(8, 'Anantapur', 'Andhra Pradesh'),
(9, 'Badepalle', 'Andhra Pradesh'),
(10, 'Banganapalle', 'Andhra Pradesh');

DROP DATABASE IF EXISTS `SG_TMS`;
CREATE DATABASE `SG_TMS`;
USE `SG_TMS`; 

CREATE TABLE `Vehicle` (
  `Vehicle_ID` int NOT NULL AUTO_INCREMENT,
  `Vehicle_Num` varchar(50) NOT NULL,  
  `Model` varchar(50) NOT NULL,
  `Current_Location` varchar(50) NOT NULL,
  `Status` varchar(50) NOT NULL,
  PRIMARY KEY (`Vehicle_ID`)
);

CREATE TABLE `Consignor_Consignee` (
  `ID` int NOT NULL auto_increment,
  `Name` varchar(50) NOT NULL,
  `Contact` varchar(50) NOT NULL,
  `Address` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`)
);


CREATE TABLE `Consignment` (
  `Consignment_ID` varchar(50) NOT NULL,
  `Consignor_ID` int NOT NULL,
  `Consignee_ID` int NOT NULL,
  `Vehicle_ID` int NOT NULL,
  `Loading_Date` date NOT NULL,
  `To` varchar(50) NOT NULL,
  `From` varchar(50) NOT NULL,
  `Weight` float NOT NULL,
  `Rate` float default NULL,
  `Misc_Charges` float default NULL,
  `Amount` float default NULL,
  `Chargeable_Qty` int default NULL,
  `Invoice_No.` int NOT NULL,
  `Invoice_Date` date NOT NULL,
  
  FOREIGN KEY (`Consignor_ID`) references `Consignor_Consignee`(`ID`),
  FOREIGN KEY (`Consignee_ID`) REFERENCES `Consignor_Consignee`(`ID`),
  FOREIGN KEY (`Vehicle_ID`) REFERENCES `Vehicle`(`Vehicle_ID`),
  PRIMARY KEY (`Consignment_ID`)
);

CREATE TABLE `Repair_Log` (
  `Repair_ID` int NOT NULL auto_increment,
  `Vehicle_ID` int NOT NULL,
  `Repair_Date` date NOT NULL,
  `Amount` varchar(50) NOT NULL,
  `From` varchar(50) NOT NULL,
  FOREIGN KEY (`Vehicle_ID`) REFERENCES `Vehicle`(`Vehicle_ID`),
  PRIMARY KEY (`Repair_ID`)
);