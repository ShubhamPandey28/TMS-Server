-- Schema of the database architechture

DROP DATABASE IF EXISTS `SG_TMS`;
CREATE DATABASE `SG_TMS`;
USE `SG_TMS`; 

CREATE TABLE `Vehicle` (
  `ID` varchar(10),  
  `Model` varchar(50) NOT NULL,
  `Current_Location` varchar(50),
  `Status` varchar(50) DEFAULT "IDLE",
  PRIMARY KEY (`ID`)
);

CREATE TABLE `Consignor_Consignee` (
  `ID` int NOT NULL auto_increment,
  `Name` varchar(50) NOT NULL,
  `Contact` varchar(50) NOT NULL,
  `Address` varchar(50) NOT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `GST_Number` varchar(15) NOT NULL UNIQUE,
  PRIMARY KEY (`ID`)
);


CREATE TABLE `Consignment` (
  `ID` varchar(50) NOT NULL,
  `Consignor_ID` int NOT NULL,
  `Consignee_ID` int NOT NULL,
  `Vehicle_Num` varchar(10) DEFAULT NULL,
  `Loading_Date` date DEFAULT NULL,
  `To` varchar(50) NOT NULL,
  `From` varchar(50) NOT NULL,
  `Weight` float NOT NULL,
  `Rate` float default NULL,
  `Misc_Charges` float default NULL,
  `Amount` float default NULL,
  `Chargeable_Qty` float default NULL,
  `Invoice_No.` int NOT NULL,
  `Invoice_Date` date NOT NULL,
  `Invoice_Qty` float NOT NULL,
  `Bill_Num` varchar(20) DEFAULT NULL,
  
  FOREIGN KEY (`Consignor_ID`) references `Consignor_Consignee`(`ID`),
  FOREIGN KEY (`Consignee_ID`) REFERENCES `Consignor_Consignee`(`ID`),
  FOREIGN KEY (`Vehicle_NUM`) REFERENCES `Vehicle`(`ID`),
  PRIMARY KEY (`ID`)
);

CREATE TABLE `Repair_Log` (
  `ID` int NOT NULL auto_increment,
  `Vehicle_Num` int NOT NULL,
  `Repair_Date` date NOT NULL,
  `Amount` varchar(50) NOT NULL,
  `From` varchar(50) NOT NULL,
  FOREIGN KEY (`Vehicle_Num`) REFERENCES `Vehicle`(`ID`),
  PRIMARY KEY (`ID`)
);

CREATE TABLE `Bills` (
  `Num` varchar(20),
  `Consignments` int NOT NULL,
  `BIll_Date` date NOT NULL,
  `Amount` varchar(50) NOT NULL,
  PRIMARY KEY (`Num`)
)