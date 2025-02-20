CREATE DATABASE `demoweb` ;

CREATE USER humanda@localhost IDENTIFIED BY "humanda";
CREATE USER humanda@"%" IDENTIFIED BY "humanda";

GRANT ALL PRIVILEGES ON `demoweb`.* to humanda@localhost;
GRANT ALL PRIVILEGES ON `demoweb`.* to humanda@"%";

FLUSH PRIVILEGES;

use `demoweb`;

CREATE TABLE `member` (
  `memberid` varchar(20) NOT NULL,
  `passwd` varchar(200) NOT NULL,
  `email` varchar(50) NOT NULL,
  `usertype` varchar(50) DEFAULT (_utf8mb4'user'),
  `regdate` datetime DEFAULT (now()),
  `active` tinyint(1) DEFAULT (true),
  PRIMARY KEY (`memberid`),
  CONSTRAINT `member_chk_1` CHECK ((`usertype` in (_utf8mb4'user',_utf8mb4'admin')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `board` (
  `boardno` int NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `writer` varchar(20) NOT NULL,
  `content` varchar(4000) NOT NULL,
  `writedate` date DEFAULT (now()),
  `modifydate` date DEFAULT (now()),
  `readcount` int DEFAULT (0),
  `deleted` tinyint(1) DEFAULT (false),
  PRIMARY KEY (`boardno`),
  KEY `fk_board_to_member` (`writer`),
  CONSTRAINT `fk_board_to_member` FOREIGN KEY (`writer`) REFERENCES `member` (`memberid`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `attachment` (
  `attachno` int NOT NULL AUTO_INCREMENT,
  `boardno` int NOT NULL,
  `userfilename` varchar(100) NOT NULL,
  `savedfilename` varchar(100) NOT NULL,
  `downloadcnt` int DEFAULT (0),
  PRIMARY KEY (`attachno`),
  KEY `FK_board_TO_attachment` (`boardno`),
  CONSTRAINT `FK_board_TO_attachment` FOREIGN KEY (`boardno`) REFERENCES `board` (`boardno`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

