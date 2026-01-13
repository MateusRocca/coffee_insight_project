CREATE TABLE `sales_coffee` (
  `hour_of_day` int DEFAULT NULL,
  `cash_type` varchar(50) DEFAULT NULL,
  `money` decimal(10,2) DEFAULT NULL,
  `coffee_name` varchar(100) DEFAULT NULL,
  `time_of_day` varchar(50) DEFAULT NULL,
  `weekday` varchar(50) DEFAULT NULL,
  `month_name` varchar(50) DEFAULT NULL,
  `weekdaysort` int DEFAULT NULL,
  `monthsort` int DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
