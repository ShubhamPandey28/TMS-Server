
-- CREATING DATABASE SYSTEM. RIGHT NOW IT IS A DUMMY ONE

DROP DATABASE IF EXISTS SG_TMS;
CREATE DATABASE SG_TMS;

USE SG_TMS;

CREATE TABLE IF NOT EXISTS `cities` (
  `city_id` int(11) NOT NULL auto_increment,
  `city_name` varchar(100) NOT NULL,
  `city_state` varchar(100) NOT NULL,
  PRIMARY KEY  (`city_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1624 ;

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
