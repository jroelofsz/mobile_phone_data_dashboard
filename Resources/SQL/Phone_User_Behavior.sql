CREATE TABLE phone_user_behavior (
  user_id INT NOT NULL,
  device_model VARCHAR(255) NOT NULL,
  operating_system VARCHAR(255) NOT NULL, 
  app_usage_minutes_per_day INT NOT NULL,
  screen_time_hours_per_day DECIMAL(100,1) NOT NULL, 
  battery_drain_mah_per_day INT NOT NULL,
  number_of_apps_installed INT NOT NULL, 
  data_usage_mb_per_day INT NOT NULL, 
  age INT NOT NULL,
  gender VARCHAR(255) NOT NULL, 
  user_behavior_class INT NOT NULL, 
  PRIMARY KEY (user_id)
);