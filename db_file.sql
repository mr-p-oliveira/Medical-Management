CREATE DATABASE `testedatabase`;

CREATE TABLE `log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome`     varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `role`     varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `pat_reg` (
  `idpat_reg` int NOT NULL AUTO_INCREMENT,
  `firstnam`  varchar(45) NOT NULL,
  `lastnam`   varchar(45) NOT NULL,
  `gender`    varchar(45) NOT NULL,
  `birthdate` date NOT NULL,
  `adress`    varchar(100) NOT NULL,
  `city`      varchar(45) NOT NULL,
  `zipcod`    varchar(45) NOT NULL,
  `phone`     varchar(45) NOT NULL,
  `email`     varchar(55) NOT NULL,
  `sscnumber` varchar(100) NOT NULL,
  `nhsnumber` int NOT NULL,
  `blood`     varchar(45) NOT NULL,
  `martial`   varchar(45) NOT NULL,
  `weight`    decimal(5,2) NOT NULL,
  `height`    decimal(5,2) NOT NULL,
  `allerg`    varchar(45) NOT NULL,
  `doctor`    varchar(45) NOT NULL,
  PRIMARY KEY (`idpat_reg`)
);
