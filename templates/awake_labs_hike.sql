# Creates data base if it doesn't exist yet
CREATE DATABASE  IF NOT EXISTS `awake_labs_hike` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `awake_labs_hike`;

#creates the table for database
CREATE TABLE `tbl_hike` (
  `hike_id` BIGINT NOT NULL AUTO_INCREMENT,
  `hike_name` VARCHAR(45) NULL,
  `hike_location` VARCHAR(45) NULL,
  `hike_duration` VARCHAR(45) NULL,
  PRIMARY KEY (`hike_id`))