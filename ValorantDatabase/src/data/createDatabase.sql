-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema valorantDatabase
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema valorantDatabase
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `valorantDatabase` ;
USE `valorantDatabase` ;

-- -----------------------------------------------------
-- Table `valorantDatabase`.`player`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `valorantDatabase`.`player` (
  `name` VARCHAR(150) NOT NULL,
  `tag` VARCHAR(150) NOT NULL,
  `region` CHAR(3) NOT NULL,
  `rank` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`name`, `tag`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `valorantDatabase`.`round`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `valorantDatabase`.`round` (
  `player_name` VARCHAR(150) NOT NULL,
  `player_tag` VARCHAR(150) NOT NULL,
  `damage_round` DOUBLE NULL,
  `kills_round` DOUBLE NULL,
  `score_round` DOUBLE NULL,
  PRIMARY KEY (`player_name`, `player_tag`),
  CONSTRAINT `fk_round_player1`
    FOREIGN KEY (`player_name` , `player_tag`)
    REFERENCES `valorantDatabase`.`player` (`name` , `tag`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `valorantDatabase`.`total_game_stats`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `valorantDatabase`.`total_game_stats` (
  `player_name` VARCHAR(150) NOT NULL,
  `player_tag` VARCHAR(150) NOT NULL,
  `headshots` INT NULL,
  `headshot_percent` DOUBLE NULL,
  `aces` INT NULL,
  `clutches` INT NULL,
  `flawless` INT NULL,
  `first_bloods` INT NULL,
  `kills` INT NULL,
  `deaths` INT NULL,
  `assists` INT NULL,
  `most_kills` INT NULL,
  `kd_ratio` DOUBLE NULL,
  `wins` INT NULL,
  `win_percent` DOUBLE NULL,
  PRIMARY KEY (`player_name`, `player_tag`),
  CONSTRAINT `fk_total_game_stats_player1`
    FOREIGN KEY (`player_name` , `player_tag`)
    REFERENCES `valorantDatabase`.`player` (`name` , `tag`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `valorantDatabase`.`player_agents`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `valorantDatabase`.`player_agents` (
  `player_name` VARCHAR(150) NOT NULL,
  `player_tag` VARCHAR(150) NOT NULL,
  `agents_usage_rank` INT NOT NULL,
  `agent_name` VARCHAR(50) NULL,
  PRIMARY KEY (`player_name`, `player_tag`, `agents_usage_rank`),
  CONSTRAINT `fk_player_agents_player1`
    FOREIGN KEY (`player_name` , `player_tag`)
    REFERENCES `valorantDatabase`.`player` (`name` , `tag`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `valorantDatabase`.`gun_stats`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `valorantDatabase`.`gun_stats` (
  `player_name` VARCHAR(150) NOT NULL,
  `player_tag` VARCHAR(150) NOT NULL,
  `gun_usage_rank` INT NOT NULL,
  `gun_name` VARCHAR(50) NULL,
  `gun_head` INT NULL,
  `gun_body` INT NULL,
  `gun_leg` INT NULL,
  `gun_kills` INT NULL,
  PRIMARY KEY (`player_name`, `player_tag`, `gun_usage_rank`),
  CONSTRAINT `fk_gun_stats_player1`
    FOREIGN KEY (`player_name` , `player_tag`)
    REFERENCES `valorantDatabase`.`player` (`name` , `tag`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
