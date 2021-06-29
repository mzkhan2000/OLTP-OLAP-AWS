-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema prd_demo_monir
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema prd_demo_monir
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `prd_demo_monir` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `prd_demo_monir` ;

-- -----------------------------------------------------
-- Table `prd_demo_monir`.`ffa_client`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `prd_demo_monir`.`ffa_client` (
  `client_id` BIGINT NOT NULL,
  `city` VARCHAR(100) NULL DEFAULT NULL,
  `postcode` VARCHAR(10) NULL DEFAULT NULL,
  `state` VARCHAR(100) NULL DEFAULT NULL,
  `comments` VARCHAR(800) NULL DEFAULT NULL,
  `external_id` VARCHAR(50) NULL DEFAULT NULL,
  `active` INT NULL DEFAULT NULL,
  PRIMARY KEY (`client_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `prd_demo_monir`.`ffa_employment_type`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `prd_demo_monir`.`ffa_employment_type` (
  `employment_type` TINYINT NOT NULL,
  `name` VARCHAR(200) NULL DEFAULT NULL,
  PRIMARY KEY (`employment_type`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `prd_demo_monir`.`ffa_project`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `prd_demo_monir`.`ffa_project` (
  `project_id` BIGINT NOT NULL,
  `client_id` BIGINT NULL DEFAULT NULL,
  `start_date` DATE NULL DEFAULT NULL,
  `end_date` DATE NULL DEFAULT NULL,
  `email` VARCHAR(100) NULL DEFAULT NULL,
  `address` VARCHAR(255) NULL DEFAULT NULL,
  `address_geo` POINT NULL DEFAULT NULL,
  `suburb` VARCHAR(100) NULL DEFAULT NULL,
  `state` VARCHAR(50) NULL DEFAULT NULL,
  `postcode` VARCHAR(10) NULL DEFAULT NULL,
  `external_id` VARCHAR(50) NULL DEFAULT NULL,
  `active` TINYINT(1) NULL DEFAULT NULL,
  `parent_id` BIGINT NULL DEFAULT NULL,
  PRIMARY KEY (`project_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `prd_demo_monir`.`ffa_order_status`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `prd_demo_monir`.`ffa_order_status` (
  `status_id` TINYINT NOT NULL,
  `status_name` VARCHAR(20) NULL DEFAULT NULL,
  PRIMARY KEY (`status_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `prd_demo_monir`.`ffa_suppliers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `prd_demo_monir`.`ffa_suppliers` (
  `id` INT UNSIGNED NOT NULL,
  `city` VARCHAR(100) NULL DEFAULT NULL,
  `postcode` VARCHAR(10) NULL DEFAULT NULL,
  `state` VARCHAR(100) NULL DEFAULT NULL,
  `comments` VARCHAR(800) NULL DEFAULT NULL,
  `external_id` VARCHAR(50) NULL DEFAULT NULL,
  `active` TINYINT(1) NULL DEFAULT NULL,
  `date_added` DATETIME NULL DEFAULT NULL,
  `date_modified` DATETIME NULL DEFAULT NULL,
  `modified_time` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `prd_demo_monir`.`ffa_user_type`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `prd_demo_monir`.`ffa_user_type` (
  `ut_id` BIGINT NOT NULL,
  `user_type` VARCHAR(20) NULL DEFAULT NULL,
  `label` VARCHAR(30) NULL DEFAULT NULL,
  PRIMARY KEY (`ut_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `prd_demo_monir`.`ffa_user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `prd_demo_monir`.`ffa_user` (
  `user_id` BIGINT NOT NULL,
  `ut_id` BIGINT NULL DEFAULT NULL,
  `suburb` VARCHAR(100) NULL DEFAULT NULL,
  `state` VARCHAR(50) NULL DEFAULT NULL,
  `postcode` VARCHAR(10) NULL DEFAULT NULL,
  `employment_type` TINYINT NULL DEFAULT NULL,
  `active` TINYINT(1) NULL DEFAULT NULL,
  `modified_time` DATETIME NULL DEFAULT NULL,
  `comments` TEXT NULL DEFAULT NULL,
  `app_version` VARCHAR(10) NULL DEFAULT NULL,
  `device_os` VARCHAR(100) NULL DEFAULT NULL,
  `device_os_version` VARCHAR(30) NULL DEFAULT NULL,
  `app_timezone` INT NULL DEFAULT NULL,
  `last_logged_in` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  INDEX `fk_ffa_user_ffa_employment_type1_idx` (`employment_type` ASC) VISIBLE,
  INDEX `fk_ffa_user_ffa_user_type1_idx` (`ut_id` ASC) VISIBLE,
  CONSTRAINT `fk_ffa_user_ffa_user_type1`
    FOREIGN KEY (`ut_id`)
    REFERENCES `prd_demo_monir`.`ffa_user_type` (`ut_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ffa_user_ffa_employment_type1`
    FOREIGN KEY (`employment_type`)
    REFERENCES `prd_demo_monir`.`ffa_employment_type` (`employment_type`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `prd_demo_monir`.`ffa_order`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `prd_demo_monir`.`ffa_order` (
  `id` INT NOT NULL,
  `active` TINYINT(1) NULL DEFAULT NULL,
  `job_number` VARCHAR(100) NULL DEFAULT NULL,
  `po_number` VARCHAR(100) NULL DEFAULT NULL,
  `client_id` BIGINT NULL DEFAULT NULL,
  `project_id` BIGINT NULL,
  `job_description` VARCHAR(100) NULL DEFAULT NULL,
  `shift_duration` VARCHAR(100) NULL DEFAULT NULL,
  `start_date` DATE NULL DEFAULT NULL,
  `end_date` DATE NULL DEFAULT NULL,
  `comments` TEXT NULL DEFAULT NULL,
  `date_created` DATETIME NULL DEFAULT NULL,
  `modified_time` DATETIME NULL DEFAULT NULL,
  `status_id` TINYINT NULL DEFAULT NULL,
  `supplier_id` BIGINT NULL DEFAULT NULL,
  `user_id` BIGINT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_ffa_order_ffa_project1_idx` (`project_id` ASC) VISIBLE,
  INDEX `fk_ffa_order_ffa_order_status1_idx` (`status_id` ASC) VISIBLE,
  INDEX `fk_ffa_order_ffa_client1_idx` (`client_id` ASC) VISIBLE,
  INDEX `fk_ffa_order_ffa_user1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_ffa_order_ffa_project1`
    FOREIGN KEY (`project_id`)
    REFERENCES `prd_demo_monir`.`ffa_project` (`project_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ffa_order_ffa_order_status1`
    FOREIGN KEY (`status_id`)
    REFERENCES `prd_demo_monir`.`ffa_order_status` (`status_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ffa_order_ffa_suppliers1`
    FOREIGN KEY ()
    REFERENCES `prd_demo_monir`.`ffa_suppliers` ()
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ffa_order_ffa_client1`
    FOREIGN KEY (`client_id`)
    REFERENCES `prd_demo_monir`.`ffa_client` (`client_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ffa_order_ffa_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `prd_demo_monir`.`ffa_user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
