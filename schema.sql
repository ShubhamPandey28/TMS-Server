-- Schema of the database architechture

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