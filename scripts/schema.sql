CREATE TABLE IF NOT EXISTS `Customer_Satisfaction` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `User_ID` FLOAT NOT NULL,
    `Experience_score` FLOAT DEFAULT NULL,
    `Engagement_score` FLOAT DEFAULT NULL,
    `Satisfaction_score` FLOAT DEFAULT NULL,




    PRIMARY KEY (`id`)
) ;